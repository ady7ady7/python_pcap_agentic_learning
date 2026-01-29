# Week 4, Day 4 - Thursday
## Topic: Week 4 Review & PCAP Drills (Pre-Exam)

**Date:** 2026-01-29

**Purpose:** Review all Week 4 topics before Friday's exams. Heavy PCAP focus.

**Target Difficulty:** 5/10

**Remember:** Work in `practice.py`, paste FINAL answers here for review.

---

## Task 1: Quick Fire Review (10 Questions)

**Instructions:** Answer quickly - these test your Week 4 knowledge.

**Q1:** What does lambda return if you write `lambda x: x > 5`?
- A) True or False
- B) x
- C) A function that returns True or False
- D) Nothing

D - if we assume that we only have that

**Q2:** What is the output?
```python
result = list(map(lambda x: x * 2, [1, 2, 3]))
print(result)

Answer: [2, 4, 6]
```

**Q3:** What is the output?
```python
result = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
print(result)

Answer: [2, 4]
```

**Q4:** What does `nonlocal` do?
- A) Creates a global variable
- B) Allows modifying a variable in an enclosing (non-global) scope
- C) Prevents variable modification
- D) Deletes a variable

Answer: B

**Q5:** What is the output?
```python
def outer():
    x = 10
    def inner():
        return x
    return inner

f = outer()
print(f())


Answer: 10
```

**Q6:** What is the output?
```python
from functools import reduce
print(reduce(lambda a, b: a + b, [1, 2, 3, 4], 10))

Answer: 20
```

**Q7:** What does `@decorator` above a function definition do?
- A) Deletes the function
- B) Calls the function immediately
- C) Replaces the function with `decorator(function)`
- D) Creates a copy of the function

Answer: C

**Q8:** True or False: `map()` and `filter()` return lists in Python 3.

Answer: False - you'd have to manually convert them to lists as normally they return map/filter object respectively (a memory object string as in <filter object at 0x0000018D79150130>
<map object at 0x0000018D1930C700>)

**Q9:** What is the late binding trap?
- A) Lambda functions are slow
- B) Lambda captures variable reference, not value at creation time
- C) Lambda cannot use variables
- D) Lambda runs too late

Answer: B

**Q10:** How do you fix the late binding trap in a loop?
```python
# Broken:
functions = [lambda: i for i in range(3)]

# Fixed:
functions = [i for i in range(3)]
print(functions)
```

The best way would be to use a list comprehension instead

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
Q9:
Q10:
```

---

## Task 2: PCAP Output Predictions (6 Snippets)

**Instructions:** Predict the exact output for each.

**Snippet A:**
```python
f = lambda x, y=10: x + y
print(f(5))
print(f(5, 5))
```

**Snippet B:**
```python
nums = [1, 2, 3, 4, 5]
result = map(lambda x: x ** 2, nums)
print(next(result))
print(next(result))
```

**Snippet C:**
```python
def make_power(n):
    return lambda x: x ** n

square = make_power(2)
cube = make_power(3)
print(square(4), cube(2))
```

**Snippet D:**
```python
from functools import reduce

words = ["P", "C", "A", "P"]
result = reduce(lambda a, b: a + b, words)
print(result)
```

**Snippet E:**
```python
def add_prefix(prefix):
    def decorator(func):
        def wrapper(*args):
            return prefix + func(*args)
        return wrapper
    return decorator

@add_prefix("Hello, ")
def greet(name):
    return name

print(greet("World"))
```

**Snippet F:**
```python
funcs = []
for i in range(3):
    funcs.append(lambda i=i: i * 2)

print(funcs[0](), funcs[1](), funcs[2]())
```

**Your answers:**
```
A: 15, 10

B: 1, 4

C: 16, 8

D: PCAP

E: Hello, World

F: 0 2 4

