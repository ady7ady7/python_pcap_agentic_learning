# Week 3: The `random` Module

The `random` module provides functions for generating pseudo-random numbers and making random selections. This is a **standard library** module - no installation required.

```python
import random
```

---

## Basic Random Number Generation

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

## Selecting from Sequences

The basic functions above generate numbers, but they **cannot guarantee unique values** or select directly from a list. For that, use `choice()` and `sample()`.

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

## Quick Reference

| Function | Returns | Range/Behavior |
|----------|---------|----------------|
| `random()` | float | [0.0, 1.0) |
| `seed(n)` | None | Sets generator state |
| `randint(a, b)` | int | a <= N <= b (inclusive) |
| `randrange(start, stop, step)` | int | Like range(), stop excluded |
| `choice(seq)` | element | Single random element |
| `sample(seq, k)` | list | k unique elements, random order |

---

## PCAP Traps

1. **`randint` is inclusive on both ends** - `randint(1, 10)` can return 10
2. **`randrange` excludes stop** - `randrange(1, 10)` cannot return 10
3. **`sample(seq, k)` requires `k <= len(seq)`** - otherwise ValueError
4. **`sample()` returns unique elements** - no duplicates possible
5. **`random()` excludes 1.0** - range is [0.0, 1.0), never exactly 1.0
