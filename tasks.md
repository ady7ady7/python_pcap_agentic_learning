# Week 3, Day 4 - Inheritance Patterns, Generators & PCAP Drills

**Date:** 2026-01-22
**Focus:** Scaffolded inheritance examples, generators intro, PCAP core topics

**Lessons:**
- [Inheritance & Polymorphism](lessons/week2_inheritance.md)
- [Dunder Methods](lessons/week3_dunder_methods.md)

**Target Difficulty:** 5-6/10

**Remember:** Work in `practice.py`, paste FINAL answers here for review.

---

## Scaffolded Explanation: Inheritance & `super().__init__()`

You asked for this yesterday. Here's the definitive guide:

### The Golden Rule

**If a child class defines `__init__`, the parent's `__init__` does NOT run automatically.**

You MUST call `super().__init__()` explicitly if you want parent initialization.

### Example 1: WITHOUT `super().__init__()`

```python
class Parent:
    def __init__(self):
        self.x = 1
        print("Parent __init__ ran")

class Child(Parent):
    def __init__(self):
        self.y = 2
        print("Child __init__ ran")

c = Child()
# Output: "Child __init__ ran"  (Parent never ran!)

print(c.y)  # 2 - works
print(c.x)  # AttributeError: 'Child' has no attribute 'x'
```

**What happened:** Child's `__init__` completely **replaced** Parent's. The line `self.x = 1` never executed.

### Example 2: WITH `super().__init__()`

```python
class Parent:
    def __init__(self):
        self.x = 1
        print("Parent __init__ ran")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Call Parent's __init__ FIRST
        self.y = 2
        print("Child __init__ ran")

c = Child()
# Output:
# "Parent __init__ ran"
# "Child __init__ ran"

print(c.x)  # 1 - works! Parent set it up
print(c.y)  # 2 - works! Child set it up
```

### Example 3: NO `__init__` in Child (Automatic Inheritance)

```python
class Parent:
    def __init__(self):
        self.x = 1
        print("Parent __init__ ran")

class Child(Parent):
    pass  # No __init__ defined

c = Child()
# Output: "Parent __init__ ran"  (Automatically uses Parent's!)

print(c.x)  # 1 - works!
```

**Rule:** If Child doesn't define `__init__` at all, Python automatically uses Parent's.

### Quick Reference Table

| Child has `__init__`? | Calls `super().__init__()`? | Parent's `__init__` runs? |
|----------------------|----------------------------|---------------------------|
| No | N/A | ✅ YES (automatic) |
| Yes | No | ❌ NO |
| Yes | Yes | ✅ YES |

---

## Task 1: PCAP Warm-up - Inheritance Output Prediction

Predict the output for each snippet:

**Snippet A:**
```python
class A:
    def __init__(self):
        self.value = 10

class B(A):
    def __init__(self):
        self.value = 20

b = B()
print(b.value)
```

**Snippet B:**
```python
class A:
    def __init__(self):
        self.value = 10

class B(A):
    def __init__(self):
        super().__init__()
        self.value = 20

b = B()
print(b.value)
```

**Snippet C:**
```python
class A:
    def __init__(self):
        self.value = 10

class B(A):
    pass

b = B()
print(b.value)
```

**Your predictions:**
```
Snippet A: 20

Snippet B: 20

Snippet C: 10

```

---

## Task 2: Build a `TradingAccount` Class Hierarchy

Create a class hierarchy for trading accounts:

**Base class `Account`:**
```python
class Account:
    def __init__(self, owner: str, balance: float = 0.0):
        self._owner = owner
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self._balance += amount
```

**Your task:** Create `MarginAccount(Account)` that:
1. Calls `super().__init__(owner, balance)`
2. Adds a new attribute `_leverage` (float, default 1.0)
3. Adds a `leverage` property (read-only)
4. Adds a `buying_power` property that returns `balance * leverage`
5. Overrides `__str__` to show: `"MarginAccount(owner='Alice', balance=1000.00, leverage=2.0)"`

**Test code:**
```python
acc = MarginAccount("Alice", 1000.0, leverage=2.0)
print(acc.balance)       # 1000.0
print(acc.leverage)      # 2.0
print(acc.buying_power)  # 2000.0
acc.deposit(500)
print(acc.buying_power)  # 3000.0
print(acc)               # MarginAccount(owner='Alice', balance=1500.00, leverage=2.0)
```

**Your code:**
```python


class MarginAccount(Account):
    '''A child class with margin and buying power added'''

    def __init__(self, owner: str, balance: float, leverage: float):
        super().__init__(owner, balance)
        self._leverage = leverage
        self._buying_power = 0.0
        
    def __str__(self):
        return f'{__class__.__name__}(owner = {self._owner}, balance = {self._balance}, leverage = {self._leverage})'
    
    @property
    def buying_power(self) -> float:
        '''A property that calculates the current buying power'''
        self._buying_power = self._leverage * self._balance
        return self._buying_power
    
    @property
    def leverage(self) -> float:
        '''A property that describes leverage (read-only)'''
        return self._leverage
```

