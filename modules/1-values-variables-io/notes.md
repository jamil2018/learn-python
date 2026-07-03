# Knowledge Notes: Values, Variables, And Basic I/O

## Core Ideas

Python programs are made from statements. A statement can assign a value, call a function, or control what happens next.

```python
name = "Ada"
age = 36
print(name, age)
```

Variables do not need declarations. A variable name points to a value, and the value has a type.

Common beginner types:

- `str`: text, such as `"Python"`
- `int`: whole numbers, such as `42`
- `float`: decimal numbers, such as `3.14`
- `bool`: `True` or `False`
- `None`: the absence of a value

## Printing

`print()` writes values to the terminal.

```python
print("Hello")
print("Total:", 25)
```

Use f-strings when you want readable formatted output.

```python
name = "Ada"
print(f"Hello, {name}")
```

## Input

`input()` always returns a string.

```python
age_text = input("Age: ")
age = int(age_text)
```

Convert input before doing math:

- `int("10")` gives `10`
- `float("10.5")` gives `10.5`
- `str(10)` gives `"10"`

## Math Operators

```python
total = 10 + 3
difference = 10 - 3
product = 10 * 3
quotient = 10 / 3
whole_quotient = 10 // 3
remainder = 10 % 3
power = 10 ** 3
```

`/` always returns a float. Use `//` for floor division and `%` for remainders.

## Naming

Python uses `snake_case` for variables and functions.

```python
download_speed_mbps = 25
file_size_mb = 100
```

Prefer names that describe meaning, not type. `bill_total` is better than `number`.

## Formatting Numbers

Use `round()` for simple rounding.

```python
result = round(10 / 3, 2)
```

Use format specifiers for display.

```python
amount = 12.5
print(f"${amount:.2f}")
```

## TypeScript Lens

Python is strongly typed, but variables are not declared with types by default. This means `age = "36"` is a string until you explicitly convert it.

TypeScript:

```typescript
const age = Number(input)
```

Python:

```python
age = int(input_text)
```

## Common Mistakes

- Trying to do math with raw `input()` strings.
- Forgetting that Python uses `True`, `False`, and `None` with capital letters.
- Using camelCase names out of TypeScript habit.
- Formatting money with `round()` but printing inconsistent decimal places.

