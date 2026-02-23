# Week 8, Day 1 — Exam Crunch & Documentation
**Date:** 2026-02-23 | **Focus:** PCAP gap consolidation + project docstrings

---

## Task 1 — PCAP Trap Gauntlet (no code, pure prediction)

Answer all 8. No running code allowed.

**Q1:** What is the output?
```python
x = []
def f(val, lst=x):
    lst.append(val)
    return lst

f(1)
f(2)
print(x)
```

**Q2:** What is the output?
```python
class A:
    count = 0
    def __init__(self):
        A.count += 1

a1 = A()
a2 = A()
a3 = A()
print(A.count, a1.count)
```

**Q3:** What is the output?
```python
def make():
    funcs = []
    for i in range(3):
        funcs.append(lambda x, i=i: x + i)
    return funcs

fns = make()
print(fns[0](10), fns[1](10), fns[2](10))
```

**Q4:** What is the output?
```python
try:
    pass
except ValueError:
    print("A")
else:
    print("B")
finally:
    print("C")
```

**Q5:** What is the output?
```python
gen = (x ** 2 for x in range(4))
next(gen)
next(gen)
print(sum(gen))
```

**Q6:** What is the output?
```python
class Base:
    def greet(self):
        return "Base"

class Child(Base):
    def greet(self):
        return super().greet() + " Child"

class GrandChild(Child):
    def greet(self):
        return super().greet() + " GrandChild"

print(GrandChild().greet())
```

**Q7:** What is the output?
```python
a = (1, [2, 3], 4)
a[1].append(5)
print(a)
```

**Q8:** What is the output?
```python
print(type(lambda: None).__name__)
```

---

## Task 2 — Scope Trap Drill (write + predict)

Fill in each blank so the function works correctly, then predict the final output.

**Puzzle A:** Make this run without error and print `1`:
```python
def outer():
    count = 0
    def inner():
        ___________
        count += 1
        return count
    return inner

f = outer()
print(f())
```

**Puzzle B:** Make this print `[10, 20]` using a closure (no class):
```python
def make_accumulator(factor):
    items = []
    def add(x):
        items.append(_________)
        return items
    return add

acc = make_accumulator(10)
acc(1)
print(acc(2))
```

**Puzzle C:** Predict the output — think before you answer:
```python
def outer():
    x = "outer"
    def middle():
        x = "middle"
        def inner():
            print(x)
        inner()
    middle()

outer()
```

---

## Task 3 — Exception Hierarchy (PCAP direct)

Answer without running code.

**Q1:** Python's exception hierarchy — which of the following is TRUE?
- A) `Exception` inherits from `BaseException`
- B) `SystemExit` inherits from `Exception`
- C) `KeyboardInterrupt` inherits from `Exception`
- D) All exceptions must inherit from `Exception`

**Q2:** What is the output?
```python
def risky():
    try:
        raise KeyboardInterrupt
    except Exception:
        return "caught by Exception"
    except BaseException:
        return "caught by BaseException"

print(risky())
```

**Q3:** Write a custom exception `InvalidPriceError` that:
- Inherits from `ValueError`
- Takes `price` and `reason` in `__init__`
- `__str__` returns: `"Invalid price 99.0: must be positive"`

Demonstrate it being raised and caught in a `try/except` block.

Work in `practice.py`. Paste final class + demo in the answer box below.

---

## Task 4 — PROJECT: Docstrings Pass (Google style)

Open [algo_backtest/engine/backtest_engine.py](algo_backtest/engine/backtest_engine.py).

**Your job:**
1. The module currently has no module-level docstring. Add one.
2. The class docstring exists but is minimal. Rewrite it in proper Google style (include `Attributes:` section).
3. `open_position()` has a docstring but is missing `Args:` and `Raises:` (it should raise `ValueError` if `side` is not `"BUY"` or `"SELL"`). Add the validation + full docstring.
4. `process_price()` docstring has implementation notes inside it (step 1, 2, 3…). Replace with clean Google-style (`Args:`, `Returns:`).
5. Remove the dead `fmt` formatter object at module level (line 10 — it's never attached to anything).

Write the finished file in place. This is a real project edit, not `practice.py`.

---

## Task 5 — PCAP Simulation (10 questions, 12 minutes)

Time yourself. No code runner.

**Q1:** Which statement about `__slots__` is true?
- A) Prevents instance attribute creation entirely
- B) Replaces `__dict__` with a fixed set of allowed attributes, reducing memory usage
- C) Is inherited automatically by subclasses
- D) Can only be used with `@dataclass`

