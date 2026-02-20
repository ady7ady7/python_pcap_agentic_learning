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

#Start 8:35


---

## Task 1: Quick-Fire Gap Closers — No Code (5 Minutes)

These are the exact concepts wrong in Day 4. No running code.

**Q1:** `raise "error"` — what happens and when?
- A) `SyntaxError` at parse time
- B) `TypeError` at runtime — strings are not valid exception types
- C) `ValueError` at runtime
- D) Nothing — bare strings are silently ignored

D

**Q2:** A closure *reads* an outer variable without `nonlocal`. What happens?
- A) `NameError`
- B) Works fine — LEGB lookup finds it automatically
- C) `UnboundLocalError`
- D) `nonlocal` required for both reading and writing

C

**Q3:** `logger.exception("msg")` — which is true?
- A) Logs at CRITICAL and raises the exception
- B) Logs at ERROR and appends the current traceback; does not raise
- C) Only valid outside `except` blocks
- D) Identical to `logger.error("msg")`

B


**Q4:** In `%(levelname)s` vs `logger.warning("bad value: %s", x)` — which placeholder style belongs to which context?


%(levelname)s belongs typically to Formatter settings in logging.
The other one is used for the actual logging calls.

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


import logging
import sys

def build_logger(name: str, filepath: str, level: int = logging.INFO) -> logging.Logger:
    
    if logging.getLogger(name).handlers:
        return logging.getLogger(name)
    
    else:
        root = logging.getLogger(name)
        root.setLevel(level)
    
        fmt = logging.Formatter('[%(levelname)s]: %(message)s')
        
        console = logging.StreamHandler(sys.stdout)
        console.setFormatter(fmt)
        
        file_handler = logging.FileHandler(filepath)
        file_handler.setFormatter(fmt)
        
        root.addHandler(console)
        root.addHandler(file_handler)
        return logging.getLogger(name)


logger = build_logger('logger_test', 'test.log')


def safe_divide(a: float, b: float) -> float:
    '''Function created to safely divide numbers and handle errors'''
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError
        result = a / b
        
    except ValueError as e:
        logger.warning('Invalid input %s', e)
    except ZeroDivisionError as e:
        logger.error('Division by zero: %s / %s', a, b)
    
    else:
        logger.info('The division was successful')
        return result
    
    
x = safe_divide(5, 0)
print(x)
x = safe_divide(5, 'XD')
print(x)
x = safe_divide(5, 2)
print(x)

$ python practice.py
[ERROR]: Division by zero: 5 / 0
None
[WARNING]: Invalid input
None
[INFO]: The division was successful
2.5
(.venv) 

Now it works properly



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


from algo_backtest.engine.position import Position
position = Position('DAX', 'BUY', 24600, 5)




def audit_object(obj: object) -> dict:
    
    object_name = type(obj).__name__
    instance_attributes = obj.__dict__
    others = type(obj).__dict__
    print(f'The class name of the object is {object_name}')
    print(f'The instance attributes of this class instance are: {instance_attributes}')
    print(f'The private attributes are: {[attribute for attribute in instance_attributes if str(attribute).startswith('_')]}')
    has_repr = True if '__repr__' in others else False
    print(f'The object has a __repr__ method: {has_repr}')


x = audit_object(position)


I've used Position as it was quite handy - everything seems to work properly and I can also paste the log for you. I've used prints to be able to see the output easily


$ python practice.py
The class name of the object is Position
The instance attributes of this class instance are: {'position_id': '107f3c09-fd78-4046-b41d-9112b0ac5568', 'ticker': 'DAX', 'side': 'BUY', 'entry_price': 24600, 'quantity': 5, 'stop_loss': None, 'take_profit': None}
The private attributes are: []
The object has a __repr__ method: True
{'__module__': 'algo_backtest.engine.position', '__firstlineno__': 6, '__doc__': '\nRepresents a single trading position\n\nAttributes:\nticker: e.g. EURUSD, FDAX,\nentry_price: float e.g. 24500.25\nquantity: Number of units\nstop_loss: stop loss price - float e.g. 24470.5 (optional)\ntake_profit: take profit price - float e.g. 24530.0 (optional)\n\n', '__init__': <function Position.__init__ at 0x000001F19F4F7100>, '__str__': <function Position.__str__ at 0x000001F19F5314E0>, '__repr__': <function Position.__repr__ at 0x000001F19F531580>, '__hash__': <function Position.__hash__ at 0x000001F19F531620>, '__eq__': <function Position.__eq__ at 0x000001F19F5316C0>, 'calculate_pnl': <function Position.calculate_pnl at 0x000001F19F531760>, 'should_close': <function Position.should_close at 0x000001F19F5318A0>, 'calculate_position_size': <classmethod(<function Position.calculate_position_size at 0x000001F19F531940>)>, '__static_attributes__': ('entry_price', 'position_id', 'quantity', 'side', 'stop_loss', 'take_profit', 'ticker'), '__dict__': <attribute '__dict__' of 'Position' objects>, '__weakref__': <attribute '__weakref__' of 'Position' objects>}
(.venv) 

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


A C
We could be puzzled which exception would be raised in this case - as we're raising the ValueError, but since the first Exception is a general Exception, it would be called and show the message.


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

We'd get an ERROR from logging print first with proper naming of the function and divisio nby zero output, but we'd also get another output with classical ZeroDivisionError, so we get a doubled output.

First of all, we could save our result in a separate result variable, before returning it.
Second of all, we should add more specific error handling, and maybe checking with raise for specific types of errors.


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

def make_validator(min_val: float, max_val: float):
    '''A fuctory function that creates validators with min and max value to check any number'''
    def validate(value: float):
        result = (value >= min_val) and (value <= max_val)
        return result
    return validate


x = make_validator(10, 20)
print(x(15))
print(x(1))
print(x(555))

is_valid_price = make_validator(0.01, 10000.0)
print(is_valid_price(4343434))
print(is_valid_price(43))
print(is_valid_price(-1))

Log:
$ python practice.py
True
False
False
False
True
False




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

C

**Q2:** What does `iter(obj)` return when `obj` is a generator?
- A) A new independent generator
- B) The same generator object (`obj` itself)
- C) A list copy of the generator's remaining values
- D) Raises `TypeError`

A

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

B

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

A

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

B

**Q6:** `%y` vs `%Y` in `strftime` — what is the difference?
- A) `%y` = full 4-digit year, `%Y` = 2-digit year
- B) `%y` = 2-digit year, `%Y` = full 4-digit year
- C) They are interchangeable
- D) `%y` includes timezone, `%Y` does not

B

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

B

**Q8:** Which exception is raised?
```python
d = {'a': 1}
print(d['b'])
```
- A) `IndexError`
- B) `ValueError`
- C) `KeyError`
- D) `AttributeError`

C

**Q9:** What is `__name__` equal to inside `algo_backtest/engine/backtest.py` when run as an import?
- A) `"backtest"`
- B) `"engine.backtest"`
- C) `"algo_backtest.engine.backtest"`
- D) `"__main__"`

A

**Q10:** `isinstance(True, int)` — what does this return?
- A) `False` — `bool` and `int` are separate types
- B) `True` — `bool` is a subclass of `int`
- C) `TypeError`
- D) Depends on Python version

B

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
