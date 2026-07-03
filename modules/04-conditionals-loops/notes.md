# Knowledge Notes: Conditionals And Loops

## Core Ideas

Conditionals choose a path. Loops repeat work.

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("Keep practicing")
```

Python uses indentation instead of braces.

## Comparisons

```python
age >= 18
name == "Ada"
status != "done"
count < limit
```

Combine conditions with `and`, `or`, and `not`.

```python
if age >= 18 and has_ticket:
    print("Enter")
```

## Truthiness

Falsy values include:

- `False`
- `None`
- `0`
- `""`
- `[]`
- `{}`
- `set()`

This lets you write:

```python
if not name:
    print("Name is required")
```

## For Loops

Use `for` when looping over a known collection or range.

```python
for number in range(1, 6):
    print(number)

for name in names:
    print(name)
```

`range(1, 6)` gives `1, 2, 3, 4, 5`.

## While Loops

Use `while` when repeating until a condition changes.

```python
choice = ""
while choice != "q":
    choice = input("Choice: ")
```

Menu programs often use `while True` plus `break`.

## Break And Continue

```python
for number in numbers:
    if number < 0:
        continue
    if number == target:
        break
```

`continue` skips to the next loop iteration. `break` exits the loop.

## State

Interactive programs need state: score, balance, inventory, attempts, current room.

Keep state in clearly named variables or dictionaries. Update it in one obvious place.

## TypeScript Lens

Python has no braces around blocks. The indentation is not style; it is the syntax. Python also has no `switch` in older versions, so many beginner programs use `if`/`elif` or dictionaries of actions later.

## Common Mistakes

- Writing a `while` loop whose condition never changes.
- Using `=` instead of `==` in comparisons. Python will usually reject this.
- Forgetting that `range(stop)` stops before `stop`.
- Letting menu logic and business logic become one giant block.

