# Week 5, Day 4 - Thursday
## Topic: Review & Consolidation (Lighter Day)

**Date:** 2026-02-05

**Target Difficulty:** 4/10

**Focus:** Reinforce weak areas, shorter session before Friday exam prep

**Remember:** Work in `practice.py`, paste FINAL answers here for review.

---

## Task 1: Decorator with Arguments Pattern (Drill)

**Instructions:** Which is correct for `@decorator(arg)`? Choose and explain.

```python
# A:
def decorator(arg):
    def inner(func):
        def wrapper(*args):
            return func(*args)
        return wrapper
    return inner

# B:
def decorator(func):
    def inner(arg):
        def wrapper(*args):
            return func(*args)
        return wrapper
    return inner

# C:
def decorator(func, arg):
    def wrapper(*args):
        return func(*args)
    return wrapper
```

**Your answer and explanation:**
```
A - it works.
It's useless here in this form, as it requires an argument and it doesn't really do anything with it in the current state, but it works properly.

def decorator(arg):
    def inner(func):
        def wrapper(*args):
            return func(*args)
        return wrapper
    return inner

@decorator(5)
def add(a, b):
    return a + b

print(add(4, 15))
$ python practice.py
19
(.venv) 
```

---

## Task 2: Quick Decorator Practice

**Instructions:** Implement a `@timer` decorator that prints how long a function takes.

```python
from datetime import datetime
from functools import wraps

def timer(func):
    """
    Decorator that prints execution time of a function.

    Example output:
        add took 0.001 seconds
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Your code:
        pass
    return wrapper

# Test:
@timer
def slow_function():
    total = 0
    for i in range(1000000):
        total += i
    return total

result = slow_function()
print(f'Result: {result}')
# Expected output:
# slow_function took X.XXX seconds
# Result: 499999500000
```

**Your code:**
```python
from datetime import datetime
from functools import wraps

def timer(func):
    '''Decorator that prints execution time of a function.
    
    
       Example output: add took 0.001 seconds
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        end = datetime.now()
        print(f'{func.__name__} took {end - start}')
        return result
    return wrapper



$ python practice.py
slow_function took 0:00:00.023520
Result: 499999500000
(.venv) 
HARDPC@DESKTOP-5F8NBD1 MINGW64 ~/Desktop/AL/projekty/python_pcap_agentic_learning (main)
$ python practice.py
slow_function took 0:00:00.024573
Result: 499999500000
(.venv) 
HARDPC@DESKTOP-5F8NBD1 MINGW64 ~/Desktop/AL/projekty/python_pcap_agentic_learning (main)
$ python practice.py
slow_function took 0:00:00.027695
Result: 499999500000
(.venv) 
```

---

## Task 3: PCAP Quick Fire (8 Questions)

**Q1:** What is `@decorator` equivalent to?
- A) `decorator(func)`
- B) `func(decorator)`
- C) `decorator = func`
- D) `func = decorator`

A

**Q2:** What does `f.seek(0)` do?
- A) Closes the file
- B) Moves cursor to beginning
- C) Reads first byte
- D) Writes at position 0

B

**Q3:** What is `datetime.now().strftime("%Y")`?
- A) "2026"
- B) 2026
- C) "26"
- D) Error

B


**Q4:** What is the output?
```python
def f(x=[]):
    x.append(1)
    return x

print(len(f()), len(f()))
```
- A) 1 1
- B) 1 2
- C) 2 2
- D) Error

B

**Q5:** What does `@wraps(func)` preserve?
- A) Function arguments
- B) Function return value
- C) Function metadata (__name__, __doc__)
- D) Function execution time

C

**Q6:** What mode creates a file if it doesn't exist but fails if it does?
- A) 'w'
- B) 'a'
- C) 'r'
- D) 'x'

D

**Q7:** What is the output?
```python
from datetime import date
d = date(2026, 2, 1)
print(d.weekday())
```
- A) 1 (Monday)
- B) 0 (Sunday)
- C) 6 (Sunday)
- D) 7 (Sunday)

C

**Q8:** Which is TRUE about closures?
- A) Inner function must return outer function
- B) Inner function can access outer function's variables
- C) Closures require the `global` keyword
- D) Closures cannot modify outer variables

B - yes, sometimes with proper keywords (nonlocal)

**Your answers:**
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

## Task 4: Fix the BacktestEngine Bug

**Instructions:** You forgot to return the position in `open_position`. Fix it.

Open `algo_backtest/engine/backtest_engine.py` and add the missing return statement.

**Confirm fix:**
```
Fixed: yes/no
```
Yes

---

## Task 5: PROJECT - Test Your BacktestEngine

**Instructions:** Write a simple test in `practice.py` that:
1. Creates a BacktestEngine
2. Opens 2 positions (one BUY, one SELL)
3. Processes a price that triggers one of them
4. Prints the results

```python
# Run from algo_backtest/engine/ directory or adjust imports

# Your test code:

```

**Paste your test and output:**
```python

from algo_backtest.engine.backtest_engine import BacktestEngine
engine = BacktestEngine()
print(engine)

engine.open_position('FDAX', 'BUY', 24410, 7, 24390, 25600)

engine.process_price(25610)
engine.open_position('BTCUSD', 'SELL', 70800, 5, 72100, 66400)
engine.process_price(66300)

print(engine.total_pnl)
print(engine.win_rate)


$ python practice.py
<algo_backtest.engine.backtest_engine.BacktestEngine object at 0x00000200727AB8C0>
Position BUY 7 FDAX @ 24410 [SL = 24390, TP = 25600] added successfully
Position SELL 5 BTCUSD @ 70800 [SL = 72100, TP = 66400] added successfully
30900
[8400, 22500]
100.0
(.venv) 
```

---

## Task 6: Mutable Default Arguments Trap (PCAP Classic)

**Q1:** What's the bug in this code?
```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item('a'))
print(add_item('b'))

The issue is that we have a mutable default argument - an empty list.
It will hold all of our entries instead of separating them
```

**Q2:** What is the output?

a, b

**Q3:** How do you fix it?

We can store the empty list inside of the functions

def add_item(item, items=None):

    if items is None:
        items = []
    items.append(item)
    return items

print(add_item('a'))
print(add_item('b'))


**Your answers:**
```
Q1 bug:

Q2 output:

Q3 fix:
```

---

## Solutions Checklist

- [ ] Task 1: Decorator pattern choice
- [ ] Task 2: @timer decorator
- [ ] Task 3: PCAP quick fire (8 questions)
- [ ] Task 4: Fix BacktestEngine bug
- [ ] Task 5: Test BacktestEngine
- [ ] Task 6: Mutable default trap

---

## Feedback Section

**Time spent:** ___ minutes

**Difficulty (1-10):**

**What clicked today:**


**Ready for Friday exam prep?** yes/no


---

**When complete:** Notify me for assessment.

**Tomorrow:** Friday = Final review + Weekend Mock Exams generated
