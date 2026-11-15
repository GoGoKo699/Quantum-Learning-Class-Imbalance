#!/usr/bin/env python3
"""Finite numerical checks; these are not proofs or interval certificates."""

from __future__ import annotations

import hashlib
import json
import math
import platform
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import scipy
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.optimize import linprog


ATOL = 3e-10
RNG = np.random.default_rng(20261115)
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.diag([1.0, -1.0]).astype(complex)
PAULI = [X, Y, Z]


def herm(a):
    return (a + a.conj().T) / 2


def trace_norm(a):
    return float(np.sum(np.abs(np.linalg.eigvalsh(herm(a)))))


def min_eig(a):
    return float(np.linalg.eigvalsh(herm(a))[0])


def projector(v):
    return np.outer(v, v.conj())


def sphere_rule(order):
    """Normalized sphere integral, exact here for all required polynomial moments."""
    nodes, weights = leggauss(order)
    phases = 2 * order + 1
    for z, wz in zip(nodes, weights):
        for l in range(phases):
            angle = 2 * np.pi * l / phases
            ket = np.array([np.sqrt((1 + z) / 2),
                            np.exp(1j * angle) * np.sqrt((1 - z) / 2)])
            yield ket, float(wz / (2 * phases))


def coherent(ket, n):
    """Product ket in normalized Dicke coordinates, no projector formula."""
    a, b = ket
    return np.array([np.sqrt(math.comb(n, k)) * a ** (n-k) * b ** k
                     for k in range(n+1)], dtype=complex)


def averaged_states(n, order_extra=0):
    """Construct actual pure-product integrals in A,B,C ordering."""
    d = n + 1
    a_mean = np.zeros((d, d), complex)
    ab_mean = np.zeros((2*d, 2*d), complex)
    bc_mean = np.zeros((2*d, 2*d), complex)
    for ket, weight in sphere_rule(n + 3 + order_extra):
        a = coherent(ket, n)
        a_mean += weight * projector(a)
        ab_mean += weight * projector(np.kron(a, ket))
        bc_mean += weight * projector(np.kron(ket, a))
    return herm(np.kron(ab_mean, a_mean)), herm(np.kron(a_mean, bc_mean))


def training_test_order(sigma, n):
    d = n + 1
    return sigma.reshape(d, 2, d, d, 2, d).transpose(0, 2, 1, 3, 5, 4).reshape(d*d, 2, d*d, 2)


def partial_transpose_test(a, n):
    d = n + 1
    return a.reshape(d, 2, d, d, 2, d).transpose(0, 4, 2, 3, 1, 5).reshape(a.shape)


def posterior(sigma_tb, v, n):
    # The training marginal is exactly I/(n+1)^2.
    return herm((n+1)**2 * np.einsum('i,ibjc,j->bc', v.conj(), sigma_tb, v))


def conditional_bias(sigma0_tb, sigma1_tb, v, n, p):
    return trace_norm(p * posterior(sigma0_tb, v, n) -
                      (1-p) * posterior(sigma1_tb, v, n))


def quantum_bias_formula(n, p):
    s = abs(2*p - 1)
    return float(2*s/(n+2) + 2/((n+1)*(n+2)) * sum(
        k*np.sqrt(1-(1-s*s)*k*k/(n+1)**2) for k in range(1, n+1)))


def classical_one_formula(s):
    if s <= 1/(3*np.sqrt(3)):
        return float(np.sqrt(3)/6)
    if s <= 1/3:
        return float(3*s/4 + 1/(36*s))
    return float(s)


def spins(n):
    """Spin n/2 in Dicke order, and product-register total operators."""
    j = n/2
    z = np.diag([j-k for k in range(n+1)]).astype(complex)
    plus = np.zeros_like(z)
    for k in range(1, n+1):
        m = j-k
        plus[k-1, k] = np.sqrt((j-m)*(j+m+1))
    single = [(plus+plus.T)/2, (plus-plus.T)/(2j), z]
    eye = np.eye(n+1)
    aa = [np.kron(t, eye) for t in single]
    cc = [np.kron(eye, t) for t in single]
    total = [a+c for a, c in zip(aa, cc)]
    total_sq = sum(t@t for t in total)
    ev, vec = np.linalg.eigh(herm(total_sq))
    projectors = [vec[:, np.abs(ev-jj*(jj+1)) < 1e-7] for jj in range(n+1)]
    projectors = [v@v.conj().T for v in projectors]
    assert all(round(np.trace(P).real) == 2*jj+1 for jj, P in enumerate(projectors))
    return aa, cc, total, total_sq, projectors


def cliffords():
    """Generate the 24 projective one-qubit Cliffords from H and S."""
    h = np.array([[1, 1], [1, -1]], complex)/np.sqrt(2)
    s = np.diag([1, 1j])
    def key(u):
        nz = np.flatnonzero(np.abs(u.ravel()) > 1e-8)[0]
        canon = u / (u.ravel()[nz]/abs(u.ravel()[nz]))
        return tuple(np.round(canon.real, 9).ravel()) + tuple(np.round(canon.imag, 9).ravel())
    todo, seen, out = [I2], set(), []
    while todo:
        u = todo.pop()
        k = key(u)
        if k in seen:
            continue
        seen.add(k)
        out.append(u)
        todo.extend([h@u, s@u])
    assert len(out) == 24
    return out


SINGLET = np.array([0, 1, -1, 0], complex)/np.sqrt(2)
TRIPLET0 = np.array([0, 1, 1, 0], complex)/np.sqrt(2)


def one_copy_seeds(s):
    if s <= 1/(3*np.sqrt(3)):
        return [(1.0, np.sqrt(.25)*SINGLET + np.sqrt(.75)*TRIPLET0)]
    if s < 1/3:
        u = 9*s*s/(1+9*s*s)
        w = 1/(4*u)
        return [(w, np.sqrt(u)*SINGLET + np.sqrt(1-u)*TRIPLET0),
                (1-w, np.array([1, 0, 0, 0], complex))]
    return []  # The always-majority rule attains this branch.


def one_copy_povm(seeds, rotations, sig0, sig1, p):
    a0, a1 = training_test_order(sig0, 1), training_test_order(sig1, 1)
    completeness = np.zeros((4, 4), complex)
    bias = 0.0
    for weight, seed in seeds:
        for u in rotations:
            v = np.kron(u, u)@seed
            coefficient = 4*weight/len(rotations)
            completeness += coefficient * projector(v)
            bias += coefficient/4 * conditional_bias(a0, a1, v, 1, p)
    return completeness, float(bias)


def check_dense_global():
    rows, max_formula_error, max_quadrature_change = [], 0.0, 0.0
    for n in range(1, 5):
        sigma0, sigma1 = averaged_states(n)
        fine0, fine1 = averaged_states(n, 2)
        max_quadrature_change = max(max_quadrature_change,
                                    np.max(np.abs(sigma0-fine0)), np.max(np.abs(sigma1-fine1)))
        assert abs(np.trace(sigma0)-1) < ATOL and abs(np.trace(sigma1)-1) < ATOL
        assert min_eig(sigma0) > -ATOL and min_eig(sigma1) > -ATOL
        for p in [0, .1, .49, .5, .51, .6, .8, .99, 1]:
            delta = herm(p*sigma0 - (1-p)*sigma1)
            ev, vec = np.linalg.eigh(delta)
            direct = float(np.sum(np.abs(ev)))
            formula = quantum_bias_formula(n, p)
            error = abs(direct-formula)
            max_formula_error = max(max_formula_error, error)
            assert error < ATOL
            assert abs(formula-quantum_bias_formula(n, 1-p)) < ATOL
            if .5 < p < 1:
                minority = vec[:, ev < -1e-11]
                effect = minority@minority.conj().T
                npt = min_eig(partial_transpose_test(effect, n))
                assert npt < -1e-7
                assert abs(effect[0, 0]) < ATOL
                # The partial-transpose row must nevertheless contain a nonzero entry.
                row_norm = np.linalg.norm(partial_transpose_test(effect, n)[0])
                assert row_norm > 1e-6
                rows.append({'n': n, 'p': p, 'quantum_risk': (1-direct)/2,
                             'minority_effect_partial_transpose_min_eigenvalue': npt,
                             'zero_diagonal_row_norm_after_partial_transpose': float(row_norm)})
    return {'tested_n': [1, 2, 3, 4], 'priors': [0, .1, .49, .5, .51, .6, .8, .99, 1],
            'max_jordan_vs_dense_bias_error': max_formula_error,
            'max_entry_change_with_finer_sphere_rule': float(max_quadrature_change),
            'npt_examples': rows}


