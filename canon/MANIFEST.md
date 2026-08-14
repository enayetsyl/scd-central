# canon/MANIFEST.md — machine-readable canon index (read by canon_check.py)

Status: REQUIRED (check fails if missing) · PENDING (warn until slotted).
On slotting a file, flip its row to REQUIRED.

**Cross-reference — there are two canon indexes and they do not overlap.** This file is the
**existence** index: every row is a path the gate proves is present. `canon/refs/MANIFEST.md` is the
**P00 REF register**: it resolves `REF-NN` citations to titles, versions, lock status and consuming
workstreams, and carries the HISTORICAL aliases for the retired support-book numbers. **The
MarkLogic spines are deliberately absent from the REF register** — they are MarkLogic lineage, not
REFs, and no REF row is owed for them. A file may appear in both indexes; the questions they answer
are different.

| canon/marklogic/MarkLogic_Rules.md | REQUIRED |
| canon/marklogic/MarkLogic_BAN_Spine.md | REQUIRED |
| canon/marklogic/MarkLogic_ENG_Spine.md | REQUIRED |
| canon/marklogic/MarkLogic_MATH_Spine.md | REQUIRED |
| canon/marklogic/MarkLogic_SCI_BGS_Spine.md | REQUIRED |
| canon/marklogic/MarkLogic_QuestionPolicy.md | REQUIRED |
| canon/marklogic/C5_Bangla_Source_13-23.md | REQUIRED |
| canon/islamic-curation/REF-01_Curation_Policy.md | REQUIRED |
| canon/names/REF-20_Approved_Names_Pool.md | REQUIRED |
| canon/refs/MANIFEST.md | REQUIRED |
| canon/refs/SB_CITATION_BASELINE.md | REQUIRED |
| canon/refs/Bloom_Taxonomy_Comprehensive_Primer_Teachers_V1A.md | REQUIRED |
| canon/refs/_ref06_header.txt | REQUIRED |
| canon/refs/LOCKED_REF-02_Three_Layer_Lesson_Plan_Template_v1_6.md | REQUIRED |
| canon/refs/LOCKED_REF-03_Bangla_Subject_Spine_Playbook_v1_2.md | REQUIRED |
| canon/refs/LOCKED_REF-03_English_Subject_Spine_Playbook_v1_2.md | REQUIRED |
| canon/refs/LOCKED_REF-03_Math_Subject_Spine_Playbook_v1_0.md | REQUIRED |
| canon/refs/LOCKED_REF-03_Science_Subject_Spine_Playbook_v1_0.md | REQUIRED |
| canon/refs/LOCKED_REF-03_BGS_Subject_Spine_Playbook_v1_0.md | REQUIRED |
| canon/refs/NCTB_Stability_Analysis_Playbook.md | REQUIRED |
| canon/refs/Bloom_Taxonomy_Comprehensive_Primer_Teachers_V1A.docx | REQUIRED |
| canon/refs/LOCKED_REF-07_Revision_Architecture_v1_2.md | REQUIRED |
| canon/refs/LOCKED_REF-08_Homework_Architecture_v1_3.md | REQUIRED |
| canon/refs/LOCKED_REF-09_Tier1_Question_Setting_Guidelines_v1_0.md | REQUIRED |
| canon/refs/LOCKED_REF-10_Tier2_Question_Setting_Guidelines_v1_0.md | REQUIRED |
| canon/refs/LOCKED_REF-11_Classroom_Observation_Rubric_v1_1.md | REQUIRED |
| canon/refs/LOCKED_REF-12_School_Mission_and_Islamic_Values_Reference_v1_0.md | REQUIRED |
| canon/refs/LOCKED_REF-17_Blooms_Primer_V1B_Standard_Reference_v1_0.md | REQUIRED |
| canon/refs/LOCKED_REF-18_Blooms_Primer_V1C_Daily_Use_Pocket_v1_1.md | REQUIRED |
| canon/refs/LOCKED_REF-21_Curation_Trigger_Lexicon_Skeleton_Scan_Protocol_v1_0.md | REQUIRED |
| canon/refs/LOCKED_REF-22_English_Controlled_WordBank_C1-C5_v1_0.xlsx | REQUIRED |
| canon/refs/LOCKED_REF-23_Lean_Project_Scaffolding_Standard_v1_0.md | REQUIRED |
| canon/refs/LOCKED_REF-24_Teacher_Image_Handling_Protocol_v1_0.md | REQUIRED |
| canon/refs/LOCKED_REF-25_Paper_Assembly_Template_Standard_v1_0.md | REQUIRED |
| canon/refs/LOCKED_REF-26_Exam_Anchor_Set_v1_0.md | REQUIRED |
| canon/image-rules/IMAGE_RULES.md | REQUIRED |
| canon/language/LANGUAGE_RULES.md | REQUIRED |
| canon/school-facts/SCHOOL_FACTS.md | REQUIRED |
| canon/sources/SOURCE_POLICY.md | REQUIRED |
| canon/topics/LOCKED_REF-19_Vertical_Topic_Progression_Map_v1_10.md | REQUIRED |
| canon/topics/TOPIC_NUMBERS.md | REQUIRED |
| canon/DECISIONS.md | REQUIRED |
