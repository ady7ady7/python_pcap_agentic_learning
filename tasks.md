# Week 1, Day 3 - OOP Fundamentals: Classes, Objects & Methods

**Date:** 2026-01-07
**Topic:** Object-Oriented Programming - Classes, `__init__`, `self`, Attributes & Methods
**Target:** 8 Tasks Completed
**Rules:** PCAP Drills = Pure Python (no external libraries). Project Tasks = Pandas/NumPy allowed.

**IMPORTANT:** Read [lessons/week1_oop_fundamentals.md](lessons/week1_oop_fundamentals.md) BEFORE starting these tasks!

---

## Task 1: PCAP Warm-up - Understanding `self` (Pure Python)

**Predict the output** of this code:

```python
class Counter:
    def __init__(self, start):
        self.value = start

    def increment(self):
        self.value += 1

    def get_value(self):
        return self.value

c1 = Counter(10)
c2 = Counter(20)

c1.increment()
c1.increment()
c2.increment()

print(c1.get_value())
print(c2.get_value())
```

**Your answer:**
- Line 1 output: `___`
- Line 2 output: `___`

**Explain:** Why do `c1` and `c2` have different values even though they're both `Counter` objects?

**Answer here:**

---

## Task 2: PCAP Warm-up - Instance vs Class Attributes (Pure Python)

**Predict the output** of this code:

```python
class Dog:
    species = "Canis familiaris"

    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")
dog2 = Dog("Max")

print(dog1.name)
print(dog2.name)
print(dog1.species)
print(dog2.species)

Dog.species = "Canis lupus"

print(dog1.species)
print(dog2.species)
```

**Your predictions:**
1. `dog1.name` → `___`
2. `dog2.name` → `___`
3. `dog1.species` (first time) → `___`
4. `dog2.species` (first time) → `___`
5. `dog1.species` (after change) → `___`
6. `dog2.species` (after change) → `___`

**Question:** What's the difference between `self.name` and `species` in this class?

**Answer here:**

---

## Task 3: Theory Drill - Build Your First Class (Pure Python)

Create a `BankAccount` class with the following requirements:

**Requirements:**
```python
class BankAccount:
    """
    Represents a simple bank account.

    Attributes:
        owner: Account owner's name.
        balance: Current account balance.
    """

    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        """Initialize account with owner and optional starting balance."""
        # Your code here

    def deposit(self, amount: float) -> None:
        """
        Deposit money into account.

        Only allows positive amounts.
        Prints confirmation message.
        """
        # Your code here

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw money from account.

        Returns True if successful, False if insufficient funds.
        Only allows positive amounts.
        """
        # Your code here

    def get_balance(self) -> float:
        """Return current balance."""
        # Your code here
```

**Professional Standards:**
- Type hints on all methods
- Docstrings (already provided)
- Validation (no negative deposits/withdrawals, no overdrafts)
- PEP 8 formatting

**Test your code in `practice.py`:**
```python
account = BankAccount("Alice", 100.0)
account.deposit(50.0)
print(account.get_balance())  # Should print 150.0
account.withdraw(30.0)
print(account.get_balance())  # Should print 120.0
account.withdraw(200.0)       # Should fail (insufficient funds)
print(account.get_balance())  # Should still be 120.0
```

**Paste your BankAccount class here:**

---

## Task 4: PCAP Trap Hunt - Mutable Class Attributes (Pure Python)

**Find the bug** in this code:

```python
class TodoList:
    tasks = []  # Shared by all instances!

    def __init__(self, owner):
        self.owner = owner

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

alice_todos = TodoList("Alice")
bob_todos = TodoList("Bob")

alice_todos.add_task("Buy groceries")
bob_todos.add_task("Walk dog")

print(f"Alice's tasks: {alice_todos.get_tasks()}")
print(f"Bob's tasks: {bob_todos.get_tasks()}")
```

**Questions:**
1. What will this code print? (Predict the output)
2. What's the bug?
3. Fix the code so each TodoList has its own tasks list
4. Explain why this happens (reference class vs instance attributes)

