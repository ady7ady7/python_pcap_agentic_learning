# Week 4, Day 3 - Wednesday
## Topic: reduce(), Decorators & Functional Patterns

**Date:** 2026-01-28

**NEW CONTENT:** Read the **reduce()** and **Decorators** sections added to `lessons/week4_lambda_closures.md` before starting!

**Target Difficulty:** 5/10

**Remember:** Work in `practice.py`, paste FINAL answers here for review.

---

## Task 1: reduce() Basics (PCAP Warm-up)

**Instructions:** You need `from functools import reduce` for these.

**Q1:** What is the output?
```python
from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda acc, x: acc + x, numbers)
print(result)

Answer: 10
```

**Q2:** What is the output?
```python
from functools import reduce

numbers = [1, 2, 3, 4]
result = reduce(lambda acc, x: acc * x, numbers)
print(result)

Answer: 24
```

**Q3:** What is the output? (Notice the initializer!)
```python
from functools import reduce

numbers = [1, 2, 3]
result = reduce(lambda acc, x: acc + x, numbers, 10)
print(result)

Answer: 16
```

**Q4:** What is the output?
```python
from functools import reduce

words = ["a", "b", "c"]
result = reduce(lambda acc, x: acc + x, words)
print(result)

Answer: abc
```

**Your answers:**
```
Q1:
Q2:
Q3:
Q4:
```

---

## Task 2: reduce() Implementation

**Instructions:** Use `reduce()` to solve these. Import functools.

**Part A:** Calculate the product of all numbers in a list.
```python
from functools import reduce

numbers = [2, 3, 4, 5]
# Your code here - should print 120

calc = reduce(lambda acc, x: acc * x, numbers)
print(calc)
```

**Part B:** Find the maximum value using reduce (don't use max()).
```python
from functools import reduce

numbers = [3, 7, 2, 9, 4]
# Your code here - should print 9

maximum = reduce(lambda acc, x: x if x > acc else acc, numbers)
print(maximum)

```

**Part C:** Flatten a nested list using reduce.
```python
from functools import reduce

nested = [[1, 2], [3, 4], [5, 6]]
# Result should be [1, 2, 3, 4, 5, 6]
# Hint: acc + x where both are lists


flattened = reduce(lambda acc, x: acc + x if type(x) == list else x, nested)
print(flattened)

```

**Your code:**
```python
# Part A:


# Part B:


# Part C:

```

---

## Task 3: Decorator Basics

**Q1:** What is the output?
```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hi():
    print("Hi!")

say_hi()

Before
Hi!
After
```

**Q2:** The `@decorator` syntax is shorthand for what?
```python
@my_decorator
def foo():
    pass

# Is equivalent to: foo = ???

foo = my_decorator.foo() #foo function wrapped in a decorator
```

**Q3:** True or False: A decorator is essentially a closure that wraps a function.

True

**Q4:** What is the output?
```python
def double_result(func):
    def wrapper(x):
        return func(x) * 2
    return wrapper

@double_result
def add_ten(n):
    return n + 10

print(add_ten(5))


30

```

**Your answers:**
```
Q1:

Q2: foo =

Q3:

Q4:
```

---

## Task 4: Create a Simple Decorator

**Instructions:** Create a decorator that prints "Executing..." before a function runs.

```python
def announce(func):
    """
    Decorator that prints 'Executing...' before calling the function.
    """
    # Your code here
    pass

# Test:
@announce
def greet(name):
    print(f"Hello, {name}!")

@announce
def add(a, b):
    return a + b

greet("Alice")
# Expected output:
# Executing...
# Hello, Alice!

result = add(3, 5)
# Expected output:
# Executing...
print(result)  # 8
```

**Hint:** Use `*args, **kwargs` to handle any function signature.

**Your code:**
```python


def announce(func):
    '''A decorator that wraps a function which prints 'Executing' before calling the function'''
    
    def wrapper(*args, **kwargs):
        print(f'Executing...')
        func(*args, **kwargs) 
        return func(*args, **kwargs)
    
    return wrapper

Your hint was very important here - but anyway I need to practice this, as it's unintuitive at this point.


```

---

## Task 5: PROJECT - Trade Statistics with reduce()

**Instructions:** Use `reduce()` to calculate trade statistics.

```python
from functools import reduce

trades = [
    {"ticker": "AAPL", "pnl": 150.0},
    {"ticker": "GOOGL", "pnl": -50.0},
    {"ticker": "MSFT", "pnl": 200.0},
    {"ticker": "TSLA", "pnl": -100.0},
    {"ticker": "NVDA", "pnl": 300.0},
]

# Part A: Calculate total PnL using reduce
total_pnl = # Your code here
print(f"Total PnL: ${total_pnl}")  # Total PnL: $500.0

# Part B: Count winning trades using reduce
# Hint: accumulator is a count, increment if pnl > 0
win_count = # Your code here
print(f"Winning trades: {win_count}")  # Winning trades: 3

# Part C: Find the best trade (highest pnl) using reduce
best_trade = # Your code here
print(f"Best trade: {best_trade['ticker']} with ${best_trade['pnl']}")
# Best trade: NVDA with $300.0
```

**Your code:**
```python

# Part A: Calculate total PnL using reduce
total_pnl = reduce(lambda acc, value: acc + value['pnl'], trades, 0)
print(f"Total PnL: ${total_pnl}")  # Total PnL: $500.0
#Tutaj kluczowe było dodanie 0 jako wartości startowej, bo inaczej nie mogłem tego chwycić i wyskakiwały TypeErrory!


# Part B: Count winning trades using reduce
win_count = reduce(lambda acc, trade: acc + 1 if trade['pnl'] > 0 else acc, trades, 0)
print(f"Winning trades: {win_count}")  # Winning trades: 3

# Part C: Find the best trade (highest pnl) using reduce
best_trade = reduce(lambda acc, trade: acc if acc['pnl'] > trade['pnl'] else trade, trades)
print(f"Best trade: {best_trade['ticker']} with ${best_trade['pnl']}")
# Best trade: NVDA with $300.0


```

---

## Task 6: PCAP Multiple Choice

**Q1:** What does `reduce()` do?
- A) Removes elements from a list
- B) Applies a function cumulatively to reduce a sequence to a single value
- C) Filters elements based on a condition
- D) Maps a function to all elements

