# accepted/ — class tests actually given

Historical record, **not templates**. These papers are imported as they were printed and are
**never edited** — the same rule the reference CTs carry under CD-023.

| File | Paper | Chapter |
|---|---|---|
| `C5_Bangla_ClassTest_Ch19.md` | শ্রেণি পরীক্ষা — ৩ক | পাঠ ১৯ ভাষার খেলা |
| `C5_Bangla_ClassTest_Ch20.md` | শ্রেণি পরীক্ষা — ৩খ | পাঠ ২০ শিক্ষাগুরুর মর্যাদা |

**Both carry `সময়: ৪৫ মিনিট`, which is superseded.** Canon is **35 minutes standard for a
25-mark class test, 30 permitted, 35 the maximum** (CD-021). The line stays on these papers
because they record what was given; **it must never be copied into a new paper.** The living
rule is `tools/render/ct_docx.py`'s config default, which rejects anything outside 30–35.

Header numbering (`৩ক` / `৩খ`) likewise comes from `--ct-number` at generation time and is never
taken from an existing paper (CR-001).

Moved here from `_inbox/` on the Principal's instruction 2026-08-09 (CD-047). They had no
counterpart anywhere under `workstreams/` before that.
