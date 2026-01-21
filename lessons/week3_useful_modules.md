# Week 3: Useful Standard Library Modules

This lesson covers several useful modules from Python's standard library. These are **built-in** - no installation required.

---

## Table of Contents

| Module | Description | Line |
|--------|-------------|------|
| [`random`](#the-random-module) | Pseudo-random number generation | ~20 |
| [`platform`](#the-platform-module) | System and hardware information | ~160 |

---

## The `random` Module

The `random` module provides functions for generating pseudo-random numbers and making random selections.

```python
import random
```

---

### `random.random()` - Float between 0 and 1

Returns a random float in the range `[0.0, 1.0)` (includes 0, excludes 1).

```python
import random

print(random.random())  # e.g., 0.7134589023
print(random.random())  # e.g., 0.2918374651
```

---

### `random.seed()` - Reproducible Results

The `seed()` function initializes the random number generator. Using the same seed produces the same sequence of "random" numbers.

```python
import random

random.seed(42)
print(random.random())  # Always: 0.6394267984578837

random.seed(42)
print(random.random())  # Always: 0.6394267984578837 (same!)
```

**Use case:** Testing - when you need predictable "random" values for debugging.

---

### `random.randint(a, b)` - Random Integer (Inclusive)

Returns a random integer N such that `a <= N <= b` (both endpoints included).

```python
import random

print(random.randint(1, 6))   # Dice roll: 1, 2, 3, 4, 5, or 6
print(random.randint(0, 100)) # Random percentage: 0 to 100
```

**PCAP Trap:** Both `a` and `b` are **inclusive**. `randint(1, 6)` can return 6.

---

### `random.randrange(start, stop, step)` - Random from Range

Returns a random element from `range(start, stop, step)`. The `stop` value is **excluded** (like `range()`).

```python
import random

print(random.randrange(10))        # 0 to 9 (stop only)
print(random.randrange(1, 7))      # 1 to 6 (like randint but stop excluded)
print(random.randrange(0, 100, 5)) # 0, 5, 10, 15, ..., 95
```

**Key difference from `randint`:**
- `randint(1, 6)` → can return 1, 2, 3, 4, 5, **6**
- `randrange(1, 7)` → can return 1, 2, 3, 4, 5, 6 (same result, different syntax)

---

### `random.choice(sequence)` - Pick One Element

Returns a single random element from a non-empty sequence.

```python
from random import choice

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(choice(my_list))  # e.g., 4

colors = ['red', 'green', 'blue']
print(choice(colors))   # e.g., 'green'

word = "Python"
print(choice(word))     # e.g., 'h'
```

---

### `random.sample(sequence, k)` - Pick Multiple Unique Elements

Returns a list of `k` unique elements chosen from the sequence. The elements are placed in **random order**.

```python
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))       # e.g., 4
print(sample(my_list, 5))    # e.g., [3, 1, 8, 9, 10]
print(sample(my_list, 10))   # e.g., [10, 8, 5, 1, 6, 4, 3, 9, 7, 2]
```

**Critical rule:** `k` must not be greater than `len(sequence)`.

```python
sample(my_list, 15)  # ValueError: Sample larger than population
```

**Key property:** `sample()` returns **unique** elements - no duplicates. This is different from calling `choice()` multiple times, which can return the same element twice.

```python
# choice() can repeat:
[choice(my_list) for _ in range(5)]  # e.g., [3, 3, 7, 1, 3]

# sample() never repeats:
sample(my_list, 5)                    # e.g., [3, 7, 1, 9, 2] (all unique)
```

---

### `random` Quick Reference

| Function | Returns | Range/Behavior |
|----------|---------|----------------|
| `random()` | float | [0.0, 1.0) |
| `seed(n)` | None | Sets generator state |
| `randint(a, b)` | int | a <= N <= b (inclusive) |
| `randrange(start, stop, step)` | int | Like range(), stop excluded |
| `choice(seq)` | element | Single random element |
| `sample(seq, k)` | list | k unique elements, random order |

### `random` PCAP Traps

1. **`randint` is inclusive on both ends** - `randint(1, 10)` can return 10
2. **`randrange` excludes stop** - `randrange(1, 10)` cannot return 10
3. **`sample(seq, k)` requires `k <= len(seq)`** - otherwise ValueError
4. **`sample()` returns unique elements** - no duplicates possible
5. **`random()` excludes 1.0** - range is [0.0, 1.0), never exactly 1.0

---

## The `platform` Module

The `platform` module provides access to information about the underlying system - the hardware, OS, and Python interpreter.

```python
import platform
```

### Understanding the Execution Layers

When your Python code runs, it goes through several layers:

```
┌─────────────────────────────┐
│      Your Python Code       │  ← You write this
├─────────────────────────────┤
│    Python Interpreter       │  ← Executes your code
├─────────────────────────────┤
│    Operating System (OS)    │  ← Windows, Linux, macOS
├─────────────────────────────┤
│         Hardware            │  ← CPU, RAM, etc.
└─────────────────────────────┘
```

The `platform` module lets you query information from each of these layers. This is useful when:
- Writing cross-platform code that behaves differently on Windows vs Linux
- Debugging environment-specific issues
- Logging system information for diagnostics

**Note:** You may not need this module often, but understanding how your code interacts with the system is valuable knowledge.

---

### `platform.platform()` - Full System Description

Returns a single string identifying the underlying platform with as much useful information as possible.

```python
import platform

print(platform.platform())
# Example outputs:
# Windows: 'Windows-10-10.0.19041-SP0'
# Linux:   'Linux-5.4.0-42-generic-x86_64-with-glibc2.31'
# macOS:   'macOS-12.0-arm64-arm-64bit'
```

**Parameters:**
- `aliased` (default `False`) - If `True`, uses common aliases (e.g., "Windows" instead of "Windows-10")
- `terse` (default `False`) - If `True`, returns minimal information

```python
print(platform.platform(aliased=True))   # May use aliases
print(platform.platform(terse=True))     # Minimal output
```

---

### Common `platform` Functions

```python
import platform

# Operating System
print(platform.system())        # 'Windows', 'Linux', 'Darwin' (macOS)
print(platform.release())       # '10' (Windows 10), '5.4.0' (Linux kernel)
print(platform.version())       # Detailed OS version string

# Hardware
print(platform.machine())       # 'AMD64', 'x86_64', 'arm64'
print(platform.processor())     # CPU info (may be empty on some systems)

# Python Interpreter
print(platform.python_version())           # '3.10.4'
print(platform.python_implementation())    # 'CPython', 'PyPy', etc.
print(platform.python_version_tuple())     # ('3', '10', '4')
```

---

### Practical Example: Cross-Platform Code

```python
import platform

if platform.system() == 'Windows':
    path_separator = '\\'
    clear_command = 'cls'
else:
    path_separator = '/'
    clear_command = 'clear'

print(f"Running on {platform.system()}")
print(f"Python version: {platform.python_version()}")
```

---

### `platform` Quick Reference

| Function | Returns | Example |
|----------|---------|---------|
| `platform()` | Full platform string | 'Windows-10-10.0.19041-SP0' |
| `system()` | OS name | 'Windows', 'Linux', 'Darwin' |
| `release()` | OS release | '10', '5.4.0' |
| `machine()` | Hardware architecture | 'AMD64', 'x86_64' |
| `processor()` | CPU info | 'Intel64 Family 6...' |
| `python_version()` | Python version string | '3.10.4' |
| `python_implementation()` | Interpreter type | 'CPython' |

---
