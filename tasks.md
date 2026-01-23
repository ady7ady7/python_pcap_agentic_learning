# Week 3, Day 5 - Friday
## Topic: Generators Practice, Week Review & Exam Prep

**Date:** 2026-01-23

**IMPORTANT:** READ `lessons/week3_generators.md` FIRST before starting tasks!

The lesson is now available with full scaffolded examples. Study it before attempting these tasks.

**Target Difficulty:** 5/10

**Remember:** Work in `practice.py`, paste FINAL answers here for review.

---

## Task 1: Generator Basics (After Reading Lesson)

**Instructions:** Answer these questions AFTER reading the generators lesson.

**Q1:** What is the output?
```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))
print(next(g))

```

**Q2:** What is the output?
```python
def gen():
    yield "a"
    yield "b"

g = gen()
result = list(g)
print(result)
print(list(g))  # Called again on same generator
```

**Q3:** What's the difference between these two?
```python
a = [x**2 for x in range(5)]
b = (x**2 for x in range(5))
print(type(a))
print(type(b))
```

**Q4:** What exception is raised?
```python
def simple():
    yield 1

g = simple()
next(g)
next(g)  # What happens here?
```

**Your answers:**
```
Q1: 1 2 (below)

Q2: [a, b], StopIteration error

Q3: First is a list, the second one is a generator.

Q4: StopIteration exception
```

---

## Task 2: Write Your First Generator

**Instructions:** Write a generator function called `countdown` that yields numbers from `n` down to 1.

```python
def countdown(n):
    # Your code here - use yield!
    pass

# Test it:
for num in countdown(5):
    print(num)

# Expected output:
# 5
# 4
# 3
# 2
# 1
```

**Your code:**
```python


def countdown(n):
    for num in range(n, 0, -1): #I assume we want to include 1
        yield num

```

**Test output:**
```

$ python practice.py
5
4
3
2
1

```

---

## Task 3: Generator Expression Practice

**Instructions:** Convert these list comprehensions to generator expressions.

```python
# A) Convert this list comprehension to a generator expression
squares_list = [x**2 for x in range(10)]

# Your generator expression (hint: change [ ] to ( ))
squares_gen = ???

# B) Convert this filtered list comprehension to a generator expression
evens_list = [x for x in range(20) if x % 2 == 0]

# Your generator expression:
evens_gen = ???

# C) Predict the output:
gen = (x * 2 for x in [1, 2, 3])
print(next(gen))
print(next(gen))
print(list(gen))  # What remains?
```

**Your answers:**
```
# A) Convert this list comprehension to a generator expression
squares_list = [x**2 for x in range(10)]

# Your generator expression (hint: change [ ] to ( ))
squares_gen = (x ** 2 for x in range (10))

# B) Convert this filtered list comprehension to a generator expression
evens_list = [x for x in range(20) if x % 2 == 0]

# Your generator expression:
evens_gen = (x for x in range (20) if x % 2 == 0)

# C) Predict the output:
gen = (x * 2 for x in [1, 2, 3])
print(next(gen)) # 2
print(next(gen)) # 4
print(list(gen))  # What remains? [6]

```

---

## Task 4: PROJECT - PriceTickGenerator (Proper Version)

**Instructions:** Create a generator that simulates price movements. Use `yield` this time!

```python
import random

def price_ticks(start_price: float, num_ticks: int):
    """
    Generate simulated price movements.

    Each tick moves the price by -1% to +1% randomly.

    Args:
        start_price: Starting price
        num_ticks: Number of prices to generate

    Yields:
        float: Each new price (rounded to 2 decimals)
    """
    # Your code here - use yield!
    pass

# Test:
random.seed(42)  # For reproducible results
for price in price_ticks(100.0, 5):
    print(f"${price:.2f}")
```

**Requirements:**
1. Use `yield` (NOT return a list)
2. Each tick: `price = price * (1 + random.uniform(-0.01, 0.01))`
3. Round each price to 2 decimal places: `round(price, 2)`
4. Never let price go below 0.01

**Your code:**
```python


import random

def price_ticks(start_price: float, num_ticks: int):
    """
    Generate simulated price movements.

    Each tick moves the price by -1% to +1% randomly.

    Args:
        start_price: Starting price
        num_ticks: Number of prices to generate

    Yields:
        float: Each new price (rounded to 2 decimals)
    """

    for num in range(num_ticks):
        exit_price = round(random.uniform(start_price * 0.99, start_price * 1.01), 2)
        yield exit_price
```

