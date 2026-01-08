# Week 1, Day 4 - Magic Methods & Pandas Essentials

**Date:** 2026-01-08
**Topic:** `__str__`, `__repr__`, and Essential Pandas Operations
**Target:** 8 Tasks Completed
**Rules:** PCAP Drills = Pure Python (no external libraries). Project Tasks = Pandas/NumPy allowed.

**IMPORTANT:** Read [lessons/week1_magic_methods_pandas.md](lessons/week1_magic_methods_pandas.md) BEFORE starting these tasks!

---

## Task 1: PCAP Warm-up - `__str__` vs `__repr__` (Pure Python)

**Predict the output** of this code:

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price})"

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"

product = Product("Laptop", 999.99)

print(str(product))
print(repr(product))
print(product)
```

**Your predictions:**
1. `str(product)` → `Laptop: $999.99`
2. `repr(product)` → `Product(name = 'Laptop'), price = 999.99`
3. `print(product)` → `Laptop: $999.99`

**Question:** What happens if you remove `__str__` but keep `__repr__`? What will `print(product)` output?

**Answer here:**
It will print the repr printout instead, same as str(product), which is quite interesting.


---

## Task 2: PCAP Warm-up - Magic Method Trap (Pure Python)

**Find the bug** in this code:

```python
class Counter:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        print(f"Counter: {self.value}")

counter = Counter(10)
result = str(counter)
print(f"Result: {result}")
```

**Questions:**
1. What will this code print?
2. What's the bug?
3. Fix the code

**Answer here:**
Nothing, it will return a TypeError, as there's no return statement.
It should be:

return f"Counter: {self.value}"


---

## Task 3: Theory Drill - Add Magic Methods to Position Class (Pure Python)

Update your `Position` class in `algo_backtest/engine/position.py` to include proper `__str__` and `__repr__` methods.

**Requirements:**

**`__repr__`** should return a string that could recreate the object:
```python
Position(ticker='EURUSD', side='BUY', entry_price=1.085, quantity=10000, stop_loss=1.08, take_profit=1.095)
```

**`__str__`** should return a user-friendly trading format:
```python
BUY 10000 EURUSD @ 1.0850 [SL=1.0800, TP=1.0950]
```

**Special cases for `__str__`:**
- If `stop_loss` is `None`, show "No SL" instead of "SL=None"
- If `take_profit` is `None`, show "No TP" instead of "TP=None"
- Format prices to 4 decimal places (`.4f`)

**Test your code:**
```python
from algo_backtest.engine.position import Position

pos = Position("EURUSD", "BUY", 1.0850, 10000, stop_loss=1.0800, take_profit=1.0950)
print(repr(pos))  # Should show Position(ticker='EURUSD', ...)
print(str(pos))   # Should show BUY 10000 EURUSD @ 1.0850 [SL=1.0800, TP=1.0950]
print(pos)        # Should use __str__

pos_no_sl = Position("GBPUSD", "SELL", 1.2500, 5000)
print(pos_no_sl)  # Should show SELL 5000 GBPUSD @ 1.2500 [No SL, No TP]
```

**Paste your two magic methods here:**

    def __str__(self) -> str:
        '''A Python magic method used to return information about class instead of memory object'''
        return f'{self.side} {self.quantity} @ {self.entry_price} [SL = {self.stop_loss}, TP = {self.take_profit}]'
    
    
    def __repr__(self) -> str:
        '''A Python magic method used to provide devs with useful information to recreate the object '''
        return f'{__name__}(ticker = {self.ticker}, side = {self.side}, entry_price = {self.entry_price}, quantity = {self.quantity}, stop_loss = {self.stop_loss}, take_profit = {self.take_profit})'


I've tried to use Optional for my SL/TP, but it didn't really worked and I've got a TypeError: Cannot instantiate typing.Optional.

Anyway, the current application seems to work perfectly fine and I don't think there are major updates necessary, LOG BELOW:

$ python practice.py
algo_backtest.engine.position(ticker = EURUSD, side = BUY, entry_price = 1.085, quantity = 10000, stop_loss = 1.08, take_profit = 1.095)
BUY 10000 @ 1.085 [SL = 1.08, TP = 1.095]
BUY 10000 @ 1.085 [SL = 1.08, TP = 1.095]
SELL 5000 @ 1.25 [SL = None, TP = None]

---

## Task 4: Pandas Drill - Understanding `.any()` (Pandas Allowed)

Now that you've learned Pandas properly, let's fix the Task 6 issue from Day 3.

**Given this code:**
```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'ticker': ['EURUSD', 'GBPUSD', 'USDJPY'],
    'open': [1.08, 1.25, np.nan],
    'close': [1.09, np.nan, 110.5],
    'volume': [1000, 1500, 2000]
})

