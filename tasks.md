# Week 12 Day 5 — String Comparisons + raise-from + Full Gap Closure
**Date:** 2026-04-03 | **Focus:** String ordering, raise X from Y, final gap sweep + Trade exit_reason fix + 2 mock exams

---

## Task 1 — String comparison: ordinal ordering [User request]

**TEACH — how Python compares strings:**
```
Comparison is character by character using Unicode ordinal (ord()) values.
First differing character determines the result.
If one string runs out of characters first → shorter string is "less than".
```

**Key ordinal values to know:**
```
'A'–'Z' = 65–90     (uppercase)
'a'–'z' = 97–122    (lowercase)
'0'–'9' = 48–57     (digits)

Rules:
  digits < uppercase < lowercase
  'A' < 'B' < ... < 'Z' < ... < 'a' < 'b' < ... < 'z'
  'a' > 'A'   (97 > 65)
  '9' < 'A'   (57 < 65)
```

**Comparison algorithm:**
```python
'abc' vs 'abd'
  'a'=='a' → tie, next
  'b'=='b' → tie, next
  'c' < 'd' → 'abc' < 'abd'

'aa' vs 'aaa'
  'a'=='a' → tie, next
  'a'=='a' → tie, next
  left runs out → 'aa' < 'aaa'
```

**A)** Predict True or False:
```python
print('abc' < 'abd')        # ?
print('aa' < 'aaa')         # ?
print('aa' > 'aaa')         # ?
print('abc' == 'abc')       # ?
print('A' < 'a')            # ?
print('Z' < 'a')            # ?
print('9' < 'A')            # ?
print('banana' > 'apple')   # ?  ← which letter decides?
print('Python' > 'python')  # ?  ← uppercase vs lowercase first char
```

**B)** Sort these strings as Python would — lowest to highest:
```
'z', 'A', '9', 'aa', 'aA', 'AA', 'Aa'
```
Write the sorted order and explain why.

**C)** Predict — mixed comparison:
```python
words = ['banana', 'Apple', 'cherry', 'apple', 'Banana']
print(sorted(words))    # ← what order does Python produce?
```

Write answers here:
```
A) 9 results:
print('abc' < 'abd')        # True
print('aa' < 'aaa')         #  True
print('aa' > 'aaa')         # False
print('abc' == 'abc')       # True
print('A' < 'a')            # True
print('Z' < 'a')            # True
print('9' < 'A')            # True
print('banana' > 'apple')   # True
print('Python' > 'python')  # False


B) Sorted order + explanation:
'9', 'A', 'AA', 'Aa', 'aA', 'aa', 'z'

#Digits < Uppercase < Lowercase, simple as that

C)
['Apple', 'Banana', 'apple', 'banana', 'cherry']
```

---

## Task 2 — `raise X from Y` — closed for good [T5C gap]

**TEACH — the complete mental model:**

```
raise ValueError("new") from original_exception
```

This creates a CHAIN:
- The outer world sees `ValueError` — that's what `except` catches
- The original exception is stored in `e.__cause__`
- `type(e)` → `ValueError`  (the NEW one)
- `type(e.__cause__)` → whatever the original was

**Analogy:** You're a manager. Employee (inner code) reports a broken database. You re-report it to your boss as "service unavailable". Your boss catches "service unavailable" (`ValueError`). The root cause (broken database = `ZeroDivisionError`) is stored in `__cause__` — it's the WHY, not the WHAT.

**What `type(e)` trap from earlier has in common:**
Both trap you into thinking about the ORIGINAL exception. For `type(e)`, it's the object class. For `raise X from Y`, `e` IS the new exception X, and `__cause__` is Y.

**A)** Predict ALL outputs:
```python
def f():
    try:
        int("abc")
    except ValueError as original:
        raise TypeError("bad type") from original

try:
    f()
except TypeError as e:
    print(type(e).__name__)            # what exception was caught?
    print(type(e.__cause__).__name__)  # what caused it?
    print(str(e))                      # message of the caught exception
    print(str(e.__cause__))            # message of the original
```

