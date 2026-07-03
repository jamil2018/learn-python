# Knowledge Notes: Errors, Validation, And Defensive Code

## Core Ideas

Programs fail. Good programs fail clearly, recover where reasonable, and protect their data.

Use `try`/`except` around operations that can fail.

```python
try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a whole number.")
```

## Catch Specific Exceptions

Prefer specific exceptions over broad `except`.

```python
try:
    text = path.read_text()
except FileNotFoundError:
    print("File not found")
```

Common exceptions:

- `ValueError`: invalid value conversion or validation failure
- `KeyError`: missing dictionary key
- `IndexError`: invalid list index
- `FileNotFoundError`: missing file
- `json.JSONDecodeError`: invalid JSON

## Validation

Validation checks data before using it.

```python
def require_positive_number(value):
    number = float(value)
    if number <= 0:
        raise ValueError("Number must be positive")
    return number
```

Separate validation from business logic where possible.

## Raising Errors

Raise an exception when a function cannot do its job.

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount
```

## Friendly Messages

Internal errors and user messages are different. A traceback is useful to a developer, but not friendly to a user.

```python
try:
    balance = withdraw(balance, amount)
except ValueError as error:
    print(error)
```

## Collecting Multiple Errors

For record validation, collect all errors instead of stopping at the first one.

```python
errors = []
if not user.get("email"):
    errors.append("Email is required")
if not user.get("name"):
    errors.append("Name is required")
```

## TypeScript Lens

Python does not force `Result` types. Many Python APIs use exceptions. For exercise code, both styles are worth practicing:

- Return `(success, value)` when failure is expected and common.
- Raise an exception when the function cannot complete its contract.

## Common Mistakes

- Catching every exception and hiding real bugs.
- Validating only interactive input but not file-loaded data.
- Mixing validation, calculation, and printing into one function.
- Using exceptions for ordinary branching when a simple `if` would be clearer.

