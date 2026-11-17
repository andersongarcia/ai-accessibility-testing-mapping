# Decision log

Methodological decisions of the systematic mapping, grouped by phase. Each entry states the decision, its rationale and its effect on the data in this package. The only dates recorded are the milestones of the study (search execution and the data release).

## 1. Planning

**P1. Scope covers any disability.** The target disability is an extraction field (with "explicitly stated by the study", "inferred by the reviewer" or "not specified"), not a search facet or a selection criterion. *Rationale:* a visual-impairment facet strongly reduced the recall of the control set during calibration (configuration C1 in `search/search_log.csv`), and only 2 of 15 abstracts of the source studies of the control set mentioned visual impairment. *Effect:* RQ4.2 is answered from the extraction.

**P2. Accessibility testing is defined operationally.** *Accessibility testing* denotes the identification of accessibility issues (testing, evaluating, detecting or inspecting) in a web or mobile application. A study is in scope when AI performs, decides or supports this identification, including support to the evaluation process without emitting the violation judgment (e.g., sampling pages, prioritizing or reporting issues, building evaluation heuristics). Out of scope: studies in which AI-generated code or content is the object evaluated; studies in which AI only repairs, generates or adapts content without identifying issues; assistive technologies that do not evaluate an application.

**P3. PIOC instead of PICOC.** The Comparison facet is omitted because a mapping study does not compare interventions. Population: web and mobile applications and their user interfaces; Intervention: AI techniques; Outcome: AI-based identification of accessibility issues (remediation considered only when it follows AI-based identification); Context: software engineering, automated testing, quality assurance and CI/CD.

**P4. Research question RQ4 split in two.** RQ4.1 (issues and guidelines) and RQ4.2 (target disabilities) are independent questions and are extracted separately.

**P5. English-language, peer-reviewed studies only.** Grey literature and preprints are excluded (a multivocal review would require a different design). This also applies to the control set.

**P6. Publication period 2022–2026.** The period captures the emergence of large language models (from late 2022) and about one year of earlier machine learning and computer vision work. Extending the period to 2020 would add about 84 records in Scopus. Records indexed by the databases with year 2027 were kept; none of the included studies is dated 2027.

**P7. Selection criteria.** One inclusion criterion: *primary study, written in English, with full text available, that uses Artificial Intelligence as a means to test, evaluate, detect, or inspect accessibility issues in web or mobile software applications; remediation approaches are included only when the issues are identified by AI.* Nine exclusion criteria, numbered in the order of the protocol: EC1 not in English; EC2 duplicate; EC3 not peer-reviewed; EC4 not a primary study; EC5 not related to AI; EC6 not related to digital accessibility; EC7 not related to software applications; EC8 does not address accessibility testing, evaluation, detection or analysis; EC9 no full text available.

**P8. No quality assessment.** No quality scores were applied to the primary studies; the mapping characterizes the literature, and the validation reported by each study is extracted (RQ6).

**P9. Extraction form.** Sixteen fields (see `protocol/protocol.md`). Fields with predefined values accept several values separated by "; ". The form includes the analyzed artifact, the relation to rule-based tools, the development phase (SDLC), the models and the ground truth and metrics, in addition to the bibliographic and classification fields.

## 2. Search

**S1. Volume target of 1,000–1,500 Scopus records**, so that screening remained feasible.

**S2. Calibration in Scopus.** Fifteen configurations were tested against the control set (`search/search_log.csv`). From the base configuration D4, "validat\*" was added to the testing clause to retrieve a control study that uses only validation terminology, and "AI" was added to the AI clause. "AI" is kept as the standard abbreviation in the field; it was first added to retrieve a study of the source set that was later found to be outside the scope of this mapping. No other term depends on studies outside the scope.

**S3. Final string T3 accepted above the volume target.** T3 returned 1,634 records during calibration (about 9% above the target) and full recall of the Scopus-indexed in-scope control studies (6/6); it returned 1,656 records when executed.

**S4. Control set.** The control set is drawn from a recent study on AI agents for web accessibility (S001) and the relevant references it cites, restricted to peer-reviewed studies within the scope of this mapping (P2): eight studies (`control/control_set.csv`). Seven are retrieved in the union of the four databases; B017 was not found in any of the four databases by title searches without filters, and its venue, a health informatics journal, is classified outside Computer Science in Scopus; its absence reflects database coverage rather than the search string, and it is kept as a documented miss. The control set validates the search, not the selection decisions.

**S5. Databases.** ACM Digital Library, IEEE Xplore, Scopus and Web of Science Core Collection were searched on 2026-10-13 with the adaptations described in `search/search_strings.md`. In IEEE Xplore the search was restricted to title, abstract and author keywords to align with Scopus (the "All Metadata" field returned 1,722 records with a high share of off-topic results).

**S6. Taylor & Francis searched, not imported.** Five records, none in scope.

**S7. ScienceDirect and Springer Link not searched separately.** ScienceDirect rejects the string (limit of eight Boolean connectors per field, no wildcards) and Springer Link searches only full text. The search is on title, abstract and keywords, and Scopus and Web of Science index the journals and proceedings of both publishers. Splitting the string into dozens of ScienceDirect queries was considered and not adopted. Reported as a threat to validity.

