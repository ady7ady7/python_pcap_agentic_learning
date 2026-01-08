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

---

## Week 2: Object-Oriented Programming - Advanced (Coming Soon)

### OOP Fundamentals
- What are classes and why use them
- `__init__` and `self`
- Instance vs class attributes
- Methods vs functions

### Inheritance & Polymorphism
- Class inheritance
- Method overriding
- super() usage
- Multiple inheritance (MRO)

---

## Week 3-8: Advanced Topics (Planned)

*Topics will be added as we progress through the course*

---

**Navigation Tip:** Use your IDE's file search (Ctrl+P / Cmd+P) to quickly jump to specific lessons!
