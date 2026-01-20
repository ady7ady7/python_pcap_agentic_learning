# Week 3, Day 2 - Advanced Properties, Validation & `random` Module

**Date:** 2026-01-20
**Focus:** Property patterns, data validation, `random` module basics, PCAP drills

**Lessons:**
- [Encapsulation & Properties](lessons/week3_oop_encapsulation.md)
- [The random Module](lessons/week3_random_module.md)

**Target Difficulty:** 5-6/10

**Remember:** Work in `practice.py`, paste FINAL answers here for review.

---

## Task 1: PCAP Warm-up - `random` Module Basics (Pure Python)

Answer these questions about the `random` module:

**Q1:** What is the output range of `random.random()`?
- A) 0 to 1 (inclusive on both ends)
- B) 0 to 1 (excludes 0)
- C) 0 to 1 (excludes 1)
- D) 1 to 100

**Q2:** What is the difference between `random.randint(1, 10)` and `random.randrange(1, 10)`?

**Q3:** What error occurs with `random.sample([1, 2, 3], 5)`?

**Q4:** True or False: `random.choice([1, 2, 3])` can return the same element multiple times if called repeatedly.

**Your answers:**
```
Q1: B

Q2: Randint returns int values, randrange returns floats.

Q3: The sample cannot be longer than the length of the source it uses (here the list has 3 elements, and we're asking for a sample of 5 - it's literally impossible)

Q4: True

```

---

## Task 2: Predict the Output - `random` with `seed()`

```python
import random

random.seed(100)
a = random.randint(1, 10)

random.seed(100)
b = random.randint(1, 10)

random.seed(200)
c = random.randint(1, 10)

print(a == b)
print(a == c)
```

**Predict the output and explain WHY.**

**Your prediction:**
```
# Output (2 lines):
print(a == b) #True
print(a == c) #False

# Explanation:
Seed is a guarantee of returning the same results if we use the same seed setting.

```

---

## Task 3: Property with Validation - `Percentage` Class

Create a `Percentage` class that:
1. Stores a value as a protected attribute `_value`
2. Has a `value` property (getter)
3. Has a `value` setter that:
   - Accepts values 0-100 (inclusive)
   - Raises `ValueError` with message "Percentage must be between 0 and 100" if out of range
4. Has a `as_decimal` property (read-only) that returns value / 100

**Test code:**
```python
p = Percentage(50)
print(p.value)      # 50
print(p.as_decimal) # 0.5
p.value = 75
print(p.value)      # 75
p.value = 150       # ValueError: Percentage must be between 0 and 100
```

**Your code:**
```python

class Percentage:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, setter):
        if setter in range(0, 101):
            self._value = setter
        else:
            raise ValueError('Percentage must be between 0 and 100!')
    
    @property
    def as_decimal(self):
        return self._value / 100



```

---

## Task 4: Property Trap - Infinite Recursion

**What happens when you run this code?**

```python
class BadExample:
    def __init__(self, value):
        self.value = value

    @property
    def value(self):
        return self.value

    @value.setter
    def value(self, new_value):
        self.value = new_value

obj = BadExample(10)
```

**A)** Prints 10
**B)** RecursionError (infinite loop)
**C)** AttributeError
**D)** Works fine, obj.value is 10

**Your answer and explanation:**
```
Answer:
B


Explanation:
The value attribute is left unprotected, but honestly I DON'T UNDERSTAND THIS MYSELF, and I'd like you to explain this further and focus on that tomorrow with a scaffolding approach.


How to fix it:
If we protect the attribute by turning self.value into self._value, the issue disappears.

```

---

## Task 5: PROJECT - Trade Class Enhancement

Enhance your `Trade` class from Day 1 with:

1. Add a `@property` called `return_percent` that calculates:
   - For BUY: `((exit_price - entry_price) / entry_price) * 100`
   - For SELL: `((entry_price - exit_price) / entry_price) * 100`

2. Add a `@property` called `risk_reward_ratio` that:
   - Requires the Trade to have `stop_loss` and `take_profit` attributes (add if needed)
   - Calculates: `abs(take_profit - entry_price) / abs(entry_price - stop_loss)`
   - Returns `None` if stop_loss equals entry_price (division by zero protection)

3. **Fix the `calculate_win_rate` classmethod bug from Day 1:**
   - Change `trade.pnl()` to `trade.pnl` (property, not method!)

**Test with:**
```python
trade = Trade(
    ticker="EURUSD",
    side="BUY",
    entry_price=1.1000,
    exit_price=1.1050,
    quantity=10000,
    stop_loss=1.0950,
    take_profit=1.1100
)
print(f"P&L: ${trade.pnl:.2f}")
print(f"Return: {trade.return_percent:.2f}%")
print(f"R:R Ratio: {trade.risk_reward_ratio:.2f}")
```

