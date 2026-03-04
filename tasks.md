# Week 9, Day 3 — Gap Closure: except ordering, UnboundLocalError, closures + DataLoader wiring
**Date:** 2026-03-04 | **Focus:** Close the 3 remaining PCAP gaps + minimal DataLoader update for real CSV

---

## Task 1 — Warm-up: Predict the output (6 questions, no code)

These target your 3 open gaps directly. Answer fast, no second-guessing.

**Q1:**
```python
try:
    raise ValueError("bad value")
except Exception as e:
    print("Exception")
except ValueError as e:
    print("ValueError")


Exception - although it's very unintuitive - but the order of exception placement is wrong here.


```

**Q2:**
```python
try:
    open("missing.txt")
except OSError:
    print("OSError")
except FileNotFoundError:
    print("FileNotFoundError")
```

FileNotFoundError

**Q3:**
```python
x = 10

def f():
    print(x)
    x = 20

f()

UnboundLocalError

```

**Q4:**
```python
x = 10

def f():
    global x
    print(x)
    x = 20

f()
print(x)

10
20

```

**Q5:**
```python
def make_adder(n):
    def add(x):
        return x + n
    n = n * 10
    return add

fn = make_adder(3)
print(fn(1))

40

```

**Q6:**
```python
fns = []
for i in range(3):
    fns.append(lambda: i * i)

print([f() for f in fns])


[4, 4, 4]

```

---

## Task 2 — except ordering deep-dive (no code, 4 questions)

Answer from memory. No running code.

**Q1:** What is the rule about ordering `except` clauses?
Write it in one sentence.

We should order them from more specific to general. We should first handle exceptions that we expect to happen, but we can also create a window for the unexpected issues.


**Q2:** What is the output?
```python
try:
    raise FileNotFoundError("no file")
except Exception:
    print("A")
except OSError:
    print("B")
except FileNotFoundError:
    print("C")

A
```

**Q3:** Fix this code so that `FileNotFoundError` is caught by its own clause:
```python
try:
    open("x.txt")
except Exception:
    print("generic")
except FileNotFoundError:
    print("file missing")


```

Write the corrected version (just the two except lines, in the right order).

    
try:
    open("x.txt")
except FileNotFoundError:
    print("file missing")
except Exception:
    print("generic")


**Q4:** What is the output?
```python
try:
    raise KeyError("k")
except LookupError:
    print("LookupError")
except KeyError:
    print("KeyError")


LookupError
```

*(Hint: `KeyError` is a subclass of `LookupError`.)*

---

## Task 3 — UnboundLocalError vs NameError vs AttributeError (no code, 4 questions)

**Q1:** What is the output?
```python
def f():
    print(val)
    val = 5

f()

UnboundLocalError
```

**Q2:** What is the output?
```python
def f():
    print(val)

f()

NameError
```

**Q3:** What is the difference between `UnboundLocalError` and `NameError`? Write one sentence each.

It seems that UnboundLocalError relates to situations where a given name is occupied/defined, but it's defined later. It seems that it still precreates a memory object or something like that, that makes it an UnboundLocalError before a given variable/name is actually defined. Anyway, for me this is a sign that the variables/object names are prechecked to check if they exist, before they are checked again to check their values. It's interesting.

As for NameError, it simply occurs when a given name is not defined.

**Q4:** What is the output?
```python
def counter():
    count += 1
    return count

count = 0
counter() #no explicit output, as we do not print anything - but it would be 1 if we printed it

```

---

## Task 4 — PCAP Simulation: 10 questions (12 minutes, timed)

**Q1:** What is the output?
```python
def f(a, b=2, *args, c=10):
    print(a, b, args, c)

f(1, 3, 5, 7, c=99)
```
- A) `1 3 (5, 7) 99`
- B) `1 2 (3, 5, 7) 99`
- C) `1 3 (5, 7) 10`
- D) `TypeError`

A

**Q2:** What is the output?
```python
class A:
    data = []

class B(A):
    pass

B.data.append(1)
A.data.append(2)
print(A.data, B.data)
```
- A) `[2] [1]`
- B) `[1, 2] [1, 2]`
- C) `[2] [1, 2]`
- D) `[1] [1, 2]`

B


**Q3:** What is the output?
```python
def gen():
    x = yield 1
    yield x * 2

g = gen()
print(next(g))
print(g.send(5))
```
- A) `1`, `10`
- B) `1`, `None`
- C) `1`, `5`
- D) `TypeError`

A

