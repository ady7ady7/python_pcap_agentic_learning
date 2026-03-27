# Week 11, Day 5 — 2026-03-27

**Topic:** datetime deep dive | gap closure | PCAP simulation | Project: Opening Range strategy
**Mode:** High volume — exam prep + project

---

## Task 1 — datetime: predict the output (volume drill)

```python
from datetime import datetime, date, time, timedelta

# Part A
dt = datetime(2026, 3, 27, 14, 45, 30)
print(dt.year)
print(dt.hour)
print(dt.minute)
print(dt.date())
print(dt.time())
```

```python
# Part B
dt = datetime(2026, 3, 27, 9, 0, 0)
delta = timedelta(days=2, hours=3, minutes=30)
result = dt + delta
print(result.day)
print(result.hour)
print(result.minute)
```

```python
# Part C
td1 = timedelta(hours=2, minutes=30)
td2 = timedelta(hours=1, minutes=45)
diff = td1 - td2
print(diff.seconds)
print(diff.total_seconds())
```

```python
# Part D
dt = datetime(2026, 3, 27, 9, 30, 0)
print(dt.strftime("%Y-%m-%d"))
print(dt.strftime("%H:%M:%S"))
print(dt.strftime("%d/%m/%Y %H:%M"))
```


from datetime import datetime, timedelta

dt = datetime(2026, 3, 27, 14, 45, 30)
print(dt.year) #2026
print(dt.hour) #14
print(dt.minute) #45
print(dt.date()) #2026-03-27
print(dt.time()) #14:45:30


dt = datetime(2026, 3, 27, 9, 0, 0)
delta = timedelta(days=2, hours=3, minutes=30)
result = dt + delta #2026-03-29 12:30
print(result.day) #29
print(result.hour) #12
print(result.minute) #30


td1 = timedelta(hours=2, minutes=30)
td2 = timedelta(hours=1, minutes=45)
diff = td1 - td2 #
print(diff.seconds) #45 mins * 60 - WHAT THE FUCK, WHY WOULD I EVEN REMEMBER THAT?
print(diff.total_seconds()) #same, stupid, retarded question - humans are not meant to be living calculators


dt = datetime(2026, 3, 27, 9, 30, 0)
print(dt.strftime("%Y-%m-%d")) #2026-03-27
print(dt.strftime("%H:%M:%S")) #09:30:00
print(dt.strftime("%d/%m/%Y %H:%M")) #27/03/2026 9:30

---

## Task 2 — datetime: strptime + comparisons

```python
# Part A — strptime
from datetime import datetime

from datetime import datetime, time

s = "2026-03-27 09:30:00"
dt = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
print(dt.year) #2026
print(dt.minute) #30
print(type(dt).__name__) #datetime
```



```python
# Part B — time comparisons
from datetime import time

t1 = time(9, 0)
t2 = time(17, 30)
t3 = time(10, 15)

print(t1 < t3 < t2) #True
print(t3 > t2) #False
print(t1 == time(9, 0, 0)) #True
```

```python
# Part C — date arithmetic
from datetime import date

d1 = date(2026, 3, 27)
d2 = date(2026, 3, 1)
delta = d1 - d2
print(delta.days) #26
print(type(delta).__name__) #timedelta
```

Also answer:
- What is the difference between `strptime()` and `strftime()`? (one-liner each)
- What does `datetime.now()` return vs `datetime.today()`?

1. strptime converts a given string into a datetime (with a specified format)
strftime does the same, but in the opposite direction (from datetime to string)

2. They return the same results

---

## Task 3 — PCAP simulation: exceptions

**Q1:**
```python
try:
    x = int("abc")
except TypeError:
    print("TypeError")
except ValueError:
    print("ValueError")
except Exception:
    print("Exception")

ValueError
```

**Q2:**
```python
def f():
    try:
        return 1
    finally:
        return 2

print(f())

#2
```