```

---

## Task 3: Debug the Decorator

**Instructions:** This decorator has bugs. Find and fix them.

```python
def validate_positive(func):
    """Decorator that ensures the result is positive."""
    def wrapper(args):
        result = func(args)
        if result < 0:
            raise ValueError("Result must be positive")
        return result
    return wrapper

@validate_positive
def subtract(a, b):
    return a - b

# Should work:
print(subtract(10, 3))  # 7

# Should raise ValueError:
print(subtract(3, 10))  # -7 → ValueError
```

**Bugs found:**
```
1. Asterisk missing in wrapper function
2. Asterisk missing in result processing 
```

**Fixed code:**
```python

def validate_positive(func):
    """Decorator that ensures the result is positive."""
    def wrapper(*args):
        result = func(*args)
        if result < 0:
            raise ValueError("Result must be positive")
        return result
    return wrapper

@validate_positive
def subtract(a, b):
    return a - b

```

---

## Task 4: Closure State Challenge

**Instructions:** Create a closure that tracks running statistics.

```python
def make_stats_tracker():
    """
    Create a statistics tracker using closures.

    Returns a function that:
    - Accepts a number
    - Tracks count, sum, min, max
    - Returns a dict with current stats

    Example:
        track = make_stats_tracker()
        print(track(10))  # {'count': 1, 'sum': 10, 'min': 10, 'max': 10, 'avg': 10.0}
        print(track(20))  # {'count': 2, 'sum': 30, 'min': 10, 'max': 20, 'avg': 15.0}
        print(track(5))   # {'count': 3, 'sum': 35, 'min': 5, 'max': 20, 'avg': 11.67}
    """
    # Your code here
    pass

# Test:
track = make_stats_tracker()
print(track(10))
print(track(20))
print(track(5))
print(track(15))
```

**Your code:**
```python

def make_stats_tracker():
    """
    Create a statistics tracker using closures.

    Returns a function that:
    - Accepts a number
    - Tracks count, sum, min, max
    - Returns a dict with current stats

    Example:
        track = make_stats_tracker()
        print(track(10))  # {'count': 1, 'sum': 10, 'min': 10, 'max': 10, 'avg': 10.0}
        print(track(20))  # {'count': 2, 'sum': 30, 'min': 10, 'max': 20, 'avg': 15.0}
        print(track(5))   # {'count': 3, 'sum': 35, 'min': 5, 'max': 20, 'avg': 11.67}
    """
    
    tracker = defaultdict(int)
    tracker['max'] = 0
    tracker['min'] = 999
    
    def track(number):
        tracker['sum'] += number
        tracker['count'] += 1
        if number < tracker['min']:
            tracker['min'] = number
        elif number > tracker['max']:
            tracker['max'] = number
        tracker['avg'] = round(tracker['sum'] / tracker['count'], 2)
        return tracker
    return track


$ python practice.py
defaultdict(<class 'int'>, {'max': 0, 'min': 10, 'sum': 10, 'count': 1, 'avg': 10.0})
defaultdict(<class 'int'>, {'max': 20, 'min': 10, 'sum': 30, 'count': 2, 'avg': 15.0})
defaultdict(<class 'int'>, {'max': 20, 'min': 5, 'sum': 35, 'count': 3, 'avg': 11.666666666666666})
defaultdict(<class 'int'>, {'max': 20, 'min': 5, 'sum': 50, 'count': 4, 'avg': 12.5})


```

---

## Task 5: PCAP Multiple Choice (8 Questions)

**Q1:** What is the output?
```python
print((lambda: 42)())
```
- A) `<function>`
- B) `42`
- C) `None`
- D) Error

Answer: B

**Q2:** What is the output?
```python
x = [1, 2, 3]
y = map(str, x)
print(type(y))
```
- A) `<class 'list'>`
- B) `<class 'map'>`
- C) `<class 'str'>`
- D) `<class 'generator'>`

Answer: B

**Q3:** What is the output?
```python
from functools import reduce
result = reduce(lambda a, b: a * b, [2, 3, 4])
print(result)
```
- A) 9
- B) 24
- C) 6
- D) [2, 3, 4]

Answer: B

**Q4:** What is the output?
```python
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

