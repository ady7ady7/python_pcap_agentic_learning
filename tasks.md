# Week 1, Day 5 - Week 1 Review & Integration

**Date:** 2026-01-09
**Topic:** Week 1 Wrap-up - Comprehensive Review & Project Polish
**Target:** 8 Tasks Completed
**Rules:** Mix of Pure Python (PCAP prep) and Project Tasks (Pandas/NumPy allowed)

**IMPORTANT:** This is Friday - Week 1 final day! Focus on integration, review, and preparing for weekend mock exams.

---

## Task 1: Week 1 Concepts Review - Quick Fire (Pure Python)

**Answer these short questions to test your Week 1 retention:**

1. What's the difference between `import math` and `from math import sqrt`?
2. What does `"PCAP"[10:20]` return? (No IndexError!)
3. In exception handling, why must specific exceptions come before general ones?
4. What's the difference between an instance attribute and a class attribute?
5. When does Python call `__repr__` vs `__str__`?
6. What operator do you use for multiple conditions in Pandas filtering? (`and`/`or` or `&`/`|`?)

**Your answers:**

1. Two differences - in the first example we import all the relevant functions from math that are set to be imported there by default if we use this general import (this is also the best practice, as we're not occupying the namespace), but to use them we have to call math.module_name; In the second example we only import the sqrt function and we can call it by naming it sqrt. It's not the best practice as we're also occupying the namespace and may cause naming conflicts, especially if our codebase is large and we import a lot of functions like that.
2. Empty string
3. Because otherwise we would always catch the general exception catch, and it would block the other exception handling cases (so effectively, they would be pointless)
4. Instance attribute is tied to a given instance of a class, while a class attribute is shared among all instances of a given class.
5. It calls __str__ by default if it's available and if we do print(class_name); __repr__ would be called instead if __str__ is not available. We can also simply explicitly call both methods as in print(repr(class_name)) or print(str(class_name))
6. If we compare single elements we use and/or, and for series we use & / | instead, so in this case the answer is `&`/`|`.

---

## Task 2: Integration Challenge - Complete Backtest Workflow (Pure Python + Pandas)

Create a simple end-to-end backtest simulation that ties together all Week 1 concepts.

**File:** Create `algo_backtest/main.py`

**Requirements:**
```python
"""
Main entry point for AlgoBacktest engine.
Demonstrates complete workflow: Load data → Simulate trades → Calculate statistics.
"""

from algo_backtest.data.data_loader import DataLoader
from algo_backtest.engine.position import Position
from algo_backtest.engine.trade import Trade


def run_simple_backtest() -> None:
    """
    Run a simple backtest:
    1. Load OHLC data
    2. Simulate 3 manual trades (you choose entry/exit points from data)
    3. Print each trade with magic methods
    4. Calculate and display win rate
    """

    print("=== AlgoBacktest Core - Week 1 Demo ===\n")

    # Step 1: Load data
    loader = DataLoader('ohlc_mock_data.csv')
    print(f"Loader: {repr(loader)}")

    data = loader.load_data()
    if data is None:
        print("Failed to load data!")
        return

    print(f"Loaded {len(data)} candles\n")

    # Step 2: Create sample trades (pick 3 trades from your data)
    # Example: BUY at row 5's open, exit at row 10's close
    # You choose the indices based on your ohlc_mock_data.csv

    trades = []

    # Trade 1: Your choice (BUY)
    # Hint: data.iloc[index]['column_name'] to access specific values
    # Your code here

    # Trade 2: Your choice (SELL)
    # Your code here

    # Trade 3: Your choice (BUY)
    # Your code here

    # Step 3: Print trades
    print("=== Trade Results ===")
    for i, trade in enumerate(trades, 1):
        print(f"{i}. {trade}")  # Uses __str__

    print()

    # Step 4: Calculate statistics
    win_rate = Trade.calculate_win_rate(trades)
    total_pnl = sum(trade.pnl for trade in trades)

    print(f"=== Statistics ===")
    print(f"Total Trades: {len(trades)}")
    print(f"Win Rate: {win_rate:.1f}%")
    print(f"Total P&L: ${total_pnl:.2f}")


if __name__ == "__main__":
    run_simple_backtest()
```

**Test your code:**
```bash
python algo_backtest/main.py
```

**Paste your completed `main.py` here (including the 3 trade creations):**


import sys
from __init__ import __version__
import check_dependencies

from engine.trade import Trade
from data.data_loader import DataLoader


def run_simple_backtest() -> None:
    """
    Run a simple backtest:
    1. Load OHLC data
    2. Simulate 3 manual trades (you choose entry/exit points from data)
    3. Print each trade with magic methods
    4. Calculate and display win rate
    """

    print("=== AlgoBacktest Core - Week 1 Demo ===\n")

    # Step 1: Load data
    loader = DataLoader('ohlc_mock_data.csv')
    print(f"Loader: {repr(loader)}")

    data = loader.load_data()
    if data is None:
        print("Failed to load data!")
        return

    print(f"Loaded {len(data)} candles\n")

    # Step 2: Create sample trades (pick 3 trades from your data)
    # Example: BUY at row 5's open, exit at row 10's close
    # You choose the indices based on your ohlc_mock_data.csv

    trades = []
    trade1 = Trade(data.iloc[24]['ticker'], 
                  'BUY', 
                  data.iloc[24]['open'],
                  data.iloc[26]['close'],
                  10000,
                  data.iloc[24]['timestamp'],
                  data.iloc[26]['timestamp'],
                  ''
                  )
    
    trade2 = Trade(data.iloc[28]['ticker'], 
                  'SELL', 
                  data.iloc[28]['open'],
                  data.iloc[29]['close'],
                  10000,
                  data.iloc[28]['timestamp'],
                  data.iloc[30]['timestamp'],
                  ''
                  )
    
    trade3 = Trade(data.iloc[14]['ticker'], 
                  'BUY', 
                  data.iloc[14]['open'],
                  data.iloc[24]['close'],
                  10000,
                  data.iloc[14]['timestamp'],
                  data.iloc[25]['timestamp'],
                  ''
                  )
    
    trades = [trade1, trade2, trade3]
    # Trade 1: Your choice (BUY)
    # Hint: data.iloc[index]['column_name'] to access specific values

    print("=== Trade Results ===")
    for i, trade in enumerate(trades, 1):
        print(f"{i}. {trade}")  # Uses __str__


    # Step 4: Calculate statistics
    win_rate = Trade.calculate_win_rate(trades)
    total_pnl = sum(trade.pnl for trade in trades)
 

    print(f"=== Statistics ===")
    print(f"Total Trades: {len(trades)}")
    print(f"Win Rate: {win_rate:.1f}%")
    print(f"Total P&L: ${total_pnl:.2f}")



if __name__ == '__main__':
    check_dependencies.check_deps()
    print(f'Current version: {__version__}')
    print('AlgoBacktest Core - Ready')
    run_simple_backtest()

---

## Task 3: PCAP Trap - Mixed Concepts (Pure Python)

**Predict the output** of this code:

```python
class Portfolio:
    total_portfolios = 0

    def __init__(self, name):
        self.name = name
        Portfolio.total_portfolios += 1

    def __str__(self):
        return f"Portfolio: {self.name}"

    def __repr__(self):
        return f"Portfolio({self.name!r})"

p1 = Portfolio("Tech Stocks")
p2 = Portfolio("Bonds")

print(p1)
print(repr(p2))
print(f"Total: {Portfolio.total_portfolios}")

portfolios = [p1, p2]
print(portfolios)
```

**Your predictions:**
- Line 1 (`print(p1)`): `Portfolio: Tech Stocks`
- Line 2 (`print(repr(p2))`): `Portfolio('Bonds')`
- Line 3 (`print(f"Total: ...")`): `Total: 2`
- Line 4 (`print(portfolios)`): `[Portfolio('Tech Stocks'), Portfolio('Bonds')]` (What format does list use for objects?)

**Answer here:**

Answered above.

---

## Task 4: Exception Handling Integration (Pure Python)

Write a function that safely executes a backtest with comprehensive error handling.

**Requirements:**
```python
"""Safe backtest execution with error handling."""

from typing import Optional, List
from algo_backtest.data.data_loader import DataLoader
from algo_backtest.engine.trade import Trade


def safe_backtest_runner(filepath: str) -> Optional[List[Trade]]:
    """
    Safely run backtest with error handling.

    Args:
        filepath: Path to OHLC data CSV.

    Returns:
        List of Trade objects if successful, None if any error occurs.

    Error Handling:
        - FileNotFoundError: Data file missing
        - ValueError: Invalid data format
        - KeyError: Missing required columns
        - Exception: Catch-all for unexpected errors
    """

    try:
        # Your code here:
        # 1. Load data with DataLoader
        # 2. Validate it has required columns: ['timestamp', 'ticker', 'open', 'close']
        # 3. Create at least 2 sample trades
        # 4. Return trades list
        pass

    except FileNotFoundError as e:
        # Your error handling here
        pass

    except ValueError as e:
        # Your error handling here
        pass

    except KeyError as e:
        # Your error handling here
        pass

    except Exception as e:
        # Your error handling here
        pass

    else:
        # Runs if NO exceptions occurred
        # Your code here
        pass

    finally:
        # Always runs (cleanup code)
        # Your code here
        pass
```

**Test cases:**
```python
# Test 1: Valid file
result = safe_backtest_runner('ohlc_mock_data.csv')
print(f"Valid file: {result is not None}")  # Should be True

# Test 2: Missing file
result = safe_backtest_runner('nonexistent.csv')
print(f"Missing file: {result is None}")  # Should be True
```

**Paste your completed function here:**


from typing import Optional, List
from algo_backtest.data.data_loader import DataLoader
from algo_backtest.engine.trade import Trade


def safe_backtest_runner(filepath: str) -> Optional[List[Trade]]:
    """
    Safely run backtest with error handling.

    Args:
        filepath: Path to OHLC data CSV.

    Returns:
        List of Trade objects if successful, None if any error occurs.

    Error Handling:
        - FileNotFoundError: Data file missing
        - ValueError: Invalid data format
        - KeyError: Missing required columns
        - Exception: Catch-all for unexpected errors
    """

    try:
        
        trades = []
        loader = DataLoader(filepath)
        data = loader.load_data()
        x = loader.validate_data(data)
        
        if x:
            trade1 = Trade(data.iloc[0]['ticker'],     #ticker
                           'BUY',                      #side     
                           data.iloc[15]['open'],      #entry_price
                           data.iloc[34]['close'],     #exit_price
                           15000,                      #quantity
                           data.iloc[15]['timestamp'], #entry_time
                           data.iloc[35]['timestamp'], #exit_time
                           '')                         #reason (nie wrzucam nic na razie)
            
            
            trade2 = Trade(data.iloc[0]['ticker'],     #jw.
                           'SELL',
                           data.iloc[18]['open'],
                           data.iloc[27]['close'],
                           15000,
                           data.iloc[18]['timestamp'],
                           data.iloc[28]['timestamp'],
                           '')
            trades = [trade1, trade2]

    except FileNotFoundError as e:
        print(f'File not found: {str(e)}')
        return None

    except ValueError as e:
        print(f'Wrong value: {str(e)}')
        return None

    except KeyError as e:
        print(f'Key not found: {str(e)}')
        return None
    
    except Exception as e:
        print(f'Unexpected error: {str(e)}')
        return None
    
    else:
        print('Trades added successfully, returning the list of trades.')
        return trades

    finally:
       print('Operation finished')

# Test 1: Valid file
result = safe_backtest_runner('ohlc_mock_data.csv')
print(f"Valid file: {result is not None}")  # Should be True

# Test 2: Missing file
result = safe_backtest_runner('nonexistent.csv')
print(f"Missing file: {result is None}")  # Should be True


---

## Task 5: Pandas Advanced Filtering (Pandas Allowed)

Using your `ohlc_mock_data.csv`, write code to answer these questions:

```python
import pandas as pd

data = pd.read_csv('ohlc_mock_data.csv')

# Question 1: What's the average close price for bullish candles only?
# Your code here

# Question 2: Find the candle with the highest volume
# Return the entire row as a Series
# Your code here

# Question 3: Calculate the total volume for candles where close > 100.5
# Your code here

# Question 4: Create a new column 'candle_type' with values 'bullish' or 'bearish'
# based on close vs open
# Your code here

# Question 5: Get all candles where high is in the top 10 highest values
# Hint: Use .nlargest()
# Your code here
```

**Paste your solutions here:**
<!-- 
import numpy as np
# Question 1: What's the average close price for bullish candles only?
# Your code here
avg_bullish_close = np.mean([data['close'][data['close'] > data['open']]])
print(avg_bullish_close)
# Question 2: Find the candle with the highest volume
# Return the entire row as a Series
# Your code here
highest_vol = np.max([data['volume']])
highest_vol_candle = data[data['volume'] == highest_vol]
print(highest_vol_candle)
# Question 3: Calculate the total volume for candles where close > 100.5
# Your code here

total_vol_candles = sum(data['volume'][data['close'] > 100.5])
print(total_vol_candles)

# Question 4: Create a new column 'candle_type' with values 'bullish' or 'bearish'
# based on close vs open
# Your code here
for index, row in data.iterrows():
    row['candle_type'] = 'bullish' if row['close'] > row['open'] else 'bearish'
    print(row)
#Here we iterate, creating a copy of each row, so we don't add anything to the original df

data['candle_type'] = data.apply(lambda row: 'bullish' if row['open'] > row['close'] else 'bearish',
                                         axis = 1)
print(data)

# Question 5: Get all candles where high is in the top 10 highest values
# Hint: Use .nlargest()
# Your code here
top_10_highs = data.nlargest(10, 'high')
print(top_10_highs) -->

---

## Task 6: PROJECT TASK - Position Manager Class (Pure Python)

Create a `PositionManager` class to manage multiple positions.

**File:** Create `algo_backtest/engine/position_manager.py`

**Requirements:**
```python
"""Position manager for handling multiple open positions."""

from typing import List, Optional
from algo_backtest.engine.position import Position


class PositionManager:
    """
    Manages multiple open positions.

    Attributes:
        positions: List of currently open Position objects.
    """

    def __init__(self) -> None:
        """Initialize empty position manager."""
        self.positions: List[Position] = []

    def add_position(self, position: Position) -> None:
        """
        Add a new position to the manager.

        Args:
            position: Position object to add.
        """
        # Your code here
        pass

    def get_total_pnl(self, current_price: float) -> float:
        """
        Calculate total unrealized P&L for all positions.

        Args:
            current_price: Current market price.

        Returns:
            Sum of all position P&Ls.
        """
        # Your code here
        # Hint: Sum position.calculate_pnl(current_price) for all positions
        pass

    def close_triggered_positions(self, current_price: float) -> List[Position]:
        """
        Check all positions for SL/TP triggers and remove them.

        Args:
            current_price: Current market price.

        Returns:
            List of positions that should be closed.
        """
        # Your code here
        # Hint: Use position.should_close(current_price)
        # Remove triggered positions from self.positions
        # Return list of closed positions
        pass

    def get_position_count(self) -> int:
        """Return number of open positions."""
        # Your code here
        pass

    def __repr__(self) -> str:
        """Return unambiguous representation."""
        return f"PositionManager(positions={len(self.positions)})"

    def __str__(self) -> str:
        """Return user-friendly representation."""
        if not self.positions:
            return "PositionManager: No open positions"
        return f"PositionManager: {len(self.positions)} open positions"
```

**Test your code:**
```python
from algo_backtest.engine.position_manager import PositionManager
from algo_backtest.engine.position import Position

manager = PositionManager()

# Add positions
pos1 = Position("EURUSD", "BUY", 1.0800, 10000, stop_loss=1.0750, take_profit=1.0900)
pos2 = Position("GBPUSD", "SELL", 1.2500, 5000, stop_loss=1.2550, take_profit=1.2450)

manager.add_position(pos1)
manager.add_position(pos2)

print(manager)  # PositionManager: 2 open positions

# Check P&L at current price
current_price = 1.0850
total_pnl = manager.get_total_pnl(current_price)
print(f"Total P&L: ${total_pnl:.2f}")

# Check for triggered positions
closed = manager.close_triggered_positions(1.0900)
print(f"Closed {len(closed)} positions")
print(manager)  # Should show 1 open position now
```

**Paste your PositionManager class here:**

from typing import List, Optional
from algo_backtest.engine.position import Position
from algo_backtest.engine.trade import Trade


class PositionManager:
    """
    Manages multiple open positions.

    Attributes:
        positions: List of currently open Position objects.
    """

    def __init__(self) -> None:
        """Initialize empty position manager."""
        self.positions: List[Position] = []

    def add_position(self, position: Position) -> None:
        """
        Add a new position to the manager.

        Args:
            position: Position object to add.
        """
        
        self.positions.append(position)
        print(f'Position {position} added successfully')
        

    def get_total_pnl(self, current_price: float) -> float:
        """
        Calculate total unrealized P&L for all positions.

        Args:
            current_price: Current market price.

        Returns:
            Sum of all position P&Ls.
        """
        
        total_pnl = sum([position.calculate_pnl(current_price) for position in self.positions])
        if total_pnl is not None:
            return f'The total P/L for all currently open positions is ${total_pnl:.2f}'
        else:
            return 0

    def close_triggered_positions(self, current_price: float) -> List[Position]:
        """
        Check all positions for SL/TP triggers and remove them.

        Args:
            current_price: Current market price.

        Returns:
            List of positions that should be closed.
        """
        closed_positions = []
        
        for position in self.positions:
            if position.should_close(current_price):
                closed_positions.append(position)
                self.positions.remove(position)

        return closed_positions
                

    def get_position_count(self) -> int:
        """Return number of open positions."""
        return len(self.positions)

    def __repr__(self) -> str:
        """Return unambiguous representation."""
        return f"PositionManager(positions={len(self.positions)})"

    def __str__(self) -> str:
        """Return user-friendly representation."""
        if not self.positions:
            return "PositionManager: No open positions"
        return f"PositionManager: {len(self.positions)} open positions"


---

## Task 7: PCAP Multiple Choice - Week 1 Concepts

**Question 1:**
What is the output?

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    result = 0
except Exception:
    result = -1
else:
    result = 1
finally:
    result = 2

print(result)
```

**Choices:**
A) `0`
B) `1`
C) `2`
D) `ZeroDivisionError`

**Your answer:**
C

---

**Question 2:**
What is the output?

```python
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
        self.count = Counter.count

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(c1.count, c2.count, Counter.count)
```

**Choices:**
A) `1 2 3`
B) `3 3 3`
C) `1 2 2`
D) `0 1 2`

**Your answer:**
A

---

**Question 3:**
What happens when you run this?

```python
import pandas as pd

df = pd.DataFrame({'a': [1, 2, 3]})
result = df[df['a'] > 1][df['a'] < 3]
```

**Choices:**
A) Works fine, returns row with value 2
B) `ValueError: Boolean Series key will be reindexed`
C) `KeyError: False`
D) `TypeError: cannot index with boolean Series`

**Your answer:**
It doesn't trigger an error, we get a weird row with value 2, so it's kind of answer A.
BUT also we get a UserWarning: Boolean Series key will be reindexed to match DataFrame index.  
Antyway, it doesn't seem like a good practice at all.


---

## Task 8: Code Review Challenge (Pure Python)

Review this code and identify **ALL issues** (aim for at least 5):

```python
"""Broken trading simulator - find all bugs!"""

class trade:
    def __init__(self, Ticker, side, entry, exit, qty):
        self.ticker = Ticker
        self.Side = side
        self.entry = entry
        self.exit = exit
        self.qty = qty

    def __str__(self):
        print(f"{self.Side} {self.ticker}")

    def calc_pnl(self):
        if self.Side == "BUY":
            return (self.exit - self.entry) * self.qty
        else:
            return (self.entry - self.exit) * self.qty

trades = []

import pandas as pd
df = pd.read_csv("data.csv")

for i in range(len(df)):
    row = df.iloc[i]
    t = trade(row['ticker'], 'BUY', row['open'], row['close'], 1000)
    trades.append(t)

total = 0
for t in trades:
    total = total + t.calc_pnl()

print(f"Total PNL: {total}")
```

**List all issues you find:**

# 1. uncapitalized class name - trade
# 2. capitalized parameter name - Ticker
# 3. capitalized self.Side 
# 4. it would be nice to also add .upper to side to account for potential case issues
# 5. weird __str__ representation with unclear information (missing data) AND an error - it uses print instead of return
# 6. wrong place to import pandas module
# 7. general lack of exception handling
# 8. wrong total_pnl calculation

**Rewrite the code fixing all issues:**


'''
Fixed trade simulator
'''

import pandas as pd

class Trade:
    def __init__(self, ticker, side, entry, exit, qty):
        '''init constructor for the Trade class'''
        self.ticker = ticker
        self.side = side.upper()
        self.entry = entry
        self.exit = exit
        self.qty = qty
        
    def __str__(self):
        '''A clear representation of a class if anybody decides to use print(Trade)'''
        return f"{self.side} {self.qty} {self.ticker} @ {self.entry}, EXIT @ {self.exit}"
    
    def calc_pnl(self):
        '''Method used to calculate profit of a given position
        
        Returns the pnl value, depending on the side (buy or sell)
        '''
        if self.qty < 0 or self.entry < 0 or self.exit < 0:
            print(f'Wrong value, it should be above 0!')
            return None
        
        if self.side == "BUY":
            return (self.exit - self.entry) * self.qty
        else:
            return (self.entry - self.exit) * self.qty
    

trades = []
filepath = 'ohlc_mock_data.csv'

df = pd.read_csv(filepath)

for i in range(len(df)):
    row = df.iloc[i]
    t = Trade(row['ticker'], 'BUY', row['open'], row['close'], 1000)
    trades.append(t)

total = 0
for t in trades:
    total += t.calc_pnl()

print(f"Total PNL: {total}")

---

## Self-Assessment

After completing all tasks, rate yourself:

- **Score:** ___/8 tasks completed
- **Difficulty:** (Easy/Medium/Hard)
- **Time Spent:** ___ hours
- **Week 1 Confidence:** How ready do you feel for Week 2?

Document this in `feedback.md`.

---

**Weekend Assignment:**

I'll generate **TWO mock PCAP exams** for you to complete over the weekend. They'll be in the `exams/` folder:
- `Week1_Exam_A.md` - 40 questions, 90 minutes
- `Week1_Exam_B.md` - 40 questions, 90 minutes

**Goals:**
1. Complete both exams (don't look up answers!)
2. Polish your AlgoBacktest project (clean up code, add docstrings)
3. Review any Week 1 concepts that felt shaky

**Great work this week! 🎉 See you Monday for Week 2!**
