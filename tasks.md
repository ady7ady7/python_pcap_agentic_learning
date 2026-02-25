# Week 8, Day 3 — R-Multiples & Strategy-Aware Positions
**Date:** 2026-02-25 | **Focus:** PCAP crunch + project extended goals (R-multiple, strategy_id)

---

## Task 1 — PCAP Warm-up (no code, 6 questions)

**Q1:** What is the output?
```python
def f(a, b=2, *args, c=3):
    print(a, b, c, args)

f(1, 4, 5, 6, c=10)

1, 4, 10, (5, 6)
```

**Q2:** What is the output?
```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.__mro__)



```
Pick the correct MRO order:
- A) `D → B → C → A → object`
- B) `D → B → A → C → object`
- C) `D → C → B → A → object`
- D) `D → A → B → C → object`

A

**Q3:** What is the output?
```python
a = {"x": 1}
b = a.copy()
b["x"] = 99
b["y"] = 2
print(a)


x : 1 (with proper formatting, but you get the idea)


```

**Q4:** What is the output?
```python
print(bool(0), bool(""), bool([]), bool(0.0), bool(None))
```

**Q5:** What is the output?
```python
def gen(n):
    for i in range(n):
        yield i * i

g = gen(5)
print(next(g), next(g), sum(g))



0 1 29

```

**Q6:** What is the output?
```python
class A:
    def __init__(self):
        self.items = []

    def __iadd__(self, other):
        self.items.append(other)
        return self

a = A()
a += "x"
a += "y"
print(a.items)
```

WE DIDN'T HAVE iadd!!!!
I reckon it's [x, y] but IT SHOULDN'T BE HERE!


---

## Task 2 — PROJECT: Fix the stray print in Trade

Before adding new features, clean up one existing bug.

Open [algo_backtest/engine/trade.py](algo_backtest/engine/trade.py).

`calculate_win_rate()` has a stray `print(trades_profits)` inside it — that's what was printing the PnL list before the win rate in Day 1's console output. Remove it.

While you're there: `exit_reason` in `__init__` calls `.upper()` on the reason string, but `should_close()` returns strings like `"Buy TP hit"`. After `.upper()` that becomes `"BUY TP HIT"` — inconsistent with what gets logged. Change the `exit_reason` storage to preserve the original case (remove the `.upper()` call, or lowercase it consistently — your choice, but pick one and apply it).

Edit the file directly. No answer box needed — just note what you changed.

- print(trades_profits) removed
- init exit reason also changed to .lower() instead

    def __init__(self,
                 position_id: str,
                 ticker: str,
                 side: str,
                 entry_price: float,
                 exit_price: float,
                 quantity: float,
                 entry_time: Optional[str] = None,
                 exit_time: Optional[str] = None,
                 stop_loss: Optional[float] = None,
                 take_profit: Optional[float] = None,
                 exit_reason: Optional[str] = None
                 ):
        
        """Initialize a completed trade and calculate P&L."""
        
        self._position_id = position_id
        self._ticker = ticker
        self._side = side.upper()
        self._entry_price = entry_price
        self._exit_price = exit_price
        self._quantity = quantity
        self._entry_time = entry_time
        self._exit_time = exit_time
        self._stop_loss = stop_loss
        self._take_profit = take_profit
        
        if exit_reason is not None:
            self._exit_reason = exit_reason.lower()
        else:
            self._exit_reason = ''


---

## Task 3 — PROJECT: R-multiple on Trade

The R-multiple measures profit in units of risk, not dollars. It's the standard metric in professional trading:

```
R = pnl / (abs(entry_price - stop_loss) * quantity)
```

A trade that risked $100 and made $300 = **+3R**.
A trade that risked $100 and lost $100 = **-1R** (by definition).

Open [algo_backtest/engine/trade.py](algo_backtest/engine/trade.py).

Add a `r_multiple` property that:
- Returns `pnl / (abs(entry_price - stop_loss) * quantity)`
- If `stop_loss` is `None` or `stop_loss == entry_price` (division by zero), returns `None`
- Is a read-only `@property`, consistent with the other properties on this class

Then open [algo_backtest/engine/backtest_engine.py](algo_backtest/engine/backtest_engine.py).

`process_price()` creates `Trade` objects but currently doesn't pass `stop_loss` and `take_profit` through from the closed `Position`. Fix this — pass `position.stop_loss` and `position.take_profit` as keyword arguments when constructing the `Trade`. Without this, `r_multiple` will always return `None`.

Verify it works by running main.py and checking that `r_multiple` gives a sensible number for at least one trade.

---

## Task 4 — PROJECT: strategy_id on Position

Open [algo_backtest/engine/position.py](algo_backtest/engine/position.py).

Add two optional attributes to `Position.__init__`:
- `strategy_id: Optional[str] = None` — a unique ID for this strategy instance (e.g. `"ma_cross_v1"`)
- `strategy_name: Optional[str] = None` — a human-readable label (e.g. `"MA Crossover"`)