# Task: Check if DataFrame has ANY NaN values
# Write THREE different correct ways to do this:
```

**Your three solutions:**

**Solution 1 (using `.sum().sum()`):**
```python
# Your code here

check_nan1 = df.isna().sum().sum()
print(check_nan1)

#As an output, we simply get 2, as the total sum of NaN values

```

**Solution 2 (using `.any().any()`):**
```python
# Your code here

check_nan2 = df.isna().any().any() #returns True
print(check_nan2)

#As a result, we get TRUE if there are any NaN values.
```

**Solution 3 (using `.sum()` with comparison):**
```python
# Your code here

check_nan3 = df.isna().sum()
print(check_nan3)

As a result, we see a nice breakdown of all the columns and the number of NaN values with each one - this is probably hte most informative output.

```

**Question:** Why was `if nan_values.any() > 0:` wrong in Day 3 Task 6?

**Answer here:**

As any() returns True or False, which obviously can't be compared with any numerical values.

---

## Task 5: Pandas Drill - Boolean Indexing (Pandas Allowed)

Given this DataFrame:

```python
import pandas as pd

df = pd.DataFrame({
    'timestamp': ['2024-01-01 09:00', '2024-01-01 09:01', '2024-01-01 09:02', '2024-01-01 09:03'],
    'ticker': ['EURUSD', 'EURUSD', 'EURUSD', 'EURUSD'],
    'open': [1.0800, 1.0820, 1.0850, 1.0830],
    'high': [1.0850, 1.0870, 1.0900, 1.0880],
    'low': [1.0790, 1.0810, 1.0840, 1.0820],
    'close': [1.0820, 1.0850, 1.0830, 1.0850],
    'volume': [1000, 1500, 2000, 1200]
})
```

**Write code to:**

1. Filter rows where `close > open` (bullish candles)
2. Filter rows where `volume > 1200` AND `close > 1.0840`
3. Get the `high` values (as a Series) where `close > open`
4. Count how many candles are bullish (close > open)

**Paste your solutions here:**


bullish_candles = df[df['close'] > df['open']]
filtered_rows = df[(df['volume'] > 1200) & (df['close'] > 1.0840)]
high_series = pd.Series(df['high'][df['close'] > df['open']])
bullish_candles_count = len(df[df['close'] > df['open']])

---

## Task 6: PROJECT TASK - Create Trade Class (Pure Python + Type Hints)

Create a `Trade` class to represent a completed trade (closed position).

**File:** Create `algo_backtest/engine/trade.py`

**Requirements:**
```python
"""Trade management for completed positions."""

from typing import Optional
from datetime import datetime


class Trade:
    """
    Represents a completed trade.

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
    """

    def __init__(
        self,
        ticker: str,
        side: str,
        entry_price: float,
        exit_price: float,
        quantity: float,
        entry_time: str,
        exit_time: str,
        exit_reason: str = 'MANUAL'
    ) -> None:
        """Initialize a completed trade and calculate P&L."""
        self.ticker = ticker
        self.side = side.upper()
        self.entry_price = entry_price
        self.exit_price = exit_price
        self.quantity = quantity
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.exit_reason = exit_reason.upper()

        # Calculate P&L automatically
        self.pnl = self._calculate_pnl()

    def _calculate_pnl(self) -> float:
        """
        Calculate profit/loss based on side.

        Returns:
            P&L in currency units.
        """
        # Your code here
        # Hint: Same logic as Position.calculate_pnl()
        pass

    def is_winner(self) -> bool:
        """Check if trade was profitable."""
        # Your code here
        pass

    def __repr__(self) -> str:
        """Unambiguous representation."""
        return (
            f"Trade(ticker={self.ticker!r}, side={self.side!r}, "
            f"entry_price={self.entry_price}, exit_price={self.exit_price}, "
            f"quantity={self.quantity}, pnl={self.pnl:.2f}, exit_reason={self.exit_reason!r})"
        )

    def __str__(self) -> str:
        """
        User-friendly representation.

        Format: [WIN/LOSS] SIDE QUANTITY TICKER: ENTRY -> EXIT (REASON) | P&L: $X.XX
        Example: [WIN] BUY 10000 EURUSD: 1.0800 -> 1.0850 (TP) | P&L: $500.00
        """
        # Your code here
        # Hint: Use [WIN] if is_winner(), else [LOSS]
        # Format prices to 4 decimals, P&L to 2 decimals
        pass