**Answer here:**

---

## Task 5: PROJECT TASK - Create Position Class (Pure Python + Type Hints)

Create a `Position` class to represent a trading position in the AlgoBacktest project.

**File:** Create `algo_backtest/engine/position.py`

**Requirements:**
```python
"""Position management for trading strategies."""

from typing import Optional


class Position:
    """
    Represents a single trading position.

    Attributes:
        ticker: Trading symbol (e.g., "EURUSD").
        entry_price: Price at which position was opened.
        quantity: Number of units (positive for long, negative for short).
        stop_loss: Stop loss price (optional).
        take_profit: Take profit price (optional).
    """

    def __init__(
        self,
        ticker: str,
        entry_price: float,
        quantity: int,
        stop_loss: Optional[float] = None,
        take_profit: Optional[float] = None
    ) -> None:
        """Initialize a new position."""
        # Your code here - store all parameters as instance attributes
        # Also calculate and store position_type: "long" if quantity > 0, "short" if < 0

    def is_long(self) -> bool:
        """Check if position is long (quantity > 0)."""
        # Your code here

    def is_short(self) -> bool:
        """Check if position is short (quantity < 0)."""
        # Your code here

    def calculate_pnl(self, current_price: float) -> float:
        """
        Calculate unrealized profit/loss.

        Formula:
        - Long: (current_price - entry_price) * quantity
        - Short: (entry_price - current_price) * abs(quantity)

        Returns:
            Unrealized P&L in currency units.
        """
        # Your code here

    def should_close(self, current_price: float) -> bool:
        """
        Check if position should close (hit SL or TP).

        Returns:
            True if stop loss or take profit is hit, False otherwise.
        """
        # Your code here
        # Hint: For long positions, close if price <= stop_loss OR price >= take_profit
        #       For short positions, close if price >= stop_loss OR price <= take_profit
```

**Test your code in `practice.py`:**
```python
from algo_backtest.engine.position import Position

# Long position
long_pos = Position("EURUSD", entry_price=100.0, quantity=1000, stop_loss=99.0, take_profit=102.0)
print(long_pos.is_long())  # True
print(long_pos.calculate_pnl(101.0))  # 1000.0
print(long_pos.should_close(98.5))  # True (hit SL)

# Short position
short_pos = Position("GBPUSD", entry_price=120.0, quantity=-500, stop_loss=121.0, take_profit=118.0)
print(short_pos.is_short())  # True
print(short_pos.calculate_pnl(119.0))  # 500.0
print(short_pos.should_close(117.5))  # True (hit TP)
```

**Paste your Position class here:**

---

## Task 6: PROJECT TASK - Fix DataLoader Class (Pandas Allowed)

Now that you understand OOP, go back and **fix the bugs** in your `DataLoader` class from Day 2.

**File:** `algo_backtest/data/data_loader.py`

**Issues to fix (from Day 2 feedback):**

1. **Missing context manager in `load_data()`**
   - Current: `data = pd.read_csv(self.filepath)`
   - Required: Use `with open(...) as f:` and `pd.read_csv(f)`

2. **Missing return statement in ValueError handler**
   ```python
   except ValueError as e:
       print(f'Value Error! {str(e)}')
       # Add: return None
   ```

3. **Logic error in `validate_data()` - missing columns check**
   - Current: `missing_columns = set(df.columns) - set(df.columns)`
   - Fix: `missing_columns = set(req_columns) - set(df.columns)`

4. **Fix NaN check** (this one is tricky - we'll teach Pandas properly soon, but try to fix it)
   - The `nan_values.any()` check doesn't properly validate
   - Hint: You want to check if the sum is greater than 0, not just if `.any()` returns True

**Test your fixes:**
```python
from algo_backtest.data.data_loader import DataLoader

loader = DataLoader('ohlc_mock_data.csv')
data = loader.load_data()
if data is not None:
    is_valid = loader.validate_data(data)
    print(f"Data valid: {is_valid}")  # Should print True
```

**Paste your corrected methods here (just the fixed parts):**

---

## Task 7: PCAP Simulation - Multiple Choice

**Question 1:**
What is the output of this code?

```python
class Test:
    value = 10

    def __init__(self):
        self.value = 20

obj = Test()
print(obj.value)
print(Test.value)
```

**Choices:**
A) `20` then `20`
B) `10` then `10`
C) `20` then `10`
D) `10` then `20`

