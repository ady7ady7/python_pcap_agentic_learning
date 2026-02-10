# Week 6, Day 2 - Tuesday
## Topic: Iterator Mastery, Bug Fixes & Trade ID Propagation

**Date:** 2026-02-10

**Target Difficulty:** 5-6/10

**Focus:** Fix Day 1 gaps (Fibonacci state, `__init__` args), fix critical project bug, propagate `position_id` to Trade

**Lesson:** Review `lessons/week6_iterators_generators_advanced.md` sections on iterators & `__new__`.

**Remember:** Work in `practice.py`, paste FINAL answers here for review.

---

## Task 1: PCAP Warm-up (Pure Python)

**Q1:** What is the output?
```python
class Repeater:
    def __init__(self, value, times):
        self.value = value
        self.times = times
        self.count = 0

    def __iter__(self):
        self.count = 0   # reset on every iter() call
        return self

    def __next__(self):
        if self.count >= self.times:
            raise StopIteration
        self.count += 1
        return self.value

r = Repeater("hi", 3)
print(list(r))
print(list(r))

['hi', 'hi', 'hi']
['hi', 'hi', 'hi']

I don't exactly understand why it works like that, it's a bit weird.
```

**Q2:** What is the output?
```python
data = [10, 20, 30, 40]
it = iter(data)
next(it)
next(it)

for x in it:
    print(x, end=' ')
```

30, 40

**Your answers:**
```
Q1:

Q2:

```

---

## Task 2: Decorator Scaffolded — Day 2: FILL IN THE BLANKS

**Goal:** Complete the missing parts of a decorator that validates argument types. The structure is given — you fill the gaps.

**Instructions:** Replace each `___BLANK___` with the correct code. There are 5 blanks total.

```python
from functools import wraps

def enforce_types(*expected_types):
    """
    Decorator that checks if positional arguments match expected types.
    Usage: @enforce_types(str, float)
    """
    def decorator(___BLANK_1___):          # What goes here?
        @wraps(___BLANK_2___)              # What goes here?
        def wrapper(*args, **kwargs):
            for arg, expected in zip(args, expected_types):
                if not isinstance(arg, ___BLANK_3___):   # What goes here?
                    return f"TypeError: expected {expected.__name__}, got {type(arg).__name__}"
            return ___BLANK_4___           # What goes here? (call the original function)
        return ___BLANK_5___               # What goes here?
    return decorator

# Test:
@enforce_types(str, float, int)
def create_order(ticker, price, quantity):
    return f"Order: {ticker} @ {price} x {quantity}"

print(create_order("FDAX", 24500.0, 1))
print(create_order("FDAX", "bad_price", 1))
print(create_order.__name__)
```

**Expected output:**
```
Order: FDAX @ 24500.0 x 1
TypeError: expected float, got str
create_order
```

**Your code (fill in the blanks):**
```python
from functools import wraps

def enforce_types(*expected_types):
    """
    Decorator that checks if positional arguments match expected types.
    Usage: @enforce_types(str, float)
    """
    def decorator(func):          # What goes here?
        @wraps(func)              # What goes here?
        def wrapper(*args, **kwargs):
            for arg, expected in zip(args, expected_types):
                if not isinstance(arg, expected):   # What goes here?
                    return f"TypeError: expected {expected.__name__}, got {type(arg).__name__}"
            return func(*args, **kwargs)         # What goes here? (call the original function)
        return wrapper            # What goes here?
    return decorator

# Test:
@enforce_types(str, float, int)
def create_order(ticker, price, quantity):
    return f"Order: {ticker} @ {price} x {quantity}"

print(create_order("FDAX", 24500.0, 1))
print(create_order("FDAX", "bad_price", 1))
print(create_order.__name__)

#$ python practice.py
# Order: FDAX @ 24500.0 x 1
# TypeError: expected float, got str
# create_order

---

## Task 3: FibonacciIterator — Fix & Learn the State Pattern

Yesterday you hardcoded a list of Fibonacci numbers — that only works up to the numbers you typed in. The correct approach uses **two state variables** that compute the next value dynamically.

**The pattern you need:**
```python
# This is how you compute Fibonacci with dynamic state:
self.a, self.b = self.b, self.a + self.b
# Before: a=0, b=1
# After:  a=1, b=1
# Next:   a=1, b=2
# Next:   a=2, b=3
# This works for ANY max_value — no hardcoding needed.
```

**Your job:** Rewrite `FibonacciIterator` using this pattern. Key rules:
- `__init__`: store `max_value`, set `self.a = 0` and `self.b = 1`
- `__iter__`: return `self`
- `__next__`: check if `self.a` exceeds `max_value` BEFORE returning, then advance state

```python
class FibonacciIterator:
    """Iterator that yields Fibonacci numbers up to max_value."""

    def __init__(self, max_value: int):
        # Your code

    def __iter__(self):
        # Your code

    def __next__(self) -> int:
        # Your code — use self.a, self.b = self.b, self.a + self.b