**Q4:** What is the output?
```python
xs = [1, 2, 3]
ys = xs[:]
ys.append(4)
print(xs, ys)
```
- A) `[1, 2, 3, 4] [1, 2, 3, 4]`
- B) `[1, 2, 3] [1, 2, 3, 4]`
- C) `[1, 2, 3, 4] [1, 2, 3]`
- D) `TypeError`

B

**Q5:** What is the output?
```python
import logging
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("test")
logger.setLevel(logging.DEBUG)
logger.debug("debug msg")
logger.warning("warn msg")
```
- A) `debug msg` and `warn msg`
- B) `warn msg` only
- C) Nothing printed
- D) `debug msg` only

A

**Q6:** What is the output?
```python
class C:
    def __init__(self):
        self.__x = 10

c = C()
c.__x = 99
print(c.__x, c._C__x)
```
- A) `99 99`
- B) `99 10`
- C) `10 10`
- D) `AttributeError`

B


**Q7:** What is the output?
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
- C) `[]`, `[1]`, `[1, 1]`
- D) `TypeError`

B

**Q8:** What is the output?
```python
try:
    raise RuntimeError("r")
except RuntimeError as e:
    err = e

print(err)
```
- A) `r`
- B) `RuntimeError: r`
- C) `NameError`
- D) `RuntimeError`

A

**Q9:** What is the output?
```python
xs = list(range(5))
it = iter(xs)
next(it)
next(it)
print(list(it))
```
- A) `[0, 1, 2, 3, 4]`
- B) `[2, 3, 4]`
- C) `[1, 2, 3, 4]`
- D) `StopIteration`

B


**Q10:** What is the output?
```python
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner"
    inner()
    return x

print(outer())
```
- A) `outer`
- B) `inner`
- C) `NameError`
- D) `None`

B

---

## Task 5 — Closure trap: capture by reference (3 snippets, no code)

Predict the output for each. These are variations of the same trap.

**Snippet A:**
```python
multipliers = []
for n in [1, 2, 3]:
    multipliers.append(lambda x: x * n)

print([m(10) for m in multipliers])

30, 30, 30

```

**Snippet B:**
```python
multipliers = []
for n in [1, 2, 3]:
    multipliers.append(lambda x, n=n: x * n)

print([m(10) for m in multipliers])

10 20 30
```

**Snippet C:**
```python
def make_fns():
    result = []
    for i in range(4):
        def fn(i=i):
            return i ** 2
        result.append(fn)
    return result

print([f() for f in make_fns()])

0 1 4 9
```

---

## Task 6 — PROJECT: Adapt DataLoader for real FDAX CSV

Open [algo_backtest/data/data_loader.py](algo_backtest/data/data_loader.py).

Your real FDAX CSV has these columns:
```
candle_open, candle_close, open, high, low, close,
bid_volume, ask_volume, vwap_rth, vwap_full
```

The current `load_data()` hard-codes a 7-column rename to:
`['timestamp', 'ticker', 'open', 'high', 'low', 'close', 'volume']`

That line will break on real data. Do the following **minimal** changes:

1. Remove the hard-coded column rename — let `pd.read_csv()` keep the real column names from the CSV header row.
2. Update `validate_data()` to check for the real FDAX columns instead of the old fake ones. Required columns to validate: `['candle_open', 'open', 'high', 'low', 'close']`.
3. Update the docstring of `load_data()` to reflect the real column names.
4. Add one new method `get_close_series(self, df: pd.DataFrame) -> pd.Series` that returns only the `close` column as a Series — this will be the price feed into the engine later.

No other changes. Do not touch `get_bullish_candles`, `get_candle_count`, or `__repr__`. Keep all existing error handling.

Paste the final `data_loader.py` content into `practice.py` and then update the actual file.

FEW things:

1. I removed the hard-coded column names, BUT I also added columns parameter to the class (self.columns).
Self.columns takes all columns present in a given file - this allows us to work with different files without changing anything. open/high/low/close columns ARE ALMOST ALWAYS present, and if there are edge cases, I will simply handle them.
2. Again, in this scenario validating columns DOES NOT MAKE ANY SENSE, so i removed it for now, also marking that in documentation.
3. Done - it reflects THE CURRENT STATE of my choice.
4. No, thanks! This doesn't make sense, as I might choose different prices that I want to feed to my engine. You made unnecessary assumptions. What if I wanted to feed the open prices OR what's also possible in my case, feed the raw EOBI trade prices in order of their execution on the market? I might be doing that as well - it would be more precise than the OHLC close/open prices, and would automatically allow me to handle the SL/TP on the same candle dilemma etc. 
The problem is that I would have to feed the engine with substantially more rows then. I also wonder if that's a big deal, but this would probably be the best. 

