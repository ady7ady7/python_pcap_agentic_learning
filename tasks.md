# Week 9, Day 5 — Final Gap Closure + Weekend Exam Prep
**Date:** 2026-03-06 | **Priority gaps:** logging double-propagation (4th session), IEEE 754, starred unpacking → list, except ordering

---

## Task 1 — Logging double-propagation: the hardest variant (6 questions)

This is the gap that has survived 4 sessions. The rule:

**When a named logger has its own handler AND `propagate=True` (the default), a message that passes the named logger's level is processed by BOTH the named handler AND the root handler.**

Count the output lines carefully.

**Q1:**
```python
import logging

logging.basicConfig(level=logging.INFO)   # root handler: INFO+

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.ERROR)
logger.addHandler(handler)

logger.info("info")
logger.error("error")
```
How many lines total, and which handler(s) print each?

Very interesting thing to learn indeed.
3 lines in total
root handler prints both (INFO:app:info and ERROR:app:error).
The named handler only prints error.

**Q2:**
```python
import logging

logging.basicConfig(level=logging.WARNING)  # root handler: WARNING+

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

logger.debug("debug")
logger.warning("warn")
```
How many lines total, and which handler(s) print each?

debug + warn - named handler
root handler - warning only (in appropriate formatting)


**Q3:**
```python
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)
logger.propagate = False             # <-- notice this

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

logger.info("info")
logger.error("error")
```
How many lines total?

both -> info/error from the named handler, only two lines

**Q4:**
```python
import logging

parent = logging.getLogger("app")
child  = logging.getLogger("app.module")

parent.setLevel(logging.DEBUG)
child.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
parent.addHandler(handler)

child.warning("warn from child")
```
How many lines, and why?

1 line from child only

**Q5:**
```python
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("app")
# No setLevel called on logger
# No handlers added to logger

logger.debug("debug")
logger.warning("warn")
```
How many lines, and why? *(Hint: what is the default level of a named logger that never calls setLevel?)*

DEBUG:app:debug
WARNING:app:warn

It's because we set the basicConfig to DEBUG at the beginning.
Normally, we'd have only warn.


**Q6:**
```python
import logging

logging.basicConfig(level=logging.ERROR)

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

h1 = logging.StreamHandler()
h1.setLevel(logging.WARNING)
logger.addHandler(h1)

logger.warning("warn")
logger.error("error")
logger.critical("critical")
```
How many lines total? List each message and which handler(s) print it.

3 lines, printed by the h1 handler for all the messages

---

## Task 2 — IEEE 754 & float traps: 5 predict-the-output (no code)

**Q1:** What is the output?
```python
print(0.1 + 0.2 == 0.3)

False, yet I don't understand why

```

**Q2:** What is the output?
```python
print(round(0.1 + 0.2, 10) == round(0.3, 10))

True, I guess so, but again - I think it's a nonsense question. Why would that be an issue?
```
*(Think carefully — is `round` enough here?)*

**Q3:** What is the output?
```python
import math
print(math.isclose(0.1 + 0.2, 0.3))


Same idea again? Come on, I didn't see that on PCAP course, it's some bullshit - erase evaluating this bullshit.

```

**Q4:** What is the output?
```python
x = 0.1 + 0.2
print(x)
```
- A) `0.3`
- B) `0.30000000000000004`
- C) `0.300000000000000`
- D) `TypeError`

B


**Q5:** What is the output?
```python
a = 0.1
b = 0.1
c = 0.1
print(a + b + c == 0.3)
print(a + b + c)

False
0.30000000000000004
```

---

## Task 3 — Starred unpacking mechanics: 5 questions (no code)

**Q1:** What is the output?
```python
a, *b, c = (1, 2, 3, 4, 5)
print(type(b), b)


list, [2, 3, 4]

```

**Q2:** What is the output?
```python
first, *rest = "hello"
print(type(rest), rest)

list, ['e', 'l', 'l', 'o']
```

**Q3:** What is the output?
```python
*a, b = [10]
print(a, b)

[1], [0]
```

**Q4:** What is the output?
```python
x, *y, z = range(5)
print(x, y, z)

0 [1, 2, 3] 4
```

**Q5:** Which of these is a SyntaxError?
```python
# A
a, *b, c = [1, 2, 3]

# B
*a, *b = [1, 2, 3]

# C
a, *b = [1]

# D
*a, b = (1, 2)

B
```

---

## Task 4 — except clause ordering: 4 questions (no code)

**Q1:** What happens?
```python
try:
    open("nofile.txt")
except Exception:
    print("Exception")
except FileNotFoundError:
    print("FileNotFoundError")

Exceptino
```

**Q2:** Rewrite the except block from Q1 in the correct order (most specific first).

try:
    open("nofile.txt")
except FileNotFoundError:
    print("FileNotFoundError")
except Exception:
    print("Exception")


**Q3:** What happens?
```python
try:
    raise ValueError("v")
except (TypeError, ValueError):
    print("caught")
except Exception:
    print("exception")

caught
```

**Q4:** Which ordering is correct for a try block that could raise `FileNotFoundError`, `OSError`, or `Exception`?
- A) `Exception` → `OSError` → `FileNotFoundError`
- B) `FileNotFoundError` → `OSError` → `Exception`
- C) `OSError` → `FileNotFoundError` → `Exception`
- D) Order doesn't matter for `except` clauses

B

---

## Task 5 — PCAP Simulation: 10 questions (12 minutes)

**Q1:** What is the output?
```python
x = [1, 2, 3]
y = x
y += [4]
print(x)
```
- A) `[1, 2, 3]`
- B) `[1, 2, 3, 4]`
- C) `[1, 2, 3, [4]]`
- D) `TypeError`

B

**Q2:** What is the output?
```python
x = (1, 2, 3)
y = x
y += (4,)
print(x)
```
- A) `(1, 2, 3)`
- B) `(1, 2, 3, 4)`
- C) `TypeError`
- D) `(1, 2, 3, (4,))`

C

**Q3:** What is the output?
```python
def f(x=[]):
    x.append(1)
    return x

print(f())
print(f())
print(f())
```
- A) `[1]`, `[1]`, `[1]`
- B) `[1]`, `[1, 1]`, `[1, 1, 1]`
- C) `[1]`, `[1, 1]`, `[1, 1, 1]` — only if called on the same object
- D) `TypeError`

B

**Q4:** What is the output?
```python
class A:
    x = 0

a = A()
b = A()
a.x += 1
print(A.x, a.x, b.x)
```
- A) `1 1 1`
- B) `0 1 0`
- C) `1 1 0`
- D) `AttributeError`

B


**Q5:** What is the output?
```python
gen = (i for i in range(10))
print(next(gen))
print(next(gen))
list(gen)
print(next(gen))
```
- A) `0`, `1`, `StopIteration`
- B) `0`, `1`, `2`
- C) `0`, `1`, `[]`
- D) `0`, `1`, raises `StopIteration`

A

**Q6:** What is the output?
```python
try:
    raise ValueError("v")
except ValueError as e:
    err = e
print(err)
```
- A) `ValueError: v`
- B) `v`
- C) `NameError: name 'err' is not defined`
- D) `<class 'ValueError'>`

A

**Q7:** What is the output?
```python
def outer():
    x = 1
    def inner():
        nonlocal x
        x += 1
    inner()
    inner()
    return x

print(outer())
```
- A) `1`
- B) `2`
- C) `3`
- D) `UnboundLocalError`

C


**Q8:** What is the output?
```python
xs = [1, 2, 3, 4, 5]
print(xs[::2])
print(xs[::-1])
```
- A) `[1, 3, 5]`, `[5, 4, 3, 2, 1]`
- B) `[2, 4]`, `[5, 4, 3, 2, 1]`
- C) `[1, 3, 5]`, `[1, 2, 3, 4, 5]`
- D) `TypeError`

A



**Q9:** What is the output?
```python
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.count)
```
- A) `0`
- B) `1`
- C) `3`
- D) `AttributeError`

C

**Q10:** What is the output?
```python
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("myapp")
logger.setLevel(logging.DEBUG)

h = logging.StreamHandler()
h.setLevel(logging.WARNING)
logger.addHandler(h)

logger.info("info")
logger.warning("warn")
logger.error("error")
```
How many total lines are printed, and from which handler(s)?
- A) 1 line — `warn` only, from `myapp` handler
- B) 2 lines — `info` from root, `warn` + `error` from `myapp` handler
- C) 3 lines — `info` from root, `warn` from `myapp` handler, `error` from both
- D) 4 lines — `info` from root, `warn` from both, `error` from both

D, but in fact it's 5 lines, and not 4...


---

## Task 6 — PROJECT: Wire DataLoader into BacktestEngine — first integration step

The DataLoader works and returns a clean DataFrame. Now wire it into the engine.

In `main.py`:

1. Keep the existing DataLoader block (working).
2. Below it, uncomment `setup_logging()` and call it.
3. Add an engine test block (currently commented out) but **feed it from the DataFrame** instead of hardcoded values:
   - Create a `BacktestEngine` instance.
   - Use `df.iloc[0]` to open one BUY position: ticker from `row['ticker']`, entry from `row['close']`, quantity=1000, stop_loss=`entry - 1.0`, take_profit=`entry + 2.0`.
   - Call `engine.process_price()` using `df.iloc[5]['close']` as the current price.
   - Print `engine` (uses `__str__`).
   - Print `engine.total_pnl`.

This is purely wiring — no new classes, no new methods. All the pieces exist. You are connecting them.


Yes, I've tested it while adding more price checks in process price. It works just fine.
I need we have to move on with real data very soon.

2026-03-06 13:50:53,972 [DEBUG   ] root: Logging in main initialized.
Starting the backtest test procedure in main.py - logging set!
Position Position_id = e712bb0b-b8df-4274-9809-68cbfae8f87b | BUY 1000 EURUSD @ 100.8 [SL = 99.8, TP = 102.8] [@Aha_pl | 555] added successfully
2026-03-06 13:50:53,973 [INFO    ] engine.backtest_engine: @Strategy Aha_pl: 555 Position e712bb0b-b8df-4274-9809-68cbfae8f87b: BUY EURUSD @ 100.8
2026-03-06 13:50:53,973 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $102.5
2026-03-06 13:50:53,973 [INFO    ] engine.backtest_engine: @Strategy 555, Aha_pl || Position e712bb0b-b8df-4274-9809-68cbfae8f87b @ EURUSD closed with 1700.0000000000027 as a Still open
2026-03-06 13:50:53,973 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $102.85
2026-03-06 13:50:53,973 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $104.25
BacktestEngine: 0 open | 1 closed | PnL: $1700.0
repr: BacktestEngine: 0 open | 1 closed | PnL: $1700.0
str: BacktestEngine: 0 open | 1 closed | PnL: $1700.0
1700.0
100.0
[np.float64(1.7)]
{('555', 'Aha_pl'): [Trade(position_id='e712bb0b-b8df-4274-9809-68cbfae8f87b', ticker='EURUSD', side='BUY', entry_price=100.8, exit_price=102.5, quantity=1000, pnl=1700.00, exit_reason='still open', strategy_id='555', strategy_name='Aha_pl')]}
--- Aha_pl (ID: 555) ---

                  Trades: 1
                  Win Rate: 100.0%
                  Total PnL: $1700.00
                  Avg R: 1.70R


--- PORTFOLIO TOTAL  ---

                  Trades: 1
                  Win Rate: 100.0%
                  Total PnL: $1700.0
                  Avg R: 1.7R


(.venv) 


---

## Task 7 — PROJECT: Add a `run_backtest()` function to main.py

Extract the engine logic into a reusable function (still in `main.py` for now):

```python
def run_backtest(df: pd.DataFrame) -> BacktestEngine:
    ...
```

The function should:
1. Accept a DataFrame.
2. Create a `BacktestEngine`.
3. Open one position using `df.iloc[0]` (as above).
4. Iterate the rest of the DataFrame using `df.iloc[1:].iterrows()` and call `engine.process_price(row['ticker'], row['close'])` for each row.
5. Return the engine.

Call it from `if __name__ == '__main__'`, store the result, and print `engine.strategy_report()`.

This is the first end-to-end backtest run on real data.

Done:

def run_backtest(df: pd.DataFrame) -> BacktestEngine:
    backtest_engine = BacktestEngine()
    backtest_engine.open_position(ticker = data.iloc[0]['ticker'], 
                                  side = 'BUY', 
                                  entry = data.iloc[0]['close'], 
                                  quantity = 10000, stop_loss = data.iloc[0]['close'] - 0.01 * data.iloc[0]['close'], 
                                  take_profit = data.iloc[0]['close'] + 0.01 * data.iloc[0]['close'],
                                  strategy_id = '999',
                                  strategy_name = 'main_mock_tester'
                                  )
    for idx, row in df.iloc[1:].iterrows():
        backtest_engine.process_price(data.iloc[idx]['ticker'], data.iloc[idx]['close'])
    
    return backtest_engine


test_engine = run_backtest(data)
print(test_engine)
test_engine.strategy_report()


LOG: 
2026-03-06 13:59:06,156 [DEBUG   ] root: Logging in main initialized.
Starting the backtest test procedure in main.py - logging set!
Position Position_id = 988e0252-8a43-4b46-a8ca-061d38980716 | BUY 10000 EURUSD @ 100.8 [SL = 99.792, TP = 101.80799999999999] [@main_mock_tester | 999] added successfully
2026-03-06 13:59:06,157 [INFO    ] engine.backtest_engine: @Strategy main_mock_tester: 999 Position 988e0252-8a43-4b46-a8ca-061d38980716: BUY EURUSD @ 100.8
2026-03-06 13:59:06,157 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $101.3
2026-03-06 13:59:06,157 [INFO    ] engine.backtest_engine: @Strategy 999, main_mock_tester || Position 988e0252-8a43-4b46-a8ca-061d38980716 @ EURUSD closed with 5000.0 as a Still open
2026-03-06 13:59:06,157 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $101.5
2026-03-06 13:59:06,157 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $101.9
2026-03-06 13:59:06,157 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $102.3
2026-03-06 13:59:06,157 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $102.5
2026-03-06 13:59:06,158 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $102.4
2026-03-06 13:59:06,158 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $102.0
2026-03-06 13:59:06,158 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $101.8
2026-03-06 13:59:06,158 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $101.5
2026-03-06 13:59:06,158 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $101.7
2026-03-06 13:59:06,158 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $102.1
2026-03-06 13:59:06,158 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $101.95
2026-03-06 13:59:06,158 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $102.15
2026-03-06 13:59:06,159 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $102.55
2026-03-06 13:59:06,159 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $102.85
2026-03-06 13:59:06,159 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $102.75
2026-03-06 13:59:06,159 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $102.9
2026-03-06 13:59:06,159 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $103.2
2026-03-06 13:59:06,159 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $103.15
2026-03-06 13:59:06,159 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $103.05
2026-03-06 13:59:06,159 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $102.95
2026-03-06 13:59:06,160 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $103.0
2026-03-06 13:59:06,160 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $103.3
2026-03-06 13:59:06,160 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $103.25
2026-03-06 13:59:06,160 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $103.4
2026-03-06 13:59:06,160 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $103.6
2026-03-06 13:59:06,160 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $103.5
2026-03-06 13:59:06,161 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $103.45
2026-03-06 13:59:06,161 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $103.7
2026-03-06 13:59:06,161 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $103.85
2026-03-06 13:59:06,161 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $103.9
2026-03-06 13:59:06,161 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $104.05
2026-03-06 13:59:06,161 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $104.15
2026-03-06 13:59:06,162 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $104.3
2026-03-06 13:59:06,162 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $104.25
2026-03-06 13:59:06,162 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $104.35
2026-03-06 13:59:06,162 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $104.45
2026-03-06 13:59:06,162 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $104.55
2026-03-06 13:59:06,162 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $104.65
2026-03-06 13:59:06,162 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $104.75
2026-03-06 13:59:06,162 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $104.85
2026-03-06 13:59:06,163 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $104.95
2026-03-06 13:59:06,163 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $105.05
2026-03-06 13:59:06,163 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $105.15
2026-03-06 13:59:06,163 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $105.25
2026-03-06 13:59:06,163 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $105.35
2026-03-06 13:59:06,163 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $105.45
2026-03-06 13:59:06,163 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $105.55
2026-03-06 13:59:06,163 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $105.65
BacktestEngine: 0 open | 1 closed | PnL: $5000.0
--- main_mock_tester (ID: 999) ---

                  Trades: 1
                  Win Rate: 100.0%
                  Total PnL: $5000.00
                  Avg R: 0.50R


--- PORTFOLIO TOTAL  ---

                  Trades: 1
                  Win Rate: 100.0%
                  Total PnL: $5000.0
                  Avg R: 0.5R


(.venv) 

---

## Task 8 — Self-assessment: PCAP readiness rating

No code. Write answers in `tasks.md` below.

After 9 weeks of drilling, rate yourself on each of the core PCAP-31-03 exam sections (1–10):

1. Modules & packages (import, sys.path, `__init__.py`) - 8
2. Strings & string methods - 9
3. Exception handling hierarchy - 8
4. OOP — classes, inheritance, MRO - 7
5. OOP — encapsulation, properties, dunder methods - 8
6. Generators & iterators - 6
7. Functional programming (lambda, map, filter, closures) - 8
8. Standard library (logging, datetime, os, errno) - 6
9. File I/O (text + binary, modes, context managers) - 7
10. Scope rules (LEGB, global, nonlocal, UnboundLocalError) - 8

Identify your **2 weakest** sections and explain in one sentence each why they still feel shaky.

It's really difficult to tell, I'm pretty sure I can handle about 80-90% of the tasks if they're not designed to be very tricky, but I know the basics and sometimes get lost at more comlicated tasks, that are designed to be tricky by design, but I doubt real code works that way. Generally feeling that I should be able to pass the PCAP exam at this point, perhaps not at the 90%+ mark, but I should be able to do at least 75%.

---

## Answers

### Task 1
Q1:
Q2:
Q3:
Q4:
Q5:
Q6:

### Task 2
Q1:
Q2:
Q3:
Q4:
Q5:

### Task 3
Q1:
Q2:
Q3:
Q4:
Q5:

### Task 4
Q1:
Q2 (correct order):
Q3:
Q4:

### Task 5
Q1:
Q2:
Q3:
Q4:
Q5:
Q6:
Q7:
Q8:
Q9:
Q10:

### Task 6
Done / notes:

### Task 7
Done / notes:

### Task 8 — PCAP Readiness
1. Modules & packages:
2. Strings:
3. Exception handling:
4. OOP inheritance:
5. OOP encapsulation/dunder:
6. Generators:
7. Functional programming:
8. Standard library:
9. File I/O:
10. Scope rules:

Weakest 2 and why:
