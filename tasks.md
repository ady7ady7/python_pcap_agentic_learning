# Week 12 Day 2 — OOP Internals + Exception Propagation Chains
**Date:** 2026-03-31 | **Focus:** `__dict__`/`__bases__`/`__mro__` drills, assert propagation, name mangling, `isinstance` vs `type`, platform/os module, bytes/bytearray

---

## Task 1 — Assert propagation chains [Day 1 gap — T2B]

**TEACH — The propagation chain rule:**
Every exception, when raised, travels UP the call stack looking for a matching `except`.
If the `assert` is OUTSIDE the inner `try/except`, it bypasses it entirely.

```
foo() called
  → assert fires → AssertionError raised
  → NOT inside inner try → propagates OUT of foo()
  → outer try catches it
  → ArithmeticError? No. bare except? Yes → m += 1
```

**A)** Trace and predict the output of each — show step-by-step:

```python
# Snippet 1
x = 0

def bar(n):
    assert n > 0, "must be positive"
    try:
        return 100 / n
    except ZeroDivisionError:
        return -1

try:
    result = bar(0)
except AssertionError:
    x = 1
except:
    x = 2
print(x)
```

```python
# Snippet 2
count = 0

def process(val):
    assert isinstance(val, int), "not int"
    try:
        return val * 2
    except TypeError:
        return 0

try:
    process("hello")
except TypeError:
    count = 10
except AssertionError:
    count = 20
except:
    count = 30
print(count)
```

```python
# Snippet 3 — nested propagation
def inner(x):
    if x < 0:
        raise ValueError("negative")
    return x

def outer(x):
    try:
        return inner(x) * 2
    except TypeError:
        return -1

try:
    outer(-5)
except ValueError as e:
    print("caught:", e)
except:
    print("bare caught")
```

**B)** This is Q10 variant — same pattern, different exception. Trace it:
```python
m = 0

def foo(n):
    global m
    assert n > 0          # guard — fires if n <= 0
    try:
        return 10 / n
    except ArithmeticError:
        raise RuntimeError("math fail")

try:
    foo(-1)
except RuntimeError:
    m += 10
except AssertionError:
    m += 5
except:
    m += 1
print(m)
```

Write your answers here:
```
A) Snippet 1: step-by-step trace + output: #bar() is called with 0 as an argument.
1. assertion fails, but it's not handled in the function, so it's propagated outside to the outer try.
2. it's handled there and x is set to 1

Snippet 2: step-by-step trace + output: #process is called with 'hello' string as an argument
#the assertion fails, and it's not handled in the process function, so it would normally crash the code, but it's in the outer try block instead
#TypeError is ignored, as it's not the error type raised here
#It's handled by the except with AssertionError, setting the count to 20


Snippet 3: step-by-step trace + output: #outer is called with -5 as an argument
#outer calls inner with -5 as an argument in a try block
#inner does a check and since -5 is lower than 0, it raises ValueError with 'negative'
#since everything is put in a try/except block with ValueError handling, it prints caught: nagative

This example is very tricky and difficult to me at this point. I've got it right,but I still don't feel that confident when two different ValueError raises/handles coexist - it's very confusing.

B) trace + output: #foo is called with -1 as an argument
#foo properly grabs the value of m with global keyword
#foo runs an assertion for the argument, which fails, as -1 is lower than 0 
#It's NOT handled by the foo function , as it's put outside the try/except block there, so it propagates to the outside
#Since the whole foo call is put into a try/except block - there is a chance it will handle that exception
#It's handled by the except AssertionError handle, putting m at 5

5
```

---

## Task 2 — class `__dict__` vs instance `__dict__` [Day 1 gap — T4A]

**TEACH — The rule:**
```
class.__dict__    → contains: class variables, methods, class-level defs
instance.__dict__ → contains: instance variables (set via self.x = ...)
```
Instance attributes set in `__init__` via `self.x = ...` are ONLY in the instance's `__dict__`.
They do NOT appear in the class's `__dict__` — even though the class defined `__init__`.

```python
class Dog:
    species = "Canis lupus"    # class attr → in Dog.__dict__
    def __init__(self, name):
        self.name = name       # instance attr → in d.__dict__, NOT Dog.__dict__

d = Dog("Rex")
'species' in Dog.__dict__   # True
'name' in Dog.__dict__      # False  ← defined in __init__ but it's an INSTANCE attr
'name' in d.__dict__        # True
```

