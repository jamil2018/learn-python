# Knowledge Notes: Files, Paths, JSON, And CSV

## Core Ideas

Files let your programs persist data between runs. In Python, prefer `pathlib.Path` for paths.

```python
from pathlib import Path

path = Path("notes.txt")
```

## Reading And Writing Text

```python
text = path.read_text()
path.write_text("Hello\n")
```

For appending:

```python
with path.open("a") as file:
    file.write("New line\n")
```

Use `with` when manually opening files so Python closes them automatically.

## Paths

```python
folder = Path("data")
file_path = folder / "expenses.csv"
```

Useful path methods:

```python
path.exists()
path.is_file()
path.is_dir()
path.glob("*.txt")
path.rglob("*.py")
```

## JSON

JSON is good for nested structured data.

```python
import json

data = {"name": "Ada", "active": True}
path.write_text(json.dumps(data, indent=2))
loaded = json.loads(path.read_text())
```

Python maps JSON values like this:

- JSON object -> `dict`
- JSON array -> `list`
- JSON string -> `str`
- JSON number -> `int` or `float`
- JSON `true`/`false` -> `True`/`False`
- JSON `null` -> `None`

## CSV

CSV is good for table-shaped data.

```python
import csv

with Path("expenses.csv").open() as file:
    reader = csv.DictReader(file)
    rows = list(reader)
```

Use `DictReader` and `DictWriter` when columns have names.

## Data Boundaries

When reading from files, assume the data may be messy:

- Missing file
- Empty file
- Invalid JSON
- Missing columns
- Strings where you expected numbers

Validation becomes important in the next module.

## Common Mistakes

- Hardcoding absolute paths.
- Loading a huge file entirely into memory when line-by-line would work.
- Treating CSV numbers as numbers before converting them from strings.
- Overwriting original input files while experimenting.