def check_one_copy():
    sigma0, sigma1 = averaged_states(1)
    a0, a1 = training_test_order(sigma0, 1), training_test_order(sigma1, 1)
    rotations = cliffords()
    ps = [.5, .525, (1+1/(3*np.sqrt(3)))/2, .6, .625, 2/3, .8, 1]
    # Independent finite-grid physical seed optimization: exact moment constraint,
    # posterior objectives computed from dense states, not from the risk curve.
    grid = np.linspace(0, 1, 4001)
    seed_list = [np.sqrt(u)*SINGLET + np.sqrt(1-u)*TRIPLET0 for u in grid]
    seed_list += [np.array([1, 0, 0, 0], complex)]
    for _ in range(250):
        v = RNG.normal(size=4) + 1j*RNG.normal(size=4)
        seed_list.append(v/np.linalg.norm(v))
    u_values = np.array([abs(np.vdot(SINGLET, v))**2 for v in seed_list])
    P_s = projector(SINGLET)
    P_t = np.eye(4)-P_s
    rows = []
    for p in ps:
        s = 2*p-1
        expected = classical_one_formula(s)
        objectives = np.array([conditional_bias(a0, a1, v, 1, p) for v in seed_list])
        lp = linprog(-objectives, A_eq=np.vstack([np.ones(len(seed_list)), u_values]),
                     b_eq=[1, .25], bounds=(0, None), method='highs')
        assert lp.success, lp.message
        achieved = float(-lp.fun)
        assert achieved <= expected + 2e-8
        assert expected-achieved < 3e-6
        if s <= 1/(3*np.sqrt(3)):
            ys, yt = 1/np.sqrt(3), 1/(3*np.sqrt(3))
        elif s < 1/3:
            ys, yt = 1/(9*s), s
        else:
            ys = yt = s
        dual = ys*P_s + yt*P_t
        delta_tb = p*a0-(1-p)*a1
        hz = herm(4*np.einsum('ibjc,cb->ij', delta_tb, Z))
        dual_slack = min(min_eig(dual-s*np.eye(4)), min_eig(dual-hz))
        assert dual_slack > -ATOL
        assert abs(np.trace(dual).real/4-expected) < ATOL
        seeds = one_copy_seeds(s)
        if seeds:
            complete, physical_bias = one_copy_povm(seeds, rotations, sigma0, sigma1, p)
            assert np.max(np.abs(complete-np.eye(4))) < ATOL
        else:
            physical_bias = s
        assert abs(physical_bias-expected) < ATOL
        rows.append({'p': float(p), 's': float(s), 'formula_bias': expected,
                     'finite_physical_seed_lp_bias': achieved,
                     'formula_minus_lp': expected-achieved,
                     'dense_dual_min_slack_eigenvalue': dual_slack,
                     'finite_clifford_povm_bias': physical_bias,
                     'training_outcomes': 24*len(seeds) if seeds else 1})
    return {'seed_grid_size': len(seed_list), 'clifford_rotations': len(rotations), 'rows': rows}


