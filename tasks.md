# Week 6, Day 4 - Thursday
## Topic: Advanced Generators, Parameterized Decorators & Context Recognition


**Date:** 2026-02-12


**Target Difficulty:** 6-7/10


**Focus:** Iterable recognition in exam context (Day 3 Q8 Q1 gap), parameterized decorators, generator performance patterns, more project integration


**Remember:** Work in `practice.py`, paste FINAL answers here for review.


#Start 10:52


---


## Task 1: PCAP Warm-up — Iterator vs Iterable Recognition Drill


**Context:** You nailed the concepts but missed Q8 Q1. This drill focuses on **quick recognition** under exam pressure.


**Q1:** Examine this class. Is it an **iterator** or **iterable**? What will happen on the second `list()` call?
```python
class Mystery1:
    def __init__(self):
        self.data = [10, 20, 30]
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= len(self.data):
            raise StopIteration
        val = self.data[self.i]
        self.i += 1
        return val

m = Mystery1()
print(list(m))  # What?
print(list(m))  # What?

Answer: [10, 20, 30], [] - empty list
```


**Q2:** Examine this class. Is it an **iterator** or **iterable**? What will happen on the second `list()` call?
```python
class Mystery2:
    def __init__(self):
        self.data = [10, 20, 30]

    def __iter__(self):
        return iter(self.data)

m = Mystery2()
print(list(m))  # What?
print(list(m))  # What?

It's an iterable, so we can iterate over it over and over again, getting
[10, 20, 30] every single time
```


**Q3:** Examine this class. Is it an **iterator** or **iterable**? What will happen on the second `list()` call?
```python
class Mystery3:
    def __init__(self):
        self.data = [10, 20, 30]

    def __iter__(self):
        for item in self.data:
            yield item

m = Mystery3()
print(list(m))  # What?
print(list(m))  # What?

Same, it's an iterable, although I don't QUITE understand why it doesn't get exhausted like example1.
But to be clear, we would get [10, 20, 30] with every call
```


**Quick Recognition Rule:**
- `__iter__` returns `self` → **Iterator** → exhausted after first use
- `__iter__` returns new iterator (via `yield`, `iter(...)`, etc.) → **Iterable** → reusable


**Your answers:**
```
Q1: Iterator / Iterable? Output?


Q2: Iterator / Iterable? Output?


Q3: Iterator / Iterable? Output?


```


---


## Task 2: Decorator Evolution — Parameterized Version


**Day 1:** Trace. **Day 2:** Fill blanks. **Day 3:** Write from scratch. **Day 4:** Add parameters.


**Goal:** Write `@repeat(n)` that runs a function `n` times and collects all results in a list.


**Requirements:**
- Takes a parameter `n` (number of repetitions)
- Calls the decorated function `n` times with the same arguments
- Returns a list of all results
- Uses `@wraps` to preserve metadata


**Template:**
```python
from functools import wraps

def repeat(n):
    """Decorator factory that repeats function execution n times."""
    # Your code — THREE nested functions:
    # 1. repeat(n) — decorator factory (takes parameter)
    # 2. decorator(func) — actual decorator (takes function)
    # 3. wrapper(*args, **kwargs) — wrapper (takes function args)


# Test 1 — simple function:
@repeat(3)
def roll_dice():
    import random
    return random.randint(1, 6)

print(roll_dice())  # Should return list of 3 random numbers


# Test 2 — function with arguments:
@repeat(4)
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # ['Hello, Alice!', 'Hello, Alice!', 'Hello, Alice!', 'Hello, Alice!']


# Test 3 — metadata preserved:
print(greet.__name__)  # greet
```


**Your code:**
```python

from functools import wraps

def repeat(n):
    """Decorator factory that repeats function execution n times."""
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result_list = []
            for _ in range(n):
                result = func(*args, **kwargs)
                result_list.append(result)
            return result_list
        return wrapper
    return decorator





```


---


## Task 3: Generator Performance — When Lists ARE Better


**Context:** You said "generators always faster" in Day 3 Q3. Not quite! Here's when lists win.


**Q1:** Predict which is faster and why:
```python
import time

# Scenario A: Multiple passes needed
def scenario_a_gen():
    data = (x ** 2 for x in range(10000))
    result = sum(data) + max(data)  # BUG! What happens?
    return result

def scenario_a_list():
    data = [x ** 2 for x in range(10000)]
    result = sum(data) + max(data)
    return result

#The max() argument in scenario a with generator will be empty, we'd have to do a separate pass for max and sum, but then we'd already EXHAUST the generator with the first pass, even if we'd split sum(data) and max(data). We'd have to create/recreate a separate generator to make it work
#The list works WITHOUT any problems, it's simply faster/more efficient and convenient here.


# Scenario B: Single pass, memory-constrained
def scenario_b_gen():
    data = (x ** 2 for x in range(10000000))
    return sum(data)

def scenario_b_list():
    data = [x ** 2 for x in range(10000000)]
    return sum(data)

#Here generator works just fine, as we get the sum with the first pass, that also exhausts the generator, but it's alright.
```


**Q2:** True or False — explain:
- "Generators use less memory than lists." 
- "Generators are always faster than lists."
- "If you need to iterate data multiple times, generators are better."


**Your answers:**
```
Q1 Scenario A: Which is faster? What's the bug?


Q1 Scenario B: Which is faster? Why?


Q2:
Statement 1:


Statement 2:


Statement 3:


```


---


## Task 4: Predict Output — Generator Return Values & send()


**Q1:** What is the output?
```python
def gen_with_return():
    yield 1
    yield 2
    return "DONE"

g = gen_with_return()
print(list(g))
```
- A) `[1, 2, "DONE"]`
- B) `[1, 2]`
- C) `[1, 2, None]`
- D) Error


Answer: B

**Q2:** What is the output?
```python
def counter():
    total = 0
    while True:
        x = yield total
        if x is not None:
            total += x

c = counter()
next(c)  # Prime the generator
c.send(5)
c.send(10)
print(c.send(3))
```
- A) `3`
- B) `18`
- C) `15`
- D) Error


**Q3:** What is the output?
```python
def chained():
    yield from range(3)
    yield from [10, 20]

print(list(chained()))
```
- A) `[0, 1, 2, 10, 20]`
- B) `[[0, 1, 2], [10, 20]]`
- C) `[range(0, 3), [10, 20]]`
- D) Error


**Your answers:**
```
Q1:


Q2:


Q3:


```


---


## Task 5: PROJECT — Filtered Price Stream with Filter Predicate


**Goal:** Extend `create_price_stream()` to accept a custom filter function (not just ticker).


**Requirements:**
- Add optional parameter `filter_func: callable = None`
- If provided, only yield ticks where `filter_func(tick)` returns `True`
- Preserve existing `ticker` filter for backward compatibility
- Both filters can work together


```python
def create_price_stream(file_path: str, ticker: str = None, filter_func: callable = None):
    """
    Generator that streams price data with optional filtering.

    Args:
        file_path: Path to CSV file.
        ticker: Optional ticker filter.
        filter_func: Optional predicate function. Should take a PriceTick and return bool.

    Yields:
        PriceTick namedtuple for each row that passes filters.
    """
    # Your code


# Test 1 — filter by ticker AND high price:
def high_volatility(tick):
    return tick.high - tick.low > 2.0

stream = create_price_stream('ohlc_mock_data.csv', 
                              ticker='EURUSD', 
                              filter_func=high_volatility)

for i, tick in enumerate(stream):
    if i >= 3:
        break
    print(f"{tick.timestamp} | Range: {tick.high - tick.low:.2f}")


# Test 2 — filter by volume threshold:
stream2 = create_price_stream('ohlc_mock_data.csv',
                               filter_func=lambda t: t.volume > 15000)

print(f"\nHigh volume ticks: {sum(1 for _ in stream2)}")
```


**Your code:**
```python




```


---


## Task 6: PROJECT — Strategy Pattern with Generators


**Goal:** Create a `SimpleMovingAverage` indicator that consumes price stream and yields signals.


**Requirements:**
- Takes a price stream generator as input
- Calculates SMA over a window (e.g., 5 ticks)
- Yields tuple: `(tick, sma_value)` for each tick after window fills
- Uses generator chaining pattern


```python
from collections import deque

def sma_indicator(price_stream, window=5):
    """
    Generator that calculates Simple Moving Average over price stream.

    Args:
        price_stream: Generator yielding PriceTick objects.
        window: Number of periods for SMA calculation.

    Yields:
        Tuple of (PriceTick, sma_value) for each tick after window fills.
    """
    # Your code — use deque for efficient window management


# Test:
stream = create_price_stream('ohlc_mock_data.csv', ticker='EURUSD')
sma_stream = sma_indicator(stream, window=3)

for i, (tick, sma) in enumerate(sma_stream):
    if i >= 5:
        break
    print(f"{tick.timestamp} | Close: {tick.close} | SMA(3): {sma:.2f}")
```