**Q3:**
```python
x = 0
try:
    x = 1
    raise RuntimeError
    x = 2
except RuntimeError:
    x += 10
else:
    x += 100
finally:
    x += 1000

print(x) #1011
```

**Q4:**
```python
class MyError(Exception):
    pass

class SpecificError(MyError):
    pass

try:
    raise SpecificError("oops")
except MyError as e:
    print(type(e).__name__)

#SpecificError
```

---

## Task 4 — PCAP simulation: OOP + MRO

**Q1:**
```python
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super().__init__()
        self.x += 10

class C(A):
    def __init__(self):
        super().__init__()
        self.x += 100

class D(B, C):
    pass

d = D()
print(d.x)

D -> B -> C -> A
Output: 111

```

**Q2:**
```python
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

a = Counter()
b = Counter()
c = Counter()
print(Counter.count) #3
print(a.count) #3
```

**Q3:**
```python
class A:
    def hello(self):
        return "A"

class B(A):
    pass

class C(A):
    def hello(self):
        return "C"

class D(B, C):
    pass

print(D().hello())
```


#MRO: D -> B -> C -> A
#Output: C

---

## Task 5 — PCAP simulation: generators + iterators

**Q1:**
```python
def gen(n):
    for i in range(n):
        yield i * 2

g = gen(4)
print(next(g))
print(next(g))
print(list(g))
print(list(g))

0
2
[4, 6]
[]

```

**Q2:**
```python
def gen():
    yield 1
    yield from range(2, 5)
    yield 5

print(list(gen()))

#[1, 2, 3, 4, 5]
```

**Q3:**
```python
class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        self.current += 1
        return self.current

print(list(Counter(4)))

#[1, 2, 3, 4]
```

**Q4:**
```python
g = (x for x in range(10) if x % 3 == 0)
print(next(g))
print(next(g))
print(list(g))

#0
#3
#[6, 9]

```

---

## Task 6 — PCAP simulation: closures + lambdas

**Q1:**
```python
fns = []
for i in range(3):
    fns.append(lambda: i * 2)

print([f() for f in fns])

#[4, 4, 4]

```

**Q2:**
```python
fns = [lambda i=i: i * 2 for i in range(3)]
print([f() for f in fns])

#[0, 2, 4]
```

**Q3:**
```python
from functools import reduce

nums = [1, 2, 3, 4, 5]
result = reduce(lambda acc, x: acc + x, nums, 10)
print(result)

#25
```

**Q4:**
```python
data = [3, 1, 4, 1, 5, 9]
result = sorted(data, key=lambda x: -x)
print(result[:3])

#[9, 5, 4]

```

---

## Task 7 — PCAP simulation: modules + packages

**Q1:** Which correctly imports only `sqrt` from `math`?
- A) `import math.sqrt`
- B) `from math import sqrt`
- C) `import sqrt from math`
- D) `from math import *`

B

**Q2:** What does `__all__` control?
- A) Which names are loaded when the module is first imported
- B) Which names are exported when `from module import *` is used
- C) Which names are private and cannot be accessed externally
- D) Which names are automatically deleted after import

B


**Q3:** What is printed?
```python
import mymodule       # mymodule.x = 10
import mymodule       # second import
mymodule.x = 99
import mymodule       # third import
print(mymodule.x)
```
- A) `10`  B) `99`  C) `ImportError`  D) `None`

A

---

## Task 8 — PROJECT: Local Pivot Point Strategy

### Concept

From the 09:00–10:00 candle window each day, calculate:
- `H` = highest high, `L` = lowest low, `C` = close of last candle (09:59)

Then compute **Local Pivot Point levels**:
```
LPP = (H + L + C) / 3
LR1 = (2 * LPP) - L
LS1 = (2 * LPP) - H
LR2 = LPP + (H - L)
LS2 = LPP - (H - L)
LR3 = H + 2 * (LPP - L)
LS3 = L - 2 * (H - LPP)
```
Plus sub-levels between each pair (025/050/075 divisions).