counter = outer()
print(counter(), counter(), counter())
```
- A) 0 0 0
- B) 1 1 1
- C) 1 2 3
- D) Error

Answer: C

**Q5:** Which creates a closure?
- A) `def f(): return 42`
- B) `lambda x: x + 1`
- C) `def outer(n): def inner(): return n; return inner`
- D) `class C: pass`

Answer: C

**Q6:** What is the output?
```python
def deco(f):
    def w():
        return f() + "!"
    return w

@deco
def say():
    return "Hi"

print(say())
```
- A) Hi
- B) Hi!
- C) !Hi
- D) Error

Answer : B

**Q7:** What does `filter(None, [0, 1, "", "a", [], [1]])` return (as a list)?
- A) `[None]`
- B) `[0, 1, "", "a", [], [1]]`
- C) `[1, "a", [1]]`
- D) `[]`

Answer: C - Could you however EXPLAIN this to me, because to me it looks like we are filtering for None objects, so that we're looking for None objects, AND YET here all we get is NOT None objects in return.

**Q8:** What is the output?
```python
add = lambda a, b: a + b
print(add.__name__)
```
- A) `add`
- B) `lambda`
- C) `<lambda>`
- D) Error

Answer: C

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

## Task 6: PROJECT - Functional Trade Processor

**Instructions:** Create a complete trade processing pipeline using functional patterns.

```python
from functools import reduce
from typing import List, Dict, Callable

# Sample trades
trades = [
    {"id": 1, "ticker": "AAPL", "side": "BUY", "entry": 150, "exit": 165, "qty": 10},
    {"id": 2, "ticker": "GOOGL", "side": "BUY", "entry": 2800, "exit": 2750, "qty": 5},
    {"id": 3, "ticker": "MSFT", "side": "SELL", "entry": 300, "exit": 280, "qty": 20},
    {"id": 4, "ticker": "TSLA", "side": "BUY", "entry": 700, "exit": 720, "qty": 8},
    {"id": 5, "ticker": "NVDA", "side": "SELL", "entry": 500, "exit": 520, "qty": 15},
]

# Part A: Create a function that calculates PnL based on side
def calculate_pnl(trade: Dict) -> float:
    """Calculate PnL: BUY = (exit-entry)*qty, SELL = (entry-exit)*qty"""
    # Your code here (use ternary expression)
    pass

# Part B: Add PnL to each trade using map
trades_with_pnl = # Your code using map and calculate_pnl

# Part C: Create filter functions
is_winner = lambda t: # Your code - returns True if pnl > 0
is_loser = lambda t:  # Your code - returns True if pnl < 0
is_buy = lambda t:    # Your code - returns True if side == "BUY"

# Part D: Get statistics using reduce
def get_stats(trades_list: List[Dict]) -> Dict:
    """
    Calculate: total_pnl, win_count, loss_count, best_trade, worst_trade
    """
    if not trades_list:
        return {}

    total_pnl = # reduce to sum all pnl
    win_count = # reduce to count winners
    loss_count = # reduce to count losers
    best = # reduce to find max pnl trade
    worst = # reduce to find min pnl trade

    return {
        "total_pnl": total_pnl,
        "win_count": win_count,
        "loss_count": loss_count,
        "best_ticker": best["ticker"],
        "worst_ticker": worst["ticker"],
    }

# Test:
print("All trades with PnL:")
for t in trades:
    print(f"  {t['ticker']}: ${t['pnl']}")

print(f"\nWinners: {[t['ticker'] for t in filter(is_winner, trades_with_pnl)]}")
print(f"Losers: {[t['ticker'] for t in filter(is_loser, trades_with_pnl)]}")
print(f"BUY trades: {[t['ticker'] for t in filter(is_buy, trades_with_pnl)]}")