def check_plateau():
    rows = []
    for n in range(1, 9):
        aa, cc, total, total_sq, P = spins(n)
        h0 = (aa[2]-cc[2])/(n+2)
        y = np.array([(jj*np.sqrt((n+1)**2-jj**2) +
                       (jj+1)*np.sqrt(max(0, (n+1)**2-(jj+1)**2)))/
                      ((n+2)*(2*jj+1)) for jj in range(n+1)])
        dual = sum(yj*pj for yj, pj in zip(y, P))
        s0 = float(min(y)*min(1, (n+2)/(2*n*n)))
        expected = quantum_bias_formula(n, .5)
        # Build |j,0> directly from J_total^2 in the zero-magnetization product basis.
        indices = np.flatnonzero(np.abs(np.diag(total[2])) < 1e-8)
        ev, vv = np.linalg.eigh(total_sq[np.ix_(indices, indices)])
        coupled = []
        for jj in range(n+1):
            v = np.zeros((n+1)**2, complex)
            v[indices] = vv[:, np.argmin(abs(ev-jj*(jj+1)))]
            if coupled and np.vdot(v, h0@coupled[-1]).real < 0:
                v *= -1
            coupled.append(v)
        seed = sum(np.sqrt(2*jj+1)*v for jj, v in enumerate(coupled))/(n+1)
        assert abs(np.linalg.norm(seed)-1) < ATOL
        assert abs(np.vdot(seed, h0@seed).real-expected) < ATOL
        assert abs(np.trace(dual).real/(n+1)**2-expected) < ATOL
        twirl_coeff_error = max(abs(np.vdot(seed, pj@seed).real/(2*jj+1)-1/(n+1)**2)
                               for jj, pj in enumerate(P))
        assert twirl_coeff_error < ATOL
        min_block_slack = 1.0
        for s in [0, s0/2, s0]:
            hz = h0+s*total[2]/(n+2)
            assert min_eig(dual-s*np.eye((n+1)**2)) > -ATOL
            for m in range(-n, n+1):
                ix = np.flatnonzero(np.abs(np.diag(total[2])-m) < 1e-8)
                val = min_eig((dual-hz)[np.ix_(ix, ix)])
                min_block_slack = min(min_block_slack, val)
                assert val > -ATOL
            gap = (quantum_bias_formula(n, (1+s)/2)-expected)/2
            assert gap + ATOL >= s/(n+2)
        if n <= 4:
            sig0, sig1 = averaged_states(n)
            d0, d1 = training_test_order(sig0, n), training_test_order(sig1, n)
            hz_direct = (n+1)**2*np.einsum('ibjc,cb->ij', (.5+s0/2)*d0-(.5-s0/2)*d1, Z)
            assert np.max(np.abs(hz_direct-(h0+s0*total[2]/(n+2)))) < ATOL
            achieved = conditional_bias(d0, d1, seed, n, (1+s0)/2)
            assert abs(achieved-expected) < ATOL
        rows.append({'n': n, 'certified_s0': s0, 'balanced_bias': expected,
                     'minimum_tested_magnetic_block_dual_slack': min_block_slack,
                     'covariant_seed_twirl_coefficient_max_error': float(twirl_coeff_error),
                     'gap_at_s0': (quantum_bias_formula(n, (1+s0)/2)-expected)/2,
                     'analytic_gap_lower_bound_at_s0': s0/(n+2)})
    return {'tested_n': list(range(1, 9)), 'bias_points_per_n': ['0', 's0/2', 's0'], 'rows': rows}


def symmetric_extension_projector(n):
    # Construct normalized (n+1)-qubit Dicke columns split as A^n followed by B.
    iso = np.zeros((2*(n+1), n+2), complex)
    for k in range(n+2):
        if k <= n:
            iso[2*k, k] = np.sqrt((n+1-k)/(n+1))
        if k >= 1:
            iso[2*(k-1)+1, k] = np.sqrt(k/(n+1))
    assert np.max(np.abs(iso.conj().T@iso-np.eye(n+2))) < ATOL
    return iso@iso.conj().T


