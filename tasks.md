# Week 3, Day 1 Tasks - Encapsulation & Properties (Monday)

**Focus:** Access control conventions, `@property` decorator, building the Trade class

**Lesson:** [Encapsulation & Properties](lessons/week3_oop_encapsulation.md)

**Target Difficulty:** 5-6/10

**Instructions:**
- Work in `practice.py` for experimentation
- Paste your FINAL solutions/answers below each task

---

## Task 1: PCAP Warm-up - Access Control Conventions

Answer these questions about Python's naming conventions:

**Q1:** What happens when you try to access `obj.__secret` from outside the class?

**Q2:** What does Python transform `__name` to inside a class called `MyClass`?

**Q3:** True or False: A single underscore `_name` prevents access to an attribute.

**Q4:** Which is the correct way to make an attribute "protected" by convention?
- A) `self.protected_name`
- B) `self._protected_name`
- C) `self.__protected_name`
- D) `self.protected_name_`

**Your answers:**
```
Q1: You will not be able to do so, as the name is mangled.

Q2: _MyClass__name

Q3: False - it's just a convention that it shouldn't be accessed

Q4: B -> only protected by convention, C -> actual name mangling (quasi-private, still accessible if you know the mangling rule)

```

---

## Task 2: PCAP Drill - Predict the Output (Name Mangling)

Predict the output WITHOUT running the code:

```python
class Secret:
    def __init__(self):
        self._protected = "visible"
        self.__private = "hidden"

    def reveal(self):
        return self.__private

s = Secret()
print(s._protected)
print(s.reveal())
print(hasattr(s, '__private'))
print(hasattr(s, '_Secret__private'))
```

**Your prediction:**
```
# Output (4 lines):
print(s._protected) #visible
print(s.reveal()) #hidden
print(hasattr(s, '__private')) #False
print(hasattr(s, '_Secret__private')) #True



# Explanation:
_name is only a convention.
__name does the quasi-protection, which the name mangling to _Class__name, so it's not accessible under __name, but accessible if you know the mangling rules.

```

---

## Task 3: PCAP Drill - @property Basics

Predict the output WITHOUT running:

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

t = Temperature(25)
print(t.celsius)
print(t.fahrenheit)
t.celsius = 30  # What happens here?
```

**Your prediction:**
```
# Output:
print(t.celsius) #25
print(t.fahrenheit) # 77
t.celsius = 30  # What happens here? Error - there's no such attribute as 'celsius' in the Temperature class.


# What happens on the last line?
We're trying to access the celsius class attribute, but it isn't there.
There's only _celsius, so we'd have to do t._celsius (but it's NOT RECOMMENDED, as it's obviously 'protected' by the convention)

As an alternative, we could establish a setter there and it WOULD work.
```

---

## Task 4: Code Implementation - Property with Setter

Create a `Price` class that:
1. Has a protected `_value` attribute
2. Has a `value` property (getter)
3. Has a `value` setter that validates: value must be >= 0
4. Raises `ValueError` with message "Price cannot be negative" if validation fails

**Your code:**
```python
class Price:
    # Your implementation here
    pass


# Test it:
p = Price(100)
print(p.value)      # Should print: 100
p.value = 150       # Should work
print(p.value)      # Should print: 150
p.value = -10       # Should raise ValueError
```

class Price:
    '''A mock docstring of a mock class used for practice'''
    
    def __init__(self, value: float):
        self._value = value
    
    @property
    def value(self) -> float:
        return self._value
    
    @value.setter
    def value(self, value: float) -> None:
        if value >= 0:
            self._value = value
        else:
            raise ValueError('Price cannot be negative!')



---

## Task 5: PROJECT - Trade Class Foundation

Create a basic `Trade` class in `algo_backtest/engine/trade.py`:

**Requirements:**
1. Constructor parameters: `ticker`, `side`, `entry_price`, `exit_price`, `quantity`
2. Store all as protected attributes (`_ticker`, etc.)
3. `side` should be stored as uppercase
4. Add a `pnl` property that calculates profit/loss:
   - BUY: `(exit_price - entry_price) * quantity`
   - SELL: `(entry_price - exit_price) * quantity`
5. Add an `is_winner` property that returns `True` if `pnl > 0`
6. Add `__str__` method: `"BUY AAPL: +150.00 (WIN)"` or `"SELL AAPL: -50.00 (LOSS)"`

**Paste your code below:**
```python
# algo_backtest/engine/trade.py