Update:
1. `__init__` signature and body
2. `__str__` — include strategy info if present: append `[strategy: {strategy_name}]` at the end when `strategy_name` is not None
3. `__repr__` — include both new fields
4. The class docstring `Attributes:` section

Then open [algo_backtest/engine/backtest_engine.py](algo_backtest/engine/backtest_engine.py).

Add `strategy_id` and `strategy_name` as optional keyword arguments to `open_position()`, defaulting to `None`. Pass them through to `Position(...)`.

Verify: open two positions with different `strategy_id` values and confirm `position.strategy_id` reflects what you passed.

---

Everything done, it took some time as I had to check and modify backtest_engine, position.py, position_kmanager, trade.py - literally every component we have.

This is the test formulated in main.py

if __name__ == '__main__':
    setup_logging()
    print('Starting the backtest test procedure in main.py - logging set!')
    engine = BacktestEngine()
    engine.open_position('EURUSD', 'BUY', 105.6, 10000, 103.2, 107.7, strategy_id = '432', strategy_name = 'Super XD')
    engine.open_position('EURUSD', 'SELL', 105.6, 10000, 110.2, 102.7, strategy_id = '432', strategy_name = 'Super XD')
    engine.open_position('FDAX', 'BUY', 25554, 10, 25500, 25750, strategy_id = '6546', strategy_name = 'DAXI')
    engine.open_position('FDAX', 'SELL', 25580, 10, 25660, 25350, strategy_id = '2334', strategy_name = 'DAXI')    
    

    engine.process_price('EURUSD', 104.2)
    engine.process_price('EURUSD', 106.2)
    engine.process_price('EURUSD', 108.2)
    engine.process_price('EURUSD', 102.2)
    
    engine.process_price('FDAX', 25654)
    engine.process_price('FDAX', 25760)
    engine.process_price('FDAX', 25620)
    engine.process_price('FDAX', 25440)
    engine.process_price('FDAX', 25240)
    
    print(engine)
    print(engine.total_pnl)
    print(engine.win_rate)
    print([trade.r_multiple for trade in engine.completed_trades])


LOG BELOW:

$ python algo_backtest/main.py
2026-02-25 13:48:52,345 [DEBUG   ] root: Logging in main initialized.
Starting the backtest test procedure in main.py - logging set!
Position @Strategy ('Super XD', ('432',)), Position_id = fb3f533a-34b2-42e1-8e35-a28570c53096 | BUY 10000 EURUSD @ 105.6 [SL = 103.2, TP = 107.7] added successfully
2026-02-25 13:48:52,345 [INFO    ] engine.backtest_engine: @Strategy Super XD: ('432',) Position fb3f533a-34b2-42e1-8e35-a28570c53096: BUY EURUSD @ 105.6
Position @Strategy ('Super XD', ('432',)), Position_id = 75f08aa7-bb63-40bb-9f98-5c8acfc81008 | SELL 10000 EURUSD @ 105.6 [SL = 110.2, TP = 102.7] added successfully
2026-02-25 13:48:52,345 [INFO    ] engine.backtest_engine: @Strategy Super XD: ('432',) Position 75f08aa7-bb63-40bb-9f98-5c8acfc81008: SELL EURUSD @ 105.6
Position @Strategy ('DAXI', ('6546',)), Position_id = ec86cf92-f0e0-475c-bed2-c5300e3e2c28 | BUY 10 FDAX @ 25554 [SL = 25500, TP = 25750] added successfully
2026-02-25 13:48:52,345 [INFO    ] engine.backtest_engine: @Strategy DAXI: ('6546',) Position ec86cf92-f0e0-475c-bed2-c5300e3e2c28: BUY FDAX @ 25554
Position @Strategy ('DAXI', ('2334',)), Position_id = e27914ba-8572-4d83-938f-4f99060c8cbd | SELL 10 FDAX @ 25580 [SL = 25660, TP = 25350] added successfully
2026-02-25 13:48:52,346 [INFO    ] engine.backtest_engine: @Strategy DAXI: ('2334',) Position e27914ba-8572-4d83-938f-4f99060c8cbd: SELL FDAX @ 25580
2026-02-25 13:48:52,346 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $104.2
2026-02-25 13:48:52,346 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $106.2
2026-02-25 13:48:52,346 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $108.2
2026-02-25 13:48:52,346 [INFO    ] engine.backtest_engine: @Strategy ('432',), Super XD || Position fb3f533a-34b2-42e1-8e35-a28570c53096 @ EURUSD closed with 26000.000000000084 as a Buy TP hit
2026-02-25 13:48:52,346 [DEBUG   ] engine.backtest_engine: Processing price for EURUSD at $102.2
2026-02-25 13:48:52,346 [INFO    ] engine.backtest_engine: @Strategy ('432',), Super XD || Position 75f08aa7-bb63-40bb-9f98-5c8acfc81008 @ EURUSD closed with 33999.99999999991 as a Sell TP hit
2026-02-25 13:48:52,346 [DEBUG   ] engine.backtest_engine: Processing price for FDAX at $25654
2026-02-25 13:48:52,346 [DEBUG   ] engine.backtest_engine: Processing price for FDAX at $25760
2026-02-25 13:48:52,346 [INFO    ] engine.backtest_engine: @Strategy ('6546',), DAXI || Position ec86cf92-f0e0-475c-bed2-c5300e3e2c28 @ FDAX closed with 2060 as a Buy TP hit
2026-02-25 13:48:52,347 [INFO    ] engine.backtest_engine: @Strategy ('2334',), DAXI || Position e27914ba-8572-4d83-938f-4f99060c8cbd @ FDAX closed with -1800 as a Sell SL hit
2026-02-25 13:48:52,347 [DEBUG   ] engine.backtest_engine: Processing price for FDAX at $25620
2026-02-25 13:48:52,347 [DEBUG   ] engine.backtest_engine: Processing price for FDAX at $25440
2026-02-25 13:48:52,347 [DEBUG   ] engine.backtest_engine: Processing price for FDAX at $25240
engine.backtest_engine: 0 open | 4 closed | PnL: $60260.0
60260.0
75.0
[1.08, 0.74, 3.81, -2.25]

