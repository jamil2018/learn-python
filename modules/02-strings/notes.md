# Knowledge Notes: Strings

## Core Ideas

A string is a sequence of characters.

```python
message = "Python is fun"
```

Strings are immutable. Methods like `.upper()` return a new string instead of changing the original.

```python
text = "hello"
upper_text = text.upper()
```

## Indexing And Slicing

Indexes start at `0`.

```python
word = "python"
first = word[0]
last = word[-1]
```

Slicing extracts part of a string.

```python
word[0:2]   # "py"
word[2:]    # "thon"
word[::-1]  # "nohtyp"
```

## Useful String Methods

```python
text.lower()
text.upper()
text.title()
text.strip()
text.replace("old", "new")
text.split(",")
"-".join(parts)
text.startswith("pre")
text.endswith(".py")
```

Most string methods return a new string.

## Searching And Counting

```python
"py" in "python"
"banana".count("a")
"hello".find("l")
```

`find()` returns `-1` when not found. The `in` operator is often clearer for yes/no checks.

## Normalization

Before comparing user text, normalize it.

```python
answer = input("Continue? ").strip().lower()
if answer == "yes":
    print("Continuing")
```

This matters for usernames, passwords, search terms, and palindrome checks.

## Building Strings

Use f-strings for readable interpolation.

```python
name = "Ada"
score = 95
print(f"{name} scored {score}")
```

Use `join()` when combining many strings.

```python
slug = "-".join(["learn", "python"])
```

## Validation Basics

Python has helpful character checks:

```python
text.isalpha()
text.isdigit()
text.isalnum()
text.isspace()
```

These are useful but not complete validation systems. For example, real email validation is more complex than checking for `"@"`.

## TypeScript Lens

Python strings feel similar to JavaScript strings, but methods use snake-style names less often because many are old built-ins or plain words: `.lower()`, `.split()`, `.strip()`.

JavaScript's `.trim()` is Python's `.strip()`.

## Common Mistakes

- Forgetting that `split()` returns a list.
- Comparing user input without `.strip().lower()`.
- Thinking `replace()` mutates the original string.
- Overusing complex regular expressions before simpler string methods are enough.