**A)** Given:
```python
class Vehicle:
    wheels = 4
    engine = "V6"

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self._speed = 0

    def accelerate(self):
        self._speed += 10
```
Predict True or False:
```python
v = Vehicle("Toyota", 2020)

print('wheels' in Vehicle.__dict__)      # ?
print('engine' in Vehicle.__dict__)      # ?
print('accelerate' in Vehicle.__dict__)  # ?
print('brand' in Vehicle.__dict__)       # ?
print('brand' in v.__dict__)             # ?
print('_speed' in v.__dict__)            # ?
print('wheels' in v.__dict__)            # ?  ← careful
print('__init__' in Vehicle.__dict__)    # ?
```

**B)** After calling `v.accelerate()` — what changes in `v.__dict__`?
```python
v.accelerate()
v.accelerate()
print(v.__dict__)    # predict the full output
```

**C)** True or False:
```python
class A:
    x = 1
    def __init__(self):
        self.x = 2       # shadows the class attr

a = A()
print('x' in A.__dict__)    # ?
print('x' in a.__dict__)    # ?
print(a.x)                  # ?  ← which x wins?
print(A.x)                  # ?
```

Write answers here:
```
A) wheels, engine, accelerate, brand(class), brand(instance), _speed, wheels(instance), __init__:

print('wheels' in Vehicle.__dict__)      #True
print('engine' in Vehicle.__dict__)      #True
print('accelerate' in Vehicle.__dict__)  #True
print('brand' in Vehicle.__dict__)       #False
print('brand' in v.__dict__)             #True
print('_speed' in v.__dict__)            #True
print('wheels' in v.__dict__)            #False
print('__init__' in Vehicle.__dict__)    #True

B) v.__dict__ after 2 accelerates:

{'brand': 'Toyota', 'year': 2020, '_speed': 20}

C) in A.__dict__, in a.__dict__, a.x, A.x:

print('x' in A.__dict__)    #True
print('x' in a.__dict__)    #True
print(a.x)                  #2
print(A.x)                  #1

```

---

## Task 3 — `isinstance` vs `type` — the exam trap

**TEACH:**
```python
type(obj) is SomeClass    → EXACT match only — ignores inheritance
isinstance(obj, SomeClass) → True if obj is SomeClass OR any subclass
```

Real exam loves to give you an inheritance chain and ask which is True.

**A)** Given:
```python
class Animal: pass
class Dog(Animal): pass
class GuideDog(Dog): pass

g = GuideDog()
```
Predict True or False:
```python
print(type(g) is GuideDog)      # ?
print(type(g) is Dog)           # ?
print(type(g) is Animal)        # ?
print(isinstance(g, GuideDog))  # ?
print(isinstance(g, Dog))       # ?
print(isinstance(g, Animal))    # ?
print(isinstance(g, object))    # ?
```

**B)** Multiple choice (PCAP style) — which TWO are True?
```python
class X: pass
class Y(X): pass
obj = Y()
```
- A: `type(obj) is X`
- B: `type(obj) is Y`
- C: `isinstance(obj, X)`
- D: `type(obj) == isinstance(obj, Y)`

**C)** Predict — what does this print?
```python
print(type(42) is int)
print(type(42) is float)
print(isinstance(42, (int, float)))    # tuple of types!
print(isinstance(True, int))           # ← tricky
print(type(True) is int)               # ← also tricky
```

Write answers here:
```
A) 7 results: 
print(type(g) is GuideDog)      # True
print(type(g) is Dog)           # False
print(type(g) is Animal)        # False
print(isinstance(g, GuideDog))  # True
print(isinstance(g, Dog))       # True
print(isinstance(g, Animal))    # True
print(isinstance(g, object))    # True

B) Two True options:

print(type(obj) is X) #False
print(type(obj) is Y) #True
print(isinstance(obj, X)) #True
print(type(obj) == isinstance(obj, Y)) #False



C) 5 results:

print(type(42) is int) #True
print(type(42) is float) #False
print(isinstance(42, (int, float)))  #True
print(isinstance(True, int))        #True
print(type(True) is int)        #False

```

---

## Task 4 — Name mangling: 3-level inheritance drill

**TEACH — recap:**
- `__x` in class `Foo` → stored as `_Foo__x`
- Every method is compiled where it's **defined** — the mangling is baked in at that point
- When you call `obj.method()`, Python resolves WHICH method via MRO, then runs that method's pre-compiled bytecode