**Q2:** What is the output?
```python
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        self.y = 2

b = B()
print(hasattr(b, 'x'), hasattr(b, 'y'))
```
- A) `True True`
- B) `False True`
- C) `True False`
- D) `AttributeError`

**Q3:** Which is the correct way to make a class a context manager?
- A) Define `__enter__` and `__exit__`
- B) Define `__open__` and `__close__`
- C) Inherit from `contextlib.ContextManager`
- D) Define `__start__` and `__stop__`

**Q4:** What is the output?
```python
x = "Python"
print(x[-3:])
```
- A) `"Pyt"`
- B) `"hon"`
- C) `"tho"`
- D) `"ython"`

**Q5:** `@staticmethod` vs `@classmethod` — which is true?
- A) Both receive the instance as their first argument
- B) `@classmethod` receives `cls`; `@staticmethod` receives neither `self` nor `cls`
- C) `@staticmethod` can access class attributes via `cls`
- D) They are interchangeable

**Q6:** What is the output?
```python
def f(*args, **kwargs):
    print(type(args).__name__, type(kwargs).__name__)

f(1, 2, a=3)
```
- A) `list dict`
- B) `tuple dict`
- C) `tuple OrderedDict`
- D) `list OrderedDict`

**Q7:** What does `__repr__` return by default (no override)?
- A) The object's `__str__` output
- B) `None`
- C) A string like `<ClassName object at 0x...>`
- D) `"object"`

**Q8:** What is the output?
```python
d = {"a": 1}
d2 = d.copy()
d2["a"] = 99
print(d["a"])
```
- A) `99`
- B) `1`
- C) `KeyError`
- D) `None`

**Q9:** Which raises `TypeError`?
- A) `raise ValueError`
- B) `raise ValueError()`
- C) `raise "error message"`
- D) `raise ValueError from None`

**Q10:** What is the output?
```python
class Counter:
    def __init__(self, limit):
        self.current = 0
        self.limit = limit
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current

print(list(Counter(3)))
```
- A) `[0, 1, 2]`
- B) `[1, 2, 3]`
- C) `StopIteration`
- D) `[0, 1, 2, 3]`

---

## Task 6 — Refactor / Debug

The following decorator is broken. Identify **all** bugs and write the corrected version in `practice.py`. There are **three** bugs.

```python
import logging

def log_call(func):
    def wrapper(*args):
        logging.info("Calling %s", func.__name__)
        result = func(*args)
        logging.info("Done")
        return
    return func
```

Paste the corrected version + a brief comment on each bug into the answer box.

---

## Task 7 — PROJECT: Run the full backtest

Open [algo_backtest/main.py](algo_backtest/main.py).

Write a `main()` function (or extend the existing one) that runs a **complete end-to-end demonstration**:

1. Call `setup_logging()` at the top
2. Create a `BacktestEngine`
3. Open at least **3 positions** on 2 different tickers with realistic prices (use FDAX and EURUSD from the existing test data in the file)
4. Feed price ticks that trigger at least **2 SL hits and 1 TP hit**
5. Print the engine summary via `print(engine)` — make sure `__str__` works correctly
6. Print `total_pnl` and `win_rate`

Run it from `practice.py` or directly (`python -m algo_backtest.main`). Paste the console output into the answer box below.

---

```
## Answers

### Task 1
Q1:
Q2:
Q3:
Q4:
Q5:
Q6:
Q7:
Q8:

### Task 2
Puzzle A (blank):
Puzzle B (blank):
Puzzle C output:

### Task 3
Q1:
Q2:
Code (InvalidPriceError):

### Task 4
(edit made directly in backtest_engine.py — paste any notes here)

### Task 5
Q1:
Q2:
Q3:
Q4:
Q5:
Q6:
Q7:
Q8:
Q9:
Q10:

### Task 6
Bugs found:
Corrected code:

### Task 7
Console output:
```