def check_rare_class():
    rows = []
    for n in range(1, 5):
        d = n+1
        sig0, sig1 = averaged_states(n)
        d0, d1 = training_test_order(sig0, n), training_test_order(sig1, n)
        smallest, largest = 1.0, 0.0
        for _ in range(70):
            v = RNG.normal(size=d*d)+1j*RNG.normal(size=d*d)
            v /= np.linalg.norm(v)
            for sig in [d0, d1]:
                ev = np.linalg.eigvalsh(posterior(sig, v, n))
                smallest, largest = min(smallest, ev[0]), max(largest, ev[-1])
                assert ev[0] >= 1/(n+2)-ATOL
                assert ev[-1] <= (n+1)/(n+2)+ATOL
        extremal = np.zeros(d*d, complex)
        extremal[n] = 1  # A all up, C all down.
        e0, e1 = posterior(d0, extremal, n), posterior(d1, extremal, n)
        assert abs(min_eig(e0)-1/(n+2)) < ATOL
        boundary_q = 1/(n+2)
        boundary_min = min_eig((1-boundary_q)*e0-boundary_q*e1)
        assert abs(boundary_min) < ATOL
        q = boundary_q/2
        strict_min = min_eig((1-q)*e0-q*e1)
        assert strict_min > 0
        assert abs(trace_norm((1-q)*e0-q*e1)-(1-2*q)) < ATOL
        qabove = boundary_q + .01
        selected_risk = (1-trace_norm((1-qabove)*e0-qabove*e1))/2
        two_outcome_risk = selected_risk/d**2 + (1-1/d**2)*qabove
        assert two_outcome_risk < qabove - 1e-7
        comp = np.kron(np.eye(2*d)-symmetric_extension_projector(n), np.eye(d))
        fp = float(np.trace(comp@sig0).real)
        recall = float(np.trace(comp@sig1).real)
        assert abs(fp) < ATOL
        assert abs(recall-n/(2*(n+1))) < ATOL
        # Direct quadrature of the covariant majority-estimation + orthogonal-test rule.
        majority_marginal = np.einsum('abcdec->abde', sig0.reshape(d, 2, d, d, 2, d)).reshape(2*d, 2*d)
        estimation_fp = 0.0
        for ket, weight in sphere_rule(n+4):
            effect = (n+1)*np.kron(projector(coherent(ket, n)), I2-projector(ket))
            estimation_fp += weight*np.trace(effect@majority_marginal).real
        assert abs(estimation_fp-1/(n+2)) < ATOL
        rows.append({'n': n, 'random_effect_posterior_eigenvalue_range': [float(smallest), float(largest)],
                     'allowed_posterior_eigenvalue_range': [1/(n+2), (n+1)/(n+2)],
                     'boundary_weighted_posterior_min_eigenvalue': boundary_min,
                     'strict_weighted_posterior_min_eigenvalue': strict_min,
                     'classical_risk_above_threshold': two_outcome_risk,
                     'majority_risk_above_threshold': qabove,
                     'comparison_false_positive_probability': fp,
                     'comparison_minority_recall': recall,
                     'covariant_estimation_false_positive_probability': float(estimation_fp)})
    eta = .25
    target_rows = []
    for q in [1e-1, 1e-2, 1e-3, 1e-4]:
        # Integer necessary/sufficient bounds, not an evaluation of the unknown exact optimum.
        lower_n = max(0, math.floor(1/q-2)+1)
        upper_n = max(0, math.ceil((1-q)/((.5-eta)*q)-2))
        quantum_n = math.ceil(2*eta/(1-2*eta))
        assert (1-q)/(upper_n+2)+q/2 <= (1-eta)*q+1e-12
        assert q*(quantum_n+2)/(2*(quantum_n+1)) <= (1-eta)*q+1e-12
        target_rows.append({'q': q, 'target_fraction_eta': eta,
                            'classical_necessary_n_lower_bound': lower_n,
                            'classical_constructive_n_upper_bound': upper_n,
                            'comparison_sufficient_quantum_n': quantum_n})
    return {'tested_n': [1, 2, 3, 4], 'matrix_checks': rows, 'sample_cost_examples': target_rows,
            'boundary_qualification': 'Risk q at equality; uniquely majority-only decisions require strict q<1/(n+2).'}


