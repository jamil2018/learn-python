# Knowledge Notes: Data Wrangling

## Core Ideas

Data wrangling means turning messy input into useful output.

Typical flow:

1. Load raw data.
2. Validate and clean rows.
3. Normalize values.
4. Transform records.
5. Summarize or export.

## Cleaning Values

Raw CSV values are usually strings.

```python
amount = float(row["amount"])
category = row["category"].strip().lower()
```

Decide how to handle missing values:

- reject the row
- fill a default
- keep it but mark it incomplete

## Normalization

Normalization makes inconsistent values consistent.

```python
category_map = {
    "food": "Food",
    "groceries": "Food",
    "grocery": "Food",
}
```

Normalize early so later grouping is accurate.

## Grouping

Nested dictionaries are useful for summaries.

```python
totals = {}
for row in rows:
    category = row["category"]
    totals[category] = totals.get(category, 0) + row["amount"]
```

`defaultdict` can reduce boilerplate once you understand the plain version.

## Dates

Use `datetime` for real date parsing.

```python
from datetime import datetime

date = datetime.strptime("2026-07-03", "%Y-%m-%d").date()
month = date.strftime("%Y-%m")
```

## Reports

A good report answers a question:

- What are the top categories?
- Which month had the highest total?
- Which rows are duplicates?
- Which values look suspicious?

## Common Mistakes

- Cleaning data after summarizing it.
- Treating empty strings as valid values by accident.
- Sorting numbers while they are still strings.
- Overwriting raw input before you trust the cleaning logic.

