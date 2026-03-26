# Week 11, Day 4 — 2026-03-26

**Topic:** os.path | escape sequences | generators | gap closure | Project: multi-strategy run_backtest
**Mode:** PCAP drills + project task

---

## Task 1 — os.path: predict the output (gap reinforcement)

```python
import os

path = "/var/log/app/error.log"
print(os.path.basename(path)) #error.log (the file)
print(os.path.dirname(path)) #/var/log/app (the folder)
print(os.path.split(path)) #('/var/log/app', 'error.log') - tuple with folder and file split
print(os.path.splitext(path)) #('/var/log/app/error', '.log') - again tuple with folder and file, but this time the split fragment is the file type
print(os.path.join("var", "log", "app")) #\var\log\app (and this is very important, that this uniquely handles both Linux/Windows paths, dpeending on the used environment)
```

Five outputs. Be exact about what `split()` and `splitext()` return (types matter conceptually, not syntax).

Also answer:
- Does `dirname()` include a trailing slash? No
- What does `splitext()` do when the file has no extension, e.g. `os.path.splitext("/etc/hosts")`?
Not sure. Is that so relevant here?
---

## Task 2 — Escape sequences (gap reinforcement)

### The rule — read this first

Python reads strings **left to right, one character at a time**. A backslash `\` always grabs the next character and forms an escape pair. You cannot "split" an escape sequence.

Key escape pairs:
| Sequence | Meaning | `len()` |
|---|---|---|
| `\\` | one literal backslash `\` | 1 |
| `\'` | one literal single quote `'` | 1 |
| `\"` | one literal double quote `"` | 1 |
| `\n` | newline | 1 |
| `\t` | tab | 1 |

**How to trace a string manually:**

Take `'\\\''` and read token by token inside the outer quotes `'...'`:
```
'           ← opens the string
\\          ← escape pair → one literal backslash \
\'          ← escape pair → one literal quote ' (does NOT close the string)
            ← string still open, waiting for closing '
            ← end of input — string never closed → SyntaxError
```

The closing `'` was consumed by the `\'` escape. There is nothing left to close the string.

**Contrast with `"\\'"` (double-quoted):**
```
"           ← opens the string
\\          ← escape pair → one literal backslash \
'           ← plain single quote — harmless inside double quotes
"           ← closes the string
Result: \'  (two chars: backslash + quote)  len = 2
```

**The pattern to remember:**
- `'\\'` → one backslash — string closed by final `'` → prints `\`, len=1
- `'\\\''` → valid — `\\` = backslash, `\'` = quote, string closed by final `'` → prints `'`, len=1
- `"\\'"` → valid — `\\` = backslash, `'` = plain quote → prints `\'`, len=2

---

For each string below, state: valid or `SyntaxError`? If valid, what does `print()` show and what is `len()`?

```python
a = '\\'        # ? Valid, len = 1
b = "it\'s"     # ? Valid, it's, len = 4
c = '\\\''      # ? Valid, \' , len = 2
d = '\n\t'      # ? Valid, looks empty. len = 2
e = "\\"        # ? Valid, \, len = 1
```

Then: what is the difference between `'\\'` and `"\\"` — same or different?

In this context it's the same, the only thing that matters it that we have to be consistent in using one type of quotes in a given string.

---

## Task 3 — Generators: write the code (gap reinforcement)

**Part A:** Write an infinite generator `fibonacci()` (no parameter, no limit) using `yield` and `while True`. Print the first 10 values with a `for` loop and `enumerate` or a counter.

def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


gen = fibonacci()
for i in range(10):
    print(f'Number: {i+1}, {next(gen)}')



**Part B:** Write a generator `squares(n)` that yields squares of numbers from 0 to n-1. Then:
- Use `next()` to get the first value
- Use `list()` to get all remaining values
- What happens if you call `next()` again after exhaustion? How do you avoid the error?
You could use a try/except block.

def squares(n):
    for i in range(n-1):
        yield i**2


