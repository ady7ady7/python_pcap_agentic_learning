# Week 6, Day 1 - Monday
## Topic: The Iterator Protocol & Advanced Generators

**Date:** 2026-02-09

**Target Difficulty:** 6/10

**Focus:** Iterator protocol (`__iter__`/`__next__`), `__new__` method, `yield from`, named tuples

**Lesson:** Read `lessons/week6_iterators_generators_advanced.md` before starting.

**Remember:** Work in `practice.py`, paste FINAL answers here for review.

---

## Task 1: PCAP Warm-up (Pure Python)

**Q1:** What is the output?
```python
numbers = [10, 20, 30]
it = iter(numbers)
print(next(it))
print(next(it))

it2 = iter(numbers)
print(next(it2))
```

**Q2:** What is the output?
```python
gen = (x * 2 for x in range(4))
print(next(gen))
print(next(gen))

gen2 = iter(gen)
print(next(gen2))
print(gen is gen2)
```

**Your answers:**
```
Q1: 10, 20; 10 (separate entities)
Q2: 0, 2, 4, True (two entities referencing the same object)
```

---

## Task 2: Decorator Trace (Scaffolded — Day 1: READ ONLY)

**Goal:** Understand how a decorator with arguments works by tracing execution step-by-step. Do NOT write code — just trace on paper/mentally.

**Instructions:** For the code below, write out **what happens at each step** when Python runs it. Number each step.

```python
from functools import wraps

def require_positive(param_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if isinstance(arg, (int, float)) and arg < 0:
                    return f"Error: {param_name} must be positive"
            return func(*args, **kwargs)
        return wrapper
    return decorator

@require_positive("price")
def process_trade(price):
    return f"Trade at ${price:.2f}"

result1 = process_trade(150.0)
result2 = process_trade(-50.0)
print(result1)
print(result2)
```

**Your trace:**
```
Step 1: Python defines require_positive function
Step 2: Python runs the decorator with passed process_trade function
Step 3: Python runs the wrapper part with passed args/kwargs, it checks whether the passed arg (price) value is an int/float and is over 0
Step 4: Depending on the check, it returns an error or the actual result of the function (e.g. trade at ${price})
(continue until you reach the print outputs)

Final output:
result1 = Trade at $150.0
result2 = Error: -50.0 must be positive
```

**Hint:** Remember the 3-layer structure: `require_positive("price")` returns `decorator`, which is applied to `process_trade`, replacing it with `wrapper`.

---

## Task 3: Iterator Protocol — Build a Custom Iterator

**Instructions:** Implement a `FibonacciIterator` class that yields Fibonacci numbers up to a maximum value.

```python
class FibonacciIterator:
    """
    Iterator that yields Fibonacci numbers up to max_value.

    Usage:
        for n in FibonacciIterator(100):
            print(n)
        # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
    """

    def __init__(self, max_value: int):
        # Your code: store max_value and initialize Fibonacci state
        pass

    def __iter__(self):
        # Your code: return the iterator object
        pass

    def __next__(self) -> int:
        # Your code: return next Fibonacci number or raise StopIteration
        pass

# Test:
fib = FibonacciIterator(50)
print(list(fib))
# Expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Test: Can be used in for loop
for n in FibonacciIterator(20):
    print(n, end=' ')
# Expected: 0 1 1 2 3 5 8 13
```

**Your code:**
```python

class FibonacciIterator:
    """
    Iterator that yields Fibonacci numbers up to max_value.

    Usage:
        for n in FibonacciIterator(100):
            print(n)
        # Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
    """

    def __init__(self, max_value: int):
        # Your code: store max_value and initialize Fibonacci state
        self.fibo_nums = iter([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
        self.current = 0
        self.max_value = max_value
        

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current >= self.max_value:
            raise StopIteration
        self.current = next(self.fibo_nums)
        return self.current


# Test:
fib = FibonacciIterator(50)
print(list(fib))
# Expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Test: Can be used in for loop
for n in FibonacciIterator(20):
    print(n, end=' ')
# Expected: 0 1 1 2 3 5 8 13

Results:

[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
0 1 1 2 3 5 8 13 21 (.venv) 


```

---

## Task 4: `__new__` vs `__init__` — Predict the Output

