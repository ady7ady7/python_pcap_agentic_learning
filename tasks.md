# Week 3, Day 3 - Decorators, Special Methods & PCAP Drills

**Date:** 2026-01-21
**Focus:** More coding, PCAP core topics, scaffolded property explanation

**Lesson:** [Encapsulation & Properties](lessons/week3_oop_encapsulation.md)

**Target Difficulty:** 5-6/10

**Remember:** Work in `practice.py`, paste FINAL answers here for review.

---

## Scaffolded Explanation: Property Recursion Trap

You asked for this yesterday. Here's the step-by-step breakdown:

### The Problem Code
```python
class BadExample:
    def __init__(self, value):
        self.value = value  # Line A

    @property
    def value(self):
        return self.value   # Line B

    @value.setter
    def value(self, new_value):
        self.value = new_value  # Line C
```

### What Happens Step-by-Step

**Step 1:** You call `BadExample(10)`
**Step 2:** Python runs `__init__(self, 10)`
**Step 3:** Line A executes: `self.value = value` (which is `self.value = 10`)
**Step 4:** Python sees `self.value = ...` and thinks: "Is there a setter for `value`?"
**Step 5:** YES! The `@value.setter` exists. Python calls it.
**Step 6:** The setter runs Line C: `self.value = new_value`
**Step 7:** Python sees `self.value = ...` again → calls the setter again
**Step 8:** Infinite loop → RecursionError

### The Key Insight

The **property name** (`value`) and the **storage attribute** must be DIFFERENT:
- Property name: `value` (what users access)
- Storage attribute: `_value` (where data actually lives)

### The Fix
```python
class GoodExample:
    def __init__(self, value):
        self._value = value  # Store in _value (different name!)

    @property
    def value(self):
        return self._value   # Return from _value

    @value.setter
    def value(self, new_value):
        self._value = new_value  # Store in _value
```

Now `self.value = 10` calls the setter, which stores in `self._value` (no recursion).

---

## Task 1: PCAP Warm-up - Exception Hierarchy (Pure Python)

Answer these questions:

**Q1:** Which exception is the parent of ALL built-in exceptions?
- A) `Exception`
- B) `BaseException`
- C) `Error`
- D) `object`

**Q2:** What is the output?
```python
try:
    x = int("abc")
except Exception as e:
    print(type(e).__name__)
```

**Q3:** Can you catch `KeyboardInterrupt` with `except Exception`? Why or why not?

**Q4:** What's wrong with this code?
```python
try:
    risky_operation()
except:
    pass
```

**Your answers:**
```
Q1: B

Q2: ValueError

Q3: No, it's not an Exception, but a different type of a BaseException

Q4: Except does not handle any errors, there's just the pass, which literally does nothing

```

---

## Task 2: Build a `BankAccount` Class with Full Encapsulation

Create a `BankAccount` class with:

1. **Constructor:** `__init__(self, owner: str, initial_balance: float = 0.0)`
   - Store `_owner` (protected, immutable after creation)
   - Store `_balance` (protected)
   - Validate: initial_balance cannot be negative (raise `ValueError`)

2. **Properties:**
   - `owner` - read-only property (no setter)
   - `balance` - read-only property (no setter - use methods to modify)

3. **Methods:**
   - `deposit(amount: float) -> None` - add to balance (amount must be > 0)
   - `withdraw(amount: float) -> bool` - subtract from balance if sufficient funds, return True/False
   - `__str__` - return `"BankAccount(owner='John', balance=100.00)"`

**Test code:**
```python
acc = BankAccount("Alice", 100.0)
print(acc.owner)          # Alice
print(acc.balance)        # 100.0
acc.deposit(50.0)
print(acc.balance)        # 150.0
success = acc.withdraw(200.0)
print(success)            # False (insufficient funds)
print(acc.balance)        # 150.0 (unchanged)
acc.owner = "Bob"         # AttributeError (read-only)
```

