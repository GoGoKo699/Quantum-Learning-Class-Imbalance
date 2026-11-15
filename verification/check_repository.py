#!/usr/bin/env python3
"""Check the settled learning map and local navigation; no proof certification."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
NOTES: list[str] = []


def require(condition, message):
    if not condition:
        ERRORS.append(message)


def outside_fences(text):
    """Preserve line boundaries while removing fenced code and mathematics."""
    kept = []
    fence = None
    for line in text.splitlines():
        match = re.match(r'^\s*(`{3,}|~{3,})', line)
        if match:
            marker = match.group(1)[0]
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            kept.append('')
        elif fence is None:
            kept.append(line)
        else:
            kept.append('')
    return '\n'.join(kept)


def prose_only(text):
    """Remove fenced blocks, display/inline mathematics and inline code."""
    clean = outside_fences(text)
    clean = re.sub(r'\$\$[\s\S]*?\$\$', '', clean)
    clean = re.sub(r'\$`[\s\S]*?`\$', '', clean)
    clean = re.sub(r'(?<!\\)\$(?!\$)[^\n$]*?(?<!\\)\$', '', clean)
    clean = re.sub(r'`[^`\n]*`', '', clean)
    return clean


def github_heading_ids(text):
    ids, counts = set(), {}
    for line in outside_fences(text).splitlines():
        match = re.match(r'^\s{0,3}#{1,6}\s+(.+?)\s*#*$', line)
        if not match:
            continue
        title = re.sub(r'!?(\[([^]]*)\])\([^)]*\)', r'\2', match.group(1))
        title = re.sub(r'<[^>]*>', '', title).lower()
        slug = re.sub(r'[^\w\- ]', '', title, flags=re.UNICODE).replace(' ', '-')
        count = counts.get(slug, 0)
        counts[slug] = count+1
        ids.add(slug if count == 0 else f'{slug}-{count}')
    return ids


def check_target(source, target, all_docs):
    target = target.strip().strip('<>')
    # A quoted title after a bare destination is not part of its path.
    target = re.split(r'\s+[\'\"]', target, maxsplit=1)[0]
    parsed = urlsplit(target)
    if parsed.scheme or target.startswith('//'):
        require(not re.search(r'github\.com/[^/]+/Camelot(?:/|$)', target, re.I),
                f'{source.relative_to(ROOT)}: private preservation link is public: {target}')
        return
    destination = unquote(parsed.path)
    path = (source.parent/destination).resolve() if destination else source
    require(path.is_relative_to(ROOT), f'{source.relative_to(ROOT)}: link escapes repository: {target}')
    if not path.is_relative_to(ROOT):
        return
    require(path.exists(), f'{source.relative_to(ROOT)}: missing local link: {target}')
    if path.exists() and parsed.fragment and path.suffix.lower() == '.md':
        fragment = unquote(parsed.fragment)
        body = all_docs.get(path) or path.read_text()
        explicit = set(re.findall(r'<a\s+(?:name|id)=[\'\"]([^\'\"]+)', body, re.I))
        require(fragment in github_heading_ids(body) | explicit,
                f'{source.relative_to(ROOT)}: unknown heading fragment: {target}')


def check_navigation(docs):
    checked = 0
    for path, text in docs.items():
        clean = prose_only(text)
        for match in re.finditer(r'!?\[[^\]\n]*\]\(([^)\n]+)\)', clean):
            check_target(path, match.group(1), docs)
            checked += 1
        definitions = dict(re.findall(r'^\s*\[([^]]+)\]:\s*(\S+)', clean, re.M))
        for target in definitions.values():
            check_target(path, target, docs)
            checked += 1
        for label, reference in re.findall(r'!?\[([^]\n]+)\]\[([^]\n]*)\]', clean):
            reference = reference or label
            require(reference in definitions,
                    f'{path.relative_to(ROOT)}: undefined reference link [{reference}]')
    NOTES.append(f'Checked {checked} inline/reference destinations outside fenced code and mathematics.')


def field(record, name):
    match = re.search(r'^\*\*'+re.escape(name)+r':\*\*\s*(.*?)(?=^\*\*|\Z)', record, re.M | re.S)
    return match.group(1).strip() if match else ''


def check_milestones():
    path = ROOT/'learning/MILESTONES.md'
    require(path.exists(), 'Missing learning/MILESTONES.md')
    if not path.exists():
        return
    text = path.read_text()
    matches = list(re.finditer(r'^###\s+(M\d{2}):\s+(.+)$', text, re.M))
    ids = [m.group(1) for m in matches]
    expected = [f'M{i:02d}' for i in range(1, 31)]
    require(ids == expected, 'Milestone definitions must be exactly M01 through M30, once each, in order.')
    fields = ['Phase', 'Central question', 'Understanding target', 'Dependencies and story role',
              'Conceptual connection', 'Source pointers']
    allocations = {'Background/preliminaries.': 0, 'Narrative/innovation.': 0}
    dependency_count = 0
    for i, match in enumerate(matches):
        record = text[match.end():matches[i+1].start() if i+1 < len(matches) else len(text)]
        values = {name: field(record, name) for name in fields}
        for name, value in values.items():
            require(bool(value), f'{match.group(1)} is missing its {name} field.')
        phase = values['Phase']
        require(phase in allocations, f'{match.group(1)} has an unrecognized phase: {phase}')
        if phase in allocations:
            allocations[phase] += 1
        expected_phase = 'Background/preliminaries.' if i < 12 else 'Narrative/innovation.'
        require(phase == expected_phase,
                f'{match.group(1)} disagrees with the settled 12-background / 18-narrative allocation.')
        dependency_text = values['Dependencies and story role']
        def expand_range(match):
            start, end = int(match.group(1)), int(match.group(2))
            require(start <= end, f'{match.group(1)} has a reversed milestone range.')
            return ' '.join(f'M{k:02d}' for k in range(start, end+1))
        dependency_text = re.sub(r'\bM(\d{2})\s*[–—-]\s*M(\d{2})\b', expand_range, dependency_text)
        dependencies = re.findall(r'\bM\d{2}\b', dependency_text)
        require(len(dependencies) == len(set(dependencies)), f'{match.group(1)} repeats a dependency.')
        for dep in dependencies:
            require(dep in expected[:i], f'{match.group(1)} has a missing, self, or future dependency: {dep}')
        dependency_count += len(dependencies)
    require(allocations == {'Background/preliminaries.': 12, 'Narrative/innovation.': 18},
            f'Incorrect phase allocation: {allocations}')
    require('12' in text and '18' in text, 'The map must explain its chosen two-phase allocation.')
    NOTES.append(f'Map: {len(matches)} definitions, allocation {allocations}, {dependency_count} earlier dependency edges.')


def check_anchor_and_boundary(docs):
    learning_docs = {p: t for p, t in docs.items() if p.is_relative_to(ROOT/'learning')}
    require(bool(learning_docs), 'No learning material found.')
    joined = '\n'.join(learning_docs.values())
    require('Watrous' in joined and 'The Theory of Quantum Information' in joined and '2018' in joined,
            'Learning material must identify the selected Watrous 2018 textbook and version.')
    # Primary research papers are legitimate dependencies; these guards catch
    # reopening the educational-source menu rather than banning research citations.
    require(not re.search(r'(choose|select)\s+(one\s+)?(of\s+)?(three|3)\s+(anchor|textbook|source)', joined, re.I),
            'Learning material reopens the settled educational-anchor choice.')
    forbidden_names = {'coaching.md', 'progress.md', 'learner_state.json', 'session_state.json'}
    for path, text in docs.items():
        require(path.name.lower() not in forbidden_names, f'Personal teaching record in public tree: {path.name}')
        require(not re.search(r'github\.com/[^/]+/Camelot(?:/|\b)', text, re.I),
                f'{path.relative_to(ROOT)} contains a private preservation URL.')
        if path.is_relative_to(ROOT/'learning'):
            require(not re.search(r'(failed challenge|retry challenge|learner progress|all.correct passing|Revise\s*[→>-]+\s*Learn\s*[→>-]+\s*Test)', text, re.I),
                    f'{path.relative_to(ROOT)} includes personal assessment or retry instructions.')
    NOTES.append('Selected Watrous 2018 identity and public-learning/private-coaching separation checked.')


def check_claim_guards(docs):
    """Wording regressions supplement the separate semantic reading report."""
    required = {
        'README.md': ['exact leading coefficient', 'threshold', 'strict inequality', 'one consumed prediction'],
        'science/asymptotic.md': ['liminf', 'lower coefficient', 'fixed', 'not asserted', 'uniform'],
        'science/rare_class.md': ['At equality', 'strict', 'zero', 'fraction'],
        'science/noise.md': ['simulate', 'cannot decrease', 'fixed-noise'],
        'science/resources.md': ['consum', 'unrestricted', 'relative', 'implementation'],
    }
    for relative, phrases in required.items():
        path = ROOT/relative
        require(path in docs, f'Missing canonical claim source {relative}')
        if path not in docs:
            continue
        low = docs[path].lower()
        for phrase in phrases:
            require(phrase.lower() in low, f'{relative}: reviewed claim qualifier missing: {phrase}')
    map_path = ROOT/'learning/MILESTONES.md'
    if map_path in docs:
        text = docs[map_path].lower()
        for phrase in ['lower coefficient', 'fixed', 'threshold', 'tie', 'consum']:
            require(phrase in text, f'Milestones omit a load-bearing claim distinction: {phrase}')
    NOTES.append('Load-bearing scope guards checked; their meaning is separately reviewed in LEARNING_CHECKS.md.')


def main():
    docs = {p.resolve(): p.read_text() for p in ROOT.rglob('*.md') if '.git' not in p.parts}
    check_milestones()
    check_anchor_and_boundary(docs)
    check_navigation(docs)
    check_claim_guards(docs)
    for note in NOTES:
        print(note)
    if ERRORS:
        for error in ERRORS:
            print('FAIL:', error, file=sys.stderr)
        raise SystemExit(1)
    print('PASS: learning-map structure, source identity, local navigation and scope guards.')
    print('Limits: no textbook-reading audit, theorem proof, external-link availability, hosted rendering or learner assessment is certified.')


if __name__ == '__main__':
    main()