**B)** Without `from` — what is `__cause__`?
```python
try:
    try:
        1/0
    except ZeroDivisionError:
        raise RuntimeError("failed")   # no 'from'
except RuntimeError as e:
    print(type(e).__name__)
    print(e.__cause__)       # None — no explicit chain
    print(e.__context__)     # ZeroDivisionError — implicit context
```

**TEACH difference:**
```
raise X from Y    → sets e.__cause__ = Y  (explicit chain)
raise X           → sets e.__context__ = Y (implicit — Python sets it automatically)
                    e.__cause__ is None
```

**C)** Multiple choice — after `raise KeyError("k") from ValueError("v")` is caught as `e`:
- A: `type(e) is ValueError`
- B: `type(e) is KeyError`
- C: `e.__cause__ is None`
- D: `type(e.__cause__) is KeyError`

Write answers here:
```
A)
    print(type(e).__name__)            # TypeError
    print(type(e.__cause__).__name__)  # ValueError
    print(str(e))                      # bad type
    print(str(e.__cause__))            # Value Error's message


B) __cause__, __context__:

try:
    try:
        1/0
    except ZeroDivisionError: #triggered
        raise RuntimeError("failed")   #causes this
except RuntimeError as e: #triggered
    print(type(e).__name__) #RuntimeError
    print(e.__cause__)       #None
    print(e.__context__)     #division by zero - this is weird though - i hope there will be no such examples. I also don't recall cause and context in PCAP.

C)
B
```

---

## Task 3 — finally execution order: definitive drill [T5B gap]

**TEACH — the stack frame rule:**
```
finally belongs to the function it's WRITTEN IN.
It runs before control leaves that function — whether via return, raise, or fall-through.
The outer caller only gets control AFTER the inner function is done (including its finally).
```

**Stack trace for T5B:**
```
g() called
  → try: raise KeyError         ← raised
  → except ValueError: no match ← skipped
  → finally: print("cleanup")   ← runs NOW, inside g(), before g() exits
  → KeyError propagates out of g()
outer except KeyError: catches it → print("key error: ...")
```

**A)** Trace each — show execution ORDER:
```python
# Snippet 1
def inner():
    try:
        raise IndexError
    except ValueError:
        print("inner except")
    finally:
        print("inner finally")

try:
    inner()
except IndexError:
    print("outer except")
```

```python
# Snippet 2
def process():
    try:
        return "ok"
    finally:
        print("process finally")
        # no return here

result = process()
print(result)
```

```python
# Snippet 3 — finally with return overrides
def compute():
    try:
        return "try result"
    finally:
        return "finally result"   # overrides!

print(compute())
```

**B)** Fill in the blanks — what prints in what order?
```python
def a():
    try:
        raise RuntimeError
    finally:
        print("a-finally")

def b():
    try:
        a()
    except RuntimeError:
        print("b-except")
    finally:
        print("b-finally")

b()
```

Write answers here:
```
A) Snippet 1 order: 
def inner():
    try:
        raise IndexError #1. raised
    except ValueError:
        print("inner except")
    finally:
        print("inner finally") #2. printed, as we're going out of the inner function now, as the inexerror is not handled here

try:
    inner() 
except IndexError: #raised
    print("outer except") #printed
    
#inner finally
#outer except
   Snippet 2 order:

def process():
    try:
        return "ok" #1. returned
    finally:
        print("process finally") #2. still printed


result = process() #process finally - it prints first
print(result) #ok


   Snippet 3 output: print(compute()) #finally result

B) Order of prints:
def a():
    try:
        raise RuntimeError #1. raised and propagated outside
    finally:
        print("a-finally") #2 printed first, as we're leaving A

def b():
    try:
        a() 
    except RuntimeError: #3. raised, as we're handling the RuntimeError from a() which propagates to the outside
        print("b-except") #4. printed
    finally:
        print("b-finally") #5. printed

b()

```

---

## Task 4 — Full gap sweep: PCAP simulation [Everything from W12]

20-question rapid-fire. Answer A/B/C/D or True/False. No code needed — reason through each.