```

**Test your code:**
```python
from algo_backtest.engine.trade import Trade

# Winning BUY trade
trade1 = Trade(
    ticker="EURUSD",
    side="BUY",
    entry_price=1.0800,
    exit_price=1.0850,
    quantity=10000,
    entry_time="2024-01-01 09:00",
    exit_time="2024-01-01 09:30",
    exit_reason="TP"
)

print(trade1)
# Expected: [WIN] BUY 10000 EURUSD: 1.0800 -> 1.0850 (TP) | P&L: $500.00

# Losing SELL trade
trade2 = Trade(
    ticker="GBPUSD",
    side="SELL",
    entry_price=1.2500,
    exit_price=1.2550,
    quantity=5000,
    entry_time="2024-01-01 10:00",
    exit_time="2024-01-01 10:15",
    exit_reason="SL"
)

print(trade2)
# Expected: [LOSS] SELL 5000 GBPUSD: 1.2500 -> 1.2550 (SL) | P&L: $-250.00
```

**Paste your Trade class here:**



"""Trade management for completed positions."""

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
                 entry_time: str,
                 exit_time: str,
                 exit_reason: str) -> None:
        
        """Initialize a completed trade and calculate P&L."""
        
        self.ticker = ticker
        self.side = side.upper()
        self.entry_price = entry_price
        self.exit_price = exit_price
        self.quantity = quantity
        self.entry_time = entry_time
        self.exit_time = exit_time
        self.exit_reason = exit_reason.upper()

        # Calculate P&L automatically
        self.pnl = self._calculate_pnl()
        
    def __str__(self):
        """
        User-friendly representation.

        Format: [WIN/LOSS] SIDE QUANTITY TICKER: ENTRY -> EXIT (REASON) | P&L: $X.XX
        Example: [WIN] BUY 10000 EURUSD: 1.0800 -> 1.0850 (TP) | P&L: $500.00
        """
        
        if self.is_winner() == True:
            result = '[WIN]'
        else:
            result = '[LOSS]'
            
        return (f'''{result} {self.side} {self.quantity} {self.ticker}: 
                {self.entry_price} -> {self.exit_price} ({self.exit_reason}) 
                | P&L: ${self.pnl:.2f}''')
    
    def __repr__(self):
        """Unambiguous representation."""
        
        return (f'Trade(ticker = {self.ticker!r}, side = {self.side!r},'
                f'entry_price = {self.entry_price}, exit_price = {self.exit_price}'
                f'quantity = {self.quantity}, pnl = {self.pnl:.2f}, exit_reason = {self.exit_reason!r}'
        )
    
    def _calculate_pnl(self) -> float:
        """
        Calculate profit/loss based on side.

        Returns:
            P&L in currency units.
        """

        if self.side != 'BUY' and self.side != 'SELL':
            print('Incorrect side, it should be either BUY or SELL (case insensitive)')
            return None
        elif self.exit_price < 0 or self.entry_price < 0:
            print('Incorrect exit price or entry price, it should be above 0!')
            return None
        
        if self.side == 'BUY':
            pnl = (self.exit_price - self.entry_price) * self.quantity
            return pnl
        elif self.side == 'SELL':
            pnl = (self.entry_price - self.exit_price) * self.quantity
            return pnl
        
        
    def is_winner(self) -> bool:
        """Check if trade was profitable."""
        if self.pnl > 0:
            return True
        else:
            return False
        
        

#LOG:

[WIN] BUY 10000 EURUSD: 
                1.08 -> 1.085 (TP)
                | P&L: $50.00
[LOSS] SELL 5000 GBPUSD:
                1.25 -> 1.255 (SL)
                | P&L: $-25.00
(.venv) 

And please note, these are the correct P&L calculations for the quantities you've given.
---

## Task 7: PCAP Simulation - Multiple Choice

**Question 1:**
What is the output of this code?

```python
class Account:
    def __repr__(self):
        return "Account"

    def __str__(self):
        return "My Account"