**Your code:**
```python

class BankAccount:
    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.__owner = owner
        self.initial_balance = initial_balance
        self.__balance = self.initial_balance
        
    def __str__(self):
        return f'{__class__.__name__}(owner = {self.__owner}, balance = {self.__balance})'
        
    @property
    def owner(self) -> str:
        return self.__owner
    
    @property
    def balance(self) -> float:
        if self.initial_balance < 0:
            raise ValueError('Initial balance cannot be below 0!')
        else:
            return self.__balance
        
    def deposit(self, amount: float):
        self.__balance += amount
    
    def withdraw(self, amount: float):
        if amount > self.__balance:
            print(f'The current balance is lower than the amount you want to withdraw!')
            return False
        else:
            self.__balance -= amount
            print(f'Successfully withdrawn ${amount:.2f} from the account.')
            return True


```

**Test output:**
```

$ python practice.py
Alice
100.0
150.0
The current balance is lower than the amount you want to withdraw!
False
150.0
Traceback (most recent call last):
  File "C:\Users\HARDPC\Desktop\AL\projekty\python_pcap_agentic_learning\practice.py", line 2748, in <module>
    acc.owner = "Bob"         # AttributeError (read-only)
    ^^^^^^^^^
AttributeError: property 'owner' of 'BankAccount' object has no setter

```

---

## Task 3: PCAP Drill - `__str__` vs `__repr__` Review

**Q1:** Implement both `__str__` and `__repr__` for this class:

```python
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # Add __str__ and __repr__
```

Requirements:
- `__str__` should return: `"Point at (3, 5)"`
- `__repr__` should return: `"Point(x=3, y=5)"`

**Q2:** What prints when you do this?
```python
p = Point(3, 5)
print(p)           # Which method? str
print([p])         # Which method? repr
print(f"{p}")      # Which method? str
print(f"{p!r}")    # Which method? -> repr
```

**Your code and answers:**
```python
# Q1: Your Point class


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        '''Simplified string representation if anybody wants to print a class instance'''
        return f'{__class__.__name__} at ({self.x}, {self.y})'
    
    def __repr__(self) -> str:
        '''Unambigous representation for devs'''
        return f'{__class__.__name__!r}(x = {self.x}, y = {self.y})'


# Q2: Your predictions
print(p)      # str
print([p])    # repr
print(f"{p}") # str
print(f"{p!r}") # repr

```

---

## Task 4: PROJECT - TradeManager Class

Create a `TradeManager` class to manage multiple trades:

**Requirements:**
1. **Constructor:** Initialize with empty list `_trades`
2. **Method:** `add_trade(trade: Trade) -> None` - adds trade to list
3. **Method:** `remove_trade(ticker: str) -> bool` - removes first trade matching ticker, returns True/False
4. **Property:** `total_pnl` - returns sum of all trade PnLs
5. **Property:** `win_rate` - returns percentage of winning trades (0-100)
6. **Property:** `trade_count` - returns number of trades
7. **Method:** `get_trades_by_side(side: str) -> List[Trade]` - filter by BUY/SELL
8. **`__len__`** - return number of trades (so `len(manager)` works)
9. **`__iter__`** - make it iterable (so `for trade in manager` works)

**Test code:**
```python
from algo_backtest.engine.trade import Trade

manager = TradeManager()
manager.add_trade(Trade("AAPL", "BUY", 100, 110, 10))   # +100 PnL
manager.add_trade(Trade("GOOGL", "SELL", 200, 190, 5))  # +50 PnL
manager.add_trade(Trade("MSFT", "BUY", 50, 45, 20))     # -100 PnL

print(f"Total P&L: ${manager.total_pnl:.2f}")  # $50.00
print(f"Win Rate: {manager.win_rate:.1f}%")    # 66.7%
print(f"Trade Count: {manager.trade_count}")   # 3
print(f"Length: {len(manager)}")               # 3

for trade in manager:
    print(trade)
```