**A)** Trace and predict ALL outputs:
```python
class Base:
    __secret = "base"
    def reveal(self):
        return self.__secret          # compiled: self._Base__secret

class Middle(Base):
    __secret = "middle"
    def reveal(self):
        return self.__secret          # compiled: self._Middle__secret

class Top(Middle):
    __secret = "top"
    # No reveal() defined

b = Base()
m = Middle()
t = Top()

print(b.reveal())           # ?
print(m.reveal())           # ?
print(t.reveal())           # ? ← KEY — which reveal() runs?
print(t._Top__secret)       # ?
print(t._Middle__secret)    # ?
print(t._Base__secret)      # ?
```

**B)** True or False:
```python
print(hasattr(Top, 'reveal'))         # ?
print(hasattr(Top, '_Top__secret'))   # ?
print(Top.__bases__ == (Middle,))     # ?
print(Middle in Top.__mro__)          # ?
print(Base in Top.__mro__)            # ?
print(len(Top.__mro__))               # ? (count: Top, Middle, Base, object)
```

Write answers here:
```
A) b.reveal(), m.reveal(), t.reveal(), t._Top__secret, t._Middle__secret, t._Base__secret:

print(b.reveal())           # 'base'
print(m.reveal())           # 'middle'
print(t.reveal())           # 'middle' - there's no reveal in Top, so Middle's reveal() runs
print(t._Top__secret)       # top
print(t._Middle__secret)    # middle
print(t._Base__secret)      # base



B) 6 results:

print(hasattr(Top, 'reveal'))         # False
print(hasattr(Top, '_Top__secret'))   # True
print(Top.__bases__ == (Middle,))     # True
print(Middle in Top.__mro__)          # True
print(Base in Top.__mro__)            # True
print(len(Top.__mro__))               # 4
```

---

## Task 5 — `__mro__` and `__bases__` combined drill

**A)** Given:
```python
class A: pass
class B(A): pass
class C(A): pass
class D(B): pass
class E(C, D): pass
```

Without running the code, draw the MRO for `E` using C3 linearization.
Then predict:
```python
print(E.__bases__)          # ?
print(E.__mro__)            # ? (list all classes in order)
print(len(E.__mro__))       # ?
print(A in E.__bases__)     # ?
print(A in E.__mro__)       # ?
print(B in E.__bases__)     # ?  ← careful
```

**B)** MRO conflict — will this raise a TypeError?
```python
class X: pass
class Y(X): pass
class Z(X, Y): pass    # ← is this valid?
```
Explain WHY — don't just say yes/no.

Write answers here:
```
A) __bases__, __mro__ (full list), len, A in bases, A in mro, B in bases:

print(E.__bases__)          #C, D
print(E.__mro__)            #E -> C -> D -> B -> A -> object
print(len(E.__mro__))       # 6
print(A in E.__bases__)     # False
print(A in E.__mro__)       # True
print(B in E.__bases__)     # False

B) Valid or TypeError? Explain:

TypeError, inheritance cannot go in reverse, e.g if X inherits from Y, Y cannot inherit from X later.
```

---

## Task 6 — `platform` and `os` module functions [Real exam Q1 + expansion]

**TEACH:**
```python
import platform
platform.platform()       # 'Windows-10-10.0.19041-SP0' — full string
platform.system()         # 'Windows' — just OS name
platform.node()           # hostname of machine
platform.python_version() # '3.11.4'
platform.uname()          # named tuple with ALL: system, node, release, version...

import os
os.getcwd()               # current working directory string
os.listdir(path)          # list of filenames in directory
os.path.exists(path)      # True/False
os.path.join(a, b)        # safe path joining (handles slashes)
os.path.basename(path)    # last component: '/foo/bar.txt' → 'bar.txt'
os.path.dirname(path)     # directory part: '/foo/bar.txt' → '/foo'
os.sep                    # path separator: '\\' on Windows, '/' on Unix
os.name                   # 'nt' on Windows, 'posix' on Unix/Mac
```

**A)** Multiple choice — which function returns EACH of these:

1. The string `'Windows'` (OS name only, no version)
2. A namedtuple with system, node, release, version, machine, processor
3. The Python version as a string like `'3.11.4'`
4. The full platform description string including version numbers

1 - platform.system()
2 - platform.uname()
3 - platform.python_version()
4 - platform.platform()

**B)** True or False about `os`:
```python
import os
# assume running on Windows
print(os.name == 'nt')           # True
print(os.sep == '\\')            # True
print(os.sep == '/')             # False
print(type(os.getcwd()) is str)  # True
```

**C)** Predict the output:
```python
import os
path = '/home/user/projects/algo/data/prices.csv'
print(os.path.basename(path))   # prices.csv
print(os.path.dirname(path))    # /home/user/projects/algo/data
print(os.path.exists(path))     # False
```