def noisy_states_one(eta):
    mean = np.zeros((2, 2), complex)
    pair = np.zeros((4, 4), complex)
    for ket, weight in sphere_rule(6):
        rho = (1-eta)*projector(ket)+eta*I2/2
        mean += weight*rho
        pair += weight*np.kron(rho, rho)
    return herm(np.kron(pair, mean)), herm(np.kron(mean, pair))


def check_noise():
    n, p, eta = 1, .6, .01
    pure0, pure1 = averaged_states(n)
    noisy0, noisy1 = noisy_states_one(eta)
    rq0 = (1-trace_norm(p*pure0-(1-p)*pure1))/2
    rq_eta = (1-trace_norm(p*noisy0-(1-p)*noisy1))/2
    rc0 = (1-classical_one_formula(2*p-1))/2
    delta = 1-(1-eta/2)**3
    gamma = rc0-rq0
    exact_pure_gap = (3*np.sqrt(19)-7)/90
    assert abs(gamma-exact_pure_gap) < ATOL
    distances = [trace_norm(noisy0-pure0)/2, trace_norm(noisy1-pure1)/2]
    assert max(distances) <= delta+ATOL
    assert abs(rq_eta-rq0) <= delta+ATOL
    # Known independent depolarization is simulable in each original interface.
    # Thus optimized noisy risk cannot fall below its noiseless optimum.
    assert rq_eta >= rq0-ATOL
    robust_bound = gamma-delta
    assert robust_bound > .0525
    complete, feasible_noisy_bias = one_copy_povm(one_copy_seeds(2*p-1), cliffords(), noisy0, noisy1, p)
    assert np.max(np.abs(complete-np.eye(4))) < ATOL
    feasible_risk = (1-feasible_noisy_bias)/2
    assert abs(feasible_risk-rc0) <= delta+ATOL
    return {'n': n, 'p': p, 'depolarization_eta': eta, 'pure_quantum_risk': rq0,
            'pure_classical_risk': rc0, 'pure_gap': gamma,
            'averaged_hypothesis_trace_distances': distances,
            'product_state_continuity_delta': delta,
            'noisy_quantum_optimal_risk_dense': rq_eta,
            'noisy_feasible_classical_strategy_risk': feasible_risk,
            'guaranteed_noisy_gap_lower_bound': robust_bound,
            'qualification': 'Classical monotonicity plus quantum continuity gives pure_gap-delta; no optimization of the noisy classical interface or fixed-noise large-n assertion.'}


def asymptotic_functions(s):
    integral_i = 2*(1+s+s*s)/(3*(1+s))
    integral_j = s/2*(1+2*np.log(1/s)/(1-s*s))
    return float(integral_i), float(integral_j), float((integral_j+s)/2)