**Test output:**
```
$ python practice.py
$100.28
$99.05
$99.55
$99.45
$100.47
```

---

## Task 5: Week 3 Review - Portfolio Class

**Instructions:** Create a `Portfolio` class that combines Properties + Dunder Methods from Week 3.

```python
class Portfolio:
    """
    A portfolio that holds cash and tracks transactions.

    Requirements:
    1. __init__(self, initial_cash: float) - store as _cash (protected)
    2. cash property (read-only) - returns current cash
    3. _transactions list (protected) - stores all deposit/withdrawal amounts
    4. deposit(amount) - adds to cash, appends amount to transactions
    5. withdraw(amount) - subtracts from cash (raise ValueError if insufficient), appends negative amount
    6. __len__ - returns number of transactions
    7. __iter__ - iterates over transactions
    8. __str__ - returns "Portfolio: $X.XX (N transactions)"
    """
    pass

# Test:
p = Portfolio(1000.0)
p.deposit(500.0)
p.withdraw(200.0)
print(p)              # Portfolio: $1300.00 (2 transactions)
print(len(p))         # 2
for t in p:
    print(t)          # Should print: 500.0, then -200.0
```

**Your code:**
```python


class Portfolio:
    """
    A portfolio that holds cash and tracks transactions.

    Requirements:
    1. __init__(self, initial_cash: float) - store as _cash (protected)
    2. cash property (read-only) - returns current cash
    3. _transactions list (protected) - stores all deposit/withdrawal amounts
    4. deposit(amount) - adds to cash, appends amount to transactions
    5. withdraw(amount) - subtracts from cash (raise ValueError if insufficient), appends negative amount
    6. __len__ - returns number of transactions
    7. __iter__ - iterates over transactions
    8. __str__ - returns "Portfolio: $X.XX (N transactions)"
    """

    def __init__(self, initial_cash: float):
        self._cash = initial_cash
        self._transactions_list = []
        
    def __str__(self) -> str:
        return f'{__class__.__name__}: ${self._cash:.2f}, ({len(self._transactions_list)} transactions)'
        
    def __len__(self) -> int:
        '''Dunder method that allows to check the current length of the transactions list'''
        return len(self._transactions_list)
    
    def __iter__(self) -> iter:
        '''Dunder method that allows us to iterate over transactions'''
        return iter(self._transactions_list)
        
    @property
    def cash(self) -> float:
        '''A read-only property which returns the current amount of cash'''
        return self._cash
    
    
    def deposit(self, amount):
        '''A method used to deposit any positive amount into our account'''
        if amount < 0:
            raise ValueError('The deposited amount has to be above 0!')
        else:
            self._cash += amount
            self._transactions_list.append(('deposit', amount))
    
    def withdraw(self, amount):
        '''A method used to withdraw funds if there is a sufficient amount available'''
        if amount > self._cash:
            raise ValueError('Deposit impossible, not enough funds')
        else:
            self._cash -= amount
            self._transactions_list.append(('withdraw', amount))
    

    #Please note that I've decided to use tuples in transactions list - as they're clearer

```

**Test output:**
```
$ python practice.py
Portfolio: $1300.00, (2 transactions)
2
('deposit', 500.0)
('withdraw', -200.0)
(.venv) 

```

---

## Task 6: PCAP Multiple Choice

**Q1:** What is the output?
```python
class A:
    def __init__(self):
        self.value = 1

class B(A):
    def __init__(self):
        super().__init__()
        self.value = self.value + 1

b = B()
print(b.value)
```
- A) 1
- B) 2
- C) AttributeError
- D) None

Answer: B

**Q2:** Which correctly creates a read-only property?
```python
# Option A
class A:
    def __init__(self):
        self._x = 10
    @property
    def x(self):
        return self._x

# Option B
class B:
    def __init__(self):
        self.x = 10
    @property
    def x(self):
        return self.x

# Option C
class C:
    def __init__(self):
        self.__x = 10
    def x(self):
        return self.__x
```
- A) Option A only
- B) Option B only
- C) Option C only
- D) Options A and C

Answer: D 

