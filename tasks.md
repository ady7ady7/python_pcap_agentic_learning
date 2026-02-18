# Week 7, Day 4 - Thursday
## Topic: PCAP Crunch — Exceptions, Strings, Closures + logging.exception() Final Fix

**Date:** 2026-02-19

**Target Difficulty:** 6/10

**Today's balance:** ~60% coding, ~40% prediction/theory. One logging gap to close, then full PCAP drill across older topics.

**Remember:** Work in `practice.py`. Paste FINAL answers here for review.

---

## Task 1: logging.exception() — Final Fix (Code + Observe)

Run this and study the output:

```python
import logging
import sys

logger = logging.getLogger('final_fix')
logger.setLevel(logging.DEBUG)
h = logging.StreamHandler(sys.stdout)
h.setLevel(logging.DEBUG)
h.setFormatter(logging.Formatter('[%(levelname)s] %(message)s'))
logger.addHandler(h)

print("--- before try ---")
try:
    x = int("not_a_number")
except ValueError:
    logger.error("error() was called")
    logger.exception("exception() was called")
print("--- after try ---")
```

**Q1:** Does `"--- after try ---"` appear in the output? What does that tell you about whether `exception()` stops execution?

**Q2:** What level tag appears on the `exception()` line — `[DEBUG]`, `[INFO]`, `[WARNING]`, `[ERROR]`, or `[CRITICAL]`?

**Q3:** In one sentence: what is the only difference between `logger.error("msg")` and `logger.exception("msg")`?

```
Q1:
Q2:
Q3:
```

---

## Task 2: Code — Exception Hierarchy (PCAP Core)

**Write** a function `safe_divide(a: float, b: float) -> float` that:
1. Raises `ValueError` if either argument is not a number (use `isinstance`)
2. Raises `ZeroDivisionError` if `b` is zero
3. Returns the result otherwise
4. Has a caller block that catches each exception separately and logs them — `ValueError` at WARNING level, `ZeroDivisionError` at ERROR level — using `%s` style

Then write **3 calls** to demonstrate all three paths (valid, ValueError, ZeroDivisionError).

Use your `build_logger` from Day 2 (or rebuild it quickly) to have a working logger.

```python
# Task 2 — safe_divide() with logging

```

---

## Task 3: Predict the Output — Exception Order (PCAP Trap)

No running code first. Predict, then verify.

**Q1:**
```python
try:
    raise ValueError("bad value")
except Exception as e:
    print("Exception:", e)
except ValueError as e:
    print("ValueError:", e)
```

**Q2:**
```python
def risky():
    try:
        return 1 / 0
    finally:
        print("finally ran")

print(risky())
```

**Q3:**
```python
try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print(type(e).__name__, "caught")
```

```
Q1 prediction:       Q1 actual:
Q2 prediction:       Q2 actual:
Q3 prediction:       Q3 actual:
```

---

## Task 4: Code — String Processing (PCAP Core)

**Write** a function `parse_trade_log(line: str) -> dict` that takes a raw log line like:
```
"2026-02-18,AAPL,BUY,150.25,100"
```
and returns:
```python
{"date": "2026-02-18", "ticker": "AAPL", "side": "BUY", "price": 150.25, "qty": 100}
```

Requirements:
- Use `str.split()`
- Convert price to `float`, qty to `int`
- Raise `ValueError` with a clear message if the line doesn't have exactly 5 fields
- Test with: the valid line above, a line with 3 fields (should raise), and a line with leading/trailing whitespace (should still work — use `strip()`)

```python
# Task 4 — parse_trade_log()

```

---

## Task 5: Predict the Output — Closures & `nonlocal` (PCAP Core)

No running code first.

**Q1:**
```python
def outer():
    x = 10
    def inner():
        x = 20
        print(x)
    inner()
    print(x)

outer()
```

**Q2:**
```python
def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

c = counter()
print(c())
print(c())
d = counter()
print(d())
```

**Q3:**
```python
funcs = [lambda: i for i in range(3)]
print(funcs[0]())
print(funcs[1]())
print(funcs[2]())
```

**Q4:**
```python
funcs = [lambda i=i: i for i in range(3)]
print(funcs[0]())
print(funcs[1]())
print(funcs[2]())
```

```
Q1 prediction:       Q1 actual:
Q2 prediction:       Q2 actual:
Q3 prediction:       Q3 actual:
Q4 prediction:       Q4 actual:
```

---

## Task 6: Code — Decorator with `%s` Logging (Consolidation)

**Write** a decorator `@log_calls` that:
1. Uses `%s` style (NOT f-strings) in all log calls
2. Logs at DEBUG before the call: function name and args
3. Logs at INFO after: function name and return value
4. Re-raises any exception after logging it at ERROR with `logger.exception()`
5. Uses `@wraps`

Apply it to a function `multiply(a: int, b: int) -> int` and call it with `(3, 4)` and then with `("x", 2)` to trigger the exception path.

```python
# Task 6 — @log_calls decorator

```

---

## Task 7: PCAP Simulation — Mixed Topics (8 Questions, 10 Minutes)

No running code. Covers exceptions, strings, closures, logging — all PCAP exam territory.

**Q1:** What does this print?
```python
try:
    pass
except Exception:
    print("A")
else:
    print("B")
finally:
    print("C")
```
- A) `A` then `C`
- B) `B` then `C`
- C) `C` only
- D) `B` only

**Q2:** Which raises `SyntaxError` at parse time, before execution?
- A) `raise ValueError`
- B) `raise ValueError()`
- C) `raise "error"`
- D) `raise`

**Q3:** What does `"hello world".split()` return?
- A) `['hello', 'world']`
- B) `['h','e','l','l','o',' ','w','o','r','l','d']`
- C) `('hello', 'world')`
- D) `'hello world'` unchanged

**Q4:** What is the output?
```python
s = "abcdef"
print(s[1:4])
print(s[-2:])
print(s[::2])
```
- A) `bcd`, `ef`, `ace`
- B) `bcd`, `ef`, `bdf`
- C) `abc`, `de`, `ace`
- D) `bcd`, `de`, `ace`

**Q5:** A closure reads an outer variable without `nonlocal`. What happens?
- A) `NameError` — outer variable not accessible
- B) Works fine — reading doesn't need `nonlocal`
- C) `UnboundLocalError` always
- D) `nonlocal` is required for both reading and writing

**Q6:** `logging.getLogger('engine')` called from two different files returns:
- A) Two independent logger objects
- B) The same logger object (singleton by name)
- C) A copy of the first logger
- D) Raises RuntimeError on second call

**Q7:** What does `str.find()` return when the substring is not found?
- A) `None`
- B) `0`
- C) `-1`
- D) Raises `ValueError`

**Q8:** What is printed?
```python
def f(x=[]):
    x.append(1)
    return x

print(f())
print(f())
```
- A) `[1]` then `[1]`
- B) `[1]` then `[1, 1]`
- C) `[]` then `[1]`
- D) `TypeError`

```
Q1:
Q2:
Q3:
Q4:
Q5:
Q6:
Q7:
Q8:
```

---

**Today's priority:** Close the `logging.exception()` gap once and for all (Task 1), then spend most energy on the coding tasks (2, 4, 6) — these are the closest to actual PCAP exam coding scenarios.
