# Knowledge Notes: Iteration, Comprehensions, And Pythonic Data Processing

## Core Ideas

Python is strongest when you iterate directly over data.

```python
for name in names:
    print(name)
```

Avoid index loops unless the index matters.

## Enumerate And Zip

Use `enumerate()` when you need positions.

```python
for index, item in enumerate(items, start=1):
    print(index, item)
```

Use `zip()` to pair sequences.

```python
for name, score in zip(names, scores):
    print(name, score)
```

## Comprehensions

List comprehension:

```python
squares = [n * n for n in numbers]
```

Filtering:

```python
active = [user for user in users if user["active"]]
```

Dictionary comprehension:

```python
lookup = {user["id"]: user for user in users}
```

Use comprehensions when they improve clarity. A normal loop is better for complex logic.

## Built-In Helpers

```python
any(values)
all(values)
sum(numbers)
sorted(items, key=lambda item: item["name"])
```

`any()` asks "does at least one pass?" and `all()` asks "do all pass?"

## Collections Module

```python
from collections import Counter, defaultdict

counts = Counter(words)
groups = defaultdict(list)
```

`Counter` is ideal for frequencies. `defaultdict(list)` is ideal for grouping.

## Generators

Generators produce values lazily.

```python
def even_numbers(limit):
    for number in range(limit):
        if number % 2 == 0:
            yield number
```

Use generators when processing large or streaming data.

## Common Mistakes

- Writing a clever one-liner that is harder to read than a loop.
- Using `sorted()` when you meant to mutate with `.sort()`, or the reverse.
- Forgetting that `zip()` stops at the shortest input.
- Loading huge files into memory when line-by-line processing would work.

