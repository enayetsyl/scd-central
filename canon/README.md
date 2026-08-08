# canon/ — shared authority files

The single home of every cross-workstream authority file. **Cited, never copied** (AGENTS.md §8).
Changes are Principal-gated and logged as CD-### rows in `DECISIONS.md`.
`MANIFEST.md` is the machine-readable index consumed by `tools/audits/canon_check.py`.

| Sub-folder | Holds | Consumed by |
|---|---|---|
| islamic-curation/ | REF-1 Curation Policy | support-books, storybooks(conventions), lesson-plans |
| names/ | REF-2 Content Register / Name Bank | support-books, class-tests, english-drive |
| marklogic/ | 7 MarkLogic files (mark authority) | scholarship, class-tests, question-banks, english-drive |
| image-rules/ | living-being image doctrine | support-books, storybooks(conventions) |
| language/ | Bengali/numeral/script rules | all reader-facing output |
| school-facts/ | stable school facts | all |
