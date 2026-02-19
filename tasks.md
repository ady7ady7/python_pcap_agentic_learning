# Week 7, Day 5 - Friday
## Topic: Week 7 Review + PCAP Full Simulation

**Date:** 2026-02-20

**Target Difficulty:** 6/10

**Today's balance:** ~55% coding, ~45% simulation. Friday = close all gaps + weekend exam prep.

**Lesson References:**
- `lessons/week7_introspection_reflection.md`
- `lessons/week3_5_7_stdlib_fileio.md` → Week 7 section
- All previous weeks are fair game in the simulation

**Remember:** Work in `practice.py`. Paste FINAL answers here for review.

---

## Task 1: Quick-Fire Gap Closers — No Code (5 Minutes)

These are the exact concepts wrong in Day 4. No running code.

**Q1:** `raise "error"` — what happens and when?
- A) `SyntaxError` at parse time
- B) `TypeError` at runtime — strings are not valid exception types
- C) `ValueError` at runtime
- D) Nothing — bare strings are silently ignored

**Q2:** A closure *reads* an outer variable without `nonlocal`. What happens?
- A) `NameError`
- B) Works fine — LEGB lookup finds it automatically
- C) `UnboundLocalError`
- D) `nonlocal` required for both reading and writing

**Q3:** `logger.exception("msg")` — which is true?
- A) Logs at CRITICAL and raises the exception
- B) Logs at ERROR and appends the current traceback; does not raise
- C) Only valid outside `except` blocks
- D) Identical to `logger.error("msg")`

**Q4:** In `%(levelname)s` vs `logger.warning("bad value: %s", x)` — which placeholder style belongs to which context?

```
Q1:
Q2:
Q3:
Q4 — %(levelname)s belongs to:
Q4 — %s in log call belongs to:
```

---

## Task 2: Code — `safe_divide()` Corrected

Yesterday's `safe_divide()` had two issues: the `ValueError` wasn't caught at the call site, and `%s` style wasn't used. Fix both today.

**Write the corrected version** where:
1. The function raises `ValueError` (non-number input) and lets Python raise `ZeroDivisionError` naturally
2. The *caller* catches both separately using `try/except`
3. Logs `ValueError` at WARNING using `%s` style: `logger.warning("Invalid input: %s", e)`
4. Logs `ZeroDivisionError` at ERROR using `%s` style: `logger.error("Division by zero: %s / %s", a, b)`
5. All three call paths demonstrated (valid, ValueError, ZeroDivisionError)

```python
# Task 2 — safe_divide() corrected

```

---

## Task 3: Code — Introspection Utility

Write a function `audit_object(obj: object) -> dict` that uses introspection to return a summary dict containing:
- `"type"` — the class name as a string (use `type(obj).__name__`)
- `"instance_attrs"` — list of instance attribute names from `__dict__`
- `"private_attrs"` — list of instance attribute names that start with `_`
- `"has_repr"` — `True` if the object has a custom `__repr__` (hint: check `type(obj).__dict__`)

Test it on a `Position` instance or any class you have handy. If you don't want to import, just define a quick throwaway class inline.

```python
# Task 3 — audit_object()

```

---

## Task 4: Predict + Fix — Two PCAP Traps

**Trap 1 — Exception order:**
```python
try:
    raise ValueError("oops")
except Exception:
    print("A")
except ValueError:
    print("B")
finally:
    print("C")
```
**Q1:** What prints? Why is this a trap?

**Trap 2 — Decorator missing `raise`:**
```python
from functools import wraps
import logging

def safe_call(func):
    @wraps(func)
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as e:
            logging.exception("Error in %s: %s", func.__name__, e)
    return wrapper

@safe_call
def divide(a, b):
    return a / b

result = divide(10, 0)
print("result:", result)
```
**Q2:** What prints? What silent bug exists here — and what's the fix?

```
Q1 — output and explanation:

Q2 — output:
Q2 — bug:
Q2 — fix (one line):
```

---

## Task 5: Code — `make_validator` Closure (PCAP Core)

Write a factory function `make_validator(min_val: float, max_val: float)` that returns a closure. The returned function takes a single `value: float` and:
- Returns `True` if `min_val <= value <= max_val`
- Returns `False` otherwise
- The outer `min_val` and `max_val` are captured — no `nonlocal` needed (just reading)

Then create two validators: `is_valid_price = make_validator(0.01, 10000.0)` and `is_valid_qty = make_validator(1, 10000)`. Call each with 3 test values.

```python
# Task 5 — make_validator()

```

---

## Task 6: PCAP Full Simulation — 10 Questions (12 Minutes)

No running code. Covers the full PCAP syllabus. Time yourself.

**Q1:** What is the output?
```python
class A:
    x = 1

class B(A):
    pass

B.x = 2
print(A.x, B.x)
```
- A) `1 1`
- B) `2 2`
- C) `1 2`
- D) `2 1`

**Q2:** What does `iter(obj)` return when `obj` is a generator?
- A) A new independent generator
- B) The same generator object (`obj` itself)
- C) A list copy of the generator's remaining values
- D) Raises `TypeError`

**Q3:** What prints?
```python
def f():
    try:
        return 1
    finally:
        return 2

print(f())
```
- A) `1`
- B) `2`
- C) `1` then `2`
- D) `None`

**Q4:** Which is a valid way to create a read-only property?
```python
# Option A:
class C:
    @property
    def val(self):
        return self._val

# Option B:
class C:
    @property
    def val(self):
        return self.val   # note: no underscore

# Option C:
class C:
    def val(self):
        return self._val
```
- A) Option A only
- B) Option B only
- C) Option C only
- D) All three

**Q5:** What is printed?
```python
x = [1, 2, 3]
y = x
y.append(4)
print(x)
```
- A) `[1, 2, 3]`
- B) `[1, 2, 3, 4]`
- C) `[4]`
- D) `TypeError`

**Q6:** `%y` vs `%Y` in `strftime` — what is the difference?
- A) `%y` = full 4-digit year, `%Y` = 2-digit year
- B) `%y` = 2-digit year, `%Y` = full 4-digit year
- C) They are interchangeable
- D) `%y` includes timezone, `%Y` does not

**Q7:** What does this print?
```python
def outer():
    results = []
    for i in range(3):
        results.append(lambda: i)
    return results

fns = outer()
print(fns[0](), fns[1](), fns[2]())
```
- A) `0 1 2`
- B) `2 2 2`
- C) `0 0 0`
- D) `TypeError`

**Q8:** Which exception is raised?
```python
d = {'a': 1}
print(d['b'])
```
- A) `IndexError`
- B) `ValueError`
- C) `KeyError`
- D) `AttributeError`

**Q9:** What is `__name__` equal to inside `algo_backtest/engine/backtest.py` when run as an import?
- A) `"backtest"`
- B) `"engine.backtest"`
- C) `"algo_backtest.engine.backtest"`
- D) `"__main__"`

**Q10:** `isinstance(True, int)` — what does this return?
- A) `False` — `bool` and `int` are separate types
- B) `True` — `bool` is a subclass of `int`
- C) `TypeError`
- D) Depends on Python version

```
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
```

---

**Friday goal:** 90%+ on the simulation. If anything in Q1-Q9 feels uncertain — that's your revision target for the weekend exams.
