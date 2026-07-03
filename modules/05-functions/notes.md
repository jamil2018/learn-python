# Knowledge Notes: Functions

## Core Ideas

Functions give a name to reusable behavior.

```python
def add(a, b):
    return a + b
```

Use functions to separate logic from input and output.

## Parameters And Return Values

Parameters are inputs. `return` sends a result back.

```python
def area_rectangle(width, height):
    return width * height

area = area_rectangle(4, 5)
```

If a function has no `return`, it returns `None`.

## Default Arguments

```python
def format_currency(amount, symbol="$"):
    return f"{symbol}{amount:.2f}"
```

Avoid mutable default arguments like `items=[]`. Use `None` and create the list inside.

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

## Pure Functions

A pure function depends only on its inputs and returns a result without changing outside state.

```python
def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32
```

Pure functions are easier to test and reuse.

## Main Function

Scripts are easier to organize with `main()`.

```python
def main():
    print("Run program")

if __name__ == "__main__":
    main()
```

This lets another file import your functions without running the whole script.

## Recursion

Recursion means a function calls itself. It needs a base case.

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

Many beginner recursion problems can also be solved with loops. Learn both.

## Higher-Order Functions

Python functions are values. You can pass them around or return them.

```python
def make_multiplier(n):
    def multiply(value):
        return value * n
    return multiply
```

## Type Hints

Type hints document intent.

```python
def add(a: int, b: int) -> int:
    return a + b
```

They do not enforce types at runtime by default.

## Common Mistakes

- Printing inside a function when returning would be more reusable.
- Returning too many unrelated values as a tuple.
- Making one function do input, validation, calculation, and display.
- Forgetting the `main()` guard in reusable scripts.