**Your code:**
```python

from typing import List
from algo_backtest.engine.trade import Trade

class TradeManager:
    '''Mock class used to manage trades with the Trade class, we can calculate the win rate, total pnl etc.
       Requires Trade class import from algo_backtest/engine/trade.py'''
    
    def __init__(self):
        self._trades = []
        self.__total_pnl: float = 0.0
        self.__win_rate: float = 0.0
        self.__trade_count: int = 0
        
        self.winning_trades = 0
        
    def __len__(self):
        '''Length dunder method'''
        return len(self._trades)

    def __iter__(self):
        '''Iter dunder method, making the objects in the TradeManager iterable'''
        return iter(self._trades)
    
    @property 
    def trade_count(self):
        return self.__trade_count
    
    @property
    def total_pnl(self):
        return self.__total_pnl
    
    @property
    def win_rate(self):
        self.__win_rate = (self.winning_trades / self.__trade_count * 100)
        return self.__win_rate
        
    
    def add_trade(self, trade: Trade) -> None:
        '''A method used to add trades created with a Trade class'''
        self._trades.append(trade)
        self.__trade_count += 1
        self.__total_pnl += trade.pnl
        if trade.pnl > 0:
            self.winning_trades += 1
        
    def remove_trade(self, ticker: str) -> bool:
        '''A method used to remove trades and return a T/F'''
        for trade in self._trades:
            if trade.ticker == ticker:
                self._trades.remove(trade)
                return True
        print('Did not find a trade with requested ticker')
        return False

    def get_trades_by_side(self, side: str) -> List[Trade]:
        '''Gets all of the trades that are either 'BUY' or 'SELL' '''
        filtered_trades = []
        
        for trade in self._trades:
            if trade.side == side:
                filtered_trades.append(trade)
        
        return filtered_trades




```

**Test output:**
```

$ python practice.py
Total P&L: $50.00
Win Rate: 66.7%
Trade Count: 3
Length: 3
[WIN] BUY 10 AAPL:
                100 -> 110
                | P&L: $100.00
[WIN] SELL 5 GOOGL:
                200 -> 190
                | P&L: $50.00
[LOSS] BUY 20 MSFT:
                50 -> 45
                | P&L: $-100.00
(.venv) 

```

---

## Task 5: PCAP Drill - Multiple Choice (PCAP Core Topics)

**Question 1:** What is the output?
```python
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        self.y = 2

b = B()
print(hasattr(b, 'x'), hasattr(b, 'y'))
```
- A) `True True`
- B) `False True`
- C) `True False`
- D) `False False`

**Your answer:**
B


---

**Question 2:** Which correctly makes a read-only property?
- A) `@property` with `@name.setter` that raises an error
- B) `@property` without defining a setter
- C) Using `__name` (name mangling)
- D) Using `_name` (protected convention)

**Your answer:**
B

---

**Question 3:** What exception is raised?
```python
class MyClass:
    @property
    def value(self):
        return self._value

obj = MyClass()
print(obj.value)
```
- A) `ValueError`
- B) `AttributeError`
- C) `TypeError`
- D) `NameError`

**Your answer:**
B


---

**Question 4:** What is the output?
```python
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
        self.id = Counter.count

c1 = Counter()
c2 = Counter()
c3 = Counter()
print(c1.id, c2.id, c3.id)
```
- A) `1 1 1`
- B) `1 2 3`
- C) `3 3 3`
- D) `0 1 2`

**Your answer:**
B


---

## Task 6: Debugging Exercise - Fix the Broken Class

This class has **4 bugs**. Find and fix them all:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self.price  # Bug 1

    @price.setter
    def price(self, value):
        if value > 0:
            self._price = value
        # Bug 2: What if value <= 0?

    def apply_discount(self, percent):
        self._price = self._price * (1 - percent)  # Bug 3

    def __str__(self)
        return f"Product: {self.name}, ${self._price}"  # Bug 4
```

**Your fixed code:**
```python

class Product:
    '''Mock class for exercise purpose'''
    def __init__(self, name: str, price: float):
        self.name = name
        self._price = price
    
    def __str__(self):
        return f'Product: {self.name}, ${self._price}'    
    
    @property
    def price(self):
        if self._price < 0:
            raise ValueError('Price cannot be negative!')
        else:
            return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError('Price cannot be negative!')
        else:
            self._price = value
            
    def apply_discount(self, percent):
        self._price = self._price * (1 - percent / 100)