**S8. Import and deduplication.** The four exports (3,134 records) were imported into Parsif.al, and the imported count was checked against the exported count per database (BibTeX keys containing spaces had to be corrected before import). Automatic duplicate detection marked 1,256 records; a cross-check by DOI and normalized title found 28 residual copies with spelling differences, which were marked manually. Result: 1,284 duplicates and 1,850 unique records, each duplicate group with exactly one retained copy.

**S9. Testing terms not in the string.** The testing clause does not include identif\*, check\*, verif\*, violation\* or complian\*. A Scopus check with these terms (same filters, excluding T3 results) returned 172 additional records, 13 of which mention WCAG or accessibility issues, and few appear in scope by title. The executed string is reported as is; a complementary search with these terms is planned for the continuation of the study.

## 3. Selection

**C1. Screening in a spreadsheet.** Stage 1 (title, abstract, keywords) and Stage 2 (full text) were recorded in a spreadsheet generated from the Parsif.al export; each unique record received an identifier (`REG-nnnn`) used in all files of this package.

**C2. Screening queues.** Unique records were ordered in three queues computed from the search vocabulary: queue 1 (331) has accessibility and AI terms in the title or keywords; queue 2 (386) has accessibility terms only there, or repeated accessibility terms in the abstract; queue 3 (1,133) holds the rest. The queues are an ordering aid, computed by rules, and never change a decision.

**C3. Analyzed subset.** Queue 1 was fully screened and is the subset analyzed in the paper; queues 2 and 3 (1,519 records) are left for the continuation of the study.

**C4. Recording rule.** When more than one exclusion criterion applies, the first one identified by the reviewer is recorded. Accepted records carry no criterion (they meet the inclusion criterion). Doubtful records carry no criterion and are decided in Stage 2 on the full text.

**C5. Tags for the type of reason.** Rejected records also receive a tag: AT (assistive technology that does not evaluate an application), OFFDOMAIN (other domain), SECONDARY (secondary study), NOTICE (retraction or erratum), AIGEN_EVAL (AI-generated code or content is the object evaluated), REPAIR_ONLY (AI only repairs or generates content; issues not identified by AI). CODEGEN marks borderline studies on AI code generation or repair that were kept for the full-text stage, where they were decided as included (AI identifies issues) or REPAIR_ONLY. Because the recorded criterion is the first one identified (C4), the same tag may appear under different criteria.

**C6. Assistive technologies and AI as the object evaluated.** Both are rejected under EC8, which was operationalized to cover (a) assistive technologies that do not evaluate the accessibility of an application, (b) studies in which AI is only the object evaluated and (c) studies in which AI only repairs or generates content without identifying issues.

**C7. Two passes in Stage 1.** In the first pass, borderline studies of the two kinds described in C6(b) and C6(c) were recurrent. The scope was then made explicit (P2) without changing the criteria, and a second pass re-screened all records accepted or marked as doubtful in the first pass. Records rejected in the first pass were not re-screened, since the explicit scope is narrower. Final Stage 1 result for queue 1: 39 accepted, 13 doubtful, 279 rejected.

**C8. What counts as AI (EC5).** EC5 is applied when no AI technique makes or supports the accessibility judgment: classical image processing or fixed-formula metrics (e.g., pixel comparison, thresholding, interface metrics, spectral-residual saliency), even when described as computer vision; and machine learning used only as an auxiliary pre-processing step (e.g., color quantization before a contrast formula) while the judgment relies on deterministic rules. Trained models that decide or support the identification (e.g., OCR used as an observer of rendered text or to locate text, decision trees, random forests, CNNs, LLMs, vision-language models) count as AI, as does unsupervised learning that is the core of an approach supporting the evaluation (e.g., clustering to sample pages). Three studies were excluded in Stage 2 under this rule.

**C9. Full text unavailable.** Two studies whose full text could not be obtained (including requests to the authors) were excluded under EC9.

**C10. Image descriptions as web content.** A study that grades image descriptions taken from an image-captioning dataset was kept: the technique evaluates image descriptions as web content (WCAG 1.1.1), regardless of the origin of the data.

**C11. Single reviewer.** Screening (both stages) and data extraction were performed by the first author. No inter-rater agreement was measured; an agreement check with the co-authors is planned for the continuation of the study. Mitigations: operational criteria (P2, C6, C8), tags (C5) and the decision files in this package.

## 4. Extraction

**E1. Extraction on the full text** of the 38 included studies with the form of P9 (`extraction/extraction.csv`). Values not reported by a study are recorded as "Not specified".

**E2. Coding of free-text fields after extraction.** Accessibility issues (RQ4.1), limitations and ground truth (RQ6) and the type of contribution (RQ5) were grouped into categories after extraction (`analysis/coding.csv`; codes explained in the README).

## 5. Synthesis

**Y1. Frequencies and cross-tabulations per research question.** Multi-valued fields count each study once per value, so percentages per field may add up to more than 100%. `analysis/analysis.py` reproduces the counts and figures of the paper from the files of this package.
