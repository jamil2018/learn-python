# Knowledge Notes: Testing, Debugging, And Refactoring

## Core Ideas

Tests are executable expectations. They make refactoring safer.

Start with simple `assert` statements:

```python
assert add(2, 3) == 5
```

Then move to `pytest` for real projects.

## Pytest Basics

Test files usually start with `test_`.

```python
def test_add():
    assert add(2, 3) == 5
```

Run tests with:

```bash
pytest
```

## Testing Errors

```python
import pytest

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
```

Test both happy paths and failure paths.

## Testing Files

Use temporary directories instead of writing to real project files.

```python
def test_save(tmp_path):
    path = tmp_path / "data.txt"
    save_text(path, "hello")
    assert path.read_text() == "hello"
```

## Debugging

Basic debugging loop:

1. Reproduce the bug.
2. Make the failing case small.
3. Inspect values.
4. Fix the cause.
5. Add a regression test.

`print()` debugging is fine if you remove the prints after.

## Refactoring

Refactoring changes structure without changing behavior.

Good refactoring targets:

- long functions
- repeated code
- unclear names
- mixed input/output and logic
- functions that do too many things

Write tests before risky refactors.

## Type Hints

Type hints make intent clearer.

```python
def normalize_name(name: str) -> str:
    return name.strip().title()
```

Type hints are not a replacement for tests.

## Common Mistakes

- Only testing the examples that already work.
- Testing terminal input directly instead of testing helper functions.
- Refactoring and changing behavior at the same time.
- Adding type hints that lie or are too vague to help.

