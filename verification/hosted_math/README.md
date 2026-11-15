# Hosted mathematics verification

These utilities compare exact committed Markdown mathematics against accessible MathML actually rendered on commit-pinned GitHub pages, at wide and narrow widths. The local source compiler supplies expected structure; it does not stand in for the hosted capture.

The read-only workflow checks a representative README page first. Once the shared tutorial exists, it captures every tracked Markdown page, including science and learning. Artifacts retain reports, HTML, screenshots and expression comparisons. The workflow has contents:read, no stored credentials, no secrets and no source-write operation.

A passing automated report still requires source and screenshot review. Source mathematical counts, numerical tests or a green job alone do not establish visible correctness, scientific truth or future renderer behavior.

Runtime: Playwright1.56.1 and MathJax3.2.1, installed outside source by the workflow. The utility set is content-addressed in this repository; do not mix capture and comparison versions silently.
