# Python Notes For TypeScript Developers

Use this as a lookup sheet, not a tutorial.

## Mental Model Shifts

Python values are strongly typed at runtime, but variables do not declare their type by default.

```python
name = "Ada"
age = 36
```

Type hints exist and are useful, but they are optional and not enforced by Python at runtime.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

## Indentation Is Syntax

Python uses indentation instead of braces.

```python
if score >= 90:
    print("excellent")
else:
    print("keep practicing")
```

## Common TypeScript To Python Translations

| TypeScript | Python |
| --- | --- |
| `const name = "Ada"` | `name = "Ada"` |
| `let count = 0` | `count = 0` |
| `true`, `false` | `True`, `False` |
| `null` | `None` |
| `arr.push(x)` | `arr.append(x)` |
| `arr.length` | `len(arr)` |
| `obj.key` | `dict_obj["key"]` |
| `for (const x of xs)` | `for x in xs:` |
| `try { ... } catch (err) { ... }` | `try: ... except Exception as err:` |

## Collections

Lists are ordered and mutable.

```python
numbers = [1, 2, 3]
numbers.append(4)
```

Tuples are ordered and usually treated as immutable records.

```python
point = (10, 20)
```

Dictionaries are key-value mappings.

```python
user = {"name": "Ada", "role": "admin"}
```

Sets store unique values.

```python
tags = {"python", "cli", "practice"}
```

## Truthiness

These are falsy: `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`.

Everything else is usually truthy.

## Functions

Python supports default arguments, keyword arguments, `*args`, and `**kwargs`.

```python
def invoice_total(subtotal: float, tax_rate: float = 0.08) -> float:
    return subtotal + subtotal * tax_rate

invoice_total(100)
invoice_total(subtotal=100, tax_rate=0.12)
```

Avoid mutable defaults:

```python
def add_item(item: str, items: list[str] | None = None) -> list[str]:
    if items is None:
        items = []
    items.append(item)
    return items
```

## Exceptions

Python code often uses exceptions for failure paths.

```python
try:
    amount = int(input("Amount: "))
except ValueError:
    print("Please enter a whole number.")
```

Catch specific exceptions when you can.

## Files

Use `with` so files are closed automatically.

```python
from pathlib import Path

path = Path("data.txt")
text = path.read_text()
path.write_text(text.upper())
```

## Modules

Every `.py` file is a module. A directory with Python files can become a package.

```python
from pathlib import Path
from collections import Counter
```

Use the main guard for scripts:

```python
def main() -> None:
    print("Run the program")

if __name__ == "__main__":
    main()
```

## Pythonic Style

Prefer direct iteration:

```python
for name in names:
    print(name)
```

Use `enumerate` when you need indexes:

```python
for index, name in enumerate(names, start=1):
    print(index, name)
```

Use comprehensions when they stay readable:

```python
squares = [n * n for n in numbers]
active_users = [user for user in users if user["active"]]
```

## Testing

Start with plain `assert`, then move to `pytest`.

```python
def add(a: int, b: int) -> int:
    return a + b

def test_add() -> None:
    assert add(2, 3) == 5
```

## Recommended Standard Library Areas

- `pathlib`: file paths
- `json`: JSON reading and writing
- `csv`: CSV files
- `argparse`: command-line interfaces
- `datetime`: dates and times
- `collections`: `Counter`, `defaultdict`, `deque`
- `itertools`: iterator tools
- `dataclasses`: lightweight data objects
- `typing`: type hints
- `unittest.mock`: mocks for testing
- `asyncio`: asynchronous work