**Your updated code (paste the new/changed parts):**
```python
#Changed parts below:

    def __init__(self,
                 ticker: str,
                 side: str,
                 entry_price: float,
                 exit_price: float,
                 quantity: float,
                 entry_time: Optional[str] = None,
                 exit_time: Optional[str] = None,
                 stop_loss: Optional[float] = None,
                 take_profit: Optional[float] = None,
                 exit_reason: Optional[str] = None
                 ):
        
        """Initialize a completed trade and calculate P&L."""
        
        self._ticker = ticker
        self._side = side.upper()
        self._entry_price = entry_price
        self._exit_price = exit_price
        self._quantity = quantity
        self._entry_time = entry_time
        self._exit_time = exit_time
        self._stop_loss = stop_loss
        self._take_profit = take_profit
        
        if exit_reason is not None:
            self._exit_reason = exit_reason.upper()
        else:
            self._exit_reason = ''

        #Properties - is_winner + pnl + return_percent
        self.__pnl: Optional[float] = None
        self.__is_winner: Optional[bool] = None
        self.__return_percent: Optional[float] = None
        self.__risk_reward_ratio: Optional[float] = None


    @property
    def return_percent(self) -> float:
        '''A property used to calculate the %P/L'''
        if self._side == 'BUY':
            self.__return_percent = ((self._exit_price - self._entry_price) / self._entry_price) * 100
        else:
            self.__return_percent = ((self._entry_price - self._exit_price) / self._entry_price) * 100
            
        return self.__return_percent
    
    @property
    def risk_reward_ratio(self) -> float:
        '''A property used to calc R:R ratio'''
        if self._stop_loss == self._entry_price:
            return 0
        else:
            self.__risk_reward_ratio = abs(self._take_profit - self._entry_price) / abs(self._entry_price - self._stop_loss)
        return self.__risk_reward_ratio


```

**Test output:**
```
$ python practice.py
P&L: $50.00
Return: 0.45%
R:R Ratio: 2.00
(.venv) 
```

---

## Task 6: `random.choice()` vs `random.sample()` Practice

**Q1:** Predict ALL possible outputs of this code:
```python
import random
random.seed(42)
result = random.choice(['A', 'B', 'C'])
print(result)
```
(Hint: With a seed, the output is deterministic)


**Q2:** What's the difference between these two approaches?
```python
# Approach A
picks = [random.choice(items) for _ in range(3)]

# Approach B
picks = random.sample(items, 3)
```

**Q3:** Write code that randomly selects 3 unique prices from a list of 10 prices (no duplicates).

**Your answers:**
```
Q1: We will always get the same result, as seed gives deterministic output (replicable).

Q2: A - we'd get a random item from the range each time - in a sense we'd get 3 random items, as we're using a list comprehension here - there could've been repetitions.
B - We'd get a sample of items of length 3 - random and no repetitions.

Q3 (code):

import random
prices = [random.randrange(0, 400) for i in range(10)]
print(prices)
sample = random.sample(prices, 3)
print(sample)

```

---

## Task 7: PCAP Multiple Choice - Properties & Encapsulation

**Question 1:** What does `@property` allow you to do?
- A) Make an attribute immutable
- B) Run code when an attribute is accessed
- C) Prevent a class from being inherited
- D) Create class-level constants

**Your answer:**
B


---

**Question 2:** Given this code:
```python
class Example:
    def __init__(self):
        self.__data = [1, 2, 3]

    @property
    def data(self):
        return self.__data

e = Example()
e.data.append(4)
print(len(e.data))
```
What is the output?
- A) 3
- B) 4
- C) AttributeError
- D) TypeError

**Your answer:**
B


---

**Question 3:** Which statement about `random.sample()` is TRUE?
- A) It can return duplicate elements
- B) It modifies the original list
- C) The k parameter can exceed the sequence length
- D) It returns elements in random order without duplicates

**Your answer:**
D

---

**Question 4:** What is the purpose of `random.seed()`?
- A) Generate truly random numbers
- B) Make random results reproducible
- C) Reset the random number generator to zero
- D) Increase randomness quality

**Your answer:**
B


---

## Task 8: Integration - Position Risk Validator

Create a `RiskValidator` class that validates trading positions using properties:

**Requirements:**
1. Constructor takes: `max_risk_percent` (float), `max_position_size` (float)
2. Both should be stored as protected attributes with validation:
   - `max_risk_percent` must be between 0.1 and 10.0
   - `max_position_size` must be positive
3. Add `@property` getters for both
4. Add a method `validate_position(position: Position) -> Tuple[bool, str]` that:
   - Checks if position quantity exceeds `max_position_size`
   - Returns `(False, "Position size exceeds maximum")` if invalid
   - Returns `(True, "Position valid")` if valid

