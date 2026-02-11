# Week 6, Day 3 - Wednesday
## Topic: Iterable vs Iterator, Decorator Writing & Price Stream Generator

**Date:** 2026-02-11

**Target Difficulty:** 5-6/10

**Focus:** Iterable vs Iterator distinction (Day 2 Q2 gap), write a decorator from scratch, build `create_price_stream()` generator for the project

**Lesson:** Review `lessons/week6_iterators_generators_advanced.md` — especially "Generator vs Iterator vs Iterable" section.

**Remember:** Work in `practice.py`, paste FINAL answers here for review.

#Start 11:10 
---

## Task 1: PCAP Warm-up — Iterable vs Iterator

Yesterday's Q2 exposed a gap. Here's the rule:

> **Iterator:** Has `__iter__` returning `self` + `__next__`. One-shot (unless you reset state). `iter(obj) is obj` → True.
>
> **Iterable:** Has `__iter__` that creates and returns a **new iterator** each time. Reusable. `iter(obj) is iter(obj)` → False.
>
> **When `__iter__` uses `yield`:** It becomes a generator function. Each call creates a new generator object → **iterable pattern**.

**Q1:** What is the output?
```python
class IteratorStyle:
    def __init__(self):
        self.items = [1, 2, 3]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.items):
            raise StopIteration
        val = self.items[self.index]
        self.index += 1
        return val

obj = IteratorStyle()
print(iter(obj) is obj)
print(list(obj))
print(list(obj))


Answer:  True, [1, 2, 3], []
```

**Q2:** What is the output?
```python
class IterableStyle:
    def __init__(self):
        self.items = [1, 2, 3]

    def __iter__(self):
        for item in self.items:
            yield item

obj = IterableStyle()
it1 = iter(obj)
it2 = iter(obj)
print(it1 is it2)
print(list(obj))
print(list(obj))
```

Answer: False, [1, 2, 3], [1, 2, 3]

This is a bit misleading, as here we create two separate iterators from that one object, and in q1 we did not do that, so we're not showing the real difference.


**Your answers:**
```
Q1: 


Q2:


```

---

## Task 2: Decorator Day 3 — WRITE FROM SCRATCH

Day 1: trace. Day 2: fill blanks. **Day 3: write it yourself.**

**Instructions:** Write a decorator called `@log_call` that:
1. Prints `"Calling {function_name} with args={args}, kwargs={kwargs}"` BEFORE the function runs
2. Calls the function and stores the result
3. Prints `"Returned: {result}"` AFTER the function runs
4. Returns the result
5. Uses `@wraps` to preserve metadata

**Template:**
```python
from functools import wraps

def log_call(func):
    # Your code — write the entire decorator

# Test:
@log_call
def add(a, b):
    return a + b

@log_call
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(add(3, 5))
print(greet("Alice", greeting="Hi"))
print(add.__name__)
```

**Expected output:**
```
Calling add with args=(3, 5), kwargs={}
Returned: 8
8
Calling greet with args=('Alice',), kwargs={'greeting': 'Hi'}
Returned: Hi, Alice!
Hi, Alice!
add
```

**Your code:**
```python

from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with args={args}, kwargs={kwargs}')
        result = func(*args, **kwargs)
        print(f'Returned: {result}')
        return result
    return wrapper




```

---

## Task 3: Build an Iterable — Confirm the Pattern

Build a `NumberRange` class that acts as an **iterable** (not an iterator). It should support being iterated multiple times independently.

**Requirements:**
- `__init__(self, start, end)` — stores the range boundaries
- `__iter__` — uses `yield` to produce values from `start` to `end` (inclusive)
- NO `__next__` method (the generator handles that)

```python
class NumberRange:
    """Iterable that yields numbers from start to end (inclusive)."""

    def __init__(self, start: int, end: int):
        # Your code

    def __iter__(self):
        # Your code (use yield)

# Test 1 — reusable:
r = NumberRange(1, 5)
print(list(r))   # [1, 2, 3, 4, 5]
print(list(r))   # [1, 2, 3, 4, 5] — works again!

# Test 2 — independent iterators:
it1 = iter(r)
it2 = iter(r)
print(next(it1))  # 1
print(next(it1))  # 2
print(next(it2))  # 1 — independent! Not 3!

# Test 3 — identity check:
print(iter(r) is r)         # False — it's an iterable, not an iterator
print(iter(r) is iter(r))   # False — each call makes a new generator
```

**Your code:**
```python

class NumberRange:
    '''Iterable that yields numbers from stard to end (inclusive).'''
    
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
    
    def __iter__(self):
        for num in range(self.start, self.end + 1):
            yield num
            

#Tests went well, as expected
```

---

## Task 4: Predict Output — Generator Edge Cases

**Q1:** What is the output?
```python
def gen():
    yield 1
    yield 2
    return "done"

g = gen()
print(next(g))
print(next(g))

try:
    next(g)
except StopIteration as e:
    print(e.value)

Answer: 1 2 done
```

**Q2:** What is the output?
```python
def outer():
    yield from [10, 20]
    yield from (x * 3 for x in range(3))

print(list(outer()))

Answer: [10 20 0 3 6]
```

**Q3:** What is the output?
```python
def count_up(n):
    for i in range(n):
        yield i

gen = count_up(4)
print(next(gen))
print(next(gen))

for x in gen:
    print(x, end=' ')

Answer: 
0 
1 
2 3
```

**Your answers:**
```
Q1:


Q2:


Q3:


```

---

## Task 5: PROJECT — PriceTick & create_price_stream()

**Goal:** Build a generator that streams price data from a CSV file as named tuples. This is the foundation for tick-by-tick backtesting.

**Step 1:** Define a `PriceTick` named tuple:
```python
from collections import namedtuple

PriceTick = namedtuple('PriceTick', ['timestamp', 'ticker', 'open', 'high', 'low', 'close', 'volume'])
```

**Step 2:** Write `create_price_stream()` that:
- Takes a `file_path: str` and optional `ticker: str = None`
- Uses your existing `DataLoader` to load the CSV
- Yields one `PriceTick` per row
- If `ticker` is provided, only yields rows matching that ticker
- Uses `yield` (generator function) — NOT `return list`

```python
from algo_backtest.data.data_loader import DataLoader

def create_price_stream(file_path: str, ticker: str = None):
    """
    Generator that streams price data as PriceTick namedtuples.

    Args:
        file_path: Path to CSV file.
        ticker: Optional ticker filter. If None, yields all rows.

    Yields:
        PriceTick namedtuple for each row.
    """
    # Your code — use DataLoader, iterate rows, yield PriceTick

# Test with your ohlc_mock_data.csv:
stream = create_price_stream('ohlc_mock_data.csv')

# Get first 3 ticks:
for i, tick in enumerate(stream):
    if i >= 3:
        break
    print(f"{tick.timestamp} | {tick.ticker} | Close: {tick.close}")

# Expected (something like):
# 2024-01-01 09:00:00 | EURUSD | Close: 100.8
# 2024-01-01 09:01:00 | EURUSD | Close: 101.3
# 2024-01-01 09:02:00 | EURUSD | Close: 101.5
```

**Your code:**
```python


from collections import namedtuple
from algo_backtest.data.data_loader import DataLoader

PriceTick = namedtuple('PriceTick', ['timestamp', 'ticker', 'open', 'high', 'low', 'close', 'volume'])

def create_price_stream(filepath: str, ticker: str = None):
    '''A method used to stream price data from a csv file as named tuples'''
    
    loader = DataLoader(filepath)
    data = loader.load_data()
    
    for idx, row in data.iterrows():
        if ticker is None or row.ticker == ticker:
            yield PriceTick(row.timestamp, row.ticker, row.open, row.high, row.low, row.close, row.volume)
 
    

$ python practice.py
DataLoader initialized.
Data loading succeeded
Data loading operation ended.
2024-01-01 09:00:00 | EURUSD | Close: 100.8
2024-01-01 09:01:00 | EURUSD | Close: 101.3
2024-01-01 09:02:00 | EURUSD | Close: 101.5


I didn't implement it anywhere within my project though, as I'm not sure we need this at this point, but perhaps that will change - we will see about that.
```

---

## Task 6: PROJECT — Tick-by-Tick Backtest with Generator

**Goal:** Use `create_price_stream()` from Task 5 to run a simple tick-by-tick backtest.

**Instructions:**
1. Create a `BacktestEngine`
2. Open a position (e.g., EURUSD BUY @ 101.0, SL=100.0, TP=103.0)
3. Loop through the price stream
4. For each tick, call `engine.process_price(tick.ticker, tick.close)`
5. If any trades close, print them
6. After the stream ends, print the engine summary

```python
from algo_backtest.engine.backtest_engine import BacktestEngine

engine = BacktestEngine()
engine.open_position('EURUSD', 'BUY', 101.0, 1000, stop_loss=100.0, take_profit=103.0)

stream = create_price_stream('ohlc_mock_data.csv', ticker='EURUSD')

for tick in stream:
    closed = engine.process_price(tick.ticker, tick.close)
    if closed:
        for trade in closed:
            print(f"CLOSED: {trade}")

print(f"\nFinal: {engine}")
print(f"Total trades: {len(engine.completed_trades)}")
print(f"Open positions: {engine.position_manager.get_position_count()}")
```