```

**Test your Trade class:**
```python
# In practice.py - paste your test code and output
from algo_backtest.engine.trade import Trade

# Create a winning BUY trade
t1 = Trade("AAPL", "buy", 100.0, 110.0, 10)
print(t1)           # Should show: BUY AAPL: +100.00 (WIN)
print(t1.pnl)       # Should show: 100.0
print(t1.is_winner) # Should show: True

# Create a losing SELL trade
t2 = Trade("TSLA", "sell", 200.0, 220.0, 5)
print(t2)           # Should show: SELL TSLA: -100.00 (LOSS)
```



"""Trade management for completed positions."""
from typing import Optional

class Trade:
    '''
    Represents a completed trade
    
    Attributes:
        ticker: Trading symbol.
        side: 'BUY' or 'SELL'.
        entry_price: Entry price.
        exit_price: Exit price.
        quantity: Number of units.
        entry_time: Entry timestamp (string or datetime).
        exit_time: Exit timestamp (string or datetime).
        pnl: Profit/Loss (calculated automatically).
        exit_reason: 'SL', 'TP', or 'MANUAL'.
    '''
    
    def __init__(self,
                 ticker: str,
                 side: str,
                 entry_price: float,
                 exit_price: float,
                 quantity: float,
                 entry_time: Optional[str] = None,
                 exit_time: Optional[str] = None,
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
        
        if exit_reason is not None:
            self._exit_reason = exit_reason.upper()
        else:
            self._exit_reason = ''

        #Properties - is_winner + pnl
        self.__pnl: Optional[float] = None
        self.__is_winner: Optional[bool] = None
        
    def __str__(self):
        """
        User-friendly representation.

        Format: [WIN/LOSS] SIDE QUANTITY TICKER: ENTRY -> EXIT (REASON) | P&L: $X.XX
        Example: [WIN] BUY 10000 EURUSD: 1.0800 -> 1.0850 (TP) | P&L: $500.00
        """
        
        if self.is_winner == True:
            result = '[WIN]'
        else:
            result = '[LOSS]'
        
        return (f'''{result} {self._side} {self._quantity} {self._ticker}: 
                {self._entry_price} -> {self._exit_price} {self._exit_reason}
                | P&L: ${self.pnl:.2f}''')
    
    def __repr__(self):
        
        
        return (f'Trade(ticker = {self._ticker!r}, side = {self._side!r},'
                f'entry_price = {self._entry_price}, exit_price = {self._exit_price}'
                f'quantity = {self._quantity}, pnl = {self.pnl:.2f}, exit_reason = {self._exit_reason!r}'
        )
    
    
    @property
    def pnl(self) -> float:
        '''
        Calculate profit/loss based on side.

        Returns:
            P&L in currency units.
        '''
        if self._side != 'BUY' and self._side != 'SELL':
            print('Incorrect side, it should be either BUY or SELL (case insensitive)')
            return None
        elif self._exit_price < 0 or self._entry_price < 0:
            print('Incorrect exit price or entry price, it should be above 0!')
            return None
        
        if self._side == 'BUY':
            self.__pnl = (self._exit_price - self._entry_price) * self._quantity
            return self.__pnl
        elif self._side == 'SELL':
            self.__pnl = (self._entry_price - self._exit_price) * self._quantity
            return self.__pnl
        
    @property 
    def is_winner(self) -> bool:
        """A property created to check if trade was profitable."""
        if self.pnl > 0:
            self.__is_winner = True
        else:
            self.__is_winner = False
            
        return self.__is_winner
        
    
    @classmethod
    def calculate_win_rate(cls, trades: list['Trade']) -> float:
        """
        Calculate win rate from list of trades.

        Args:
            trades: List of Trade objects.

        Returns:
            Win rate as percentage (0-100).
            Returns 0 if no trades.
        """

        if trades is not None:
            trades_profits = [trade.pnl() for trade in trades]
            winners = [profit for profit in trades_profits if profit > 0]
            print(trades_profits)
            return (len(winners) / len(trades_profits)) * 100
            
        else:
            return 0


#test_log:
$ python practice.py
[WIN] BUY 10 AAPL: 
                100.0 -> 110.0
                | P&L: $100.00
100.0
True
[LOSS] SELL 5 TSLA:
                200.0 -> 220.0
                | P&L: $-100.00
(.venv) 


---

## Task 6: PCAP Drill - Property Edge Cases

What is the output of this code?

```python
class Counter:
    def __init__(self):
        self._count = 0

    @property
    def count(self):
        self._count += 1
        return self._count

