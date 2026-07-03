# Knowledge Notes: Intermediate Design Patterns And Maintainability

## Core Ideas

Maintainable programs have clear boundaries. Each part should have a job.

Common layers:

- domain logic: rules and calculations
- storage: files, databases, APIs
- interface: CLI prompts, arguments, printing
- orchestration: coordinates the other pieces

## Separate Pure Logic From I/O

Harder to test:

```python
def add_expense():
    amount = float(input("Amount: "))
    print(amount)
```

Easier to test:

```python
def format_expense(amount):
    return f"${amount:.2f}"
```

Keep input and output near the edges.

## Repositories

A repository object hides storage details.

```python
class ExpenseRepository:
    def load_all(self):
        ...

    def save_all(self, expenses):
        ...
```

The rest of the app should not need to know whether data is stored in JSON, CSV, or something else.

## Dependency Injection

Dependency injection means passing in a thing instead of hardcoding it.

```python
def create_id(random_id):
    return random_id()
```

Useful dependencies:

- clock
- ID generator
- file path
- API client
- repository

This makes tests easier and reduces hidden global state.

## Command Registries

Instead of a long `if` chain:

```python
commands = {
    "add": add_command,
    "list": list_command,
}
```

This pattern helps when actions grow over time.

## Result Objects

If a tuple becomes unclear, use a dataclass.

```python
@dataclass
class ValidationResult:
    ok: bool
    errors: list[str]
```

Named fields are easier to read than positional values.

## Removing Abstraction

Good design is not maximum abstraction. Remove layers that do not make code easier to understand, test, or change.

Ask:

- Does this abstraction hide useful complexity?
- Does it remove duplication?
- Does it make tests cleaner?
- Would the code be clearer without it?

## Common Mistakes

- Adding patterns before the code needs them.
- Letting CLI code leak into every function.
- Hiding simple logic behind too many classes.
- Refactoring without tests around the current behavior.