**Instructions:** Predict the output of each snippet. No running code!

**Q1:**
```python
class Logger:
    _instance = None

    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        self.name = name

a = Logger("FileLogger")
b = Logger("DBLogger")
print(a.name)
print(a is b)

Answer: DBLogger, True 
```

**Q2:**
```python
class AlwaysPositive(int):
    def __new__(cls, value):
        return super().__new__(cls, abs(value))

x = AlwaysPositive(-42)
print(x)
print(type(x))
print(isinstance(x, int))

Answer: 42,  class, True

```

**Your answers:**
```
Q1 output:


Q2 output:


```

---

## Task 5: `yield from` and Generator Pipelines

**Instructions:** Refactor the following code to use `yield from`, then build a pipeline.

**Part A:** Rewrite using `yield from`:
```python
# ORIGINAL (nested for loops)
def flatten(nested_list):
    for sublist in nested_list:
        for item in sublist:
            yield item

data = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(list(flatten(data)))
# Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Part B:** Build a 3-stage generator pipeline:
```python
# Stage 1: Read prices from a list
def price_source(prices: list):
    """Yield each price from the list."""
    # Your code (1 line with yield from)

# Stage 2: Filter out prices below a threshold
def filter_above(prices, threshold: float):
    """Yield only prices above the threshold."""
    # Your code

# Stage 3: Apply a spread (add a fixed amount)
def apply_spread(prices, spread: float):
    """Yield each price with spread added."""
    # Your code

# Test the pipeline:
raw_prices = [100.5, 98.2, 105.3, 97.1, 110.0, 99.8]
pipeline = apply_spread(filter_above(price_source(raw_prices), 100.0), 0.5)
print(list(pipeline))
# Expected: [101.0, 105.8, 110.5]
```

**Your code:**
```python

def flatten(*iterables):
    for iterable in iterables:
        yield from iterable

print(flatten(data))



def price_source(prices: list):
    """Yield each price from the list."""
    for price in prices:
        yield price
        
# Stage 2: Filter out prices below a threshold
def filter_above(prices, threshold: float):
    """Yield only prices above the threshold."""
    for price in prices:
        if price > threshold:
                yield price

# Stage 3: Apply a spread (add a fixed amount)
def apply_spread(prices, spread: float):
    """Yield each price with spread added."""
    for price in prices:
            yield price + spread


Log:

$ python practice.py
<generator object flatten at 0x0000019E5EA6A5A0>
[101.0, 105.8, 110.5]
(.venv) 
```

---

## Task 6: MRO with super() — Trace the Chain

**Instructions:** Trace the MRO manually for each snippet. Write the MRO order AND the output.

**Q1:**
```python
class Base:
    def identify(self):
        return "Base"

class Left(Base):
    def identify(self):
        return "Left->" + super().identify()

class Right(Base):
    def identify(self):
        return "Right->" + super().identify()

class Child(Left, Right):
    def identify(self):
        return "Child->" + super().identify()

print(Child().identify())


Child -> Left -> Right -> Base
```

**Q2:**
```python
class A:
    def __init__(self):
        print("A", end=" ")

class B(A):
    def __init__(self):
        print("B", end=" ")
        super().__init__()

class C(A):
    def __init__(self):
        print("C", end=" ")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D", end=" ")
        super().__init__()

D()

D -> B -> C -> A
```

**Your answers:**
```
Q1:
MRO: Child -> Left -> Right -> Base -> object
Output: Child->Left->Right->Base

Q2:
MRO: D -> B -> C -> A -> object
Output: D B C A
```

**Remember:** `super()` means "next in MRO", NOT "direct parent class".

---

## Task 7: PROJECT — Position IDs & Ticker-Aware Price Processing

**The Problem:** Right now, `BacktestEngine.process_price(current_price)` checks ALL positions against one price. If you hold FDAX at 24500 and EURUSD at 1.0800, calling `process_price(24500)` would incorrectly evaluate EURUSD against 24500. Each position also has no unique identifier.

**Your job — 3 changes to existing files:**

**Step 1: Add unique `position_id` to `Position` class** (`algo_backtest/engine/position.py`)
- Use `uuid.uuid4()` from the standard library to generate a unique ID on creation
- Store it as `self.position_id`
- Include it in `__str__` and `__repr__`

**Step 2: Make `PositionManager` ticker-aware** (`algo_backtest/engine/position_manager.py`)
- Modify `close_triggered_positions(current_price)` → `close_triggered_positions(ticker: str, current_price: float)`
- It should only check positions that **match the given ticker**
- Leave non-matching positions untouched
- Add a method: `get_positions_by_ticker(ticker: str) -> List[Position]`

**Step 3: Make `BacktestEngine` ticker-aware** (`algo_backtest/engine/backtest_engine.py`)
- Modify `process_price(current_price)` → `process_price(ticker: str, current_price: float)`
- Only processes positions matching that ticker

**Test your changes:**
```python
engine = BacktestEngine()