Each strategy **instance** is configured at construction with a `side`, `entry` level, `sl` level, and `tp` level — all as string keys referencing the computed levels:

```python
LPPStrategy('FDAX', side='BUY',  entry='LR1', sl='LS1', tp='LR2')
LPPStrategy('FDAX', side='SELL', entry='LS2', sl='LR1', tp='LS3')
```

Both instances can run simultaneously in the same backtest — each has independent state.

---

### Infrastructure: prepare_day() hook on BaseStrategy

Add to `BaseStrategy` — **not abstract**, default is a no-op:

```python
def prepare_day(self, day_df: pd.DataFrame) -> None:
    """Override to pre-compute daily values. Default is no-op."""
    pass
```

`VwapStrategy` ignores it. `LPPStrategy` overrides it to compute all levels.

---

### Updated run_backtest() structure

Group by day before the loop. For each day, call `prepare_day()` on all strategies first, then run the signal loop:

```python
days = df.groupby(df['candle_open'].apply(
    lambda x: datetime.fromisoformat(x).date()
))

for day_date, day_df in days:
    for strategy in strategies:
        strategy.prepare_day(day_df)

    for _, row in day_df.iterrows():
        # RTH filter + signal loop unchanged
```

---

### generate_signal() signature fix

`run_backtest()` must call `strategy.generate_signal(row['open'])` universally — just price. Fix `VwapStrategy` so it no longer needs `vwap` passed in — instead, `prepare_day()` or a per-row setter stores `self.current_vwap` and `generate_signal()` reads it internally. Your call on the cleanest approach.

---

### What to build

**A) `BaseStrategy`** — add `prepare_day()`.

**B) `algo_backtest/strategies/lpp_strategy.py`**

```python
class LPPStrategy(BaseStrategy):
    def __init__(self, ticker: str, side: str,
                 entry: str, sl: str, tp: str): ...
    # side: 'BUY' or 'SELL'
    # entry/sl/tp: string keys e.g. 'LR1', 'LS2', 'LPP'

    def session_start(self) -> time: ...   # 10:00 — no signals during calc window
    def session_end(self) -> time: ...     # 17:30

    def prepare_day(self, day_df: pd.DataFrame) -> None:
        # 1. Reset self.levels = {} first — prevents stale data from previous day leaking in
        # 2. Filter day_df to 09:00-10:00
        # 3. Compute H, L, C
        # 4. Compute all LPP levels + sub-levels
        # 5. Store as self.levels dict: {'LR1': 12345.0, 'LS1': 12300.0, ...}
        ...

    def generate_signal(self, price: float) -> str:
        # If self.levels is empty (prepare_day hasn't run yet) → HOLD
        # BUY side: price > self.levels[self.entry] → 'BUY', else 'HOLD'
        # SELL side: price < self.levels[self.entry] → 'SELL', else 'HOLD'
        ...
```

**C) `run_backtest()` in `main.py`** — update with day-grouping structure above. When opening a position, SL and TP come from the strategy's levels:

```python
stop_loss = strategy.levels[strategy.sl]
take_profit = strategy.levels[strategy.tp]
```

**D) `main.py` strategies list:**
```python
strategies = [
    VwapStrategy('FDAX'),
    LPPStrategy('FDAX', side='BUY',  entry='LR1', sl='LS1', tp='LR2'),
    LPPStrategy('FDAX', side='SELL', entry='LS2', sl='LR1', tp='LS3'),
]
```

Run it. Report trade counts per strategy from `strategy_report()`.


The struggle is real...

---

