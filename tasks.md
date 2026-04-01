# Week 12 Day 3 — Strings, Closures, Generators + run_backtest Fix
**Date:** 2026-04-01 | **Focus:** Strings deep dive, closures/nonlocal, generators, + 3 run_backtest bugs fixed

---

## Task 1 — String methods trap shoot [PCAP string section]

**TEACH — The methods that trip people up:**
```python
str.find(sub)      → returns index or -1  (no exception)
str.index(sub)     → returns index or raises ValueError
str.count(sub)     → non-overlapping occurrences
str.split(sep)     → default sep=None splits on ANY whitespace, strips leading/trailing
str.split(' ')     → splits on single space only — '' entries for multiple spaces!
str.strip()        → removes BOTH ends
str.lstrip()       → left only
str.rstrip()       → right only
str.replace(a, b)  → replaces ALL occurrences by default
str.replace(a, b, n) → replaces at most n occurrences
```

**A)** Predict the output:
```python
s = "  hello world  "
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print(len(s))
print(len(s.strip()))
```

**B)** Predict each — watch the split trap:
```python
s = "a  b  c"
print(s.split())      # default — splits on any whitespace
print(s.split(' '))   # explicit space — different result!
print(s.count('a'))
print(s.find('z'))
print(s.index('b'))
```

**C)** Predict:
```python
s = "banana"
print(s.replace('a', 'o'))
print(s.replace('a', 'o', 2))
print(s.count('a'))
print(s.count('an'))
```

Write answers here:
```
A)

s = "  hello world  "
print(s.strip()) #"hello world"
print(s.lstrip()) #"hello world  "
print(s.rstrip()) #"  hello world"
print(len(s))  #15
print(len(s.strip())) #11
B)
print(s.split())    #['a', 'b', 'c']
print(s.split(' '))   #['a', '', 'b', '', 'c']
print(s.count('a')) #1
print(s.find('z')) #-1
print(s.index('b')) #3
C)
print(s.replace('a', 'o'))  #bonono
print(s.replace('a', 'o', 2)) #bonona
print(s.count('a')) #3
print(s.count('an')) #2

But it doesn't clear our the sexamples from the PCAP exam - there was also something as rindex, or something like that.

```

---

## Task 2 — String formatting + escape sequences [PCAP trap zone]

**TEACH — Escape sequences to know:**
```
\n   → newline
\t   → tab
\\   → literal backslash
\'   → literal single quote (inside single-quoted string)
\"   → literal double quote
\r   → carriage return (cursor to start of line, does NOT add newline)
```

**TEACH — `\r` trap:**
```python
print("hello\rworld")   # 'world' overwrites 'hello' from position 0
# Output on most terminals: 'world'
# But len("hello\rworld") = 11  — \r is ONE character
```

**A)** Predict the output:
```python
print("line1\nline2")
print("col1\tcol2")
print("back\\slash")
print(len("a\tb"))
print(len("a\\b"))
print(len("\n"))
```

**B)** What is the length and value printed?
```python
s1 = '\''
s2 = "\""
s3 = '\\\''
s4 = "\\\""

print(len(s1), s1)
print(len(s2), s2)
print(len(s3), s3)
print(len(s4), s4)
```

**C)** Predict — the `\r` trap:
```python
print("AAAA\rBB")
print(len("AAAA\rBB"))
```

Write answers here:
```
A)
print("line1\nline2") #line1(new line)line2
print("col1\tcol2") #col1   col2
print("back\\slash") #back\slash
print(len("a\tb")) #a   b
print(len("a\\b")) #a\b
print(len("\n")) # '(new line)'

B)
s1 = '\'' #"'"", 1
s2 = "\"" # """, 1
s3 = '\\\'' # "\'" 2
s4 = "\\\"" # "\""2


C)
print("AAAA\rBB") #BBAA - this is a bit weird
print(len("AAAA\rBB")) #7 -- also werid, we count all characters + /r as 1




```

---

## Task 3 — Closures and `nonlocal` [PCAP closures section]

**TEACH — closure captures the VARIABLE, not the value:**
```python
def make_adder(n):
    def add(x):
        return x + n    # n is captured by reference
    return add

add5 = make_adder(5)
print(add5(3))    # 8 — n=5 is still alive in the closure
```

