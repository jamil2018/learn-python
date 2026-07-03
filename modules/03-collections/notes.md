# Knowledge Notes: Collections

## Core Ideas

Python has several built-in containers:

- `list`: ordered, mutable sequence
- `tuple`: ordered, usually treated as immutable
- `dict`: key-value mapping
- `set`: unordered unique values

Choose the container based on the job, not habit.

## Lists

Lists hold ordered items.

```python
foods = ["rice", "eggs", "fish"]
foods.append("tea")
foods.remove("eggs")
```

Common operations:

```python
len(foods)
foods[0]
foods[-1]
foods[1:3]
```

Use lists when order matters or duplicates are allowed.

## Tuples

Tuples are useful for small fixed records.

```python
point = (10, 20)
x, y = point
```

Use tuples when the shape is fixed, such as coordinates or pairs.

## Dictionaries

Dictionaries map keys to values.

```python
user = {"name": "Ada", "role": "admin"}
print(user["name"])
user["active"] = True
```

Use `.get()` when a key might be missing.

```python
theme = settings.get("theme", "light")
```

## Sets

Sets store unique values.

```python
tags = {"python", "cli", "python"}
```

Useful set operations:

```python
a & b  # common values
a | b  # all values
a - b  # values only in a
```

## Looping Through Collections

```python
for item in items:
    print(item)

for key, value in user.items():
    print(key, value)
```

Use `.items()` for dictionary key-value pairs.

## Nested Data

Real data is often nested.

```python
students = [
    {"name": "Ada", "score": 95},
    {"name": "Linus", "score": 88},
]
```

Be deliberate about shape. If you cannot explain the data structure, the code around it will become confusing.

## TypeScript Lens

Python dictionaries are closest to plain JavaScript objects or `Record<string, T>`, but dictionary keys can be more than strings. Lists are like arrays. Sets are built in and pleasant to use.

## Common Mistakes

- Using a list when membership checks should be a set.
- Accessing a missing dictionary key with `dict[key]` when `.get()` would be safer.
- Mutating a list while looping over it.
- Creating deeply nested data before the simple shape is clear.