It all seems to work, although we definitely will have to test it on a real battlefield soon :))
I'm hoping to achieve full functionality by the end of next week.

## Task 5 — PCAP Simulation (10 questions, 12 minutes)

Time yourself. No code runner.

**Q1:** What is the output?
```python
x = 5
y = 3
print(x // y, x % y, x ** y)
```
- A) `1 2 125`
- B) `1 2 15`
- C) `2 2 125`
- D) `1.67 2 125`

A

**Q2:** Which correctly creates a set with one element?
- A) `{}`
- B) `set()`
- C) `{"hello"}`
- D) `set["hello"]`

C

**Q3:** What is the output?
```python
class A:
    def __init__(self):
        self.x = 10
    def __add__(self, other):
        return A() if isinstance(other, A) else NotImplemented

a = A()
b = A()
c = a + b
print(type(c).__name__)
```
- A) `TypeError`
- B) `NotImplemented`
- C) `A`
- D) `int`

C

**Q4:** What is the output?
```python
s = "racecar"
print(s == s[::-1])
```
- A) `False`
- B) `True`
- C) `TypeError`
- D) `"racecar"`

B

**Q5:** What does `zip([1,2,3], [4,5])` produce?
- A) `[(1,4), (2,5), (3, None)]`
- B) `[(1,4), (2,5)]`
- C) `TypeError`
- D) `[(1,4,3), (2,5)]`

A




**Q6:** What is the output?
```python
def f():
    return 1, 2, 3

a, *b = f()
print(a, b)
```
- A) `1 [2, 3]`
- B) `1 (2, 3)`
- C) `TypeError`
- D) `1 2`

B

**Q7:** What is the output?
```python
try:
    raise ValueError("bad") from TypeError("cause")
except ValueError as e:
    print(type(e.__cause__).__name__)
```
- A) `ValueError`
- B) `TypeError`
- C) `None`
- D) `AttributeError`

A

**Q8:** Which statement about `@property` is true?
- A) A property can only have a getter, never a setter
- B) A property setter is defined with `@prop_name.setter`
- C) Properties are only valid in classes that inherit from `object`
- D) A property must return a value — returning `None` raises `TypeError`

B

**Q9:** What is the output?
```python
d = {}
for i in range(3):
    d[i] = i ** 2
print(d)
```
- A) `{0: 0, 1: 1, 2: 4}`
- B) `{1: 1, 2: 4, 3: 9}`
- C) `[0, 1, 4]`
- D) `TypeError`

A

**Q10:** What is the output?
```python
class C:
    def __init__(self, val):
        self._val = val

    @property
    def val(self):
        return self._val

    @val.setter
    def val(self, new):
        self._val = new * 2

c = C(5)
c.val = 3
print(c.val)
```
- A) `3`
- B) `5`
- C) `6`
- D) `AttributeError`

C

---

## Task 6 — PCAP Trap: Predict + Explain

No code runner. Give the output and a one-sentence explanation for each.

**Snippet A:**
```python
def f(x):
    return x * 2

result = map(f, [1, 2, 3])
print(result) #map memory object - we'd need to wrap it in a list to see the actual values
print(list(result)) #[2, 4, 6] - we get the actual list of values from the map generator
print(list(result)) #[] - the generator is exhausted at this point





```

**Snippet B:**
```python
a = [1, 2, 3]
b = [4, 5, 6]
c = [*a, *b]
d = (*a, *b)
print(type(c).__name__, type(d).__name__)

list tuple

It's pretty self explanatory, it's enough to just check the brackets.

```

**Snippet C:**
```python
x = None
print(x is None, x == None, type(x).__name__)

True, False, NoneType

NoneType is not a real VALUE, so it cannot be compared as in ==, >= or <= etc. It can only be IS NONE or IS NOT NONE.

```

---

```
## Answers

### Task 1
Q1:
Q2:
Q3:
Q4:
Q5:
Q6:

### Task 2
Changes made:

### Task 3
Notes (verify r_multiple works):

### Task 4
Notes (verify strategy_id passes through):

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
Snippet A:
Snippet B:
Snippet C:
```