**TEACH — the classic loop-closure trap:**
```python
funcs = [lambda: i for i in range(3)]
print(funcs[0]())   # 2 — NOT 0! All lambdas share the SAME i variable
print(funcs[1]())   # 2
print(funcs[2]())   # 2
# Fix: lambda i=i: i  (default arg captures the VALUE at creation time)

#I KNOW THAT NIGGA, NO NEED TO REPEAT THIS PARTICULAR PATTENR
```

**TEACH — `nonlocal`:**
- `nonlocal x` lets you WRITE to an enclosing (non-global) scope variable
- Without it, assigning `x = ...` creates a LOCAL variable, shadowing the outer one
- Reading without assignment doesn't need `nonlocal`

**A)** Predict the output:
```python
def outer():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

f = outer()
print(f())
print(f())
print(f())



```

**B)** Predict — WITHOUT nonlocal (common exam trap):
```python
def outer():
    x = 10
    def inner():
        x = 20        # creates LOCAL x, does NOT modify outer x
        return x
    inner()
    return x

print(outer())
```

**C)** Predict — the loop closure trap:
```python
funcs = []
for i in range(4):
    funcs.append(lambda: i)

print(funcs[0]())
print(funcs[2]())
print(funcs[3]())
```

**D)** Fix the loop closure — use default arg to capture value:
```python
funcs = []
for i in range(4):
    funcs.append(lambda i=i: i)   # i=i captures current value

print(funcs[0]())
print(funcs[2]())
print(funcs[3]())
```

Write answers here:
```
A) 1, 2, 3

B) 10

C) 3, 3, 3 - but I know this pattern well already, no need to focus on it - focus on PCAP gaps and problems we've mentioned and shown - patterns that actually appeared on the exam and possible difficulties/traps, as this is what builds the PCAP exam

D) 0, 2, 3
```

---

## Task 4 — Generators: `yield`, `next()`, `StopIteration` [PCAP generators section]

**TEACH:**
```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
next(g)   # 1
next(g)   # 2
next(g)   # 3
next(g)   # StopIteration raised

# A generator PAUSES at each yield and resumes on next()
# The function frame stays alive between calls
```

**TEACH — `yield` with early return:**
```python
def gen():
    yield 1
    return          # legal — causes StopIteration immediately
    yield 2         # NEVER reached

list(gen())    # [1]
```

**TEACH — `yield` in a loop:**
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

list(countdown(3))   # [3, 2, 1]
```

**A)** Predict the output:
```python
def gen():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")

g = gen()
print(next(g))
print(next(g))
print("done")
```

**B)** Predict — early return:
```python
def gen(flag):
    yield 1
    if flag:
        return
    yield 2
    yield 3

print(list(gen(True)))
print(list(gen(False)))
```

**C)** Predict — generator with loop:
```python
def evens_up_to(n):
    i = 0
    while i <= n:
        if i % 2 == 0:
            yield i
        i += 1

result = list(evens_up_to(8))
print(result)
print(sum(evens_up_to(6)))
```

Write answers here:
```
A) 
# g = gen() #start
# print(next(g)) #1
# print(next(g)) #middle\n2
# print("done") #done

B)
print(list(gen(True))) #[1]
print(list(gen(False))) #[1, 2, 3]


C)
print(result) #[0, 2, 4, 6, 8]
print(sum(evens_up_to(6))) #12
```

---

## Task 5 — `hasattr` vs `__dict__` — the Day 2 gap

**TEACH — exactly what tripped you up yesterday:**
```python
hasattr(obj, 'name')          # checks the full MRO chain — inherited counts!
'name' in SomeClass.__dict__  # checks ONLY this class's own namespace

# They are NOT the same:
class A:
    def foo(self): pass

class B(A): pass

hasattr(B, 'foo')        # True — inherited from A
'foo' in B.__dict__      # False — not defined IN B
'foo' in A.__dict__      # True — defined IN A
```

**A)** Given:
```python
class Shape:
    color = 'red'
    def area(self): return 0

class Circle(Shape):
    def __init__(self, r):
        self.radius = r
    def area(self):
        return 3.14 * self.radius ** 2

