# Search strings

The four digital libraries below were last searched on **2026-10-13**. The strings are the ones executed; per-database adaptations are described after each string. The calibration that led to the final string (T3) is recorded in `search_log.csv`.

## Structure

| Clause | PIOC facet | Terms |
|---|---|---|
| 1 | Outcome (accessibility) | "accessibility", "WCAG" |
| 2 | Intervention (AI) | "artificial intelligence", "AI", "machine learning", "deep learning", "computer vision", "natural language processing", "large language model*", "LLM", "LLMs" |
| 3 | Outcome (testing) | "test\*", "evaluat\*", "assess\*", "detect\*", "inspect\*", "audit\*", "validat\*" |
| 4 | Population (platform) | "web", "mobile", "android", "ios", "website\*", "web app\*", "mobile app\*" |

Filters: publication years 2022–2026; English; conference papers and journal articles; computer science (where the database allows these filters).

## Scopus (Advanced search, Documents) — 1,656 records

```
TITLE-ABS-KEY(("accessibility" OR "WCAG") AND ("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "computer vision" OR "natural language processing" OR "large language model*" OR "LLM" OR "LLMs") AND ("test*" OR "evaluat*" OR "assess*" OR "detect*" OR "inspect*" OR "audit*" OR "validat*") AND ("web" OR "mobile" OR "android" OR "ios" OR "website*" OR "web app*" OR "mobile app*")) AND LANGUAGE(english) AND SUBJAREA(COMP) AND (DOCTYPE(cp) OR DOCTYPE(ar)) AND PUBYEAR > 2021
```

## ACM Digital Library — 211 records

Filters: `AfterYear=2022`, `BeforeYear=2026`. The ACM DL does not accept wildcards inside quotes, so stems are written without quotes; "large language model*" is written as two phrases; "web app\*" and "mobile app\*" are subsumed by "web" and "mobile". No language or subject filter is available.

```
(Title:("accessibility" OR "WCAG") OR Abstract:("accessibility" OR "WCAG") OR Keyword:("accessibility" OR "WCAG")) AND (Title:("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "computer vision" OR "natural language processing" OR "large language model" OR "large language models" OR "LLM" OR "LLMs") OR Abstract:("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "computer vision" OR "natural language processing" OR "large language model" OR "large language models" OR "LLM" OR "LLMs") OR Keyword:("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "computer vision" OR "natural language processing" OR "large language model" OR "large language models" OR "LLM" OR "LLMs")) AND (Title:(test* OR evaluat* OR assess* OR detect* OR inspect* OR audit* OR validat*) OR Abstract:(test* OR evaluat* OR assess* OR detect* OR inspect* OR audit* OR validat*) OR Keyword:(test* OR evaluat* OR assess* OR detect* OR inspect* OR audit* OR validat*)) AND (Title:(web OR mobile OR android OR ios OR website*) OR Abstract:(web OR mobile OR android OR ios OR website*) OR Keyword:(web OR mobile OR android OR ios OR website*))
```

## IEEE Xplore (Command Search) — 776 records

Filters (URL parameters): `ranges=2022_2026_Year`, `refinements=ContentType:Conferences`, `refinements=ContentType:Journals`. The accessibility and AI clauses are searched in Document Title, Abstract and Author Keywords (one field per term, since grouped syntax is not accepted); the testing and platform clauses in Abstract. Because of the limit of ten wildcards, "large language model\*" is written as two phrases. No language or subject filter is available. Results were exported as CSV and converted to BibTeX.

```
(("Document Title":"accessibility" OR "Abstract":"accessibility" OR "Author Keywords":"accessibility" OR "Document Title":"WCAG" OR "Abstract":"WCAG" OR "Author Keywords":"WCAG") AND ("Document Title":"artificial intelligence" OR "Abstract":"artificial intelligence" OR "Author Keywords":"artificial intelligence" OR "Document Title":"AI" OR "Abstract":"AI" OR "Author Keywords":"AI" OR "Document Title":"machine learning" OR "Abstract":"machine learning" OR "Author Keywords":"machine learning" OR "Document Title":"deep learning" OR "Abstract":"deep learning" OR "Author Keywords":"deep learning" OR "Document Title":"computer vision" OR "Abstract":"computer vision" OR "Author Keywords":"computer vision" OR "Document Title":"natural language processing" OR "Abstract":"natural language processing" OR "Author Keywords":"natural language processing" OR "Document Title":"large language model" OR "Abstract":"large language model" OR "Author Keywords":"large language model" OR "Document Title":"large language models" OR "Abstract":"large language models" OR "Author Keywords":"large language models" OR "Document Title":"LLM" OR "Abstract":"LLM" OR "Author Keywords":"LLM" OR "Document Title":"LLMs" OR "Abstract":"LLMs" OR "Author Keywords":"LLMs") AND ("Abstract":"test*" OR "Abstract":"evaluat*" OR "Abstract":"assess*" OR "Abstract":"detect*" OR "Abstract":"inspect*" OR "Abstract":"audit*" OR "Abstract":"validat*") AND ("Abstract":"web" OR "Abstract":"mobile" OR "Abstract":"android" OR "Abstract":"ios" OR "Abstract":"website*" OR "Abstract":"web app*" OR "Abstract":"mobile app*"))
```

## Web of Science Core Collection (Advanced Search) — 491 records

`TS` also covers Keywords Plus, which is slightly broader than `TITLE-ABS-KEY` in Scopus.

```
TS=(("accessibility" OR "WCAG") AND ("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "computer vision" OR "natural language processing" OR "large language model*" OR "LLM" OR "LLMs") AND ("test*" OR "evaluat*" OR "assess*" OR "detect*" OR "inspect*" OR "audit*" OR "validat*") AND ("web" OR "mobile" OR "android" OR "ios" OR "website*" OR "web app*" OR "mobile app*")) AND PY=(2022-2026) AND LA=(English) AND DT=(Article OR "Proceedings Paper") AND SU=("Computer Science")
```

## Taylor & Francis Online — 5 records (not imported)

Searched in the Abstract field with `AfterYear=2022` and `BeforeYear=2026`. The five records were all outside the scope and were not imported.

```
("accessibility" OR "WCAG") AND ("artificial intelligence" OR "AI" OR "machine learning" OR "deep learning" OR "computer vision" OR "natural language processing" OR "large language model*" OR "LLM" OR "LLMs") AND ("test*" OR "evaluat*" OR "assess*" OR "detect*" OR "inspect*" OR "audit*" OR "validat*") AND ("web" OR "mobile" OR "android" OR "ios" OR "website*" OR "web app*" OR "mobile app*")
```

## Planned but not searched separately

- **ScienceDirect**: rejects the string (maximum of eight Boolean connectors per field; no wildcards).
- **Springer Link**: searches full text only (32,018 results for the string).

Their journals and proceedings are indexed by Scopus and Web of Science, which are searched on title, abstract and keywords (see `decisions/decision_log.md`).

## Records not exported

The database exports (with abstracts) are not redistributed because of the publishers' terms of use. The selection files list the DOI, title, authors, year and source of each record, and the strings above allow the searches to be re-run.