# Open positions on different tickers
engine.open_position('FDAX', 'BUY', 24500, 1, stop_loss=24450, take_profit=24600)
engine.open_position('EURUSD', 'BUY', 1.0800, 10000, stop_loss=1.0750, take_profit=1.0850)

# FDAX price moves — should only affect FDAX position
closed = engine.process_price('FDAX', 24600)
print(f'FDAX trades closed: {len(closed)}')       # 1 (TP hit)
print(f'Open positions: {engine.position_manager.get_position_count()}')  # 1 (EURUSD still open)

# EURUSD price moves — should only affect EURUSD position
closed = engine.process_price('EURUSD', 1.0850)
print(f'EURUSD trades closed: {len(closed)}')      # 1 (TP hit)
print(f'Open positions: {engine.position_manager.get_position_count()}')  # 0

# Verify unique IDs
engine2 = BacktestEngine()
p1 = engine2.open_position('FDAX', 'BUY', 24500, 1, stop_loss=24450, take_profit=24600)
p2 = engine2.open_position('FDAX', 'SELL', 24500, 1, stop_loss=24550, take_profit=24400)
print(p1.position_id != p2.position_id)  # True — different IDs
```

**Your code (paste the modified methods/sections only — not entire files):**
```python

```
<!-- def process_price(self, ticker: str, current_price: float) -> List[Trade]:
        
        """
        Check all positions against current price.
        Close any that hit SL/TP and convert to Trade objects.

        Steps:
        1. Use position_manager.close_triggered_positions(current_price)
        2. For each closed position, create a Trade object
        3. Add Trade to completed_trades
        4. Return list of newly created trades

        Returns:
            List of newly closed trades (empty if none closed)
        """
        
        closed_positions = self.position_manager.close_triggered_positions(ticker, current_price)
        newly_closed_trades = []
        for position in closed_positions:
            exit_reason = position.should_close(current_price)[1]
            trade = Trade(position.ticker, 
                          position.side, 
                          position.entry_price, 
                          current_price, 
                          position.quantity,
                          exit_reason = exit_reason)
            newly_closed_trades.append(trade)
            self.completed_trades.append(trade)
            
        return newly_closed_trades



class Position:
    '''
    Represents a single trading position
    
    Attributes:
    ticker: e.g. EURUSD, FDAX,
    entry_price: float e.g. 24500.25
    quantity: Number of units
    stop_loss: stop loss price - float e.g. 24470.5 (optional)
    take_profit: take profit price - float e.g. 24530.0 (optional)
    
    '''
    
    def __init__(
        self,
        ticker: str,
        side: str,
        entry_price: float, 
        quantity: float, 
        stop_loss: Optional[float] = None,
        take_profit: Optional[float] = None
    ) -> None:
        
        '''Initialize a new position'''
        
        self.position_id = uuid.uuid4()
        self.ticker = ticker
        self.side = side.upper() #I decided to include side, as we will usually have this sorted out in this way
        self.entry_price = entry_price
        self.quantity = quantity
        self.stop_loss = stop_loss
        self.take_profit = take_profit
    
        #Therefore is_long or is_short is really redundant + it's also weird.
        
    def __str__(self) -> str:
        '''A Python magic method used to return information about class instead of memory object'''
        return f'Position_id = {self.position_id} | {self.side} {self.quantity} {self.ticker} @ {self.entry_price} [SL = {self.stop_loss}, TP = {self.take_profit}]'
    
    
    def __repr__(self) -> str:
        '''A Python magic method used to provide devs with useful information to recreate the object '''
        return f'Position(position_id = {self.position_id}, ticker = {self.ticker}, side = {self.side}, entry_price = {self.entry_price}, quantity = {self.quantity}, stop_loss = {self.stop_loss}, take_profit = {self.take_profit})'


    
        def close_triggered_positions(self, ticker: str, current_price: float) -> List[Position]:
        """
        Check all positions for SL/TP triggers and remove them.

        Args:
            current_price: Current market price.

        Returns:
            List of positions that should be closed.
        """
        closed_positions = [p for p in self.positions if p.ticker == ticker and p.should_close(current_price)]
        self.positions = [p for p in self.positions if not p.should_close(current_price)]


        return closed_positions
                
    def get_positions_by_ticker(self, ticker: str) -> List[Position]:
        '''Returns all positions that match a given ticker'''
        matching_positions = [p for p in self.positions if p.ticker == ticker]
        return matching_positions




$ python practice.py
Position Position_id = b3313b0f-cb44-4cb2-a74d-2738283f69e3 | BUY 1 FDAX @ 24500 [SL = 24450, TP = 24600] added successfully
Position Position_id = b44460ec-eb26-4d0d-a98a-08e504c2020c | BUY 10000 EURUSD @ 1.08 [SL = 1.075, TP = 1.085] added successfully
FDAX trades closed: 1
Open positions: 0
EURUSD trades closed: 0
Open positions: 0
Position Position_id = 765e9d09-b194-4184-8ea5-c8b9b5ed9229 | BUY 1 FDAX @ 24500 [SL = 24450, TP = 24600] added successfully
Position Position_id = d3987987-068b-4cb6-a5f9-329e46a3b1a8 | SELL 1 FDAX @ 24500 [SL = 24550, TP = 24400] added successfully
True
(.venv) 


I reckon that we will also ahve to modify Trade a bit to handle these ids - we might do it tomorrow or wherever. I'd advise you check the current project infrastructure to plan for necessary changes. -->



---

## Task 8: PCAP Simulation (5 Questions)

**Q1:** What is the output?
```python
class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.limit:
            raise StopIteration
        self.current += 1
        return self.current