B

**Q2:** What is the output?
```python
from functools import reduce
result = reduce(lambda a, b: a if a > b else b, [3, 1, 4, 1, 5])
print(result)
```
- A) 3
- B) 1
- C) 5
- D) 14

C

**Q3:** What is the output?
```python
def decorator(func):
    def wrapper(*args):
        return func(*args) + 10
    return wrapper

@decorator
def multiply(a, b):
    return a * b

print(multiply(3, 4))
```
- A) 12
- B) 22
- C) 10
- D) Error

B

**Q4:** Which statement about decorators is TRUE?
- A) Decorators can only wrap functions with no parameters
- B) Decorators replace the original function with a new function
- C) Decorators must return None
- D) Decorators cannot access the wrapped function's arguments

D


**Your answers:**
```
Q1:
Q2:
Q3:
Q4:
```

---

## Task 7: PROJECT - Simple Logging Decorator

**Instructions:** Create a decorator that logs function calls for the backtesting project.

```python
def log_call(func):
    """
    Decorator that prints the function name and arguments when called.

    Example output:
    Calling calculate_pnl(entry=100, exit=110, qty=10)
    """
    def wrapper(*args, **kwargs):
        # Your code here
        # 1. Build a string showing function name and arguments
        # 2. Print the log message
        # 3. Call and return the original function
        pass
    return wrapper

# Test:
@log_call
def calculate_pnl(entry: float, exit: float, qty: float) -> float:
    return (exit - entry) * qty

@log_call
def is_winner(pnl: float) -> bool:
    return pnl > 0

result = calculate_pnl(100.0, 110.0, 10.0)
# Expected: Calling calculate_pnl(100.0, 110.0, 10.0)
print(f"PnL: {result}")  # PnL: 100.0

win = is_winner(result)
# Expected: Calling is_winner(100.0)
print(f"Winner: {win}")  # Winner: True
```

**Your code:**
```python

def log_call(func):
    """
    Decorator that prints the function name and arguments when called.

    Example output:
    Calling calculate_pnl(entry=100, exit=110, qty=10)
    """
    def wrapper(*args, **kwargs):
        print(f'Executing {func.__name__}({*args, *kwargs})')
        return func(*args, **kwargs)
    
    return wrapper

```