Write answers here:
```
A) 1-4: 1 - platform.system()
2 - platform.uname()
3 - platform.python_version()
4 - platform.platform()

B) 4 results:
print(os.name == 'nt')           # True
print(os.sep == '\\')            # True
print(os.sep == '/')             # False
print(type(os.getcwd()) is str)  # True

C) basename, dirname, exists:
print(os.path.basename(path))   # prices.csv
print(os.path.dirname(path))    # /home/user/projects/algo/data
print(os.path.exists(path))     # False

```

---

## Task 7 — bytes and bytearray [Real exam file I/O section]

**TEACH:**
```python
# bytes — IMMUTABLE sequence of integers 0-255
b = b"hello"
b[0]          # 104 (ASCII code of 'h')
b[0] = 65     # TypeError! bytes is immutable

# bytearray — MUTABLE bytes
ba = bytearray(b"hello")
ba[0] = 72    # OK → bytearray(b'Hello')
ba[0]         # 72

# Creating:
bytes(5)              # b'\x00\x00\x00\x00\x00' — 5 zero bytes
bytes([72, 101, 108]) # b'Hel' — from int list
bytearray(b"abc")     # mutable copy of bytes literal

# Encoding / decoding:
"hello".encode('utf-8')        # b'hello'
b"hello".decode('utf-8')       # 'hello'
```

**A)** Predict the output or error:
```python
b = b"Python"
print(b[0])                  # ?
print(type(b[0]))            # ?
print(len(b))                # ?
b[0] = 80                    # ?  ← error or not?
```

```python
ba = bytearray(b"Python")
ba[0] = 112                  # lowercase 'p' = 112
print(ba)                    # ?
print(ba.decode('utf-8'))    # ?
```

**B)** True or False:
```
1. bytes objects support item assignment #False
2. bytearray objects support item assignment #True
3. b"hello"[0] returns the integer 104 #WTF - DON'T ASK ME SUCH QUESTIONS..
4. bytearray(3) creates bytearray(b'\x00\x00\x00') #True
5. "abc".encode() returns b'abc' (default encoding is utf-8) #True
6. b"abc" == bytearray(b"abc")    ← careful #False
```

**C)** Predict output:
```python
data = bytearray(b"hello")
data.append(33)         # 33 = '!'
print(data.decode())    # 'hello!'
print(list(data))       # 'h', 'e', 'l', 'l', 'o', '!'
```

Write answers here:
```
A) b[0], type, len, b[0]=80 result:
   ba after assignment, decoded:

# print(b[0])                  # 80 - but I had to check that  - I won't remember it by heart, this shouldn't be the goal of this
# print(type(b[0]))            # int
# print(len(b))                # 6
# b[0] = 80                    # Error!
print(ba)                    # #bytearray(b'python')
print(ba.decode('utf-8'))    # python
   

B) 1-6:

1. bytes objects support item assignment #False
2. bytearray objects support item assignment #True
3. b"hello"[0] returns the integer 104 #WTF - DON'T ASK ME SUCH QUESTIONS..
4. bytearray(3) creates bytearray(b'\x00\x00\x00') #True
5. "abc".encode() returns b'abc' (default encoding is utf-8) #True
6. b"abc" == bytearray(b"abc")    ← careful #False


C) decoded, list:
print(data.decode())    # 'hello!'
print(list(data))       # 'h', 'e', 'l', 'l', 'o', '!' #in byte codes, which I don't know and DON'T EXPECT ME TO KNOW THEM BY HEART
```

---

## Task 8 — PROJECT: Verify LPPStrategy + debug run_backtest [Next project step]

The LPPStrategy was built last week but never fully tested end-to-end. Today: run it, fix what's broken.

**Step A — Read and check** [algo_backtest/strategies/lpp_strategy.py](algo_backtest/strategies/lpp_strategy.py):
- Does `prepare(df)` correctly filter the 09:00–10:00 window?
- Is `candle_open` being parsed as datetime (not string) before comparison?
- Are the sub-levels being computed (LR1_LR2_025, etc.)?

**Step B — Run it** from [algo_backtest/main.py](algo_backtest/main.py):
```bash
python -m algo_backtest.main
```
Note any errors or unexpected output.

**Step C — Fix one issue at a time.** Common suspects:
1. `candle_open` not parsed as datetime → `pd.to_datetime(data['candle_open'], utc=True)` at load time in DataLoader
2. `levels_by_date` empty because filter produces no rows → print a sample date key to verify
3. `generate_signal` key lookup fails → print available keys vs what's being looked up