**Q1.** `type(e)` when catching `FileNotFoundError` with `except OSError` returns:
- A: `OSError`
- B: `FileNotFoundError`
- C: `Exception`
- D: Depends on how it was raised

**Q2.** `'hello'[1:4:2]` evaluates to:
- A: `'ell'`
- B: `'el'`
- C: `'eo'`  ← careful
- D: `'hlo'`

**Q3.** Which is True about `__bases__`?
- A: Contains the full MRO chain
- B: Contains only direct parent classes
- C: Is a list, not a tuple
- D: Always contains `object` as the first element

**Q4.** `'banana'.rindex('a')` returns:
- A: `1`
- B: `3`
- C: `5`
- D: `-1`

**Q5.** What does `sys.exit(1)` raise?
- A: `RuntimeError`
- B: `SystemExit`
- C: `ExitError`
- D: Nothing — it silently exits

**Q6.** `isinstance(True, int)` is:
- A: `False` — bool is not int
- B: `True` — bool is a subclass of int
- C: `TypeError`
- D: Depends on Python version

**Q7.** `os.path.split('/foo/bar.txt')` returns:
- A: `['/foo', 'bar.txt']`
- B: `('/foo', 'bar.txt')`
- C: `('/foo/bar', '.txt')`
- D: `('/foo/bar.txt', '')`

**Q8.** `lambda: 42` is:
- A: SyntaxError — lambda needs parameters
- B: Valid — returns 42 when called
- C: Valid — but always returns None
- D: Valid — but cannot be assigned to a variable

**Q9.** After `raise ValueError("x") from KeyError("y")`, caught as `e`:
- `type(e).__name__` is `'ValueError'` — True or False?
- `e.__cause__` is `None` — True or False?
- `type(e.__cause__).__name__` is `'KeyError'` — True or False?

**Q10.** `'aa' > 'aaa'` is:
- A: `True`
- B: `False`
- C: `TypeError`
- D: Depends on locale

**Q11.** `[x for x in range(5, 0, -1) if x % 2 == 0]` gives:
- A: `[2, 4]`
- B: `[4, 2]`
- C: `[2, 4, 0]`
- D: `[]`

**Q12.** `hasattr(Child, 'method')` where `method` is only defined in `Parent(Child inherits from)`:
- A: `False` — not defined in Child
- B: `True` — inherited
- C: `AttributeError`
- D: Depends on the method type

**Q13.** `b"hello"[0]` returns:
- A: `'h'`
- B: `104` (int)
- C: `b'h'`
- D: `TypeError`

**Q14.** Default mode of `open('file.txt')`:
- A: `'w'`
- B: `'a'`
- C: `'r'`
- D: `'x'`

**Q15.** Which correctly imports platform and gets the OS name string only (e.g., `'Windows'`):
- A: `platform.platform()`
- B: `platform.uname()`
- C: `platform.system()`
- D: `platform.os()`

**Q16.** Name mangling: `class Foo` with `__x = 1` — the attribute is stored as:
- A: `__x`
- B: `_x`
- C: `_Foo__x`
- D: `Foo__x`

**Q17.** `nonlocal x` inside a nested function:
- A: Makes `x` global
- B: Allows writing to the enclosing (non-global) scope's `x`
- C: Creates a new local `x`
- D: Is only valid if `x` is a list or dict

**Q18.** A generator function with `yield` — when is its body first executed?
- A: When the function is defined
- B: When the function is called (returns generator object)
- C: When `next()` is first called on the returned generator
- D: When the generator is assigned to a variable

**Q19.** `os.name` on Windows returns:
- A: `'windows'`
- B: `'win32'`
- C: `'nt'`
- D: `'Windows'`

**Q20.** `'Python'[0] > 'python'[0]` is:
- A: `True`
- B: `False`  ← 'P'=80, 'p'=112
- C: `TypeError`
- D: Depends on encoding

Write answers here:
```
Q1–Q10: B; B; B; C; B; B; B; B; True, False, True; B

Q11–Q20: B; A; B; C; C; C; B; C; C; B
```

---

## Task 5 — String comparison harder patterns