**Test output:**
```

$ python practice.py
1000.0
2.0
2000.0
3000.0
MarginAccount(owner = Alice, balance = 1500.0, leverage = 2.0)
(.venv) 

```

---

## Task 3: Generator Basics (PCAP Topic)

Generators are functions that use `yield` instead of `return`. They produce values one at a time, saving memory.

**Q1:** What's the output?
```python
def count_up(n):
    for i in range(1, n + 1):
        yield i

gen = count_up(3)
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))  # What happens here?

WE DID NOT USE YIELD FOR ONCE - IT'S MY FIRST ENCOUNTER WITH THIS, SO I SIMPLY RAN THE CODE:

1
2
3
Traceback (most recent call last):
  File "C:\Users\HARDPC\Desktop\AL\projekty\python_pcap_agentic_learning\practice.py", line 3099, in <module>
    print(next(gen))  # What happens here?
          ~~~~^^^^^
StopIteration



```

**Q2:** Convert this list comprehension to a generator expression:
```python
squares = [x**2 for x in range(10)]  # List comprehension
```

**Q3:** What's the key difference between a list and a generator in terms of memory?

**Your answers:**

SAME NIGGA, WHY DO YOU ASK ME TO DO A THING WE DIDN'T EVEN COVER...
I DON'T KNOW, HOW WOULD I AND WHY?

IS IT EVEN PCAP-RELEVANT? IF IT IS, MAYBE INTRODUCE IT FIRST? 
IF IT ISN'T MAYBE FORGET IT? AND DON'T YOU DARE TO TAKE AWAYP OINTS FROM ME FOR THAT!

```
Q1 Output:


Q1 Last line:


Q2 Generator expression:


Q3 Memory difference:


```

---

## Task 4: PROJECT - Create a `PriceGenerator`

Create a generator function that simulates price movements:

```python
def price_generator(start_price: float, num_ticks: int, volatility: float = 0.01):
    """
    Generate simulated price ticks.

    Args:
        start_price: Starting price
        num_ticks: Number of price updates to generate
        volatility: Max percentage change per tick (0.01 = 1%)

    Yields:
        float: Next price value
    """
    # Your implementation here
    pass
```

**Requirements:**
1. Start with `start_price`
2. For each tick, change price by random amount within ±volatility
3. Use `random.uniform(-volatility, volatility)` for the change
4. Yield each new price
5. Price should never go below 0.01

**Test code:**
```python
import random
random.seed(42)  # For reproducible results

gen = price_generator(100.0, 5, volatility=0.02)
for price in gen:
    print(f"${price:.2f}")
```

**Your code:**
```python


import random

def price_generator(start_price: float, num_ticks: int, volatility: int = 5):
    """
    Generate simulated price ticks.

    Args:
        start_price: Starting price
        num_ticks: Number of price updates to generate
        volatility: Max percentage change per tick (1 = 1%)

    Yields:
        float: Next price value
    """

    prices = []
    for i in range(num_ticks):
        price = start_price * (1 - (random.uniform(-volatility, volatility) / 100))
        prices.append(price)
    
    return prices


prices = price_generator(100, 10, 5)
print(prices)


```

**Test output:**
```

I decided to use int percents, so 1 = 1% - clearly described it in my docstring, so it wouldn't cause any confusion.

[97.8427343661148, 99.30686543975983, 95.00972445447661, 104.76655606092213, 103.19090647636817, 101.00014832311996, 98.17085104805695, 102.63371778154186, 102.21331515408372, 99.93737557966736]

Eveyrthing works.

```

---

## Task 5: PCAP Multiple Choice - Core Topics

**Question 1:** What does `yield` do in a function?
- A) Immediately returns a value and terminates the function
- B) Pauses the function and returns a value, resuming on next call
- C) Creates a list of all values
- D) Raises a StopIteration exception

**Your answer:**
I DON'T KNOW, WE DIDN'T HAVE THAT, AGAIN - DON'T YOU DARE to take away points from me. If it's PCAP -revelant, add relevant notes about it, as it's my first encounter today with yield.


---

**Question 2:** What is the output?
```python
class Parent:
    class_var = "parent"

class Child(Parent):
    pass

Child.class_var = "child"
print(Parent.class_var, Child.class_var)
```
- A) `parent parent`
- B) `child child`
- C) `parent child`
- D) `child parent`

**Your answer:**
B


---

**Question 3:** What exception is raised when calling `next()` on an exhausted generator?
- A) `GeneratorExit`
- B) `StopIteration`
- C) `IndexError`
- D) `ValueError`