stats = get_stats(trades_with_pnl)
print(f"\nStats: {stats}")
```

**Your code:**
```python

from functools import reduce
from typing import List, Dict, Callable

# Sample trades
trades = [
    {"id": 1, "ticker": "AAPL", "side": "BUY", "entry": 150, "exit": 165, "qty": 10},
    {"id": 2, "ticker": "GOOGL", "side": "BUY", "entry": 2800, "exit": 2750, "qty": 5},
    {"id": 3, "ticker": "MSFT", "side": "SELL", "entry": 300, "exit": 280, "qty": 20},
    {"id": 4, "ticker": "TSLA", "side": "BUY", "entry": 700, "exit": 720, "qty": 8},
    {"id": 5, "ticker": "NVDA", "side": "SELL", "entry": 500, "exit": 520, "qty": 15},
]

def calculate_pnl(trade: Dict) -> float:
    """Calculate PnL: BUY = (exit-entry)*qty, SELL = (entry-exit)*qty"""
    # Your code here (use ternary expression)
    trade['pnl'] = (trade['exit'] - trade['entry']) * trade['qty'] if trade['side'] == 'BUY' else (trade['entry'] - trade['exit']) * trade['qty']


for trade in trades:
    calculate_pnl(trade)

# unnecessary and weird, as I instantly add pnl with a single line in calculate_pnl, but I wanted to try and practice this
# trades_with_pnl = map(lambda t: {t** 'pnl': calculate_pnl(t)}, trades)

is_winner = lambda t: t['pnl'] > 0
is_loser = lambda t: t['pnl'] < 0
is_buy = lambda t: t['side'] == 'BUY'

total_pnl = reduce(lambda acc, t: acc + t['pnl'], trades, 0)
win_count = reduce(lambda acc, t: acc + 1 if t['pnl'] > 0 else acc, trades, 0)
loss_count = reduce(lambda acc, t: acc + 1 if t['pnl'] < 0 else acc, trades, 0)
best = reduce(lambda acc, t: t if t['pnl'] > acc['pnl'] else acc, trades)
worst = reduce(lambda acc, t: t if t['pnl'] < acc['pnl'] else acc, trades)
print(best)
print(worst)


def get_stats(trades_list: List[Dict]) -> Dict:
    """
    Calculate: total_pnl, win_count, loss_count, best_trade, worst_trade
    """
    if not trades_list:
        return {}

    total_pnl = reduce(lambda acc, t: acc + t['pnl'], trades, 0)
    win_count = reduce(lambda acc, t: acc + 1 if t['pnl'] > 0 else acc, trades, 0)
    loss_count = reduce(lambda acc, t: acc + 1 if t['pnl'] < 0 else acc, trades, 0)
    best = reduce(lambda acc, t: t if t['pnl'] > acc['pnl'] else acc, trades)
    worst = reduce(lambda acc, t: t if t['pnl'] < acc['pnl'] else acc, trades)

    return {
        "total_pnl": total_pnl,
        "win_count": win_count,
        "loss_count": loss_count,
        "best_ticker": best["ticker"],
        "worst_ticker": worst["ticker"],
    }
    
    
print("All trades with PnL:")
for t in trades:
    print(f"  {t['ticker']}: ${t['pnl']}")

print(f"\nWinners: {[t['ticker'] for t in filter(is_winner, trades)]}")
print(f"Losers: {[t['ticker'] for t in filter(is_loser, trades)]}")
print(f"BUY trades: {[t['ticker'] for t in filter(is_buy, trades)]}")

stats = get_stats(trades)
print(f"\nStats: {stats}")

OUTPUT:

$ python practice.py
{'id': 3, 'ticker': 'MSFT', 'side': 'SELL', 'entry': 300, 'exit': 280, 'qty': 20, 'pnl': 400}
{'id': 5, 'ticker': 'NVDA', 'side': 'SELL', 'entry': 500, 'exit': 520, 'qty': 15, 'pnl': -300}
All trades with PnL:
  AAPL: $150
  GOOGL: $-250
  MSFT: $400
  TSLA: $160
  NVDA: $-300

Winners: ['AAPL', 'MSFT', 'TSLA']
Losers: ['GOOGL', 'NVDA']
BUY trades: ['AAPL', 'GOOGL', 'TSLA']

Stats: {'total_pnl': 160, 'win_count': 3, 'loss_count': 2, 'best_ticker': 'MSFT', 'worst_ticker': 'NVDA'}

I've used trades and not trades_with_pnl FOR SIMPLICITY, not overoccupying the namespace + generally I think it's much clearer and makes a lot more sense.


```

---

## Task 7: Decorator with functools.wraps

**Instructions:** Learn about `functools.wraps` - it preserves the original function's metadata.

```python
from functools import wraps

# Without @wraps - function metadata is lost
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def greet(name):
    """Greets a person by name."""
    return f"Hello, {name}!"

print(greet.__name__)  # What does this print?
print(greet.__doc__)   # What does this print?
```

**Q1:** What does `greet.__name__` print without `@wraps`?
It prints the wrapper's name as metadata is lost.

**Q2:** What does `greet.__doc__` print without `@wraps`?
Nothing here, as it prints the wrapper's docstring, and it's empty here.

**Q3:** Now fix the decorator using `@wraps(func)`:

```python
from functools import wraps

def good_decorator(func):
    @wraps(func)  # Add this line
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def greet(name):
    """Greets a person by name."""
    return f"Hello, {name}!"

print(greet.__name__)  # Now what?
print(greet.__doc__)   # Now what?
```

**Your answers:**
```
Q1 (without @wraps): It prints the wrapper's name as metadata is lost.


Q2 (without @wraps): Nothing here, as it prints the wrapper's docstring, and it's empty here.

Q3 (with @wraps):
__name__: greet
__doc__: Greets a person by name.
```

---

## Task 8: Integration - Putting It All Together

**Instructions:** Answer these conceptual questions about when to use what.

**Q1:** When would you use `map()` vs a list comprehension?
```python
# Option A: map
result = list(map(lambda x: x * 2, numbers))

# Option B: list comprehension
result = [x * 2 for x in numbers]

Answer: I would honestly use list comprehensions in most cases and it's easier to read and understand and would probably be in most cases.
```

**Q2:** When would you use `filter()` vs a list comprehension with `if`?
```python
# Option A: filter
result = list(filter(lambda x: x > 0, numbers))

# Option B: list comprehension
result = [x for x in numbers if x > 0]

Same case as above, I'd rather use list comprehensions - it's more Pythonic and readable.
```

**Q3:** When would you use a closure vs a class?

I'd use class in 90% cases - closures mostly for very simple cases or to show I understand how they work.

**Q4:** When would you use `reduce()` vs a simple loop?
Reduce seems a good alternative - it's a one-liner and a great way to quickly sum PNLs, find the best/worst/ any particular data value - that's very useful and also more Pythonic than a loop in many cases and it takes less space.

**Q5:** What's the main advantage of decorators?
They allow you to wrap a function with them to add additional information - they also allow to keep the original function's metadata if we use wraps.

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

- [ ] Task 1: Quick fire review (10 questions)
- [ ] Task 2: Output predictions (6 snippets)
- [ ] Task 3: Debug the decorator
- [ ] Task 4: Closure state challenge
- [ ] Task 5: PCAP multiple choice (8 questions)
- [ ] Task 6: PROJECT - Functional trade processor
- [ ] Task 7: functools.wraps
- [ ] Task 8: Integration concepts (5 questions)

---

## Feedback Section

**Time spent:** ___ minutes

**Difficulty (1-10):**

**Ready for Friday's exams?**
[ ] Yes
[ ] Need more practice on: _______________

**Questions for mentor:**


---

**When complete:** Notify me for assessment. Friday = 2 PCAP Mock Exams!