c = Counter()
print(c.count)
print(c.count)
print(c.count)
```

**Your prediction:**
```
# Output (3 lines):

print(c.count) #1
print(c.count) #2
print(c.count) #3

# Why does this happen?

#Each time we call the property it is recalculated and we're given the latest value, simple as that.


```

---

## Task 7: PCAP Multiple Choice

**Question 1:** What is the purpose of name mangling (`__name`)?

A) To make attributes completely inaccessible
B) To encrypt attribute values
C) To prevent accidental name collisions in subclasses
D) To improve performance

**Your answer:**
B


---

**Question 2:** What error is raised when you try to set a property that has no setter?

A) `TypeError`
B) `AttributeError`
C) `ValueError`
D) `NameError`

**Your answer:**
B


---

**Question 3:** Which statement is TRUE about `@property`?

A) Properties must always have a setter
B) Properties are accessed with parentheses like methods
C) Properties can be used to create read-only attributes
D) Properties cannot access other instance attributes

**Your answer:**
C


---

**Question 4:** What does `hasattr(obj, '_Class__attr')` check?

A) If the class has a protected attribute
B) If the class has a private attribute (name-mangled form)
C) If the object has a static attribute
D) If the attribute is callable

**Your answer:**
B


---

## Task 8: Integration - Position and Trade Together

Write a short script that:
1. Creates a Position using `calculate_position_size` (from Week 2)
2. Simulates that the trade hit take profit
3. Creates a Trade object from the Position data
4. Prints both the Position and the Trade

**Scenario:**
- Account: $10,000, Risk: 2%
- Entry: $50, Stop Loss: $48, Take Profit: $55
- Result: Price hit TP at $55

**Your code:**
```python
# Your integration script

from typing import Optional
from algo_backtest.engine.position import Position
from algo_backtest.engine.trade import Trade


class PositionTrade:
    '''My practice class which integrates both Position and Trade classes
    
       Mainly done for practice purposes for now, but we will see.
    '''
    
    def __init__(self,
    acc_size: float,
    risk_percent: float,
    entry_price: float,
    asset_name: str,
    position_side: str,
    sl: Optional[float] = None,
    tp: Optional[float] = None,
    ):
        self.acc_size = acc_size
        self.risk_percent = risk_percent
        self.entry_price = entry_price
        self.asset_name = asset_name
        self.position_side = position_side
        
        self.sl = sl
        self.tp = tp
        
        self.position = None
        self.trade = None
        

    def create_trade(self):
        
        '''A method used to integrate the Position class and create an instance of an active position'''

        try:
            self.position_size = Position.calculate_position_size(self.acc_size, self.risk_percent, self.entry_price, self.sl)
            self.position = Position(self.asset_name, self.position_side, self.entry_price, self.position_size, self.sl, self.tp)
            
        except Exception as e:
            print(f'Unexpected error: {str(e)}')
            
    def check_trade(self, price):
        
        '''A method used to check if the position should close and IF IT SHOULD, we integrate the Trade class'''
        
        if self.position is not None and price > 0:
            check, reason = self.position.should_close(price)
            if check is True:
                print('Time to close the position!')
                self.trade = Trade(self.asset_name, self.position_side, self.entry_price, price, self.position_size, None, None, reason)
                
                print(self.trade)
                print(self.position)
            else:
                print('Position still open')
        else:
            print('There is no position or the given price is below 0')
            
            

x = PositionTrade(10000, 2, 50, 'DAX', 'Buy', 48, 55)
x.create_trade()
x.check_trade(55)



That was a lengthy one and while I started with a simple function, at some point I thought I'd need a class for hte most optimal flow here. Sure, I could hardcode some things or simply do things manually, but this flow allows us to simply enter parameters once and call them with create_trade and check_trade. Anyway, I'm looking forward to your feedback

Log:

$ python practice.py
Time to close the position!
[WIN] BUY 100.0 DAX: 
                50 -> 55 BUY TP HIT
                | P&L: $500.00
BUY 100.0 @ 50 [SL = 48, TP = 55]



```

---

## Feedback Section

**Time spent:** 120 minutes

**Difficulty (1-10):**

**What clicked:**


**What's confusing:**


**Questions:**