x = squares(5)
print(next(x)) #0
print(list(x)) #[1, 4, 9]
print(next(x)) #StopIteration error



---

## Task 4 — Predict the output: mixed gaps

**Q1:**
```python
try:
    raise ValueError("bad input")
except Exception:
    print("Exception branch")
except ValueError:
    print("ValueError branch")
```

**Q2:**
```python
try:
    pass
except ValueError:
    print("caught")
else:
    print("else")
finally:
    print("finally")
```

**Q3:**
```python
import random
print(random.randrange(1, 10, 2))
```
Which of these values is **impossible**?
- A) 1  B) 3  C) 5  D) 10  E) 9

D

---

## Task 5 — Predict the output: scope + closures

**Q1:**
```python
x = 1
def f():
    x = 2
    def g():
        return x
    x = 3
    return g()

print(f())

#3
```

**Q2:**
```python
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5), triple(5))

#10, 15
```

**Q3:**
```python
fns = [lambda x, n=n: x + n for n in range(4)]
print(fns[2](10))

#12
```

---

## Task 6 — Predict the output: generators + iterators

**Q1:**
```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))
print(next(g))
print(list(g))
print(list(g))


#1
#2
#[3]
#[]
```

**Q2:**
```python
def gen():
    return
    yield

g = gen()
print(type(g).__name__)
print(list(g))

#generator
#[]
```

**Q3:**
```python
g = (x ** 2 for x in range(5))
print(next(g))
print(next(g))
print(sum(g))


#0
#1
#29
```

---

## Task 7 — PCAP simulation: multiple choice

**Q1:** What is the output?
```python
class A:
    def f(self): return "A"

class B(A):
    def f(self): return "B" + super().f()

class C(A):
    def f(self): return "C" + super().f()

class D(B, C):
    pass

print(D().f())
```
- A) `BA`  B) `BCA`  C) `BAC`  D) `BC`

B

**Q2:** What is printed?
```python
def outer():
    x = []
    def inner(val):
        x.append(val)
        return x
    return inner

f = outer()
f(1)
f(2)
print(f(3))
```
- A) `[3]`  B) `[1, 2, 3]`  C) `UnboundLocalError`  D) `[1]`

B - lists can be modified
---

## Task 8 — PROJECT: Modularize run_backtest for multiple strategies

Current `run_backtest()` is hardcoded to `VwapStrategy`. The goal: make it accept a **list of strategies** and run all of them simultaneously on the same data.

Requirements:
1. Change signature to `run_backtest(df: pd.DataFrame, strategies: list) -> BacktestEngine`
2. `current_positions` dict is already keyed by strategy — it just needs to be built from the list
3. The session filter and force-close logic must work per-strategy (each strategy has its own `session_start()`/`session_end()`)
4. `strategy_id` should come from the strategy object itself — add a `strategy_id` attribute to `BaseStrategy.__init__` (e.g. a `uuid` or just pass it in as a parameter alongside `name`)
5. The `__main__` block should pass `[vwap_strategy]` — same result as before, just now it supports `[vwap_strategy, another_strategy]`

Write the updated `run_backtest()` and the updated `BaseStrategy.__init__`. Keep it readable.