```

**Explanation of each bug:**
```
    # 1. Wrong property name
    # 2. We aren't properly handling negative values here, which should be the msot logical step
    # 3. Whatever number we put as percent here (if it's an integer), we'd end up with a negative number most likely
    # 4. Lack of :

```

---

## Task 7: PROJECT - Enhance Position with `__eq__` and `__hash__`

Add to your `Position` class:

1. **`__eq__(self, other)`** - Two positions are equal if they have:
   - Same ticker
   - Same side
   - Same entry_price
   - Same quantity

2. **`__hash__(self)`** - Make Position hashable (so it can be used in sets/dicts)
   - Return `hash((self._ticker, self._side, self._entry_price, self._quantity))`

**Test code:**
```python
p1 = Position("AAPL", "BUY", 100.0, 10)
p2 = Position("AAPL", "BUY", 100.0, 10)
p3 = Position("AAPL", "SELL", 100.0, 10)

print(p1 == p2)  # True
print(p1 == p3)  # False

# Can use in set
positions = {p1, p2, p3}
print(len(positions))  # 2 (p1 and p2 are duplicates)
```

**Your code (just the new methods):**
```python

    
    def __hash__(self):
        '''A dunder method that allows us to hash a given position to later be used in a dictionary'''
        return hash((self.ticker, self.side, self.entry_price, self.quantity))
    
    def __eq__(self, other) -> bool:
        '''Checks whether two positions are equal to each other

```

**Test output:**
```
True
False
2

also a result of print(positions):

{Position(ticker = AAPL, side = SELL, entry_price = 100.0, quantity = 10, stop_loss = None, take_profit = None), Position(ticker = AAPL, side = BUY, entry_price = 100.0, quantity = 10, stop_loss = None, take_profit = None)}
(.venv) 
```

However, I would like to point out here that WE DIDN'T HAVE eq, len, iter, or hash dunder methods at all and they're not present in my learning materials... They all shoudl be included in a special file week3_dunder_methods, or something similar, where we begin with a table of contents (just showing the names of agiven dunder method), and a short description, information with a simple example of each method. I will then ask you to sometimes update it, or whatever. The task WASN'T difficult and required me to check the web and literally I could just copy the answer from the question. I've maybe learned something, but then I'm not sure at all I will be able toa ctually implement hash method in the acutal code.

---

## Task 8: PCAP Trap - Mutable Default Arguments (Review)

**Q1:** What's the output?
```python
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("a"))
print(add_item("b"))
print(add_item("c"))
```

**Q2:** Fix the function to work correctly.

**Your answers:**
```
Q1 Output:
[a], [a, b], [a, b, c]


Q2 Fixed code:

from typing import List

def add_item(item: str, items: List = None) -> List:
    
    if items is None:
        items = []
    items.append(item)
    return items

```

---

## Checklist

- [ ] Task 1: Exception hierarchy (4 questions)
- [ ] Task 2: BankAccount class with encapsulation
- [ ] Task 3: `__str__` vs `__repr__` review
- [ ] Task 4: TradeManager class (PROJECT)
- [ ] Task 5: Multiple choice (4 questions)
- [ ] Task 6: Debug broken Product class (4 bugs)
- [ ] Task 7: Position `__eq__` and `__hash__` (PROJECT)
- [ ] Task 8: Mutable default argument trap

---

## Feedback Section

**Time spent:** 70 minutes

**Difficulty (1-10): 5-6**

**What clicked:**
I'd say everything was doable today.

**What's confusing:**
The new dunder methods are definitely now that difficult, but I definitely want notes about them for future reference as well.

Encapsulation and inheriting values via different classes still seems tricky to me - I need more DOABLE examples to work on it, and I need some examples that will clearly show the difference and kind of ground that in my brain, becuase I sometimes still confuse whether the init values will be inherited, or not, if there's super() or not etc..

**Questions for mentor:**


---

**When complete:** Fill out feedback section above and notify mentor for assessment.