def check_fixed_prior_asymptotic_algebra():
    """Sanity-check algebra/integration, not the Bayesian-converse theorem."""
    max_v_error, max_c_error = 0.0, 0.0
    algebra_points = 0
    for s in [.05, .2, .6, .9]:
        p, q = (1+s)/2, (1-s)/2
        for _ in range(150):
            r = RNG.normal(size=3); r /= np.linalg.norm(r)
            u = RNG.normal(size=3); u /= np.linalg.norm(u)
            d = p*r-q*u
            length = np.linalg.norm(d)
            axis = d/length
            c0, c1 = np.dot(r, axis), np.dot(u, axis)
            # Construct the two complex tangent-response vectors directly.
            xl = np.array([p*c0, -q*c1], complex)
            xk = np.array([1j*p, -1j*q], complex)
            v_direct = np.vdot(xl, xl).real+np.vdot(xk, xk).real
            c_direct = np.vdot(xl, xk).imag
            v_scalar = (length*length+1)*(length*length+s*s)/(2*length*length)
            c_scalar = s*(1+length*length)/(2*length)
            max_v_error = max(max_v_error, abs(v_direct-v_scalar))
            max_c_error = max(max_c_error, abs(c_direct-c_scalar))
            assert abs(v_direct-v_scalar) < ATOL
            assert abs(c_direct-c_scalar) < ATOL
            assert c_direct > 0
            algebra_points += 1
    integral_rows, benchmark_rows, upper_rows = [], [], []
    for s in [.01, .05, .2, .6, .9, .99]:
        p, q = (1+s)/2, (1-s)/2
        integral_i, integral_j, a_bound = asymptotic_functions(s)
        def integrand(x, part):
            length = np.sqrt(p*p+q*q-2*p*q*x)
            c0, c1 = (p-q*x)/length, (p*x-q)/length
            xl = np.array([p*c0, -q*c1], complex)
            xk = np.array([1j*p, -1j*q], complex)
            v = np.vdot(xl, xl).real+np.vdot(xk, xk).real
            c = np.vdot(xl, xk).imag
            if part == 'v':
                return float(v/(4*length))/2
            if part == 'c':
                return float(c/(2*length))/2
            return float(length)/2
        v_integral, v_quad_error = quad(lambda x: integrand(x, 'v'), -1, 1, epsabs=1e-12, epsrel=1e-12)
        c_integral, c_quad_error = quad(lambda x: integrand(x, 'c'), -1, 1, epsabs=1e-12, epsrel=1e-12)
        d_integral, _ = quad(lambda x: integrand(x, 'd'), -1, 1, epsabs=1e-12, epsrel=1e-12)
        assert abs(v_integral-integral_i/2) < ATOL
        assert abs(c_integral-integral_j/2) < ATOL
        assert abs(d_integral-integral_i) < ATOL
        assert 0 < a_bound <= integral_i+ATOL
        integral_rows.append({'s': s, 'direct_integral_V_over_4D': v_integral,
                              'I_over_2': integral_i/2,
                              'direct_integral_2C_over_4D': c_integral,
                              'J_over_2': integral_j/2,
                              'direct_integral_H': v_integral+c_integral,
                              'I_plus_J_over_2': (integral_i+integral_j)/2,
                              'quadrature_reported_error_sum': v_quad_error+c_quad_error,
                              'A_lower_coefficient': a_bound, 'I_upper_coefficient': integral_i})
        if s in [.05, .2, .6, .9]:
            oracle_risk = (1-integral_i)/2
            expected_coefficient = (integral_i-s)/2
            convergence = []
            for n in [1000, 4000, 16000, 64000]:
                k = np.arange(1, n+1, dtype=float)
                direct_bias = (2*(n+1)*s+np.sum(2*k*np.sqrt(1-(1-s*s)*(k/(n+1))**2)))/((n+1)*(n+2))
                scaled_excess = n*((1-direct_bias)/2-oracle_risk)
                convergence.append({'n': n, 'n_times_quantum_excess_over_oracle': float(scaled_excess),
                                    'difference_from_limit': float(scaled_excess-expected_coefficient)})
            assert abs(convergence[-1]['difference_from_limit']) < 2e-5
            assert abs(convergence[-1]['difference_from_limit']) < abs(convergence[0]['difference_from_limit'])
            benchmark_rows.append({'s': s, 'claimed_quantum_limit_coefficient': expected_coefficient,
                                   'convergence': convergence})
        for n in [1, 4, 20]:
            shrink = n/(n+2)
            def ed_integrand(x):
                length = np.sqrt(p*p+q*q-2*p*q*x)
                return max(s, shrink*length)/2
            break_x = (p*p+q*q-(s/shrink)**2)/(2*p*q)
            points = [break_x] if -1 < break_x < 1 else None
            ed_bias, _ = quad(ed_integrand, -1, 1, points=points, epsabs=1e-12, epsrel=1e-12)
            excess = (integral_i-ed_bias)/2
            assert -ATOL <= excess <= integral_i/(n+2)+ATOL
            upper_rows.append({'s': s, 'n': n, 'independent_covariant_estimation_excess': excess,
                               'finite_upper_bound_I_over_n_plus_2': integral_i/(n+2)})
    coefficient_grid = np.geomspace(1e-8, .99999999, 1000)
    coefficient_slack = min(asymptotic_functions(float(s))[0]-asymptotic_functions(float(s))[2]
                            for s in coefficient_grid)
    assert coefficient_slack > -ATOL
    return {'pure_pair_algebra_samples': algebra_points,
            'max_V_identity_error': float(max_v_error), 'max_C_identity_error': float(max_c_error),
            'sphere_integrals': integral_rows, 'quantum_benchmark_convergence': benchmark_rows,
            'finite_estimation_upper_bound_examples': upper_rows,
            'coefficient_compatibility_grid_points': len(coefficient_grid),
            'minimum_I_minus_A_on_grid': float(coefficient_slack),
            'qualification': 'Finite algebra, quadrature and benchmark checks only. These do not prove the integrated Bayesian Holevo converse, its regularity assumptions, or an exact classical leading coefficient.'}