**Test with:**
```python
validator = RiskValidator(max_risk_percent=2.0, max_position_size=100.0)
print(validator.max_risk_percent)  # 2.0

# Create a position with 150 units (exceeds max)
large_position = Position(
    ticker="AAPL",
    side="BUY",
    quantity=150.0,
    entry_price=150.0
)

valid, message = validator.validate_position(large_position)
print(f"Valid: {valid}, Message: {message}")
# Valid: False, Message: Position size exceeds maximum
```

**Your code:**
```python


from typing import Tuple

class RiskValidator:
    
    def __init__(self, max_risk_percent: float, max_position_size: float):
        
        self.__max_risk_percent = max_risk_percent
        self.__max_position_size = max_position_size
        
    @property
    def max_risk_percent(self) -> float:
        '''Property max_risk_percent with validation'''
        if self.__max_risk_percent < 0.1 or self.__max_risk_percent > 10:
            raise ValueError('Max risk percent should be between 0.1 and 10.0!')
        else:
            return self.__max_risk_percent

    @property
    def max_position_size(self) -> float:
        '''Property max_position_size with validation'''
        if self.__max_position_size < 0:
            raise ValueError('Max position size should be above 0!')
        else:
            return self.__max_position_size
        
    def validate_position(self, position) -> Tuple[bool, str]:
        if position.quantity > self.__max_position_size:
            return (False, 'Position size exceeds maximum')
        else:
            return (True, 'Position valid!')
        

validator = RiskValidator(max_risk_percent=2.0, max_position_size=100.0)
print(validator.max_risk_percent)  # 2.0


from algo_backtest.engine.position import Position

large_position = Position(
    ticker="AAPL",
    side="BUY",
    quantity=150.0,
    entry_price=150.0
)


valid, message = validator.validate_position(large_position)
print(f"Valid: {valid}, Message: {message}")

```

**Test output:**
```

$ python practice.py
2.0
Valid: False, Message: Position size exceeds maximum
(.venv) 

```

---

## Bonus Task 9: Random Trade Generator (Optional)

Create a function `generate_random_trades(n: int, tickers: List[str]) -> List[Trade]` that:

1. Uses `random.choice()` to pick a random ticker for each trade
2. Uses `random.choice(['BUY', 'SELL'])` for side
3. Uses `random.uniform(10.0, 200.0)` for entry_price (look this up!)
4. Calculates exit_price as entry_price ± random 1-5%
5. Uses `random.randint(1, 100)` for quantity

**Example:**
```python
tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
trades = generate_random_trades(5, tickers)
for trade in trades:
    print(trade)
```

**Your code:**
```python

import random
from typing import List
from algo_backtest.engine.trade import Trade

def generate_random_trades(n: int, tickers: List[str]) -> List[Trade]:
    '''A function used to generate a number of random trades
    
    Args: 
    n - the number of trades you want to generate
    tickers - the list of tickers you want to use in the generator
    
    Returns:
    - a list of generated trades
    '''
    
    trades = []
    
    for i in range(n):
        ticker = random.choice(tickers)
        side = random.choice(['BUY', 'SELL'])
        entry_price = random.uniform(120.0, 200.0)
        exit_price = entry_price * random.uniform(0.95, 1.05)
        quantity = random.randint(1, 100)
        
        trade = Trade(ticker, side, entry_price, exit_price, quantity)
        trades.append(trade)
        
    return trades


tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
trades = generate_random_trades(5, tickers)
for trade in trades:
    print(trade)


log:
$ python practice.py
[LOSS] SELL 34 AAPL: 
                185.98111874245407 -> 186.7779514338092
                | P&L: $-27.09
[WIN] SELL 36 AMZN:
                194.20487593635704 -> 187.88404543653377
                | P&L: $227.55
[LOSS] BUY 7 GOOGL:
                120.58725843989532 -> 118.93887978985677
                | P&L: $-11.54
[WIN] BUY 5 AAPL:
                126.71241306407863 -> 131.95414869532704
                | P&L: $26.21
[WIN] SELL 10 AMZN:
                184.4049033108104 -> 181.14097146272442
                | P&L: $32.64




```

---

## Checklist

- [ ] Task 1: random module basics (4 questions)
- [ ] Task 2: seed() output prediction
- [ ] Task 3: Percentage class with validation
- [ ] Task 4: Property infinite recursion trap
- [ ] Task 5: Trade class enhancements
- [ ] Task 6: choice vs sample practice
- [ ] Task 7: Multiple choice (4 questions)
- [ ] Task 8: RiskValidator class
- [ ] Bonus Task 9: Random trade generator (optional)

---

## Feedback Section

**Time spent:** ___ minutes

**Difficulty (1-10):**

**What clicked:**


**What's confusing:**


**Questions for mentor:**


---

**When complete:** Fill out feedback section above and notify mentor for assessment.