**Q3:** What happens when you iterate over an exhausted generator?
```python
gen = (x for x in [1, 2, 3])
list(gen)  # Consumes it
for item in gen:
    print(item)
```
- A) Prints 1, 2, 3
- B) Prints nothing (empty loop)
- C) Raises StopIteration
- D) Raises TypeError

Answer: B

**Q4:** What is the output?
```python
def gen():
    yield 1
    return "done"
    yield 2

g = gen()
print(next(g))
print(next(g))
```
- A) 1, 2
- B) 1, then StopIteration
- C) 1, "done"
- D) SyntaxError

Answer: B

**Your answers:**
```
They're above as it was more convenient for me

---

## Task 7: Debug This Generator

**Instructions:** This generator has a bug. Find and fix it.

```python
def even_numbers(limit):
    """Generate even numbers from 0 up to (not including) limit."""
    n = 0
    while n < limit:
        if n % 2 == 0:
            return n  # BUG: What's wrong here?
        n += 1

# Expected behavior:
for num in even_numbers(10):
    print(num)
# Should print: 0, 2, 4, 6, 8
```

**Questions:**
1. What's the bug?
2. What does the current code actually do?
3. Write the corrected version.

**Your answers:**
```
1. Bug:

The return statement will STOP the loop.

2. Current behavior:
It stops the toop after the first iteration.

3. Fixed code:

def even_numbers(limit):
    """Generate even numbers from 0 up to (not including) limit."""
    n = 0
    while n < limit:
        if n % 2 == 0:
            yield n  # BUG - IT WILL STOP THE LOOP
        n += 1
        

```

---

## Task 8: Integration - Generator Method in Class

**Instructions:** Add a generator method to your TradeManager class (or create a simplified version here).

```python
class SimpleTradeManager:
    """Simplified version for this exercise."""

    def __init__(self):
        self._trades = []  # List of (ticker, pnl) tuples

    def add_trade(self, ticker: str, pnl: float):
        self._trades.append((ticker, pnl))

    def profitable_trades(self):
        """
        Generator that yields only profitable trades.

        Yields:
            tuple: (ticker, pnl) where pnl > 0
        """
        # Your code here - use yield!
        pass

# Test:
tm = SimpleTradeManager()
tm.add_trade("AAPL", 100.0)
tm.add_trade("GOOGL", -50.0)
tm.add_trade("MSFT", 200.0)
tm.add_trade("TSLA", -75.0)

print("Profitable trades:")
for ticker, pnl in tm.profitable_trades():
    print(f"  {ticker}: ${pnl:.2f}")

# Expected:
# Profitable trades:
#   AAPL: $100.00
#   MSFT: $200.00
```

**Your code:**
```python

import random

class SimpleTradeManager:
    """Simplified version for this exercise."""

    def __init__(self):
        self._trades = []  # List of (ticker, pnl) tuples

    def add_trade(self, ticker: str, pnl: float):
        self._trades.append((ticker, pnl))

    def profitable_trades(self):
        """
        Generator that yields only profitable trades.

        Yields:
            tuple: (ticker, pnl) where pnl > 0
        """
        
        profitable_trades = ((trade[0], trade[1]) for trade in self._trades if trade[1] > 0)
        return profitable_trades

```

**Test output:**
```
$ python practice.py
Profitable trades:
  AAPL: $100.0
  MSFT: $200.0
(.venv) 


```

**Bonus question:** Why use a generator here instead of returning a list? (1-2 sentences)
```

If we had lots of trades and a huge file, that could save some memory, as generators are way more memory-efficient.


```

---

## Solutions Checklist

- [ ] Task 1: Generator basics (4 questions)
- [ ] Task 2: countdown generator
- [ ] Task 3: Generator expressions (A, B, C)
- [ ] Task 4: price_ticks generator (PROJECT)
- [ ] Task 5: Portfolio class (Week 3 review)
- [ ] Task 6: Multiple choice (4 questions)
- [ ] Task 7: Debug generator bug
- [ ] Task 8: profitable_trades generator method

---

## Feedback Section

**Time spent:** ___ minutes

**Difficulty (1-10):**

**What clicked:**


**What's confusing:**


**Questions for mentor:**


---

**When complete:** Fill out feedback section and notify me for assessment.

**Weekend:** After assessment, you'll receive Week 3 Exam A and Exam B (30 questions each).
