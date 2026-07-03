# Knowledge Notes: Classes, Dataclasses, And Object-Oriented Design

## Core Ideas

Classes combine data and behavior.

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
```

`self` refers to the current object.

## Dataclasses

Dataclasses are great for records with fields.

```python
from dataclasses import dataclass

@dataclass
class Contact:
    name: str
    email: str
```

Dataclasses automatically provide useful methods such as `__init__` and `__repr__`.

## Methods

Instance methods operate on one object.

```python
def display_name(self):
    return f"{self.name} <{self.email}>"
```

Use methods when behavior naturally belongs to the data.

## Dunder Methods

Dunder methods customize Python behavior.

```python
def __str__(self):
    return self.title
```

Common ones:

- `__str__`: human-readable string
- `__repr__`: developer-facing representation
- `__eq__`: equality

## Serialization

Objects often need to cross a file or API boundary as dictionaries.

```python
from dataclasses import asdict

data = asdict(contact)
```

Keep domain objects inside your program. Convert to dictionaries at the boundary.

## Composition

Composition means one object contains another.

```python
@dataclass
class Order:
    items: list[LineItem]
```

Prefer composition over inheritance unless a real "is a" relationship exists.

## TypeScript Lens

Dataclasses feel close to simple typed objects or interfaces plus constructors. Python classes are more runtime-focused. You do not need a class for every data shape; dictionaries and dataclasses are often enough.

## Common Mistakes

- Creating classes that only wrap one dictionary without adding value.
- Putting file I/O inside data objects too early.
- Using inheritance when composition is simpler.
- Forgetting that mutable fields in dataclasses need care.

