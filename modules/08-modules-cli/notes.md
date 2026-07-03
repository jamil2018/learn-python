# Knowledge Notes: Modules, Packages, And Command-Line Interfaces

## Core Ideas

Every `.py` file is a module. A folder of Python files can become a package.

```text
toolkit/
  __init__.py
  __main__.py
  cli.py
  converters.py
```

`__init__.py` marks a package. `__main__.py` lets you run it with `python -m toolkit`.

## Imports

```python
from pathlib import Path
from toolkit.converters import celsius_to_fahrenheit
```

Keep reusable logic importable. Avoid putting important logic only inside interactive prompts.

## Main Guard

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

This prevents a script from running immediately when imported.

## Argparse

`argparse` builds command-line interfaces.

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("name")
parser.add_argument("--uppercase", action="store_true")
args = parser.parse_args()
```

Subcommands are useful for tools with multiple actions.

```python
subparsers = parser.add_subparsers(dest="command", required=True)
subparsers.add_parser("list")
subparsers.add_parser("add")
```

## Separating CLI From Logic

Good shape:

- `cli.py`: parse args and print output
- `storage.py`: read and write files
- `models.py`: data shapes
- `commands.py`: application actions

This makes code easier to test.

## Config

Configuration can come from:

- command-line flags
- environment variables
- config files
- defaults in code

Use the simplest source that fits the project.

## Common Mistakes

- Parsing command-line args inside pure functions.
- Running code at import time.
- Creating circular imports.
- Making one giant `cli.py` that owns all behavior.