**A)** Predict — multi-character comparisons:
```python
print('abc' < 'b')         # first char decides: 'a' < 'b'
print('ABC' < 'abc')       # uppercase vs lowercase
print('abc' < 'abcd')      # same prefix, shorter loses
print('abcd' < 'abce')     # last char decides
print('1python' < 'Python') # digit vs uppercase
print('' < 'a')            # empty string
```

**B)** What does `sorted()` produce?
```python
items = ['cherry', 'Apple', 'banana', 'CHERRY', '1apple']
print(sorted(items))
```

**C)** Predict — `min()` and `max()` on strings:
```python
print(min('a', 'A', '1', 'z'))
print(max('a', 'A', '1', 'z'))
```

Write answers here:
```
A) 6 results: True, True, True, True, True, True

B) ['1apple', 'Apple', 'CHERRY', 'banana', 'cherry']

C) 1, z
```

---

## Task 6 — PROJECT: Fix Trade exit_reason "still open" bug

**The bug:** In `process_price` ([algo_backtest/engine/backtest_engine.py:119](algo_backtest/engine/backtest_engine.py#L119)):
```python
exit_reason = position.should_close(current_price)[1]
```
`should_close()` is called AFTER `close_triggered_positions()` already removed the position from the manager. At that point `should_close()` may return `('still open', ...)` because the position is no longer in context.

**Fix:** Capture the exit reason BEFORE closing, inside `close_triggered_positions`, or pass it through with the closed position. The simplest fix: have `close_triggered_positions` return `(position, reason)` tuples instead of just positions.

**Step A:** Read `position.should_close()` in [algo_backtest/engine/position.py](algo_backtest/engine/position.py) — understand what it returns.

**Step B:** Determine the cleanest fix — either:
1. Capture reason in `close_triggered_positions` and return `(position, reason)` pairs
2. Store `exit_reason` on the Position object when it's marked for closing
3. Re-call `should_close` before removing (if it's idempotent)

**Step C:** Implement and verify — sample trade output should now show `'sl'`, `'tp'`, or `'forced close'` instead of `'still open'`.

```

What should_close() returns:

    def should_close(self, current_price: float) -> Tuple[bool, str]:
        
        '''
        Method used to check if position should close (if it hit SL or TP).
        Handles incorrect current_price.
        
        Returns:
        True if SL/TP hit, False otherwise
        '''
        
        if current_price < 0:
            print('Incorrect current price, it should be above 0!')
            return (False, 'Still open')
        if self.side != 'BUY' and self.side != 'SELL':
            print('Incorrect side, it should be either BUY or SELL (case insensitive)')
            return (False, 'Still open')
        
        
        if self.side == 'BUY' and current_price <= self.stop_loss: #Simple if-checks, starting from SL check
            print('Buy SL hit')
            return (True, 'Buy SL hit')
        elif self.side == 'BUY' and current_price >= self.take_profit:
            return (True, 'Buy TP hit')

        
        elif self.side == 'SELL' and current_price >= self.stop_loss:
            return (True, 'Sell SL hit')
        elif self.side == 'SELL' and current_price <= self.take_profit:
            return (True, 'Sell TP hit')

        return (False, 'Still open')

Chosen fix approach:

B:

- IN position_manager.py:

    def close_triggered_positions(self, ticker: str, current_price: float) -> List[Position]:
        """
        Check all positions for SL/TP triggers and remove them.

        Args:
            current_price: Current market price.

        Returns:
            List of positions that should be closed.
        """
        closed_positions = [(p, p.should_close(current_price)[1]) for p in self.positions if p.ticker == ticker and p.should_close(current_price)]
        
        closed_ids = [p[0].position_id for p in closed_positions]
        self.positions = [p for p in self.positions if p.position_id not in closed_ids]
        
        return closed_positions

in backtest_engine:

    def process_price(self, ticker: str, current_price: float) -> List[Trade]:
        
        """
        Check all positions for a given ticker and given price.
        Close any that hit SL/TP and convert to Trade objects.
        
        Args:
        - ticker: str
        - current_price: float

        Steps:
        1. Use position_manager.close_triggered_positions(current_price)
        2. For each closed position, create a Trade object
        3. Add Trade to completed_trades
        4. Return list of newly created trades

        Returns:
            List of newly closed trades (empty if none closed)
        
        Appends self.completed_trades with all the newly closed trades.
        """
        
        closed_positions = self.position_manager.close_triggered_positions(ticker, current_price)
        logger.debug(f'Processing price for {ticker} at ${current_price}')
        newly_closed_trades = []
        for position in closed_positions:
            #exit_reason = position.should_close(current_price)[1]
            trade = Trade(
                          position[0].position_id,
                          position[0].ticker, 
                          position[0].side, 
                          position[0].entry_price, 
                          current_price, 
                          position[0].quantity,
                          stop_loss = position[0].stop_loss,
                          take_profit = position[0].take_profit,
                          exit_reason = position[1],
                          strategy_id = position[0].strategy_id,
                          strategy_name = position[0].strategy_name,
                          )
            logger.info(f'@Strategy {position[0].strategy_id}, {position[0].strategy_name} || Position {trade.position_id} @ {position[0].ticker} closed with {trade.pnl} as a {position[1]}')
            newly_closed_trades.append(trade)
            self.completed_trades.append(trade)
            
        return newly_closed_trades

    
    def force_close_all(self, ticker: str, strategy_id: str, price: float) -> None:
        '''Force close all open positions on a given ticker'''
        filtered_positions = [position for position in self.position_manager.positions if (ticker == position.ticker and position.strategy_id == strategy_id)]
        for position in filtered_positions:
            trade = Trade(
                          position.position_id,
                          position.ticker, 
                          position.side, 
                          position.entry_price,
                          price, 
                          position.quantity,
                          stop_loss = position.stop_loss,
                          take_profit = position.take_profit,
                          exit_reason = 'forced close',
                          strategy_id = position.strategy_id,
                          strategy_name = position.strategy_name,
                          )
            logger.info(f'@Strategy {position.strategy_id}, {position.strategy_name} || Position {trade.position_id} @ {position.ticker} closed with {trade.pnl} as a forced close')
            self.completed_trades.append(trade)
            self.position_manager.remove_position(position)






Code change:
I've pasted the changes above.

Output after fix (sample trade):

Still doesn't fucking work properly, I don't know why as it seems I'm passing everything I should..

--- LPP Strategy (ID: 4d6e41e1-ac09-477c-a782-5e4c45d677ef) ---

                  Trades: 116
                  Win Rate: 38.793103448275865%
                  Total PnL: $-231.00
                  Avg R: -0.04R


--- PORTFOLIO TOTAL  ---

                  Trades: 209
                  Win Rate: 43.0622009569378%
                  Total PnL: $-94.0
                  Avg R: -0.02R


[@LPP Strategy | 4d6e41e1-ac09-477c-a782-5e4c45d677ef] Trade 6a01d734-cdd4-47bb-b783-ea4056a81a2a: [LOSS] BUY 1 FDAX: 22711.0 -> 22708.0 (still open) | P&L: $-3.00
[@LPP Strategy | eafdfeaa-c070-43df-9132-cf52c753b28f] Trade 46166a13-6b1b-49c4-ab93-1c2242d0a4a0: [LOSS] BUY 1 FDAX: 22744.0 -> 22744.0 (still open) | P&L: $0.00
[@LPP Strategy | 4d6e41e1-ac09-477c-a782-5e4c45d677ef] Trade d320efd0-f721-4cf6-a526-5f8ef24f1b52: [LOSS] BUY 1 FDAX: 22691.0 -> 22688.0 (still open) | P&L: $-3.00
[@LPP Strategy | eafdfeaa-c070-43df-9132-cf52c753b28f] Trade d448c853-ec46-4b4d-83b1-a74dfb2d5e00: [WIN] BUY 1 FDAX: 22729.0 -> 22744.0 (still open) | P&L: $15.00
[@LPP Strategy | 4d6e41e1-ac09-477c-a782-5e4c45d677ef] Trade 89f4c904-4883-4b6b-8a1e-557218e4e1d7: [WIN] BUY 1 FDAX: 22780.0 -> 22790.0 (still open) | P&L: $10.00
[@LPP Strategy | eafdfeaa-c070-43df-9132-cf52c753b28f] Trade 52ff1b9b-b34a-4d2f-b2e3-05f6b6e8cf9c: [WIN] BUY 1 FDAX: 22819.0 -> 22852.0 (still open) | P&L: $33.00
[@LPP Strategy | 4d6e41e1-ac09-477c-a782-5e4c45d677ef] Trade 56eb90c6-7872-4e60-b279-63e1c12cf595: [WIN] BUY 1 FDAX: 23123.0 -> 23131.0 (still open) | P&L: $8.00
[@LPP Strategy | eafdfeaa-c070-43df-9132-cf52c753b28f] Trade 8d54e7f9-480e-4806-9c30-1bb33ff28f66: [LOSS] BUY 1 FDAX: 23155.0 -> 23145.0 (still open) | P&L: $-10.00
[@LPP Strategy | 4d6e41e1-ac09-477c-a782-5e4c45d677ef] Trade acfbd5a7-07e4-4528-aad1-a4f95875906b: [LOSS] BUY 1 FDAX: 23477.0 -> 23473.0 (still open) | P&L: $-4.00
[@LPP Strategy | 4d6e41e1-ac09-477c-a782-5e4c45d677ef] Trade 09edf7ce-e9bd-46c6-a122-a839345580e4: [LOSS] BUY 1 FDAX: 23367.0 -> 23358.0 (still open) | P&L: $-9.00
```

---

## Task 7 — PCAP Simulation: exception + OOP combined [Hardest pattern]

These are the patterns closest to what failed on the real exam.

**Q1.** What is the output?
```python
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg          # no super().__init__()
    def __str__(self):
        return f"MyError: {self.msg}"

try:
    raise MyError("oops")
except MyError as e:
    print(e)
    print(e.args)
```
- A: `MyError: oops`, `('oops',)`
- B: `MyError: oops`, `()`
- C: `oops`, `('oops',)`
- D: `MyError: oops`, `MyError: oops`

A


**Q2.** What is `obj_c.get()` given:
```python
class A:
    __v = 10
    def get(self): return self.__v

class B(A):
    __v = 20
    def get(self): return self.__v

class C(B):
    __v = 30

obj_c = C()
print(obj_c.get())
```
- A: `10`
- B: `20`
- C: `30`
- D: `AttributeError`

B


**Q3.** What does this print?
```python
def gen():
    yield 1
    yield 2
    return
    yield 3

print(list(gen()))

```
- A: `[1, 2, 3]`
- B: `[1, 2]`
- C: `[1, 2, None]`
- D: `SyntaxError`

B

**Q4.** `2.` in Python is:
- A: `SyntaxError`
- B: `float` with value `2.0`
- C: `int` with value `2`
- D: Valid only inside expressions, not as standalone

B

**Q5.** After this runs, what is `m`?
```python
m = 0
def foo(n):
    global m
    assert n > 0
    try:
        return 10 / n
    except ArithmeticError:
        raise RuntimeError

try:
    foo(0)
except RuntimeError:
    m = 10
except AssertionError:
    m = 5
except:
    m = 1
print(m)
```
- A: `0`
- B: `10`
- C: `5`
- D: `1`

C

Write answers here:
```
Q1: A
Q2: B
Q3: B
Q4: B
Q5: C
```

---

## Task 8 — [FRIDAY] Generate Week 12 Mock Exams

This task is handled by the mentor — two 30-question mock exams will be placed in `exams/Week12_Exam_A.md` and `exams/Week12_Exam_B.md` before end of session.

Focus areas for the exams:
- All real exam gaps from exam_qs.md
- Heavy on exceptions, OOP, strings, closures, generators
- Platform/sys/os module questions
- Name mangling + inheritance
- raise X from Y chains
- Lambda patterns
- List comprehension order

**Nothing to do here — exams will be ready for the weekend.**