### Answer template
```python
# A) BaseStrategy.prepare_day():

'''Abstract Method Class - base strategy'''

from abc import ABC, abstractmethod
from datetime import time
import pandas as pd
import uuid
    

class BaseStrategy(ABC):
    '''A class with abstract method used to generate trading signal'''
    def __init__(self, name: str):
        self.name = name
        self.strategy_id = str(uuid.uuid4())
        
    @abstractmethod
    def generate_signal(self, price: float) -> str:
        pass
    
    @abstractmethod
    def session_start(self) -> time | None: ...

    @abstractmethod  
    def session_end(self) -> time | None: ...
    
    def get_sl(self, row: pd.Series, current_date) -> float:
        '''Override to give dynamic SL. This is just default.'''
        return row['open'] - 50


    def get_tp(self, row: pd.Series, current_date) -> float:
        '''Override to provide dynamic TP. This is just default.'''
        return row['open'] + 50
        

    def get_name(self) -> str:
        '''inherited method to fetch a given strategy name'''
        return self.name
    
    def prepare(self, df: pd.DataFrame) -> None:
        '''Optionally pre-calculate daily values for relevant levels for a given strategy. Default is None'''
        pass

In the end i've also added get_tp + get_sl

# B) lpp_strategy.py:

from .base_strategy import BaseStrategy
from datetime import datetime, time
import pandas as pd

class LPPStrategy(BaseStrategy):
    '''A class with abstract method used to generate trading signal'''
    def __init__(self, ticker, side: str = None, entry: str = None, sl: str = None, tp: str = None):
        super().__init__(f'LPP Strategy')
        self.ticker = ticker
        self.side = side
        self.entry = entry
        self.sl = sl
        self.tp = tp
        self.levels_by_date: dict = {}
        
    def generate_signal(self, price: float, current_date) -> str:
        '''Generates trade signals based on specified levels and direction set in init'''
        levels = self.levels_by_date.get(current_date)
        if not levels:
            return 'HOLD'
        entry_level = levels[self.entry]
        if self.side == 'BUY':
            return 'BUY' if price > entry_level else 'HOLD'
        return 'SELL' if price < entry_level else 'HOLD'
    
    def get_sl(self, row: pd.Series, current_date) -> float:
        return self.levels_by_date[current_date][self.sl]

    def get_tp(self, row: pd.Series, current_date) -> float:
        return self.levels_by_date[current_date][self.tp]
    
    def session_start(self) -> time:
        return time(10, 0)

    def session_end(self) -> time:
        return time(17, 30)

    def prepare(self, df: pd.DataFrame) -> None:
        '''Run once before backtest. Computes LPP levels for every trading day.'''
        times = df['candle_open'].apply(lambda x: datetime.fromisoformat(x).time())
        dates = df['candle_open'].apply(lambda x: datetime.fromisoformat(x).date())

        window_mask = (times >= time(9, 0)) & (times < time(10, 0))
        window_df = df[window_mask]

        for day_date, day_df in window_df.groupby(dates[window_df.index]):
            high = day_df['high'].max()
            low = day_df['low'].min()
            close = day_df['close'].iloc[-1]

            lpp = (high + low + close) / 3
            lr1 = (2 * lpp) - low
            ls1 = (2 * lpp) - high
            lr2 = lpp + (high - low)
            ls2 = lpp - (high - low)
            lr3 = high + 2 * (lpp - low)
            ls3 = low - 2 * (high - lpp)

            levels = {
                'LPP': lpp,
                'LR1': lr1, 'LR2': lr2, 'LR3': lr3,
                'LS1': ls1, 'LS2': ls2, 'LS3': ls3,
            }

            # Sub-levels between each adjacent pair
            pairs = [
                ('LS3', 'LS2'), ('LS2', 'LS1'), ('LS1', 'LPP'),
                ('LPP', 'LR1'), ('LR1', 'LR2'), ('LR2', 'LR3'),
            ]
            for lo_key, hi_key in pairs:
                lo = levels[lo_key]
                dist = levels[hi_key] - lo
                levels[f'{lo_key}_{hi_key}_025'] = lo + 0.25 * dist
                levels[f'{lo_key}_{hi_key}_050'] = lo + 0.50 * dist
                levels[f'{lo_key}_{hi_key}_075'] = lo + 0.75 * dist

            self.levels_by_date[day_date] = levels


It seems to look very well

# C) run_backtest() updated loop:

def run_backtest(df: pd.DataFrame, strategies: list) -> BacktestEngine:
    backtest_engine = BacktestEngine()
    current_positions = {strategy: None for strategy in strategies}

    # Step 1: preparation — each strategy pre-computes what it needs once
    for strategy in strategies:
        strategy.prepare(df)

    # Step 2: backtest — single pass through all rows
    for _, row in df.iterrows():
        t = datetime.fromisoformat(row['candle_open']).time()
        current_date = datetime.fromisoformat(row['candle_open']).date()

        for strategy in strategies:
            start = strategy.session_start()
            end = strategy.session_end()
            is_rth = (start is None) or (start <= t <= end)
            session_ending = end is not None and t > end

            if session_ending and current_positions[strategy] is not None:
                backtest_engine.force_close_all('FDAX', strategy.strategy_id, row['open'])
                current_positions[strategy] = None
                continue

            if is_rth:
                signal = strategy.generate_signal(row['open'], current_date)

                if signal == 'BUY' and current_positions[strategy] is None:
                    backtest_engine.open_position(
                        'FDAX', 'BUY', row['open'],
                        quantity=1,
                        stop_loss=strategy.get_sl(row, current_date),
                        take_profit=strategy.get_tp(row, current_date),
                        strategy_id=strategy.strategy_id,
                        strategy_name=strategy.get_name()
                    )
                    current_positions[strategy] = True

                elif signal == 'SELL' and current_positions[strategy] is None:
                    backtest_engine.open_position(
                        'FDAX', 'SELL', row['open'],
                        quantity=1,
                        stop_loss=strategy.get_sl(row, current_date),
                        take_profit=strategy.get_tp(row, current_date),
                        strategy_id=strategy.strategy_id,
                        strategy_name=strategy.get_name()
                    )
                    current_positions[strategy] = True

            newly_closed = backtest_engine.process_price('FDAX', row['close'])
            if newly_closed:
                current_positions[strategy] = None

    return backtest_engine


I needed to use Claude for this - this is still a nuisance to me.
IMO it looks just too complicated and it's not how I want to build. 
I'm honestly getting lost in it, plus I have a feeling that THERE might be some flaws, that I didn't yet discovered.



# D) strategy_report() output:


BacktestEngine: 0 open | 11862 closed | PnL: $-3424.0
--- LPP Strategy (ID: 48ad2eec-e818-4e2a-b836-11e2f6ead483) ---

                  Trades: 11862
                  Win Rate: 45.557241611869834%
                  Total PnL: $-3424.00
                  Avg R: -0.00R


--- PORTFOLIO TOTAL  ---

                  Trades: 11862
                  Win Rate: 45.557241611869834%
                  Total PnL: $-3424.0
                  Avg R: -0.0R


Here, this is a red flag - there's no way we'd make 11800 trades in 11 months, AND also there's no AVG R. I'm not sure what's the case, but this has to be studied thoroughly.

For this particular strategy I'm aiming for just 1 trade for a day by the way, if the conditions are met - TP/SL or force close, as we've settled it.

```

---

## Answers

### Task 1
```
Part A:
Part B:
Part C:
Part D:
```

### Task 2
```
Part A:
Part B:
Part C:
strptime vs strftime:
now() vs today():
```

### Task 3
```
Q1:
Q2:
Q3:
Q4:
```

### Task 4
```
Q1:
Q2:
Q3:
```

### Task 5
```
Q1:
Q2:
Q3:
Q4:
```

### Task 6
```
Q1:
Q2:
Q3:
Q4:
```

### Task 7
```
Q1:
Q2:
Q3:
```

### Task 8
```python
# A) BaseStrategy.prepare_day():

# B) lpp_strategy.py:

# C) run_backtest() updated loop:

# D) strategy_report() output:
```