---

## Task 8: Combining Everything

**Instructions:** Combine lambda, map, filter, and reduce to process trade data.

```python
from functools import reduce

trades = [
    {"ticker": "AAPL", "side": "BUY", "entry": 150, "exit": 160, "qty": 10},
    {"ticker": "GOOGL", "side": "SELL", "entry": 2800, "exit": 2750, "qty": 5},
    {"ticker": "MSFT", "side": "BUY", "entry": 300, "exit": 290, "qty": 20},
    {"ticker": "TSLA", "side": "BUY", "entry": 700, "exit": 750, "qty": 8},
    {"ticker": "NVDA", "side": "SELL", "entry": 500, "exit": 480, "qty": 15},
]

# Step 1: Calculate PnL for each trade using map
# BUY: (exit - entry) * qty
# SELL: (entry - exit) * qty
# Add 'pnl' key to each trade dict
trades_with_pnl = list(map(
    lambda t: {**t, "pnl": # Your expression here },
    trades
))

# Step 2: Filter only winning trades using filter
winners = list(filter(
    lambda t: # Your condition here,
    trades_with_pnl
))

# Step 3: Calculate total winning PnL using reduce
total_winning_pnl = reduce(
    lambda acc, t: # Your expression here,
    winners,
    0  # Initial value
)

print(f"Winning trades: {len(winners)}")
print(f"Total winning PnL: ${total_winning_pnl}")

# Expected:
# Winning trades: 3
# Total winning PnL: $950.0
```

**Your code:**
```python

trades_with_pnl = list(map(
    lambda t: {**t, "pnl": (t['exit'] - t['entry']) * t['qty']} if t['side'] == 'BUY' else
    {**t, "pnl": (t['entry'] - t['exit']) * t['qty']},
    trades
))

winning_trades = list(filter(lambda t: t if t['pnl'] > 0 else 0, trades_with_pnl))

total_winning_pnl = reduce(lambda acc, t: acc + t['pnl'], winning_trades, 0)

Also, you are wrong as there are clearly 4 winning trades with total PNL of 1050$


$ python practice.py
[{'ticker': 'AAPL', 'side': 'BUY', 'entry': 150, 'exit': 160, 'qty': 10, 'pnl': 100}, {'ticker': 'GOOGL', 'side': 'SELL', 'entry': 2800, 'exit': 2750, 'qty': 5, 'pnl': 250}, {'ticker': 'MSFT', 'side': 'BUY', 'entry': 300, 'exit': 290, 'qty': 20, 'pnl': -200}, {'ticker': 'TSLA', 'side': 'BUY', 'entry': 700, 'exit': 750, 'qty': 8, 'pnl': 400}, {'ticker': 'NVDA', 'side': 'SELL', 'entry': 500, 'exit': 480, 'qty': 15, 'pnl': 300}]
[{'ticker': 'AAPL', 'side': 'BUY', 'entry': 150, 'exit': 160, 'qty': 10, 'pnl': 100}, {'ticker': 'GOOGL', 'side': 'SELL', 'entry': 2800, 'exit': 2750, 'qty': 5, 'pnl': 250}, {'ticker': 'TSLA', 'side': 'BUY', 'entry': 700, 'exit': 750, 'qty': 8, 'pnl': 400}, {'ticker': 'NVDA', 'side': 'SELL', 'entry': 500, 'exit': 480, 'qty': 15, 'pnl': 300}]
Winning trades: 4
Total winning PnL: $1050

```

---

## Solutions Checklist

- [ ] Task 1: reduce() basics (4 questions)
- [ ] Task 2: reduce() implementations (3 parts)
- [ ] Task 3: Decorator basics (4 questions)
- [ ] Task 4: Create announce decorator
- [ ] Task 5: PROJECT - Trade stats with reduce (3 parts)
- [ ] Task 6: PCAP Multiple choice (4 questions)
- [ ] Task 7: PROJECT - log_call decorator
- [ ] Task 8: Combining map/filter/reduce

---

## Feedback Section

**Time spent:** ___ minutes

**Difficulty (1-10):**

**What clicked:**


**What's confusing:**


**Questions for mentor:**


---

**When complete:** Fill out feedback section and notify me for assessment.