def check_no_training():
    a, b = averaged_states(0)
    assert np.max(np.abs(a-b)) < ATOL
    for p in [0, .1, .5, .7, 1]:
        assert abs((1-trace_norm(p*a-(1-p)*b))/2-min(p, 1-p)) < ATOL
    return {'tested_n': 0, 'risk': 'min(p,1-p)', 'priors': [0, .1, .5, .7, 1]}


def main():
    start = time.monotonic()
    checks = {
        'dense_global_and_npt': check_dense_global(),
        'one_copy_classical_optimization': check_one_copy(),
        'plateau_dual_and_attaining_seed': check_plateau(),
        'rare_class_and_sample_cost': check_rare_class(),
        'finite_noise_continuity': check_noise(),
        'fixed_prior_asymptotic_algebra': check_fixed_prior_asymptotic_algebra(),
        'no_training': check_no_training(),
    }
    result = {
        'status': 'passed',
        'run_at_utc': datetime.now(timezone.utc).isoformat(),
        'command': 'python verification/run_all.py',
        'python': sys.version.split()[0], 'numpy': np.__version__, 'scipy': scipy.__version__,
        'platform': platform.platform(), 'random_seed': 20261115,
        'absolute_matrix_tolerance': ATOL,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'elapsed_seconds': time.monotonic()-start,
        'limits': [
            'Finite floating-point checks do not prove universal n, prior, or noise statements.',
            'Grid LP is a finite feasible measurement optimization; dense analytic duals certify only the tested floating-point instances.',
            'No interval arithmetic, hosted-rendering verification, hardware benchmarking, or exhaustive priority review is performed.',
            'The reference is consumed by one prediction; no repeated-use advantage is tested.',
        ],
        'checks': checks,
    }
    target = Path(__file__).with_name('results.json')
    target.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(f"PASS: {len(checks)} scientific check groups; wrote verification/results.json")
    print(f"Dense-vs-Jordan maximum bias error: {checks['dense_global_and_npt']['max_jordan_vs_dense_bias_error']:.3g}")
    print(f"Finite-noise guaranteed risk gap: {checks['finite_noise_continuity']['guaranteed_noisy_gap_lower_bound']:.9f}")
    print(f"Runtime: {result['elapsed_seconds']:.3f} seconds")


if __name__ == '__main__':
    main()