Paste:
- The error or output you get
- What you identified as the root cause
- The fix you applied
- Confirmed output after fix

```
Output / error:

As for step A, I tried print out to debug the code and see what happens, and this is what I've got in run_backtest, at the beginning:

def run_backtest(df: pd.DataFrame, strategies: list) -> BacktestEngine:
    backtest_engine = BacktestEngine()
    current_positions = {strategy: None for strategy in strategies}


    for strategy in strategies:
        strategy.prepare(df)

    for _, row in df.iterrows():
        t = datetime.fromisoformat(row['candle_open']).time()
        current_date = datetime.fromisoformat(row['candle_open']).date()
        print(strategy.levels_by_date[current_date])
        break

Now for the testing code:

if __name__ == '__main__':
    
    x = DataLoader('algo_backtest\data\FDAX_M1_OHLC.csv')
    print(x)
    data = x.load_data()
    x.validate_data(data)
    print(len(data))
    print(data.head(3))
    
    setup_logging()
    print('Starting the backtest test procedure in main.py - logging set!')
    
    strategies = [LPPStrategy('FDAX', 'BUY', 'LR1_LR2_075', 'LPP_LR1_050', 'LR2_LR3_050')]
    test_engine = run_backtest(data, strategies)
    print(test_engine)
    test_engine.strategy_report()
    

And finally, the output:

$ python algo_backtest/main.py
C:\Users\HARDPC\Desktop\AL\projekty\python_pcap_agentic_learning\algo_backtest\main.py:96: SyntaxWarning: invalid escape sequence '\d'
  x = DataLoader('algo_backtest\data\FDAX_M1_OHLC.csv')
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
2026-03-31 14:52:24,223 [DEBUG   ] root: Logging in main initialized.
Starting the backtest test procedure in main.py - logging set!
{'LPP': np.float64(22917.0), 'LR1': np.float64(23070.0), 'LR2': np.float64(23352.0), 'LR3': np.float64(23505.0), 'LS1': np.float64(22635.0), 'LS2': np.float64(22482.0), 'LS3': np.float64(22200.0), 'LS3_LS2_025': np.float64(22270.5), 'LS3_LS2_050': np.float64(22341.0), 'LS3_LS2_075': np.float64(22411.5), 'LS2_LS1_025': np.float64(22520.25), 'LS2_LS1_050': np.float64(22558.5), 'LS2_LS1_075': np.float64(22596.75), 'LS1_LPP_025': np.float64(22705.5), 'LS1_LPP_050': np.float64(22776.0), 'LS1_LPP_075': np.float64(22846.5), 'LPP_LR1_025': np.float64(22955.25), 'LPP_LR1_050': np.float64(22993.5), 'LPP_LR1_075': np.float64(23031.75), 'LR1_LR2_025': np.float64(23140.5), 'LR1_LR2_050': np.float64(23211.0), 'LR1_LR2_075': np.float64(23281.5), 'LR2_LR3_025': np.float64(23390.25), 'LR2_LR3_050': np.float64(23428.5), 'LR2_LR3_075': np.float64(23466.75)}

The values seem to be calculated, but I'm not entirely sure they are then read properly, for whatever reason.
I'm also not sure the current logic allows to properly determine there's a position open and prevent from another positions opening.

This is the current logic - you can ignore the break part, as it's simply for diagnostics' sake, so that I won't trigger a massive iteration over all the rows for no reason. We're going step by step here.

def run_backtest(df: pd.DataFrame, strategies: list) -> BacktestEngine:
    backtest_engine = BacktestEngine()
    current_positions = {strategy: None for strategy in strategies}


    for strategy in strategies:
        strategy.prepare(df)

    for _, row in df.iterrows():
        t = datetime.fromisoformat(row['candle_open']).time()
        current_date = datetime.fromisoformat(row['candle_open']).date()
        print(strategy.levels_by_date[current_date])
        break
    
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
                
                if signal == 'HOLD':
                    pass
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



Root cause: I wasn't able to diagnose the root cause this time - the structure of run_backtest is a bit complex and I'm not sure what exactly happens or why there's so many positions opening. There clearly should be just one position that hits TP/SL and then doesn't open for that given day. Perhaps this constraint is not met. I can imagine a position opening once, hitting a TP/SL and opening again (since it's still above/below the desired level), and hitting a fake TP/SL again, something like that. Not sure if that could be the case, but perhaps IT IS.

Fix:

Output after fix:
```