Hre's the updated DataLoader

'''
Data loading module for AlgoBacktest
'''


from typing import Optional
import pandas as pd


class DataLoader:
    '''
    Class used to load and validate data
    
    Attributes:
        file_path: path to the csv file with trading data
    
    '''

    def __init__(self, file_path: str) -> None:
        '''Initialize the DataLoader class with file path'''
        print('DataLoader initialized.')
        self.filepath = file_path
        self.columns = []
        
    def __repr__(self):
        '''
        Unambiguous representation
        '''
        return f'DataLoader(filepath = {self.filepath})'

    
    
    def load_data(self) -> Optional[pd.DataFrame]:
        '''
        Load CSV data with error handling.

        Returns:
            DataFrame with columns as in the file - used to be: timestamp, ticker, open, high, low, close, volume (and DF index).
            The current representation of columns might differ depending on the actual data scheme. It can be read by printing the columns attribute after using load_data. e.g.
            x = DataLoader('ohlc_mock_data.csv')  -> x.load_data() -> print(x.columns)
            Returns None if file not found.

        Raises:
            ValueError: If CSV format is invalid or missing required columns.
            FileNotFoundError: If file is missing or file name is wrong.
            Pandas Parser Error: If there are any issues with data parsing.
        '''
        
        try:
            with open(self.filepath, 'r') as f:
                data = pd.read_csv(f)
                #data.columns = ['timestamp', 'ticker', 'open', 'high', 'low', 'close', 'volume'] #REMOVED FOR NOW
                self.columns = [column for column in data.columns] #replaced hardcoded columns with the actual columns from a given data source
    
        
        except FileNotFoundError as e:
            print(f'File not found: {str(e)}')
            return None
        except ValueError as e:
            print(f'Value Error! {str(e)}')
            return None
        except pd.errors.ParserError as e:
            print(f'Pandas Parser Error: {str(e)}')
            return None
        except Exception as e:
            print(f'Unexpected error: {str(e)}')
            return None
            
        else:
            print('Data loading succeeded')
            return data
        
        finally:
            print('Data loading operation ended.')
    
    
    
    def validate_data(self, df: pd.DataFrame) -> bool:
        '''
        Method used to check whether all rows/columns are valid.
        
        checks if:
        #########- all the columns are in the dataframe #REMOVED - USELESS NOW, WE'RE SIMPLY GETTING THE COLUMNS FROM EACH FILE INSTEAD
        - there are no missing values
        - High price in every row is higher than Low price
        
        Args:
        - df - Pandas Dataframe with columns - columns are not hardcoded anymore
        
        Returns:
        - is_valid - True/False, depending on the results of the check
        '''
        
        ###req_columns = ['timestamp', 'ticker', 'open', 'high', 'low', 'close', 'volume'] - removed, check above
        is_valid = True
        
        
        # missing_columns = set(req_columns) - set(df.columns)
        # if missing_columns:
        #     print(f'Missing columns: {missing_columns}')
        #     is_valid = False
                
        nan_values = df[self.columns].isna().sum()
        if nan_values.any() > 0:
            print(f'Missing values found: {len(nan_values)}')
            is_valid = False
            
        invalid_rows = df[df['high'] < df['low']] #we're assuming that high and low columns are there, but I'll leave it for now, as it SHOULD be the case in every df
        if not invalid_rows.empty:
            print(f'Found {len(invalid_rows)} invalid rows: {invalid_rows}')
            is_valid = False
            
        return is_valid
    
    
    def get_candle_count(self) -> int:
       """
       Return total number of candles in loaded data.

       Returns:
           Number of rows in DataFrame, or 0 if data not loaded.
       """
       
       data = self.load_data()
       
       if data is not None:
           return len(data)
       else:
           return 0
    
    
    def get_bullish_candles(self, data: pd.DataFrame) -> pd.DataFrame:
       """
       Return only bullish candles (close > open).

       Args:
           data: OHLC DataFrame.

       Returns:
           Filtered DataFrame with only bullish candles.
       """
       
       bullish_candles = data[data['close'] > data['open']]
       return bullish_candles
       

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
Q1 (rule):
Q2:
Q3 (fixed order):
Q4:

### Task 3
Q1:
Q2:
Q3 (UnboundLocalError vs NameError):
Q4:

### Task 4
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

### Task 5
Snippet A:
Snippet B:
Snippet C:

### Task 6
Done / notes:
