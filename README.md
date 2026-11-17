# Artificial Intelligence in Accessibility Testing of Web and Mobile Applications: A Systematic Mapping Study — Replication package

Replication package of the paper *Artificial Intelligence in Accessibility Testing of Web and Mobile Applications: A Systematic Mapping Study* (Garcia, Rodrigues, Antonelli and Rodrigues). It contains the protocol, the search strings and log, the control set, the screening decisions, the extracted data, the decision log and the scripts that reproduce the counts and figures of the paper.

Version 1.0 (2026-11-17). Searches executed on 2026-10-13; publication period 2022–2026.

## Contents

| Path | Content |
|---|---|
| `protocol/protocol.md` | Objective, research questions, PIOC, selection criteria and data extraction form |
| `search/search_strings.md` | Executed strings per database, adaptations and filters |
| `search/search_log.csv` | Calibration (Scopus), execution, import and deduplication, with records and control-set recall |
| `control/control_set.csv` | Control set (8 in-scope studies) and the databases that retrieved each one |
| `selection/stage1_screening.csv` | Stage 1 decisions for the 331 records of queue 1 (analyzed subset) |
| `selection/stage2_fulltext.csv` | Stage 2 decisions for the 52 records read in full text |
| `extraction/extraction.csv` | Data extracted from the 38 included studies |
| `analysis/coding.csv` | Categories assigned to free-text fields after extraction, and short names used in the paper |
| `analysis/analysis.py` | Reproduces the selection counts, the frequencies per research question and the three figures |
| `analysis/figures/` | Figures of the paper (PDF and PNG) |
| `decisions/decision_log.md` | Methodological decisions, by phase |

## Numbers

| Step | Records |
|---|---|
| Retrieved (ACM DL 211, IEEE Xplore 776, Scopus 1,656, Web of Science 491) | 3,134 |
| Duplicates | 1,284 |
| Unique records | 1,850 |
| Queue 1 (analyzed subset), screened in Stage 1 | 331 |
| Stage 1: accepted / doubtful / rejected | 39 / 13 / 279 |
| Stage 2: full texts assessed | 52 |
| Stage 2: included / excluded | 38 / 14 |

Queues 2 (386 records) and 3 (1,133 records) are an ordering aid and remain to be screened (decision log, C2 and C3).

## Files

All files are UTF-8 CSV with a header row. `record_id` (`REG-nnnn`) identifies a unique record and is the key across files. `source` is the database of the retained copy after deduplication. Multi-valued fields use "; " as separator.

**`stage1_screening.csv`**: `stage1_decision` is Accepted, Rejected or Doubt. `stage1_criterion` is filled only for rejected records (first criterion identified). `stage1_tag` gives the type of reason:

| Tag | Meaning |
|---|---|
| AT | Assistive technology that does not evaluate the accessibility of an application |
| OFFDOMAIN | Other domain |
| SECONDARY | Secondary study |
| NOTICE | Retraction notice or erratum |
| AIGEN_EVAL | AI-generated code or content is the object evaluated |
| REPAIR_ONLY | AI only repairs or generates content; issues are not identified by AI |
| CODEGEN | Borderline study on AI code generation or repair, kept for the full-text stage |

**`stage2_fulltext.csv`**: `stage2_decision` is Accepted or Rejected; `stage2_criterion` and `stage2_tag` are filled for rejected records.

**`extraction.csv`**: one row per included study; fields described in `protocol/protocol.md`.

**`coding.csv`**:

| Column | Codes |
|---|---|
| `issues_code` (RQ4.1) | IMG images and alternative text; LBL names, labels and link purpose; CON color contrast and visual readability; STR structure and semantics (headings, landmarks, ARIA, tables, HTML validity); KBD keyboard, focus, interaction and target size; TXT readability, language and cognitive aspects; SR workflow-level barriers for screen reader users (mobile); MED multimedia; BROAD broad set of criteria; SAMP page sampling (no specific issue) |
| `limitations_code` (RQ6) | EVAL limited or no empirical evaluation; COV partial coverage of criteria, platforms or interaction; HAL errors, hallucinations, false positives or non-determinism; GT weak or missing ground truth; DEP dependence on the output of rule-based tools; REP insufficient description of the AI components; GEN limited generalizability; COST cost or dependence on proprietary models |
| `ground_truth_code` (RQ6) | NONE not described; HUMAN labels from the authors or experts; TOOL labels derived from rule-based tools or WCAG formulas; ACT W3C ACT test cases; USERS ratings by users |
| `contribution_code` (RQ5) | TOOL tool or system; METHOD method or framework; EMPIRICAL empirical evaluation of existing models; METRIC quality metric |
| `venue_type` | Conference or Journal |

## Reproducing the analysis

```
pip install -r analysis/requirements.txt
python analysis/analysis.py
```

The script prints the counts per stage and per research question and writes the figures to `analysis/figures/`.

## Not included

The database exports are not redistributed, since they contain abstracts subject to the publishers' terms of use; the strings in `search/search_strings.md` allow the searches to be re-run. Full texts of the primary studies are not included.

## License

Data and documentation: Creative Commons Attribution 4.0 International (CC BY 4.0). Code (`analysis/*.py`): MIT License. See `LICENSE`.

## How to cite

Garcia, A. C.; Rodrigues, S. S.; Antonelli, H.; Rodrigues, K. R. H. *Artificial Intelligence in Accessibility Testing of Web and Mobile Applications: A Systematic Mapping Study* — replication package, version 1.0, 2026.

## Contact

Anderson Canale Garcia — anderson.garcia@usp.br