c = Circle(5)
```
Predict True or False:
```python
print(hasattr(c, 'color'))           # ?
print(hasattr(c, 'area'))            # ?
print(hasattr(c, 'radius'))          # ?
print('color' in Circle.__dict__)    # ?
print('area' in Circle.__dict__)     # ?
print('area' in Shape.__dict__)      # ?
print('radius' in Circle.__dict__)   # ?
print('radius' in c.__dict__)        # ?
```

**B)** True or False — which expressions return True?
```python
print('color' in c.__dict__)         # ?
print('color' in Shape.__dict__)     # ?
print(hasattr(Shape, 'area'))        # ?
print(hasattr(Circle, 'color'))      # ?
```

Write answers here:
```
A) 8 results:

print(hasattr(c, 'color'))           # True
print(hasattr(c, 'area'))            # True
print(hasattr(c, 'radius'))          # True
print('color' in Circle.__dict__)    # False
print('area' in Circle.__dict__)     # True
print('area' in Shape.__dict__)      # True
print('radius' in Circle.__dict__)   # False - this is very tricky! It's not instantiated so it's not present there
print('radius' in c.__dict__)        # True

B) 4 results:

print('color' in c.__dict__)         # False
print('color' in Shape.__dict__)     # True
print(hasattr(Shape, 'area'))        # True
print(hasattr(Circle, 'color'))      # True

```

---

## Task 6 — PCAP simulation: mixed multi-topic [Exam style]

Answer A/B/C/D — no code needed, reason through each.

**Q1.** What is the output?
```python
def f(x=[]):
    x.append(1)
    return x

print(f())
print(f())
print(f())
```
- A: `[1]`, `[1]`, `[1]`
- B: `[1]`, `[1, 1]`, `[1, 1, 1]`
- C: `[]`, `[]`, `[]`
- D: `TypeError`

B - it's a mutable default parameter which adds an extra 1 with each function call.

**Q2.** Which is True about generators?
- A: A generator function must contain a `return` statement #Not true - return kinda crashes generator from normal working
- B: Calling a generator function immediately executes its body #Not true, we have to call next()
- C: `next()` on an exhausted generator raises `StopIteration` #True
- D: Generator objects can be iterated multiple times #Not True, in their simple form they're only iterable once and then exhausted

C

**Q3.** What does this print?
```python
x = 5
def foo():
    x = 10
    def bar():
        return x
    return bar()

print(foo())
print(x)
```
- A: `10`, `5`
- B: `5`, `5`
- C: `10`, `10`
- D: `NameError`

A


**Q4.** What is the output?
```python
s = "abcde"
print(s[1:4])
print(s[::-1])
print(s[::2])
print(s[-2:])
```
- A: `bcd`, `edcba`, `ace`, `de`
- B: `bcd`, `edcba`, `bd`, `de`
- C: `bcde`, `edcba`, `ace`, `de`
- D: `bcd`, `abcde`, `ace`, `cd`

A


**Q5.** What is the output?
```python
try:
    raise ValueError("oops")
except ValueError as e:
    result = str(e)
except:
    result = "other"
finally:
    result += "!"

print(result)
```
- A: `oops!`
- B: `ValueError: oops!`
- C: `oops`
- D: `other!`



Write answers here:
```
Q1: B
Q2: C
Q3: A 
Q4: A
Q5: A
```

---

## Task 7 — `finally` + `return` interaction [PCAP trap]

**TEACH:**
```python
# finally ALWAYS runs — even if return or raise happened
# If finally has its own return, it OVERRIDES the try/except return

def foo():
    try:
        return 1
    finally:
        return 2    # ← this return wins

print(foo())   # 2
```

**A)** Predict the output:
```python
def f():
    try:
        return "try"
    except:
        return "except"
    finally:
        return "finally"

print(f())
```

**B)** Predict — finally runs but doesn't return:
```python
def g():
    try:
        return 10
    finally:
        print("cleanup")

print(g())
```

**C)** Predict — exception + finally:
```python
def h():
    try:
        raise RuntimeError("boom")
    except RuntimeError:
        return "caught"
    finally:
        print("always")

print(h())
```

Write answers here:
```
A) finally

B) cleanup, 10

