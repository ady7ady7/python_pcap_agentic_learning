# PCAP-31-03 Lessons - Table of Contents

This directory contains all theoretical lessons organized by week and topic.

## Week 1: Foundations

### [Modules, Packages & PIP](week1_modules_packages.md)
- Module vs Package hierarchy
- Import mechanisms (absolute, selective, alias, wildcard)
- sys.path resolution
- pip essentials
- **PCAP Traps:** Circular imports, name shadowing, `__init__.py` execution

### [Strings, Exceptions & File I/O](week1_strings_exceptions.md)
- String operations & slicing
- String methods (find/index, strip, split/join)
- String formatting (%, .format(), f-strings)
- Exception hierarchy and handling
- File I/O with context managers
- **PCAP Traps:** Slicing edge cases, exception order, file handle leaks

### [OOP Fundamentals - Classes & Objects](week1_oop_fundamentals.md)
- What are classes and why use them
- The `__init__` constructor method
- Understanding `self` (the object reference)
- Instance attributes vs class attributes
- Methods vs functions
- Practical examples (BankAccount, OHLCCandle)
- **PCAP Traps:** Mutable class attributes, forgetting `self`, `__init__` return values

### [Magic Methods & Pandas Essentials](week1_magic_methods_pandas.md)
- `__str__` vs `__repr__` (user-friendly vs developer-friendly)
- Making objects print nicely
- Series vs DataFrame concepts
- Essential DataFrame operations (accessing, filtering, NaN handling)
- Boolean indexing and iteration
- **PCAP Traps:** Forgetting return in `__str__`, `.any()` semantics, parentheses in filters

### [Pandas Essentials](pandas.md)
- Series vs DataFrame
- Essential DataFrame operations
- Checking for missing values (NaN)
- Filtering rows (Boolean indexing)
- Advanced filtering & optimization patterns
- **PCAP Traps:** `.any()` semantics, parentheses in multiple conditions, return types

---

## Week 2: Advanced OOP

### [Inheritance & Polymorphism](week2_inheritance.md)
- Basic inheritance syntax and "IS-A" relationships
- The `super()` function for calling parent methods
- Method overriding
- Abstract Base Classes (ABC) with `@abstractmethod`
- `isinstance()` and `issubclass()` for type checking
- Method Resolution Order (MRO)
- **Polymorphism** - using objects of different types through the same interface
- Duck typing in Python
- Type-specific behavior with `isinstance()`
- Common inheritance patterns (extending behavior, template method)
- **PCAP Traps:** Forgetting `super().__init__()`, abstract methods not implemented, `isinstance()` vs `type()`, overriding vs overloading, method overloading (not supported in Python)

### [@classmethod and @staticmethod](week2_classmethod_staticmethod.md)
- Regular methods (review) - receive `self`
- `@classmethod` - receives `cls` (the class itself)
- `@staticmethod` - receives nothing automatically
- When to use which (comparison table)
- Alternative constructors with `@classmethod`
- Utility functions with `@staticmethod`
- **PCAP Traps:** Confusing `cls` and `self`, @staticmethod trying to use `cls`, first parameter naming

---

## Week 3-8: Advanced Topics (Planned)

*Topics will be added as we progress through the course*

---

**Navigation Tip:** Use your IDE's file search (Ctrl+P / Cmd+P) to quickly jump to specific lessons!
