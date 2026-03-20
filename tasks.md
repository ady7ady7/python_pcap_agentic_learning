# Week 10, Day 5 — Code Writing + Project: VWAPStrategy
**Date:** 2026-03-21 | **Focus:** Writing code from scratch, real FDAX data, VWAP strategy

---

## Task 1 — Write a function from scratch: `flatten`

Write a function `flatten(nested: list) -> list` that takes a list which may contain other lists (one level deep only) and returns a flat list of all elements.

```python
flatten([1, [2, 3], 4, [5, 6]])  # → [1, 2, 3, 4, 5, 6]
flatten([1, 2, 3])               # → [1, 2, 3]
flatten([[1], [2], [3]])         # → [1, 2, 3]
```

Requirements:
- Use a list comprehension (one line body)
- Type hints required
- No imports

def flatten(nested: list) -> list:
    
    flattened_list = []
    for element in nested:
        if isinstance(element, (int, float)):
            flattened_list.append(element)
        else:
            for el in element:
                flattened_list.append(el)
            
    return flattened_list

Not sure if this is the most Pythonic way, but it works perfectly fine!
If there's a smarter, more Pythonic way, let me know.

---

## Task 2 — Write a class from scratch: `BoundedList`

Write a class `BoundedList` that behaves like a list but never exceeds a fixed max size. When a new item is added and the list is full, the oldest item is removed (FIFO).

```python
bl = BoundedList(max_size=3)
bl.add(1)
bl.add(2)
bl.add(3)
bl.add(4)      # drops 1
print(bl.values)   # [2, 3, 4]
print(len(bl))     # 3
```

Requirements:
- `__init__(self, max_size: int)`
- `add(self, item: float) -> None`
- `values` property returning a copy of the internal list
- `__len__` returning current size
- `average() -> float` returning mean of current values (return 0.0 if empty)
- Type hints throughout

class BoundedList:
    
    def __init__(self, max_size: int):
        self.max_size = max_size
        self._items: list[float] = []
    
    @property
    def values(self) -> list:
        return list(self._items)
    
    @property
    def average(self) -> float:
        return sum(self._items) / len(self._items)
    
    def __len__(self) -> int:
        return len(self._items)
    
    def add(self, item: float) -> None:
        if self.__len__() == self.max_size:
            del self._items[0]
        self._items.append(item)



---

## Task 3 — Write a context manager from scratch: `Timer`

Write a class `Timer` that works as a context manager and prints elapsed time on exit.

```python
import time

with Timer("data loading"):
    time.sleep(0.1)

# Output: data loading: 0.10s
```