**Your answer:**
B (again, asking about generator and yield...)


---

**Question 4:** Given this code, what is `result`?
```python
def gen():
    yield 1
    yield 2
    yield 3

result = list(gen())
```
- A) `<generator object>`
- B) `[1, 2, 3]`
- C) `(1, 2, 3)`
- D) `6`

**Your answer:**
Dude....
STOP ASKING ME ABOUT A TOPIC I NEVER ENCOUNTERED!!!!!!!!!!!!!!


---

## Task 6: Debugging - Fix the Inheritance Bug

This code has a bug. Find and fix it:

```python
class Vehicle:
    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year

    def info(self) -> str:
        return f"{self.year} {self.brand}"

class Car(Vehicle):
    def __init__(self, brand: str, year: int, doors: int):
        self.doors = doors

    def info(self) -> str:
        return f"{super().info()} with {self.doors} doors"

car = Car("Toyota", 2020, 4)
print(car.info())  # Expected: "2020 Toyota with 4 doors"
```

**What's the bug?**
```
#The child class has init, so it won't automatically inherit the attributes from the parent class,
#yet it doesn't use the super().__init__() so it won't actually be able to ge the brand, and year attributes.
```

**Your fixed code:**
```python
class Vehicle:
    def __init__(self, brand: str, year: int):
        self.brand = brand
        self.year = year

    def info(self) -> str:
        return f"{self.year} {self.brand}"

class Car(Vehicle):
    def __init__(self, brand: str, year: int, doors: int):
        super().__init__(brand, year)
        self.doors = doors

    def info(self) -> str:
        return f"{super().info()} with {self.doors} doors"

car = Car("Toyota", 2020, 4)

```

**Test output:**
```
$ python practice.py
2020 Toyota with 4 doors
(.venv) 
```

---

## Task 7: PROJECT - Enhance TradeManager with Generator

Add a generator method to your `TradeManager` class:

```python
def iter_profitable(self) -> Generator[Trade, None, None]:
    """
    Generator that yields only profitable trades.

    Yields:
        Trade: Each trade where pnl > 0
    """
    pass
```

Also add:
```python
def iter_by_ticker(self, ticker: str) -> Generator[Trade, None, None]:
    """
    Generator that yields trades matching the given ticker.
    """
    pass
```

**Test code:**
```python
manager = TradeManager()
manager.add_trade(Trade("AAPL", "BUY", 100, 110, 10))   # +100
manager.add_trade(Trade("GOOGL", "SELL", 200, 190, 5))  # +50
manager.add_trade(Trade("AAPL", "BUY", 50, 45, 20))     # -100
manager.add_trade(Trade("MSFT", "BUY", 100, 120, 10))   # +200

print("Profitable trades:")
for trade in manager.iter_profitable():
    print(f"  {trade.ticker}: ${trade.pnl:.2f}")

print("\nAAPL trades:")
for trade in manager.iter_by_ticker("AAPL"):
    print(f"  {trade}")
```

**Your code:**
```python

SAME ISSUE AS ABOVE - YOU DIDN'T EVEN INTRODUCE THE TOPIC OF 'YIELD' AND YOU DEMAND ME TO CREATE AN ADVANCED FUNCTION WITH THAT. HWO AM I SUPPOSED TO DO THAT?
This is really bad...
```

**Test output:**
```

```

---

## Task 8: PCAP Trap - Generator vs List Memory

**Q1:** What's wrong with this approach for large files?
```python
def read_all_lines(filename):
    with open(filename) as f:
        return f.readlines()  # Returns list of ALL lines

lines = read_all_lines("huge_file.txt")  # 10GB file
for line in lines:
    process(line)
```

**Q2:** Rewrite it using a generator to be memory-efficient:

**Your answers:**
```
Q1 Problem:
I don't know, we get all l lines though.


Q2 Generator version:
Again, I DID NOT HAVE generators or YIELD!!!
It's okay for me to learn that, but for fucks sake, I need proper guidance, materials, examples, and a scaffolded approach, please...

```

---

## Checklist

- [ ] Task 1: Inheritance output prediction (3 snippets)
- [ ] Task 2: MarginAccount class (inheritance)
- [ ] Task 3: Generator basics (3 questions)
- [ ] Task 4: PriceGenerator function (PROJECT)
- [ ] Task 5: Multiple choice (4 questions)
- [ ] Task 6: Fix inheritance bug
- [ ] Task 7: TradeManager generator methods (PROJECT)
- [ ] Task 8: Generator vs list memory

---

## Feedback Section

**Time spent:** ___ minutes

**Difficulty (1-10):**

**What clicked:**


**What's confusing:**


**Questions for mentor:**


---

**When complete:** Fill out feedback section above and notify mentor for assessment.