**Your answer with explanation:**

---

**Question 2:**
What happens when you run this code?

```python
class Person:
    def __init__(self, name):
        self.name = name
        return self

p = Person("Alice")
```

**Choices:**
A) Works fine, `p.name` is `"Alice"`
B) `TypeError: __init__() should return None`
C) `AttributeError: 'NoneType' object has no attribute 'name'`
D) `NameError: self is not defined`

**Your answer with explanation:**

---

## Task 8: Integration Challenge - OHLCCandle Class Enhancement (Pure Python)

Enhance the `OHLCCandle` class from the lesson with a new method.

**Starting point (from lesson):**
```python
class OHLCCandle:
    """Represents a single OHLC candle."""

    def __init__(self, timestamp: str, ticker: str, open_price: float,
                 high: float, low: float, close: float, volume: int) -> None:
        self.timestamp = timestamp
        self.ticker = ticker
        self.open = open_price
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def is_bullish(self) -> bool:
        """Check if candle closed higher than it opened."""
        return self.close > self.open

    def get_body_size(self) -> float:
        """Calculate candle body size."""
        return abs(self.close - self.open)

    def get_range(self) -> float:
        """Calculate candle range (high - low)."""
        return self.high - self.low
```

**Add these three methods:**

1. **`is_doji(self, threshold: float = 0.1) -> bool`**
   - A doji is when body size is very small compared to range
   - Return `True` if `body_size / range < threshold`
   - Handle edge case: if range is 0, return `True`

2. **`get_upper_wick(self) -> float`**
   - Calculate upper wick (shadow) length
   - Formula: `high - max(open, close)`

3. **`get_lower_wick(self) -> float`**
   - Calculate lower wick (shadow) length
   - Formula: `min(open, close) - low`

**Test your enhanced class:**
```python
candle = OHLCCandle(
    timestamp="2024-01-01 09:00:00",
    ticker="EURUSD",
    open_price=100.5,
    high=101.0,
    low=100.0,
    close=100.6,
    volume=5000
)

print(f"Is doji? {candle.is_doji()}")  # Should be False (body is significant)
print(f"Upper wick: {candle.get_upper_wick():.2f}")  # 101.0 - 100.6 = 0.40
print(f"Lower wick: {candle.get_lower_wick():.2f}")  # 100.5 - 100.0 = 0.50
```

**Paste your three new methods here:**

---

## Bonus Challenge (Optional): Class Attribute Counter

Create an `Employee` class that automatically assigns unique IDs to each employee using a **class attribute** counter.

**Requirements:**
```python
class Employee:
    """
    Employee with auto-incrementing ID.

    Class Attributes:
        total_employees: Counter for total employees created.

    Instance Attributes:
        name: Employee name.
        employee_id: Unique ID assigned automatically.
    """

    # Your code here
```

**Expected behavior:**
```python
emp1 = Employee("Alice")
emp2 = Employee("Bob")
emp3 = Employee("Charlie")

print(emp1.employee_id)  # 1
print(emp2.employee_id)  # 2
print(emp3.employee_id)  # 3
print(Employee.total_employees)  # 3
```

**Paste your Employee class here:**

---

## Self-Assessment

After completing all tasks, rate yourself:

- **Score:** ___/8 tasks completed
- **Difficulty:** (Easy/Medium/Hard)
- **Time Spent:** ___ hours
- **Sticking Points:** (What was confusing?)

Document this in `feedback.md`.

---

**Next Session Preview:**
Tomorrow (Day 4) we'll continue with OOP - building more complex classes, understanding `__str__` and `__repr__`, and creating the `Trade` class for the backtesting engine!
