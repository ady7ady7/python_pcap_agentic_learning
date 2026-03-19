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
```

**Snippet C:**
```python
import os

def find_csvs(folder: str) -> list:
    return [f for f in os.listdir(folder) if f.endswith('.csv')]

files = find_csvs('nonexistent_folder')
print(files)
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