**Your code + output:**
```python

stream = create_price_stream('ohlc_mock_data.csv', ticker = 'EURUSD')

from algo_backtest.engine.backtest_engine import BacktestEngine

stream = create_price_stream('ohlc_mock_data.csv', ticker = 'EURUSD')

engine = BacktestEngine()
engine.open_position('EURUSD', 'BUY', 101.1, 10000, 100.0, 103.0)

for i, tick in enumerate(stream):
    closed = engine.process_price(tick.ticker, tick.close)
    if closed != []:
        print(f'Closed trade: {closed}')
        
print(engine)
print(engine.total_pnl, engine.win_rate)
print(engine.position_manager.get_position_count())


$ python practice.py
Position Position_id = 7b84a997-fc7b-4131-bcd6-eeedb164ef5e | BUY 10000 EURUSD @ 101.1 [SL = 100.0, TP = 103.0] added successfully
DataLoader initialized.
Data loading succeeded
Data loading operation ended.
Closed trade: [Trade 7b84a997-fc7b-4131-bcd6-eeedb164ef5e: (ticker = 'EURUSD', side = 'BUY', entry_price = 101.1, exit_price = 103.2, quantity = 10000, pnl = 21000.00, exit_reason = 'BUY TP HIT']
algo_backtest.engine.backtest_engine: 0 open | 1 closed | PnL: $21000.0
[21000.000000000084]
21000.0 100.0
0
(.venv) 


```

---

## Task 7: Generator Expressions — Lazy Evaluation

**Q1:** What is the difference? Predict the output:
```python
list_comp = [x ** 2 for x in range(5)]
gen_exp = (x ** 2 for x in range(5))

print(type(list_comp))
print(type(gen_exp))
print(list_comp)
print(list(gen_exp))
print(list(gen_exp))

Answer:
list
generator
[0, 1, 4, 9, 16]
[0, 1, 4, 9, 16]
[]

```

**Q2:** What is the output?
```python
nums = [1, 2, 3, 4, 5]
squares = (n ** 2 for n in nums)

nums.append(6)
print(list(squares))

Answer: [1, 4, 9, 16, 25, 36]
```

**Q3:** True or False — explain briefly:
- "A generator expression can be iterated multiple times."
- "A list comprehension uses more memory than a generator expression for the same data."
- "Generator expressions are always faster than list comprehensions."

- False - unless we include a generator in a class, as an iterable, and then create multiple class objects, but I guess it's not the point of the question. I assume you mean a standard generator expression as in Q2, it will only yield the results ONCE.

- True. Yes, they create an object for every element in the list, but that usually becomes relevant when we deal with very big files (GBs of data). For such files, we'd rather use generators.

- True. If we assume they use less memory, that logically implicates this should also be faster. This is however only relevant for bigger files with lots of data, and in most cases, with smaller files we'd probably just stick to list comprehensions, as they're more intuitive, reusable and the memory/speed issue is negligible IN SUCH A CONTEXT.


**Your answers:**
```
Q1: 

Q2: 


Q3:


```

---

## Task 8: PCAP Simulation (5 Questions)

**Q1:** What is the output?
```python
class Squares:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        for i in range(self.n):
            yield i ** 2

s = Squares(4)
print(list(s))
print(list(s))
```
- A) [0, 1, 4, 9] [0, 1, 4, 9]
- B) [0, 1, 4, 9] []
- C) [1, 4, 9, 16] [1, 4, 9, 16]
- D) Error

Answer: B

**Q2:** What is the output?
```python
def gen(n):
    for i in range(n):
        yield i

g = gen(3)
print(sum(g))
print(sum(g))
```
- A) 3 / 3
- B) 3 / 0
- C) 6 / 6
- D) 6 / 0

Answer: B

**Q3:** What is the output?
```python
from functools import wraps

def double_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

@double_result
def add(a, b):
    return a + b

print(add(3, 4))
print(add.__name__)
```
- A) 14 / add
- B) 14 / wrapper
- C) 7 / add
- D) 7 / wrapper

Answer: A

**Q4:** What is the output?
```python
it = iter(range(3))
print(next(it))
print(next(it))

it2 = iter(it)
print(next(it2))
print(it is it2)
```
- A) 0 / 1 / 2 / True
- B) 0 / 1 / 0 / False
- C) 0 / 1 / 2 / False
- D) Error

Answer: A

**Q5:** Which of the following is NOT a valid way to create a generator?
- A) `(x for x in range(5))`
- B) `def f(): yield 1`
- C) `[x for x in range(5)]`
- D) `def f(): yield from [1, 2, 3]`

Answer: C

#End 12:30

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

- [ ] Task 1: PCAP warm-up — iterable vs iterator (2 questions)
- [ ] Task 2: Write @log_call decorator from scratch
- [ ] Task 3: NumberRange iterable class
- [ ] Task 4: Generator edge cases (3 predictions)
- [ ] Task 5: PriceTick + create_price_stream() generator
- [ ] Task 6: Tick-by-tick backtest using generator
- [ ] Task 7: Generator expressions (3 questions)
- [ ] Task 8: PCAP simulation (5 questions)

---

## Feedback Section

**Time spent:** ___ minutes

**Difficulty (1-10):**

**What clicked today:**

**What's confusing:**

---

**When complete:** Notify me for assessment.