**Your code:**
```python


def sma_indicator(price_stream, window=5):
    """
    Generator that calculates Simple Moving Average over price stream.

    Args:
        price_stream: Generator yielding PriceTick objects.
        window: Number of periods for SMA calculation.

    Yields:
        Tuple of (PriceTick, sma_value) for each tick after window fills.
    """
    
    price_list = []
    sma_value = 0
    
    for i, tick in enumerate(price_stream):
        price_list.append(tick.close)
        if len(price_list) >= window:
            sma_value = float(sum(price_list) / window)
            price_list.pop(0)
        yield tick, sma_value
            

# Test:
stream = create_price_stream('ohlc_mock_data.csv', ticker='EURUSD')
sma_stream = sma_indicator(stream, window=3)

for i, (tick, sma) in enumerate(sma_stream):
    if i >= 5:
        break
    print(f"{tick.timestamp} | Close: {tick.close} | SMA(3): {sma:.2f}")

LOG: 
$ python practice.py
DataLoader initialized.
Data loading succeeded
Data loading operation ended.
2024-01-01 09:00:00 | Close: 100.8 | SMA(3): 0.00
2024-01-01 09:01:00 | Close: 101.3 | SMA(3): 0.00
2024-01-01 09:02:00 | Close: 101.5 | SMA(3): 101.20
2024-01-01 09:03:00 | Close: 101.9 | SMA(3): 101.33
2024-01-01 09:04:00 | Close: 102.3 | SMA(3): 101.47
(.venv) 


It works
```


---


## Task 7: PCAP Exam Context — Tricky Iterator Questions


**Q1:** What is the output?
```python
class Counter:
    def __init__(self, max_val):
        self.max_val = max_val

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current >= self.max_val:
            raise StopIteration
        self.current += 1
        return self.current

c = Counter(3)
print(list(c))
print(list(c))
```
- A) `[1, 2, 3]` then `[1, 2, 3]`
- B) `[1, 2, 3]` then `[]`
- C) `[0, 1, 2]` then `[]`
- D) `[0, 1, 2]` then `[0, 1, 2]`

Answer: C




**Q2:** What is the output?
```python
nums = [1, 2, 3]
it = iter(nums)
nums.append(4)
print(list(it))
```
- A) `[1, 2, 3]`
- B) `[1, 2, 3, 4]`
- C) `[4]`
- D) Error

B


**Q3:** What is the output?
```python
def gen():
    yield 1
    yield 2

g1 = gen()
g2 = gen()
print(next(g1))
print(next(g2))
print(next(g1))
```
- A) `1` `1` `2`
- B) `1` `2` Error
- C) `1` `2` `1`
- D) Error

Answer:  C


**Your answers:**
```
Q1:


Q2:


Q3:


```


---


## Task 8: PCAP Simulation — Mixed Concepts (5 Questions)


**Q1:** What is the output?
```python
from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args):
        print(f"Called {func.__name__}")
        return func(*args)
    return wrapper

@trace
@trace
def foo(x):
    return x * 2

foo(5)
```
- A) `Called foo` (once)
- B) `Called foo` `Called foo` (twice)
- C) `Called wrapper` `Called foo`
- D) `Called wrapper` (twice)

Answer: C


**Q2:** What is the output?
```python
class Data:
    def __init__(self):
        self.items = [1, 2, 3]

    def __iter__(self):
        return iter(self.items)

d = Data()
it = iter(d)
print(it is d)
print(list(d))
print(list(it))
```
- A) `False` `[1, 2, 3]` `[1, 2, 3]`
- B) `False` `[1, 2, 3]` `[]`
- C) `True` `[1, 2, 3]` `[]`
- D) `True` `[1, 2, 3]` `[1, 2, 3]`

D


**Q3:** What is the output?
```python
gen = (x for x in range(3))
print(0 in gen)
print(1 in gen)
```
- A) `True` `True`
- B) `True` `False`
- C) `False` `False`
- D) Error

C


**Q4:** What is the output?
```python
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times_three = make_multiplier(3)
print(times_three(5))
print(times_three.__name__)
```
- A) `15` `times_three`
- B) `15` `multiplier`
- C) `15` `make_multiplier`
- D) Error


C

**Q5:** Which statement about generators is FALSE?
- A) Generators can be exhausted after one iteration
- B) Generator functions use `yield` instead of `return`
- C) Generator expressions use parentheses `()`
- D) Generators always consume less memory than lists

D - not always

**Your answers:**
```
Q1:


Q2:


Q3:


Q4:


Q5:


```


---





**Key Focus Areas for Today:**
1. Instant iterator vs iterable recognition (Task 1, 7)
2. Parameterized decorator structure (Task 2)
3. Generator performance trade-offs (Task 3)
4. Advanced generator patterns: `send()`, `return`, chaining (Task 4)
5. Real-world project patterns (Tasks 5, 6)


**Note from yesterday:** "Iterable recognition in exam context" and "generators always faster misconception" — both addressed today.