c = Counter(3)
print(list(c))
print(list(c))
```
- A) [1, 2, 3] [1, 2, 3]
- B) [1, 2, 3] []
- C) [0, 1, 2] [0, 1, 2]
- D) Error

Answer: B

**Q2:** What is the output?
```python
def gen():
    yield 1
    yield 2
    return "end"

g = gen()
print(next(g))
print(next(g))

try:
    next(g)
except StopIteration as e:
    print(e.value)
```
- A) 1 / 2 / end
- B) 1 / 2 / StopIteration
- C) 1 / 2 / None
- D) Error

Answer: A

**Q3:** What is the output?
```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p[0], p.x)
print(isinstance(p, tuple))
```
- A) 3 3 / True
- B) 3 3 / False
- C) (3,) (3,) / True
- D) Error

Answer: A

**Q4:** What is the output?
```python
class Immutable(str):
    def __new__(cls, value):
        instance = super().__new__(cls, value.upper())
        return instance

    def __init__(self, value):
        self.original = value

s = Immutable("hello")
print(s)
print(s.original)
```
- A) HELLO / hello
- B) hello / hello
- C) HELLO / HELLO
- D) Error

Answer: C

**Q5:** What is the output?
```python
numbers = [1, 2, 3]
it = iter(numbers)
print(next(it))
print(next(it, 'default'))
print(next(it, 'default'))
print(next(it, 'default'))
```
- A) 1 / 2 / 3 / StopIteration
- B) 1 / 2 / 3 / default
- C) 1 / 2 / default / default
- D) Error

Answer: B

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
- [ ] Task 2: Decorator trace (step-by-step)
- [ ] Task 3: FibonacciIterator class
- [ ] Task 4: __new__ vs __init__ prediction
- [ ] Task 5: yield from + pipeline
- [ ] Task 6: MRO trace
- [ ] Task 7: Position IDs + ticker-aware processing
- [ ] Task 8: PCAP simulation (5 questions)

---

## Feedback Section

**Time spent:** ___ minutes

**Difficulty (1-10):**

**What clicked today:**

**What's confusing:**

---

**When complete:** Notify me for assessment.
