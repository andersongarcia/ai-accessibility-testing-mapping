# Protocol

Systematic mapping study on the use of Artificial Intelligence (AI) to identify accessibility issues in web and mobile applications. The protocol was planned in Parsif.al following the guidelines for systematic mapping studies in software engineering (Petersen et al., 2015; Kitchenham and Charters, 2007; Felizardo et al., 2017). Decisions taken while applying it are listed in `decisions/decision_log.md`.

## Objective

To map the state of the art on the use of AI techniques as a means of testing and evaluating the accessibility of web and mobile software applications, identifying approaches, tools, AI techniques, accessibility issues addressed, target disabilities, the stages of the software development life cycle (SDLC) in which AI is applied, and open research gaps.

## Research questions

| ID | Question |
|---|---|
| RQ1 | How has AI been used to identify accessibility issues (testing, evaluation, detection, inspection) in web and mobile applications? |
| RQ2 | What types of Artificial Intelligence techniques and models are employed? |
| RQ3 | What roles does AI play in the identification of accessibility issues? |
| RQ4.1 | Which accessibility issues and guidelines (e.g., WCAG) does the AI-based identification target? |
| RQ4.2 | Which target disabilities are supported, and is the target disability explicitly stated by the study? |
| RQ5 | What tools, frameworks, models, or approaches have been proposed? |
| RQ6 | What are the main limitations, open challenges and research gaps of AI-based identification of accessibility issues? |

## PIOC

- **Population:** web and mobile applications, software user interfaces, digital accessibility testing and evaluation.
- **Intervention:** AI techniques (machine learning, deep learning, natural language processing, computer vision, large language models, generative AI).
- **Outcome:** AI-based identification of accessibility issues (automated detection, violation prediction, visual inspection, test generation and compliance auditing); remediation is considered only when it follows an AI-based identification.
- **Context:** software engineering, automated testing, quality assurance and CI/CD pipelines.

## Sources and search

ACM Digital Library, IEEE Xplore, Scopus and Web of Science Core Collection (strings in `search/search_strings.md`; calibration and execution in `search/search_log.csv`; control set in `control/control_set.csv`).

## Selection criteria

**Inclusion (IC1):** primary study, written in English, with full text available, that uses Artificial Intelligence as a means to test, evaluate, detect, or inspect accessibility issues in web or mobile software applications; remediation approaches are included only when the issues are identified by AI.

**Exclusion:** EC1 not in English; EC2 duplicate; EC3 not peer-reviewed; EC4 not a primary study; EC5 not related to AI; EC6 not related to digital accessibility; EC7 not related to software applications; EC8 does not address accessibility testing, evaluation, detection or analysis; EC9 no full text available. Operationalization of EC5 and EC8: decision log, entries C6 and C8.

**Process:** Stage 1 on title, abstract and keywords; Stage 2 on the full text (decision log, section 3).

## Data extraction form

| Field (column in `extraction/extraction.csv`) | Values | RQ |
|---|---|---|
| Source (`source`) | ACM Digital Library, IEEE Xplore, Scopus, Web of Science (database of the retained copy) | – |
| Type of study (`type_of_study`) | Case study; Empirical study; Experiment; Proposal; Tool; Not specified | RQ1 |
| Context (`context`) | Web; Mobile; Both; Not specified | RQ1 |
| AI input, analyzed artifact (`ai_input`) | Source code/DOM; Rendered UI/screenshot; GUI/accessibility tree; Images/alt text; Textual content; Runtime interaction; Not specified | RQ1, RQ3 |
| Relation to rule-based tools (`relation_to_rule_based_tools`) | AI only; Hybrid (AI + rule-based tool); Compared with rule-based tools; Not specified | RQ1 |
| SDLC phase (`sdlc_phase`) | Requirements; Design; Implementation; Testing; Deployment/Maintenance; Not specified | RQ1 |
| AI technique (`ai_technique`) | Computer Vision; Deep Learning; LLM / Generative AI; Machine Learning; NLP; Not specified | RQ2 |
| Model(s) (`models`) | Free text | RQ2 |
| AI role in testing (`ai_role`) | Issue detection; Issue classification; Test generation; Recommendation of fixes; Automatic remediation; Support to the evaluation process | RQ3 |
| Accessibility issues addressed (`accessibility_issues`) | Free text (WCAG success criteria and other guidelines) | RQ4.1 |
| Target disability (`target_disability`) | Auditory impairment; Cognitive impairment; Motor impairment; Visual impairment; Multiple / Generic; Not specified | RQ4.2 |
| Disability explicitly stated? (`disability_explicitly_stated`) | Stated by the study; Inferred by the reviewer; Not specified | RQ4.2 |
| Main contribution (`main_contribution`) | Free text (tool, dataset, architecture, benchmark) | RQ5 |
| Validation method (`validation_method`) | Automated benchmark / Dataset; Comparison with static tools; Expert review; User study; None / Proof of concept | RQ6 |
| Ground truth and metrics (`ground_truth_and_metrics`) | Free text (labeling source, size, metrics) | RQ6 |
| Limitations (`limitations`) | Free text | RQ6 |

Multi-valued fields use "; " as separator. No quality assessment was applied (decision log, P8).
