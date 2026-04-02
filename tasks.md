# Week 12 Day 4 — Strings Deep Cut + sys/os + Multi-Strategy Fix
**Date:** 2026-04-02 | **Focus:** String traps from real exam, sys/os modules, PositionManager iterator fix, multi-strategy run

---

## Task 1 — String slicing traps [Real exam patterns]

**TEACH — trailing colon trap:**
```python
s[:3:]    # identical to s[:3] — trailing colon sets step=None → defaults to 1
s[::1]    # identical to s[:]  — full copy
s[::-1]   # reversed — step=-1
```
The exam puts `[:3:]` to waste your time. Treat it as `[:3]`.

**TEACH — reverse slice construction pattern:**
```python
s = "REP"
s[-1]        # 'P'       — last character
s[-2::-1]    # 'ER'      — from index -2 (='E'), going backwards to start
s[-1] + s[-2::-1]   # 'P' + 'ER' = 'PER'
```

**A)** Predict each output — trace character by character:
```python
s = 'REPTILE'
print(s[:3:])          # trailing colon trap
print(s[:3:1])         # explicit step=1
print(s[::2])          # every 2nd character
print(s[::-1])         # full reverse
print(s[-1] + s[-2::-1])  # real exam pattern
```

**B)** More reverse-slice patterns:
```python
s = 'PYTHON'
print(s[-1] + s[-2::-1])  # same pattern, different string
print(s[2:5])
print(s[2:5:])            # trailing colon — same as above?
print(s[1::2])            # from index 1, every 2nd
print(s[-3:])             # last 3 chars
```

**C)** Predict — negative indexing:
```python
s = 'abcdef'
print(s[-1])
print(s[-3:-1])
print(s[-3::1])    # trailing colon trap again
print(s[-1:-4:-1]) # step=-1, going backwards
```

Write answers here:
```
s = 'REPTILE'
print(s[:3:]) #REP
print(s[:3:1])     #REP     
print(s[::2])          #RPIE
print(s[::-1])        #ELITPER
print(s[-1] + s[-2::-1])  #E + LITPER [od drugiej litery, do tyłu]

s = 'PYTHON'
print(s[-1] + s[-2::-1])  #N + OHTYP -> NOHTYP
print(s[2:5]) #THO
print(s[2:5:])    #THO        
print(s[1::2])     #YHN   
print(s[-3:])      #HON 

s = 'abcdef'
print(s[-1]) #f
print(s[-3:-1]) #de
print(s[-3::1])    #def
print(s[-1:-4:-1])  #fed
```

---

## Task 2 — `str.find` vs `str.index` vs `str.rindex` vs `str.rfind`

**TEACH:**
```python
s.find(sub)    → index or -1          (no exception)
s.rfind(sub)   → LAST occurrence index or -1  (no exception)
s.index(sub)   → index or ValueError  (raises!)
s.rindex(sub)  → LAST occurrence index or ValueError (raises!)
```
The `r` prefix = search from the RIGHT (returns last occurrence index).

**A)** Predict each:
```python
s = "banana"
print(s.find('a'))     # first 'a'
print(s.rfind('a'))    # last 'a'
print(s.index('a'))    # same as find when found
print(s.rindex('a'))   # same as rfind when found
print(s.find('z'))     # not found
print(s.rfind('z'))    # not found
```

**B)** Which raises — predict error or output:
```python
s = "hello"
print(s.index('l'))    # ?
print(s.rindex('l'))   # ? ← note: 'l' appears twice
try:
    print(s.index('z'))
except ValueError as e:
    print(f"ValueError: {e}")
try:
    print(s.rindex('z'))
except ValueError as e:
    print(f"ValueError: {e}")
```

**C)** Multiple choice (PCAP style): What does `"abcabc".rfind('b')` return?
- A: `1`
- B: `4`
- C: `-1`
- D: `ValueError`

Write answers here:
```
A)

print(s.find('a'))     # 1
print(s.rfind('a'))    # 5
print(s.index('a'))    # 1
print(s.rindex('a'))   # 5
print(s.find('z'))     # -1
print(s.rfind('z'))    # -1

B)

print(s.index('l'))    # 2
print(s.rindex('l'))   # 3

try:
    print(s.index('z'))
except ValueError as e:
    print(f"ValueError: {e}") #ValueError: substring not found
try:
    print(s.rindex('z'))
except ValueError as e:
    print(f"ValueError: {e}") #ValueError: substring not found


C)

B
```

---

## Task 3 — `sys` module [PCAP standard library section]

**TEACH — key sys attributes:**
```python
import sys
sys.argv          # list of command-line args: argv[0] = script name
sys.path          # list of directories Python searches for modules
sys.modules       # dict of all currently imported modules (cached)
sys.stdin         # standard input stream
sys.stdout        # standard output stream
sys.stderr        # standard error stream
sys.exit(code)    # exit interpreter; code=0 is clean exit
sys.version       # Python version string: '3.11.4 (main, ...)'
sys.platform      # 'win32', 'linux', 'darwin'
```

**TEACH — `sys.modules` caching (exam trap):**
```python
import mymodule          # loads, executes, caches in sys.modules
import mymodule          # does NOT reload — returns cached version
# State mutations from first import PERSIST on re-import
```

**A)** True or False:
```
1. sys.argv[0] is the first argument passed to the script (not the script name)
2. sys.path can be modified at runtime to add new import directories
3. import X twice always re-executes the module code
4. sys.exit(0) raises SystemExit
5. sys.platform returns 'windows' on Windows
6. sys.modules is a dictionary
```

**B)** Given this file `script.py` called as `python script.py foo bar`:
```python
import sys
print(sys.argv[0])
print(sys.argv[1])
print(len(sys.argv))
```
Predict the output.

**C)** Predict — sys.modules caching:
```python
import sys

import os
import os    # second import
print(len([k for k in sys.modules if 'os' in k]))   # how many 'os'-related entries?
print('os' in sys.modules)
print(type(sys.modules['os']))
```

Write answers here:
```
A) 1-6:
# 1. sys.argv[0] is the first argument passed to the script (not the script name) #FALSE
# 2. sys.path can be modified at runtime to add new import directories #True
# 3. import X twice always re-executes the module code #False
# 4. sys.exit(0) raises SystemExit #True
# 5. sys.platform returns 'windows' on Windows #False, win32
# 6. sys.modules is a dictionary #True


B)
print(sys.argv[0]) #practice.py
#print(sys.argv[1]) #IndexError
print(len(sys.argv)) #1


C)
print(len([k for k in sys.modules if 'os' in k]))   # how many 'os'-related entries? #2
print('os' in sys.modules) #True
print(type(sys.modules['os'])) #module

```

---

## Task 4 — `os` module deeper cut [Real exam expansion]

**TEACH — all testable `os` functions:**
```python
import os

os.getcwd()                  # current working directory
os.chdir(path)               # change working directory
os.listdir(path)             # list contents of directory
os.mkdir(path)               # create directory (fails if exists)
os.makedirs(path)            # create dirs recursively
os.remove(path)              # delete a FILE
os.rmdir(path)               # delete an empty DIRECTORY
os.rename(src, dst)          # rename file or directory

os.path.exists(path)         # True/False
os.path.isfile(path)         # True only if it's a file
os.path.isdir(path)          # True only if it's a directory
os.path.join(a, b, c)        # OS-safe path join
os.path.split(path)          # returns (dir, filename) tuple
os.path.splitext(path)       # returns (path_without_ext, ext) tuple
os.path.basename(path)       # filename only
os.path.dirname(path)        # directory only
os.path.abspath(path)        # absolute path

os.sep                       # '\\' Windows, '/' Unix
os.name                      # 'nt' Windows, 'posix' Unix
os.linesep                   # '\r\n' Windows, '\n' Unix
```

**A)** Predict each:
```python
import os
path = '/home/user/projects/data/prices.csv'

print(os.path.basename(path))       # prices.csv
print(os.path.dirname(path))        # /home/user/projects/data
print(os.path.split(path))          # ?  ('/home/user/projects/data', 'prices.csv')
print(os.path.splitext(path))       # ?  ('/home/user/projects/data/prices', '.csv')
```

**B)** True or False:
```
1. os.remove() can delete a directory #False
2. os.rmdir() can delete a non-empty directory #False
3. os.path.split('/foo/bar.txt') returns ('/foo', 'bar.txt') #True
4. os.path.join('a', 'b', 'c') returns 'a/b/c' on Unix #True
5. os.name == 'nt' on Windows #True
6. os.linesep == '\n' on Windows #False - \r\n
```

**C)** Multiple choice — what does `os.path.splitext('/data/prices.csv')` return?
- A: `('/data/prices', '.csv')`
- B: `('/data/', 'prices.csv')`
- C: `('prices', '.csv')`
- D: `('/data/prices.csv', '')`

Write answers here: 
```
A)

print(os.path.basename(path))       # prices.csv
print(os.path.dirname(path))        # /home/user/projects/data
print(os.path.split(path))          # ?  ('/home/user/projects/data', 'prices.csv')
print(os.path.splitext(path))       # ?  ('/home/user/projects/data/prices', '.csv')

B) 1-6:

1. os.remove() can delete a directory #False
2. os.rmdir() can delete a non-empty directory #False
3. os.path.split('/foo/bar.txt') returns ('/foo', 'bar.txt') #True
4. os.path.join('a', 'b', 'c') returns 'a/b/c' on Unix #True
5. os.name == 'nt' on Windows #True
6. os.linesep == '\n' on Windows #False - \r\n

C)
A
```

---

## Task 5 — Exception propagation: conflicting raise/except chains

**TEACH — the pattern that confused you in T7C:**
```
raise X in try
  → except X catches it → return "caught" is queued
  → finally runs (no return in finally)
  → "caught" returns
```
VS:
```
raise X in try
  → except Y (wrong type) — doesn't catch
  → finally runs
  → X propagates OUT (uncaught)
```
VS:
```
raise X in except handler
  → finally runs
  → NEW exception (X) propagates — original is suppressed
```

**A)** Predict — exception in except handler:
```python
def f():
    try:
        raise ValueError("first")
    except ValueError:
        raise RuntimeError("second")   # new exception raised in handler
    finally:
        print("finally")

try:
    f()
except RuntimeError as e:
    print(f"caught: {e}")
```

**B)** Predict — wrong except type:
```python
def g():
    try:
        raise KeyError("missing")
    except ValueError:
        return "value error caught"
    finally:
        print("cleanup")

try:
    g()
except KeyError as e:
    print(f"key error: {e}")
```

**C)** Predict — exception chain (`raise X from Y`):
```python
try:
    try:
        1 / 0
    except ZeroDivisionError as e:
        raise ValueError("bad input") from e
except ValueError as e:
    print(type(e).__name__)
    print(type(e.__cause__).__name__)
```

Write answers here:
```
A)
# 1. inner raise is carried out by the ValueError handler - it raises RuntimeError (which is caught by the outer try/except block)
# 2. At the same time, finally is printed, as it always is.
# 3. The outer except RuntimeError handle catches the Runtime Error and prints caught: second (the msg from the handle + the message from the raise)

#finally
#caught: second

B)
#1 - KeyError is raised but there's no handler for it in the g() function
#2 - it propagates to the outside and is handler by the KeyError handler there printing - key error: missing
#3 cleanup is printed, as the last element of the g() function from the finally block

#I just tested it and I was wrong with the order - it's actualy cleanup -> key error: 'missing'.
#I don't understand why though - how to determine what is first - the inner finally or the outer message?

C)    

#The division raises the handler with ZeroDivisionError, but the handler raises ValueError found in the outer try/except block.
#The outer block prints ZeroDivisionError , ZeroDivisionError
#I was FUCKING WRONG AGAIN, BUT WHY!!!
#In the exam trap there was a KeyError handled by the BaseException handler, but it still fucking printed KeyError there....
#Here it's different. It's so FUCKING CONFUSING AND EASY TO GET LOST HERE....

```

---

## Task 6 — PCAP simulation: strings + modules [Exam style]

**Q1.** What does `"hello world".split()` return?
- A: `['hello', 'world']`
- B: `['hello', ' ', 'world']`
- C: `['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']`
- D: `('hello', 'world')`

**Q2.** What is the output?
```python
s = "abcde"
print(s[1:4:2])
```
- A: `bcd`
- B: `bd`
- C: `bc`
- D: `ce`

**Q3.** Which `sys` attribute is a LIST (not dict, not string)?
- A: `sys.modules`
- B: `sys.path`
- C: `sys.version`
- D: `sys.platform`

**Q4.** What does `os.path.split('/foo/bar/baz.txt')` return?
- A: `('/foo/bar', 'baz.txt')`
- B: `('/foo/bar/baz', '.txt')`
- C: `['foo', 'bar', 'baz.txt']`
- D: `('/foo/bar/baz.txt', '')`

**Q5.** What is the output?
```python
s = "ABCDE"
print(s[-1] + s[-2::-1])
```
- A: `EABCD`
- B: `EDCBA`
- C: `Edcba`
- D: `ABCDE`

Write answers here:
```
Q1: A
Q2: B
Q3: B
Q4: A
Q5: B
```

---

## Task 7 — `str.join`, `str.startswith`, `str.endswith` [Exam completeness]

**TEACH:**
```python
', '.join(['a', 'b', 'c'])      # 'a, b, c' — separator is the string, not argument
'hello'.startswith('he')        # True
'hello'.endswith('lo')          # True
'hello'.startswith(('he', 'wo'))  # True — accepts tuple of prefixes!
```

**A)** Predict:
```python
words = ['Python', 'is', 'great']
print(' '.join(words)) #Python is great
print('-'.join(words)) #Python-is-great
print(''.join(words)) #Pythonisgreat
print(', '.join(str(i) for i in range(5))) #0,1,2,3,4
```

**B)** Predict:
```python
s = "hello.py"
print(s.startswith('hello'))
print(s.endswith('.py'))
print(s.endswith(('.py', '.txt', '.csv')))   # tuple form!
print(s.startswith(('foo', 'bar', 'hello')))
```

**C)** What is the output?
```python
files = ['data.csv', 'model.py', 'notes.txt', 'train.py']
py_files = [f for f in files if f.endswith('.py')]
print(py_files)
print(', '.join(py_files))
```

Write answers here:
```
A)
print(' '.join(words)) #Python is great
print('-'.join(words)) #Python-is-great
print(''.join(words)) #Pythonisgreat
print(', '.join(str(i) for i in range(5))) #0, 1, 2, 3, 4


B)
print(s.startswith('hello')) #True
print(s.endswith('.py')) #True
print(s.endswith(('.py', '.txt', '.csv')))  #True
print(s.startswith(('foo', 'bar', 'hello'))) #True

C)
print(py_files) #['model.py', 'train.py']
print(', '.join(py_files)) #'model.py, train.py'

```

---

## Task 8 — PROJECT: Fix PositionManager iterator + multi-strategy test

**The bug:** In [algo_backtest/engine/backtest_engine.py](algo_backtest/engine/backtest_engine.py) line 168:
```python
filtered_positions = [position for position in self.position_manager ...]
```
`self.position_manager` is a `PositionManager` object — it has no `__iter__`. Fix: iterate over `.positions` list instead.

**Step A — Fix the bug:**
In `force_close_all`, change:
```python
filtered_positions = [position for position in self.position_manager
                      if (ticker == position.ticker and position.strategy_id == strategy_id)]
```
to:
```python
filtered_positions = [position for position in self.position_manager.positions
                      if (ticker == position.ticker and position.strategy_id == strategy_id)]
```

**Step B — Run with TWO strategies:**
In `main.py`, add a second strategy with different parameters:
```python
strategies = [
    LPPStrategy('FDAX', 'BUY', 'LR1_LR2_075', 'LPP_LR1_050', 'LR2_LR3_050'),
    LPPStrategy('FDAX', 'BUY', 'LR2_LR3_025', 'LR1_LR2_050', 'LR3_LR2_050'),
]
```
Run it. Paste the full `strategy_report()` output.

**Step C — Sample trade inspection:**
After `run_backtest`, add to `main.py`:
```python
for trade in test_engine.completed_trades[:5]:
    print(trade)
```
Verify the trade objects print meaningful info. If `__str__` on Trade isn't implemented, paste what you see.

```
Fix A applied: yes/no
Yes.

Output with 2 strategies:
BacktestEngine: 0 open | 209 closed | PnL: $-94.0
--- LPP Strategy (ID: 0997260a-5e17-40a9-b1eb-b40476dc0597) ---

                  Trades: 93
                  Win Rate: 48.38709677419355%
                  Total PnL: $137.00
                  Avg R: 0.02R


--- LPP Strategy (ID: ac0aae21-e02f-4fab-939b-c7b413b77dc5) ---

                  Trades: 116
                  Win Rate: 38.793103448275865%
                  Total PnL: $-231.00
                  Avg R: -0.04R


--- PORTFOLIO TOTAL  ---

                  Trades: 209
                  Win Rate: 43.0622009569378%
                  Total PnL: $-94.0
                  Avg R: -0.02R


Sample trades output:

[@LPP Strategy | aa16877a-0a00-49cd-ab76-f42d2f4a3ac9] Trade 93aec15b-d4c1-4921-ad5d-d64d60a67407: [LOSS] BUY 1 FDAX: 22711.0 -> 22708.0 (still open) | P&L: $-3.00
[@LPP Strategy | b26fc541-fe1c-40b6-b15f-66570e6438f7] Trade 43df0ba3-cb7a-43b6-9ba4-f465968f7b32: [LOSS] BUY 1 FDAX: 22744.0 -> 22744.0 (still open) | P&L: $0.00
[@LPP Strategy | aa16877a-0a00-49cd-ab76-f42d2f4a3ac9] Trade a643ee42-127b-4a7f-86e0-7183b78bfeeb: [LOSS] BUY 1 FDAX: 22691.0 -> 22688.0 (still open) | P&L: $-3.00
[@LPP Strategy | b26fc541-fe1c-40b6-b15f-66570e6438f7] Trade 645ccc8b-533c-41c8-a370-93060eec71b4: [WIN] BUY 1 FDAX: 22729.0 -> 22744.0 (still open) | P&L: $15.00
[@LPP Strategy | aa16877a-0a00-49cd-ab76-f42d2f4a3ac9] Trade ec1a780f-cb27-44e1-8c7f-bd91bbc31066: [WIN] BUY 1 FDAX: 22780.0 -> 22790.0 (still open) | P&L: $10.00


Any new errors?

Everything seems to work fine, except for the still open label in the completed trades.
It could be a simple labeling error though.
```
