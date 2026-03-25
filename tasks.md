# Week 11, Day 3 — 2026-03-25

**Topic:** repr() | os.path | errno | random | escape sequences | generators | closures | Project
**Mode:** PCAP drills + one project task

---

## Task 1 — repr() vs str(): predict the output

```python
class Item:
    def __repr__(self): return "Item(42)"
    def __str__(self): return "an item"

x = Item()
print(x)
print(repr(x))
print([x])
print(f"{x}")
```

What are the four outputs?

Also predict:
```python
lines = ["hello\n", "world\n"]
print(lines[0])
print(repr(lines[0]))
```

What is the difference and why?

print(x) #an item
print(repr(x)) #Item(42)
print([x]) #[Item(42)]
print(f"{x}") #{an item}

lines = ["hello\n", "world\n"]
print(lines[0]) #hello
print(repr(lines[0]))  #'hello\n'


It all depends, but str is the base print if we don't define repr/str in the print


---

## Task 2 — os.path: predict the output

```python
import os

path = "/home/user/projects/report.pdf"
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))
print(os.path.splitext(path))
```

Four outputs. Write them all exactly — types, slashes, quotes matter.

Then answer: on Linux, what does `os.path.join("home", "user", "docs")` return?
On Windows?

print(os.path.basename(path)) #report.pdf
print(os.path.dirname(path)) #/home/user/projects/
print(os.path.split(path)) #(/home/user/projects, report.pdf)
print(os.path.splitext(path)) #('/home/user/projects/report', '.pdf') - this is weird but this is how it works

On Linux, the slashes are turned to the opposite side (\), but the rest is the same.
That's the reason why we use os path, as it works correctly for both Linux/Windows, handling this difference and dealing with different slashes every time. This wway we don't have to remember or guess it, as it may be forgotten sometimes.


---

## Task 3 — errno + exceptions: predict the output

```python
import errno

try:
    open("missing.txt", "r")
except OSError as e:
    print(e.errno)
    print(errno.ENOENT)
    print(e.errno == errno.ENOENT)
    print(type(e).__name__)
```

Four outputs. Assume the file does not exist.

    
#2
#2
#True
#FileNotFoundError


Also: which of these is TRUE?
- A) `IOError is OSError` → `False`
- B) `IOError is OSError` → `True`
- C) `IOError` does not exist in Python 3
- D) `FileNotFoundError` is not a subclass of `OSError`

B

---

## Task 4 — random module: multiple choice

**Q1:** What values can `random.randint(1, 5)` produce?
- A) 1, 2, 3, 4 (stop excluded)
- B) 1, 2, 3, 4, 5 (both ends inclusive)
- C) 0, 1, 2, 3, 4
- D) 2, 3, 4

B

**Q2:** What values can `random.randrange(0, 10, 3)` produce?
- A) 0, 3, 6, 9, 10
- B) 0, 3, 6, 9
- C) 3, 6, 9
- D) 0, 3, 6

B



**Q3:** `random.choice((10, 20, 30))` — which value is **impossible**?
- A) 10
- B) 20
- C) 25
- D) 30

C

---

## Task 5 — Escape sequences + string traps

Predict — valid or `SyntaxError`? For the valid ones, what does `print()` output?

```python
a = '\\'
b = "\'"
c = '\\\''
d = "it\'s"
```

Every single one prints here.
a: \
b: '
c: \'
d: it's


Then write: what is `len(a)`? What is `len(b)`?
1, 1

---

## Task 6 — Generators: write the code

Write a generator function `fibonacci()` that yields Fibonacci numbers indefinitely (no limit).
Then write code to print the first 8 values using a loop.

Rules: pure Python, no imports, use `yield`.


def fibonacci(n: int):
    '''
    This generator generates Fibonacci numbers indefinitely
    '''
    x = 0
    y = 1
    fib_numbers = []
    
    for i in range(n):
        fib_numbers.append(x)
        x, y = y, x + y
    
    return fib_numbers
        
x = fibonacci(8)
print(x)


Not sure how to use a gen here - IMO this is way more handy, but lmk.

---

## Task 7 — Closures + scope: predict and fix

**Part A — predict:**
```python
funcs = []
for i in range(4):
    funcs.append(lambda: i)

print([f() for f in funcs])

#We'd get [3, 3, 3, 3]
```

**Part B — fix it** so the list prints `[0, 1, 2, 3]`. Write the corrected version.

funcs = []
for i in range(4):
    funcs.append(lambda i=i: i)
    
print([f() for f in funcs])


**Part C — predict:**
```python
def outer():
    total = 0
    def add(n):
        nonlocal total
        total += n
        return total
    return add

f = outer()
print(f(5))
print(f(3))
print(f(2))

5
8
10
```

---

## Task 8 — PROJECT: RTH time filter in VwapStrategy

The current `run_backtest()` runs on all 216k rows including overnight sessions where `vwap_rth` is meaningless.

Add a time filter to `VwapStrategy` or `run_backtest()` so signals are only generated during **RTH hours: 09:00–17:30 CET**.

Your `candle_open` column contains timezone-aware timestamps like `2025-03-10 09:00:00+01:00`.

Requirements:
1. Extract the time component from `row['candle_open']`
2. Only generate a signal if the candle is within RTH — otherwise return `'HOLD'`
3. Decide yourself: does the filter belong in `VwapStrategy.generate_signal()` or in `run_backtest()`? Write a one-line comment explaining your archintectural choice.
4. Re-run and note whether the trade cout drops significantly vs the previous 206k run.

This was quite a complex task, but it still will be extended even more in the future

- to add a time filter I had to make an important architectural decision - consulted Claude for that as well
For now I will be using filter in main.py's run_backtest method, which is getting pretty packed, BUT IMO STILL READABLE;

- I also implemented abstractmethod for each strategy class with start and end time (with None as default)
- I also had to add force close option (force_close_all method) to backtest_engine (which also required me to add remove_position to position_manager,
as I didn't expect manual position removal besides standard SL/TP closing)

Claude suggested ticker-based force close, but I opted for a strategy based close, as it makes A LOT MORE sense
and I could have different strategies with different start/end times for whatever reason


BacktestEngine: 0 open | 112356 closed | PnL: $-19874.0
--- VWAP Strategy (ID: 1) ---

                  Trades: 112356
                  Win Rate: 45.495567659938054%
                  Total PnL: $-19874.00
                  Avg R: -0.00R


--- PORTFOLIO TOTAL  ---

                  Trades: 112356
                  Win Rate: 45.495567659938054%
                  Total PnL: $-19874.0
                  Avg R: -0.0R


(.venv) 


As a result of time filtering we've opened 112k trades, so significantly less than 216k recently.It might mean that it's working properly


---

## Answers

### Task 1
```
Item output:
repr output:
list output:
f-string output:
lines[0] print:
repr(lines[0]):
why different:
```

### Task 2
```
basename:
dirname:
split:
splitext:
join Linux:
join Windows:
```

### Task 3
```
e.errno:
errno.ENOENT:
comparison:
type name:
MC answer:
```

### Task 4
```
Q1:
Q2:
Q3:
```

### Task 5
```
a: valid/SyntaxError, output:
b: valid/SyntaxError, output:
c: valid/SyntaxError, output:
d: valid/SyntaxError, output:
len(a):
len(b):
```

### Task 6
```python
# your generator here
```

### Task 7
```
Part A output:
Part B fix:
Part C output:
```

### Task 8
```
architectural choice comment:
new trade count:
code:
```