def run_backtest(df: pd.DataFrame, strategies: list) -> BacktestEngine:
    
    backtest_engine = BacktestEngine()
    
    for strategy in strategies:
        current_positions = {strategy: None}
        
        start = strategy.session_start() #time filtering - this will have to be modularized ``
        end = strategy.session_end()
        
        for idx, row in df.iloc[1:].iterrows():
            t = datetime.fromisoformat(row['candle_open']).time()
            is_rth = (start is None) or (start <= t <= end)
            session_ending = end is not None and t > end
            
            if session_ending and current_positions[strategy]:
                backtest_engine.force_close_all('FDAX', row['open'])
                current_positions[strategy] = None
                continue
            
            if is_rth:
                
                signal = strategy.generate_signal(row['open'], row['vwap_rth'])
                if signal == 'BUY' and current_positions[strategy] is None:
                    backtest_engine.open_position(#data.iloc[idx]['ticker'], 
                                                'FDAX',
                                                'BUY', 
                                                row['open'], 
                                                quantity = 1,
                                                stop_loss = row['open'] - 50,
                                                take_profit = row['open'] + 50,
                                                strategy_id = strategy.strategy_id,
                                                strategy_name = strategy.get_name())
                    current_positions[strategy] = True
                
                elif signal == 'SELL' and current_positions[strategy] is None:
                    backtest_engine.open_position(#data.iloc[idx]['ticker'], 
                                                'FDAX',
                                                'SELL', 
                                                row['open'], 
                                                quantity = 1,
                                                stop_loss = row['open'] + 50,
                                                take_profit = row['open'] - 50,
                                                strategy_id = strategy.strategy_id,
                                                strategy_name = strategy.get_name())
                    current_positions[strategy] = True
                    
                    
                newly_closed = backtest_engine.process_price(#data.iloc[idx]['ticker'],
                                                            'FDAX',
                                                            data.iloc[idx]['close'])
                
                if newly_closed:
                    current_positions[strategy] = None
        
    
    return backtest_engine



'''Abstract Method Class - base strategy'''

from abc import ABC, abstractmethod
from datetime import time
import uuid


#Modified base_strategy.py

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
    

    def get_name(self) -> str:
        '''inherited method to fetch a given strategy name'''
        return self.name


I've also ran tests with two different start/end times in vwap_strategy.py

here's main.py

if __name__ == '__main__':
    
    x = DataLoader('algo_backtest\data\FDAX_M1_OHLC.csv')
    print(x)
    data = x.load_data()
    x.validate_data(data)
    print(len(data))
    print(data.head(3))
    
    setup_logging()
    print('Starting the backtest test procedure in main.py - logging set!')
    
    strategies = [VwapStrategy('FDAX')]
    test_engine = run_backtest(data, strategies)
    print(test_engine)
    test_engine.strategy_report()
    
And the end of the log:


BacktestEngine: 0 open | 33217 closed | PnL: $-5909.0
--- VWAP Strategy (ID: 00cdc20a-a79c-4328-bb04-6254403e45f4) ---

                  Trades: 33217
                  Win Rate: 45.991510371195474%
                  Total PnL: $-5909.00
                  Avg R: -0.00R


--- PORTFOLIO TOTAL  ---

                  Trades: 33217
                  Win Rate: 45.991510371195474%
                  Total PnL: $-5909.0
                  Avg R: -0.0R

Here it was from choosing 15:00 - 17:30 as the start/end hours, but previously I've ran the standard 9:00-17:30 test as well:

BacktestEngine: 0 open | 112356 closed | PnL: $-19874.0
--- VWAP Strategy (ID: 0f10a250-a153-42a6-809b-f8395a78cbab) ---

                  Trades: 112356
                  Win Rate: 45.495567659938054%
                  Total PnL: $-19874.00
                  Avg R: -0.00R


--- PORTFOLIO TOTAL  ---

                  Trades: 112356
                  Win Rate: 45.495567659938054%
                  Total PnL: $-19874.0
                  Avg R: -0.0R


Everything seems to work well.
The next step we could add start/end times as instance attributes instead for each strategy object, so that I could test eacah strategy with different parameters (as start/end) if I wanted to.




---

## Answers

### Task 1
```
basename:
dirname:
split:
splitext:
join:
trailing slash question:
splitext no extension:
```

### Task 2
```
a:
b:
c:
d:
e:
'\\'  vs  "\\":
```

### Task 3
```python
# Part A

# Part B
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
```

### Task 6
```
Q1:
Q2:
Q3:
```

### Task 7
```
Q1:
Q2:
```

### Task 8
```python
# BaseStrategy changes:

# run_backtest():

# __main__ block:
```