C) always, caught
```

---

## Task 8 — PROJECT: Fix run_backtest — 3 bugs [Diagnosed in Day 2]

Three bugs were identified. Fix them one at a time in [algo_backtest/main.py](algo_backtest/main.py).

**Fix 1 — Remove the diagnostic `break` and debug `print`**
Lines 46-47 in current main.py:
```python
print(strategy.levels_by_date[current_date])
break
```
Delete both lines. The inner loop is currently unreachable dead code because of this `break`.



**Fix 2 — One-trade-per-day constraint**
After the prep pass, add a `traded_today` dict:
```python
traded_today = {strategy: None for strategy in strategies}
```
Then inside the per-row loop, after computing `current_date`:
- If `traded_today[strategy] == current_date` → skip signal generation (already traded today)
- When a position opens → set `traded_today[strategy] = current_date`

**Fix 3 — `newly_closed` references wrong strategy variable**
Current (buggy):
```python
newly_closed = backtest_engine.process_price('FDAX', row['close'])
if newly_closed:
    current_positions[strategy] = None   # ← `strategy` = last loop var

I've used shift tab to change the scope here.
```
This must be INSIDE the `for strategy in strategies` loop, using the correct `strategy` reference.

After all 3 fixes, run `python algo_backtest/main.py` and paste the output.

BacktestEngine: 0 open | 93 closed | PnL: $137.0
--- LPP Strategy (ID: 7b70378f-58c3-4a0d-9e4d-da884bc3c0f7) ---

                  Trades: 93
                  Win Rate: 48.38709677419355%
                  Total PnL: $137.00
                  Avg R: 0.02R


--- PORTFOLIO TOTAL  ---

                  Trades: 93
                  Win Rate: 48.38709677419355%
                  Total PnL: $137.0
                  Avg R: 0.02R


```
Fix 1 applied: yes/no
Dude, I told you already that 'break' WAS ADDED ON PURPOSE to diagnose if the prepare works properly. You didn't register that for some reason.
It's removed now.

Fix 2 code:

Fix 3 — where did you move process_price?

You can see the current run_backtest code properly fixed:

def run_backtest(df: pd.DataFrame, strategies: list) -> BacktestEngine:
    backtest_engine = BacktestEngine()
    current_positions = {strategy: None for strategy in strategies}
    traded_today = {strategy: None for strategy in strategies}

    for strategy in strategies:
        strategy.prepare(df)

    for _, row in df.iterrows():
        t = datetime.fromisoformat(row['candle_open']).time()
        current_date = datetime.fromisoformat(row['candle_open']).date()
        #print(strategy.levels_by_date[current_date])
    
        for strategy in strategies:
            start = strategy.session_start()
            end = strategy.session_end()
            is_rth = (start is None) or (start <= t <= end)
            session_ending = end is not None and t > end

            if session_ending and current_positions[strategy] is not None:
                backtest_engine.force_close_all('FDAX', strategy.strategy_id, row['open'])
                current_positions[strategy] = None
                continue

            if is_rth and traded_today[strategy] != current_date:
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
                    traded_today[strategy] = current_date

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
                    traded_today[strategy] = current_date

        newly_closed = backtest_engine.process_price('FDAX', row['close'])
        if newly_closed:
            current_positions[strategy] = None

    return backtest_engine


Output after all fixes:

Backtest 1 (First set of parameters using the LPP strategy)

2026-04-01 13:40:14,356 [DEBUG   ] engine.backtest_engine: Processing price for FDAX at $24981.0
BacktestEngine: 0 open | 93 closed | PnL: $137.0
--- LPP Strategy (ID: b6179065-c5e0-425a-941c-1aef1f346bc2) ---

                  Trades: 93
                  Win Rate: 48.38709677419355%
                  Total PnL: $137.00
                  Avg R: 0.02R


--- PORTFOLIO TOTAL  ---

                  Trades: 93
                  Win Rate: 48.38709677419355%
                  Total PnL: $137.0
                  Avg R: 0.02R

Backtest 2 (Different parameters):

--- LPP Strategy (ID: 38ba73c9-5e93-46ed-bc0b-4d4d5183f88c) ---

                  Trades: 116
                  Win Rate: 38.793103448275865%
                  Total PnL: $-231.00
                  Avg R: -0.04R


--- PORTFOLIO TOTAL  ---

                  Trades: 116
                  Win Rate: 38.793103448275865%
                  Total PnL: $-231.0
                  Avg R: -0.04R

Problems noticed: If I try to add the second strategy, we receive a TypeError informing that 
TypeError: 'PositionManager' object is not iterable.

We dfeinitely need to fix that next time.
Also, we could add a return of a list/dict of trades with all the relevant information somehow, so we could verify their relevance manually to test it properly.
Or at least a few of them
```