# Test:
print(list(FibonacciIterator(50)))
# Expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

print(list(FibonacciIterator(1000)))
# Expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
```

**Your code:**
```python

class FibonacciIterator:
    """Iterator that yields Fibonacci numbers up to max_value."""

    def __init__(self, max_value: int):
        self.max_value = max_value
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.a > self.max_value:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result


```

---

## Task 4: `__init__` Receives Original Arguments — Predict Output

Yesterday's Task 8 Q4 tripped you up. The key rule:

> **`__new__` transforms the object. `__init__` still receives the ORIGINAL arguments that were passed in the constructor call.**

**Q1:** Predict the output:
```python
class UpperStr(str):
    def __new__(cls, value):
        instance = super().__new__(cls, value.upper())
        return instance

    def __init__(self, value):
        self.original = value

s = UpperStr("hello")
print(s)
print(s.original)
print(type(s).__name__)

Answer: HELLO hello UpperStr

```

**Q2:** Predict the output:
```python
class ClampedInt(int):
    """Integer that clamps to range [0, 100]."""
    def __new__(cls, value):
        clamped = max(0, min(100, value))
        return super().__new__(cls, clamped)

    def __init__(self, value):
        self.raw_value = value

x = ClampedInt(250)
print(x)
print(x.raw_value)
print(x + 10)

Answer:
100
250
110
```

**Your answers:**
```
Q1 output:


Q2 output:


```

---

## Task 5: PROJECT — Fix the PositionManager Ticker Bug (CRITICAL)

**The bug:** Open `algo_backtest/engine/position_manager.py`, line 62. Look at `close_triggered_positions`:

```python
closed_positions = [p for p in self.positions if p.ticker == ticker and p.should_close(current_price)]
self.positions = [p for p in self.positions if not p.should_close(current_price)]
```

Line 1 correctly filters by ticker. But line 2 (the removal line) does NOT filter by ticker — it removes ALL positions that trigger at `current_price`, even if they belong to a different ticker.

**Example of the bug:**
```python
# You hold FDAX BUY @ 24500 (SL=24450, TP=24600)
# You hold EURUSD BUY @ 1.0800 (SL=1.0750, TP=1.0850)
# You call: process_price('FDAX', 24600)
#
# Line 1: closed_positions = [FDAX position]  ✅ correct — only FDAX matched
# Line 2: self.positions = [p for p if NOT p.should_close(24600)]
#   → EURUSD.should_close(24600) returns (False, None) → keeps it? NO!
#   → Actually it depends on EURUSD's SL/TP values vs 24600
#   → If 24600 triggers EURUSD's take_profit... it gets silently removed!
```

**Your fix:** Modify line 62 so that only positions matching the ticker are evaluated for removal. Non-matching tickers must stay untouched.

**Paste only the fixed method:**
```python

    def close_triggered_positions(self, ticker: str, current_price: float) -> List[Position]:
        """
        Check all positions for SL/TP triggers and remove them.

        Args:
            current_price: Current market price.

        Returns:
            List of positions that should be closed.
        """
        closed_positions = [p for p in self.positions if p.ticker == ticker and p.should_close(current_price)]
        
        closed_ids = [p.position_id for p in closed_positions]
        self.positions = [p for p in self.positions if p.position_id not in closed_ids]
        

        return closed_positions