acc = Account()
print(acc)
print(repr(acc))
```

**Choices:**
A) `My Account` then `My Account`
B) `Account` then `Account`
C) `My Account` then `Account`
D) `Account` then `My Account`

**Your answer with explanation:**
C, as for default print, we use __str__ when available, and then we specifically ask for repr so we get the repr output.

---

**Question 2:**
What happens when you run this code?

```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3]})
result = df['a'] > 2 and df['a'] < 5
```

**Choices:**
A) Works fine, `result` is `[False, False, True]`
B) `ValueError: The truth value of a Series is ambiguous`
C) `TypeError: cannot use and with Series`
D) `KeyError: 'a'`

**Your answer with explanation:**
C, TYPE ERROR!
result = df[(df['a'] > 2) & (df['a'] < 5)] #correct application


---

## Task 8: Integration Challenge - DataLoader Enhancement (Pandas Allowed)

Update your `DataLoader` class in `algo_backtest/data/data_loader.py` to include:

1. **Add `__repr__` method:**
   ```python
   DataLoader(filepath='ohlc_mock_data.csv')
   ```

2. **Add a new method `get_candle_count()`:**
   ```python
   def get_candle_count(self) -> int:
       """
       Return total number of candles in loaded data.

       Returns:
           Number of rows in DataFrame, or 0 if data not loaded.
       """
       pass
   ```

3. **Add a new method `get_bullish_candles()`:**
   ```python
   def get_bullish_candles(self, data: pd.DataFrame) -> pd.DataFrame:
       """
       Return only bullish candles (close > open).

       Args:
           data: OHLC DataFrame.

       Returns:
           Filtered DataFrame with only bullish candles.
       """
       pass
   ```

**Test your code:**
```python
from algo_backtest.data.data_loader import DataLoader

loader = DataLoader('ohlc_mock_data.csv')
print(repr(loader))  # DataLoader(filepath='ohlc_mock_data.csv')

data = loader.load_data()
if data is not None:
    print(f"Total candles: {loader.get_candle_count()}")

    bullish = loader.get_bullish_candles(data)
    print(f"Bullish candles: {len(bullish)}")
```

**Paste your updated methods here:**

    def __repr__(self):
        '''
        Unambiguous representation
        '''
        return f'DataLoader(filepath = {self.filepath})'


    def get_candle_count(self) -> int:
       """
       Return total number of candles in loaded data.

       Returns:
           Number of rows in DataFrame, or 0 if data not loaded.
       """
       
       data = self.load_data()
       
       if data is not None:
           return len(data)
       else:
           return 0
        
        
    def get_bullish_candles(self, data: pd.DataFrame) -> pd.DataFrame:
       """
       Return only bullish candles (close > open).

       Args:
           data: OHLC DataFrame.

       Returns:
           Filtered DataFrame with only bullish candles.
       """
       
       bullish_candles = data[data['close'] > data['open']]
       return bullish_candles
    
    




---

## Bonus Challenge (Optional): Trade Statistics

Add a **class method** to the `Trade` class that calculates win rate from a list of trades.

```python
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
    # Your code here
    # Hint: Count winners, divide by total, multiply by 100
    pass
```

**Usage:**
```python
from algo_backtest.engine.trade import Trade

trade1 = Trade("EURUSD", "BUY", 1.08, 1.09, 10000, "2024-01-01 09:00", "2024-01-01 09:30", "TP")
trade2 = Trade("GBPUSD", "SELL", 1.25, 1.26, 5000, "2024-01-01 10:00", "2024-01-01 10:15", "SL")
trade3 = Trade("USDJPY", "BUY", 110.00, 110.50, 2000, "2024-01-01 11:00", "2024-01-01 11:45", "TP")

trades = [trade1, trade2, trade3]
win_rate = Trade.calculate_win_rate(trades)
print(f"Win rate: {win_rate:.1f}%")  # Expected: 66.7%
```

**Paste your class method here:**


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
            trades_profits = [trade._calculate_pnl() for trade in trades]
            winners = [profit for profit in trades_profits if profit > 0]
            print(trades_profits)
            return (len(winners) / len(trades_profits)) * 100
            
        else:
            return 0

It was a bit unintuitive for me, but I worked it out with some tests

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
Tomorrow (Day 5) is Friday! We'll wrap up Week 1 with a comprehensive review, generate TWO mock PCAP exams for the weekend, and polish the project structure. Great work this week! 🎉
