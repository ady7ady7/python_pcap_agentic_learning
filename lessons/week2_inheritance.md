# Week 2: Advanced OOP - Inheritance

## What is Inheritance?

**Inheritance** allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass). This enables code reuse and establishes a hierarchical relationship between classes.

**Key concept:** "IS-A" relationship
- A `Dog` IS-A `Animal`
- A `SavingsAccount` IS-A `BankAccount`
- A `LevelCrossStrategy` IS-A `Strategy`

---

## Basic Inheritance Syntax

```python
"""Basic inheritance example."""

class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return "Some sound"

class Dog(Animal):  # Dog inherits from Animal
    def speak(self) -> str:  # Override parent method
        return "Woof!"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow!"

# Usage
dog = Dog("Buddy")
print(dog.name)  # Inherited attribute: "Buddy"
print(dog.speak())  # Overridden method: "Woof!"

cat = Cat("Whiskers")
print(cat.speak())  # "Meow!"
```

**Key points:**
- `Dog(Animal)` means Dog inherits from Animal
- Child class can **override** parent methods
- Child class inherits parent's `__init__` if not overridden

---

## The `super()` Function

`super()` calls methods from the parent class. Most commonly used in `__init__` to initialize parent attributes.

```python
"""Using super() to call parent __init__."""

class Vehicle:
    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year

    def info(self) -> str:
        return f"{self.year} {self.brand}"

class Car(Vehicle):
    def __init__(self, brand: str, year: int, doors: int):
        super().__init__(brand, year)  # Call parent __init__
        self.doors = doors  # Add child-specific attribute

    def info(self) -> str:
        parent_info = super().info()  # Call parent method
        return f"{parent_info} with {self.doors} doors"

car = Car("Toyota", 2023, 4)
print(car.brand)  # "Toyota" (from parent)
print(car.doors)  # 4 (child attribute)
print(car.info())  # "2023 Toyota with 4 doors"
```

**Why use `super()`?**
- Avoids hardcoding parent class name
- Required for multiple inheritance (Week 3 topic)
- Best practice for calling parent methods

---

## Method Overriding

Child classes can **override** (replace) parent methods with their own implementation.

```python
"""Method overriding example."""

class Shape:
    def __init__(self, name: str):
        self.name = name

    def area(self) -> float:
        return 0.0  # Default implementation

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self) -> float:  # Override parent method
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:  # Override parent method
        return 3.14159 * self.radius ** 2

rect = Rectangle(5, 3)
print(rect.area())  # 15 (overridden method)

circle = Circle(4)
print(circle.area())  # 50.26536 (overridden method)
```

**Rules:**
- Method signature must match (same name, can have different parameters)
- Child method completely replaces parent method
- Use `super().method()` if you want to EXTEND parent behavior, not replace

---

## Abstract Base Classes (ABC)

An **Abstract Base Class** defines a blueprint that child classes MUST implement. Use `abc` module.

```python
"""Abstract Base Class example."""

from abc import ABC, abstractmethod

class Strategy(ABC):  # Inherit from ABC
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def calculate_signal(self, price: float) -> str:
        """Child classes MUST implement this."""
        pass  # No implementation in parent

class LevelCrossStrategy(Strategy):
    def __init__(self, level: float):
        super().__init__("Level Cross")
        self.level = level

    def calculate_signal(self, price: float) -> str:
        """REQUIRED implementation."""
        if price > self.level:
            return "BUY"
        elif price < self.level:
            return "SELL"
        return "HOLD"

# Cannot instantiate abstract class:
# s = Strategy("Test")  # TypeError!

# Can instantiate child that implements abstract methods:
strategy = LevelCrossStrategy(100.0)
print(strategy.calculate_signal(105))  # "BUY"
```

**Why use ABC?**
- **Enforce contracts:** Child classes MUST implement abstract methods
- **Catch errors early:** TypeError at instantiation, not runtime
- **Design clarity:** Clearly signals which methods are required

---

## `isinstance()` and `issubclass()`

Check inheritance relationships at runtime.

```python
"""Type checking with isinstance() and issubclass()."""

class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()

# isinstance(object, Class) - checks if object is instance of Class
print(isinstance(dog, Dog))  # True
print(isinstance(dog, Animal))  # True (Dog is subclass of Animal)
print(isinstance(dog, Cat))  # False

# issubclass(ChildClass, ParentClass) - checks class hierarchy
print(issubclass(Dog, Animal))  # True
print(issubclass(Dog, Dog))  # True (class is subclass of itself)
print(issubclass(Animal, Dog))  # False
print(issubclass(Dog, Cat))  # False
```

**PCAP traps:**
- `isinstance(obj, Class)` - object vs class
- `issubclass(Child, Parent)` - class vs class
- Every class is a subclass of itself

---

## Method Resolution Order (MRO)

Python searches for methods in a specific order: **Child → Parent → Grandparent**.

```python
"""Method Resolution Order example."""

class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(B):
    pass  # Doesn't override method

obj = C()
print(obj.method())  # "B" (finds method in parent B first)

# Check MRO
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

**Key rule:** Python looks for methods from LEFT to RIGHT, BOTTOM to TOP.

---

## Common Inheritance Patterns

### 1. Extending Parent Behavior (not replacing)

```python
"""Extend parent method with super()."""

class Logger:
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")

class TimestampLogger(Logger):
    def log(self, message: str) -> None:
        super().log(message)  # Call parent first
        print(f"[TIMESTAMP] 2026-01-12 13:30:00")  # Add extra behavior

logger = TimestampLogger()
logger.log("User logged in")
# Output:
# [LOG] User logged in
# [TIMESTAMP] 2026-01-12 13:30:00
```

### 2. Template Method Pattern

Parent defines algorithm structure, children fill in details.

```python
"""Template method pattern."""

class DataProcessor(ABC):
    def process(self, data: list) -> list:
        """Template method - defines algorithm structure."""
        data = self.load(data)
        data = self.transform(data)
        data = self.save(data)
        return data

    @abstractmethod
    def load(self, data: list) -> list:
        pass

    @abstractmethod
    def transform(self, data: list) -> list:
        pass

    @abstractmethod
    def save(self, data: list) -> list:
        pass

class CSVProcessor(DataProcessor):
    def load(self, data: list) -> list:
        print("Loading CSV...")
        return data

    def transform(self, data: list) -> list:
        print("Transforming CSV...")
        return [x.upper() for x in data]

    def save(self, data: list) -> list:
        print("Saving CSV...")
        return data

processor = CSVProcessor()
result = processor.process(["a", "b", "c"])
# Loading CSV...
# Transforming CSV...
# Saving CSV...
```

---

## PCAP Traps & Common Mistakes

### Trap 1: Forgetting `super().__init__()`

```python
class Parent:
    def __init__(self, x):
        self.x = x

class Child(Parent):
    def __init__(self, x, y):
        # BUG: Forgot super().__init__(x)
        self.y = y

c = Child(10, 20)
print(c.x)  # AttributeError! self.x was never set
```

**Fix:** Always call `super().__init__()` if parent has `__init__`.

### Trap 2: Overriding vs Overloading

Python doesn't support **method overloading** (multiple methods with same name, different signatures).

```python
class Test:
    def method(self, x):
        return x

    def method(self, x, y):  # This REPLACES the first method!
        return x + y

t = Test()
t.method(5)  # TypeError! method() requires 2 arguments
```

**Python behavior:** Last method definition wins.

### Trap 3: `isinstance()` vs `type()`

```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(type(dog) == Dog)  # True
print(type(dog) == Animal)  # False (type is exact match)

print(isinstance(dog, Dog))  # True
print(isinstance(dog, Animal))  # True (considers inheritance)
```

**Rule:** Use `isinstance()` for inheritance-aware checks, `type()` for exact type match.

### Trap 4: Abstract method not implemented

```python
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def required_method(self):
        pass

class Child(Base):
    pass  # Forgot to implement required_method

c = Child()  # TypeError: Can't instantiate abstract class Child
```

**Rule:** ALL abstract methods must be implemented by child classes.

---

## When to Use Inheritance

**✅ Good use cases:**
- Clear "IS-A" relationship (Dog IS-A Animal)
- Shared behavior across multiple classes
- Template method pattern
- Polymorphism (Week 5 topic)

**❌ Bad use cases:**
- "HAS-A" relationship (use composition instead: Car HAS-A Engine)
- Single-use inheritance (just use one class)
- Deep inheritance hierarchies (>3 levels gets messy)

**Alternative: Composition over Inheritance**
```python
# BAD: Inheritance for HAS-A
class Car(Engine):  # Car IS-A Engine? No!
    pass

# GOOD: Composition for HAS-A
class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine
```

---

## Quick Reference

```python
# Basic inheritance
class Child(Parent):
    pass

# Call parent __init__
class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

# Override method
class Child(Parent):
    def method(self):
        return "Child implementation"

# Extend parent method
class Child(Parent):
    def method(self):
        result = super().method()  # Call parent first
        return result + " extended"

# Abstract Base Class
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def required_method(self):
        pass

# Type checking
isinstance(obj, Class)  # Object is instance of Class?
issubclass(Child, Parent)  # Child inherits from Parent?
```

---

## Exam Tips

**Inheritance:**
- `super()` calls parent class methods
- Child can override parent methods
- `isinstance(obj, Class)` checks if obj is instance of Class (inheritance-aware)
- `issubclass(A, B)` checks if A inherits from B
- Abstract methods MUST be implemented by child classes
- MRO: Python searches Child → Parent → Grandparent
- Every class inherits from `object` (implicit)

**Common PCAP questions:**
- "What is the output?" with inheritance hierarchies
- "Which method is called?" (MRO questions)
- "Can you instantiate this class?" (abstract class questions)
- "`isinstance()` vs `type()`" traps

---