#It was not possible to only modify that one line - I had to invent a 2-line modification for this, but it should work just fine

#I tested the code outside after that, and also slightly modified Trade's repr for better formatting, as I've noticed little issue there:


from algo_backtest.engine.backtest_engine import BacktestEngine
engine = BacktestEngine()
engine.open_position('FDAX', 'BUY', 24500, 1, 24450, 24600)
# (self, ticker, side, entry, quantity, stop_loss, take_profit)
engine.open_position('EURUSD', 'BUY', 1.0800, 100000, 1.0750, 1.0850)

x = engine.process_price('FDAX', 24600)
print(x)
print(engine)

#Output:

# $ python practice.py
# Position Position_id = b3e05dec-5f5e-4947-b329-90db875eb400 | BUY 1 FDAX @ 24500 [SL = 24450, TP = 24600] added successfully
# Position Position_id = 81476ae1-2860-49f1-830a-df6bb3d65e0b | BUY 100000 EURUSD @ 1.08 [SL = 1.075, TP = 1.085] added successfully
# [Trade(ticker = 'FDAX', side = 'BUY', entry_price = 24500, exit_price = 24600, quantity = 1, pnl = 100.00, exit_reason = 'BUY TP HIT']
# algo_backtest.engine.backtest_engine: 1 open | 1 closed | PnL: $100
# (.venv) 


```

**Test after fixing** — run the `if __name__ == '__main__'` block in backtest_engine.py and verify:
- FDAX trades closed: 1
- Open positions after FDAX: 1 (EURUSD still there)
- EURUSD trades closed: 1
- Open positions after EURUSD: 0

---

## Task 6: PROJECT — Propagate `position_id` to Trade

Right now, when a Position gets closed and converted to a Trade, the `position_id` is lost. You mentioned wanting to fix this yesterday.

**Your job — 2 changes:**

**Step 1:** Modify `Trade.__init__` to accept an optional `position_id` parameter:
- Add `position_id: Optional[str] = None` to the signature
- Store it as `self._position_id = position_id`
- Add a `@property` for it (read-only, like the other Trade attributes)

#Done

**Step 2:** Modify `BacktestEngine.process_price` to pass the position's ID when creating a Trade:
- In the `Trade(...)` constructor call, add `position_id=str(position.position_id)`

#done
Slightly diffrerent approach though, I've changed the position_id type in Position directly, so it's instantly converted to a string there - it's way easier, more convenient and I won't have to remember to change that later 

self.position_id = str(uuid.uuid4())

**Test:**
```python
engine = BacktestEngine()
p = engine.open_position('FDAX', 'BUY', 24500, 1, stop_loss=24450, take_profit=24600)
print(f"Position ID: {p.position_id}")

closed = engine.process_price('FDAX', 24600)
if closed:
    trade = closed[0]
    print(f"Trade position_id: {trade.position_id}")
    print(f"IDs match: {str(p.position_id) == trade.position_id}")
# Expected: True — the Trade carries forward the Position's ID
```

**Paste only the modified sections:**
```python

I won't be doing that, as I've changed some little bits here and there, but I'm 100% sure it works.
Simply check the test log below and you'll have a confirmation:


$ python practice.py
Position Position_id = a3b01ed0-5128-4353-b3e6-17a7f6435599 | BUY 1 FDAX @ 24500 [SL = 24450, TP = 24600] added successfully
Position ID: a3b01ed0-5128-4353-b3e6-17a7f6435599
Trade position_id: a3b01ed0-5128-4353-b3e6-17a7f6435599
IDs match: True
(.venv) 
```

---

## Task 7: Custom Iterator — CountdownIterator

Build a `CountdownIterator` that counts down from `start` to `1` (inclusive).

```python
class CountdownIterator:
    """
    Iterator counting down from start to 1.

    Usage:
        for n in CountdownIterator(5):
            print(n)
        # Output: 5, 4, 3, 2, 1
    """

    def __init__(self, start: int):
        # Your code

    def __iter__(self):
        # Your code

    def __next__(self) -> int:
        # Your code

# Test 1:
print(list(CountdownIterator(5)))
# Expected: [5, 4, 3, 2, 1]

# Test 2:
print(list(CountdownIterator(1)))
# Expected: [1]

# Test 3 — exhaustion:
c = CountdownIterator(3)
print(next(c))  # 3
print(next(c))  # 2
print(list(c))  # [1] — remaining items
print(list(c))  # [] — exhausted
```

**Your code:**
```python

class CountdownIterator:
    """
    Iterator counting down from start to 1.

    Usage:
        for n in CountdownIterator(5):
            print(n)
        # Output: 5, 4, 3, 2, 1
    """

    def __init__(self, start: int):
        self.current = start + 1
        
    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current <= 1:
            raise StopIteration
        self.current -= 1
        return self.current

```
#Result:

<!-- $ python practice.py
[5, 4, 3, 2, 1]
[1]
3
2
[1]
[]
(.venv)  -->

---

## Task 8: PCAP Simulation (5 Questions)

**Q1:** What is the output?
```python
def gen():
    yield from range(3)
    yield from range(3, 6)

print(list(gen()))
```
- A) [0, 1, 2, 3, 4, 5]
- B) [[0, 1, 2], [3, 4, 5]]
- C) [range(3), range(3, 6)]
- D) Error

Answer: A

**Q2:** What is the output?
```python
class TwoItems:
    def __iter__(self):
        yield 10
        yield 20

obj = TwoItems()
it1 = iter(obj)
it2 = iter(obj)
print(next(it1))
print(next(it2))
print(it1 is it2)
```
- A) 10 / 10 / True
- B) 10 / 10 / False
- C) 10 / 20 / True
- D) 10 / 20 / False

Answer: C - not sure about that, it might be B as well

**Q3:** What is the output?
```python
data = [1, 2, 3]
it = iter(data)
print(next(it, 'X'))
print(next(it, 'X'))
print(next(it, 'X'))
print(next(it, 'X'))
print(next(it, 'X'))
```
- A) 1 / 2 / 3 / X / X
- B) 1 / 2 / 3 / StopIteration
- C) 1 / 2 / 3 / X / StopIteration
- D) Error

Answer: A



**Q4:** What is the output?
```python
class OnlyNew:
    def __new__(cls, val):
        obj = super().__new__(cls)
        obj.x = val * 2
        return obj

o = OnlyNew(5)
print(o.x)
print(hasattr(o, '__dict__'))
```
- A) 10 / True
- B) 5 / True
- C) 10 / False
- D) Error — __init__ is required

Answer: A, BUT WE DIDN'T HAVE the __dict__ dunder method - it should be added to week3_dunder_methods.md and explained!

**Q5:** What is the output?
```python
def pipeline():
    data = range(10)
    evens = (x for x in data if x % 2 == 0)
    doubled = (x * 2 for x in evens)
    return list(doubled)

print(pipeline())
```
- A) [0, 4, 8, 12, 16]
- B) [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
- C) [0, 2, 4, 6, 8]
- D) Error

Answer: A

**Your answers:**
```
Q1:
Q2:
Q3:
Q4:
Q5:
```

---

## Solutions Checklist

- [ ] Task 1: PCAP warm-up (2 questions)
- [ ] Task 2: Decorator fill-in-the-blanks (5 blanks)
- [ ] Task 3: FibonacciIterator rewrite (dynamic state)
- [ ] Task 4: __new__ vs __init__ argument flow (2 predictions)
- [ ] Task 5: Fix PositionManager ticker bug (CRITICAL)
- [ ] Task 6: Propagate position_id to Trade
- [ ] Task 7: CountdownIterator class
- [ ] Task 8: PCAP simulation (5 questions)

---

## Feedback Section

**Time spent:** ___ minutes

**Difficulty (1-10):**

**What clicked today:**

**What's confusing:**

---

**When complete:** Notify me for assessment.