Requirements:
- Implement `__enter__` and `__exit__`
- Use `time.perf_counter()`
- `__exit__` must accept `exc_type, exc_val, exc_tb` and return `False` (don't suppress exceptions)
- Type hints throughout

---

## Task 4 — Fix the bugs: 3 broken snippets

Write the corrected version of each. Identify what is wrong first (one sentence), then fix it.

**Snippet A:**
```python
def running_average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

print(running_average([]))


We're correctly adding a number to total, but we're only calculating the running average as we finish


def running_average(numbers):
    total = 0
    length = 0
    for n in numbers:
        length += 1
        total += n
        moving_avg = total / length
    return moving_avg

```

**Snippet B:**
```python
class Stack:
    items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

s1 = Stack()
s2 = Stack()
s1.push(1)
print(s2.items)  # expected: []

Items should be an instance variable, not a Class variable.
It will make every instance of this class share the same list of items.

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

```

**Snippet C:**
```python
import os

def find_csvs(folder: str) -> list:
    return [f for f in os.listdir(folder) if f.endswith('.csv')]

files = find_csvs('nonexistent_folder')
print(files)

Unhandled exception.

import os

def find_csvs(folder: str) -> list:
    try:
        cvs = [f for f in os.listdir(folder) if f.endswith('.csv')]
        return cvs
    except FileNotFoundError as e:
        print(f'FileNotFoundError: {str(e)}')
    except Exception as e:
        print(f'Unhandled exception: {str(e)}')

files = find_csvs('nonexistent_folder')
print(files)

We could also use try-except-else structure here, but this also works



```

---

## Task 5 — PROJECT: Load real FDAX data

Your real data CSV has these columns:
```
candle_open, candle_close, open, high, low, close,
bid_volume, ask_volume, vwap_rth, vwap_full
```

1. Copy your real FDAX CSV into `algo_backtest/data/` and note the filename.
2. In `main.py`, load it with `DataLoader` and print:
   - `data.columns`
   - `data.head(3)`
   - `len(data)`
   - Whether `validate_data()` passes

Write your output in the answers section below.

DataLoader initialized.
DataLoader(filepath = algo_backtest\data\FDAX_M1_OHLC.csv)
Data loading succeeded
Data loading operation ended.
Missing values found: 10
216932
                 candle_open               candle_close     open     high      low    close  bid_volume  ask_volume  vwap_rth  vwap_full
0  2025-03-10 09:00:00+01:00  2025-03-10 09:00:59+01:00  23172.0  23191.0  23164.0  23181.0         221         198  23177.51   23177.51
1  2025-03-10 09:01:00+01:00  2025-03-10 09:01:59+01:00  23183.0  23199.0  23176.0  23192.0         149          75  23181.48   23181.48
2  2025-03-10 09:02:00+01:00  2025-03-10 09:02:59+01:00  23189.0  23191.0  23179.0  23189.0          50          42  23181.99   23181.99
0 23181.0
1 23192.0
2 23189.0
3 23178.0
4 23141.0
5 23106.0
6 23106.0
7 23116.0
8 23091.0
9 23087.0
2026-03-20 15:47:11,678 [DEBUG   ] root: Logging in main initialized.
Starting the backtest test procedure in main.py - logging set!
(.venv) 


I think 10 missing values IS PERFECTLY fine for m1 candles spanning 11 months.



---

## Task 6 — PROJECT: Implement `VWAPStrategy`

Create `algo_backtest/strategies/vwap_strategy.py`.

The strategy rule:
- If `close > vwap_rth` → signal = `'BUY'`
- If `close < vwap_rth` → signal = `'SELL'`
- If `close == vwap_rth` → signal = `'HOLD'`

Requirements:
- Inherit from `BaseStrategy`
- `__init__(self, ticker: str)` — call `super().__init__('VWAP Strategy')`
- `generate_signal(self, price: float, vwap: float) -> str` — override the abstract method signature to accept `vwap` as well
- Docstring on the class and on `generate_signal`
- Type hints throughout

Note: `BaseStrategy.generate_signal` takes only `price`. You are extending the signature. This is fine for now — note it as a design decision in a comment.

---

## Task 7 — PROJECT: Wire VWAPStrategy into `run_backtest()`

Rewrite `run_backtest(df: pd.DataFrame) -> BacktestEngine` in `main.py` to use `VWAPStrategy`.

Logic:
1. Create a `VWAPStrategy` instance (ticker = `'FDAX'`)
2. Create a `BacktestEngine`
3. Track whether there is a currently open position (`current_position = None`)
4. Iterate `df.iterrows()`:
   - Get signal: `strategy.generate_signal(row['close'], row['vwap_rth'])`
   - If signal == `'BUY'` and no open position:
     - `engine.open_position('FDAX', 'BUY', row['close'], quantity=1, stop_loss=row['close'] - 50, take_profit=row['close'] + 100, strategy_id='1', strategy_name='VWAP Strategy')`
     - Set `current_position = True`
   - If signal == `'SELL'` and no open position:
     - Open a SELL position with same SL/TP logic (reversed)
     - Set `current_position = True`
   - Always call `engine.process_price('FDAX', row['close'])`
   - If any trades were closed in that bar: set `current_position = None`
5. Return `engine`

Call it from `if __name__ == '__main__'` and print `engine.strategy_report()`.


BacktestEngine: 0 open | 206153 closed | PnL: $-18352.0
--- VWAP Strategy (ID: 1) ---

                  Trades: 206153
                  Win Rate: 41.216960218866575%
                  Total PnL: $-18352.00
                  Avg R: -0.00R


--- PORTFOLIO TOTAL  ---

                  Trades: 206153
                  Win Rate: 41.216960218866575%
                  Total PnL: $-18352.0
                  Avg R: -0.0R


(.venv) 


I've ran the strategy on 216k rows, with a very simple open/close conditions, so no wonder it worked this way hehe.
Test worked properly, I think.

The next steps would be:

1. to implement more sophisticated strategy conditions, maybe add a datetime as one of the conditions of generating a signal.
2. It would also be great to figure out a way to then simulate testing more than one strategy.
3. After we're done with running two strategies (a mini stress-test of the real purpose of this and combining the logic of more than one strategy in the code to still look neat), I have an idea of how we can simulate portfolio performance. We could maybe create a new class for that, or maybe not - that depends.

We could take the datetime and R/profit performance of a given trade, and save it in a df, or wherever.
Then we would do that for every tested strategy, and after every strategy has been tested, we would then take these performance/profit rows with datetimes and sort them by their datetime. We could then simulate portfolio's performance, extract more things like Sharpe/Profit Factor, maybe run Montecarlo simulations etc.

And it all would work without any async and complex changes - just in a kind of a simple way.
This way the codebase will stay very clear to read, and I will be able to focus on working on data/strategies.

---

## Answers

### Task 1 — flatten
```python

```

### Task 2 — BoundedList
```python

```

### Task 3 — Timer
```python

```

### Task 4 — Bug fixes
Snippet A — bug:
Fix:

Snippet B — bug:
Fix:

Snippet C — bug:
Fix:

### Task 5 — Real data output
columns:
head(3):
len:
validate_data():

### Task 6 — VWAPStrategy
Done / notes:

### Task 7 — run_backtest() output
Done / strategy_report() output:
