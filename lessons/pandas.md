Pandas Essentials for Data Manipulation

### Series vs DataFrame

```python
"""Understanding Series and DataFrame."""

import pandas as pd

# SERIES - 1D labeled array (like a column)
prices = pd.Series([100, 101, 102, 103], name='close')
print(prices)
# 0    100
# 1    101
# 2    102
# 3    103
# Name: close, dtype: int64

# DATAFRAME - 2D table (like a spreadsheet)
data = pd.DataFrame({
    'ticker': ['EURUSD', 'EURUSD', 'EURUSD'],
    'close': [1.0850, 1.0860, 1.0855],
    'volume': [1000, 1500, 1200]
})

print(data)
#    ticker   close  volume
# 0  EURUSD  1.0850    1000
# 1  EURUSD  1.0860    1500
# 2  EURUSD  1.0855    1200
```

---

### Essential DataFrame Operations

#### 1. Accessing Columns

```python
"""Accessing DataFrame columns."""

import pandas as pd

df = pd.DataFrame({
    'ticker': ['EURUSD', 'GBPUSD'],
    'open': [1.08, 1.25],
    'close': [1.09, 1.26]
})

# Get a column as Series
close_series = df['close']  # Returns Series
print(type(close_series))  # <class 'pandas.core.series.Series'>

# Multiple columns (returns DataFrame)
subset = df[['ticker', 'close']]  # Note: double brackets [[]]
print(type(subset))  # <class 'pandas.core.frame.DataFrame'>
```

---

#### 2. Checking for Missing Values (NaN)

```python
"""Handling NaN values properly."""

import pandas as pd
import numpy as np

df = pd.DataFrame({
    'ticker': ['EURUSD', 'GBPUSD', 'USDJPY'],
    'close': [1.08, np.nan, 110.5],
    'volume': [1000, 1500, np.nan]
})

# Check which cells are NaN (returns DataFrame of True/False)
print(df.isna())
#    ticker  close  volume
# 0   False  False   False
# 1   False   True   False
# 2   False  False    True

# Count NaN per column (returns Series)
nan_counts = df.isna().sum()
print(nan_counts)
# ticker    0
# close     1
# volume    1
# dtype: int64

# Check if ANY column has NaN values
has_nan = (df.isna().sum() > 0).any()
print(has_nan)  # True

# Total NaN in entire DataFrame
total_nan = df.isna().sum().sum()
print(total_nan)  # 2
```

**Key Pattern:**
```python
# CORRECT way to check if DataFrame has NaN:
if df.isna().sum().sum() > 0:
    print("DataFrame has missing values")

# OR check per column:
if (df.isna().sum() > 0).any():
    print("At least one column has NaN")
```

---

#### 3. Filtering Rows (Boolean Indexing)

```python
"""Filtering DataFrame rows."""

import pandas as pd

df = pd.DataFrame({
    'ticker': ['EURUSD', 'EURUSD', 'EURUSD'],
    'close': [1.08, 1.09, 1.10],
    'volume': [1000, 1500, 800]
})

# Filter rows where close > 1.08
high_prices = df[df['close'] > 1.08]
print(high_prices)
#    ticker  close  volume
# 1  EURUSD   1.09    1500
# 2  EURUSD   1.10     800

# Multiple conditions (use & for AND, | for OR, parentheses required!)
filtered = df[(df['close'] > 1.08) & (df['volume'] > 1000)]
print(filtered)
#    ticker  close  volume
# 1  EURUSD   1.09    1500
```

**PCAP Trap:** Forgetting parentheses in multiple conditions
```python
# WRONG (SyntaxError or wrong results):
df[df['close'] > 1.08 & df['volume'] > 1000]

# CORRECT:
df[(df['close'] > 1.08) & (df['volume'] > 1000)]
```

---

#### 4. Iterating Over Rows

```python
"""Iterating over DataFrame rows (use sparingly!)."""

import pandas as pd

df = pd.DataFrame({
    'ticker': ['EURUSD', 'GBPUSD'],
    'close': [1.08, 1.25]
})

# iterrows() - returns (index, Series)
for index, row in df.iterrows():
    print(f"Row {index}: {row['ticker']} closed at {row['close']}")
# Row 0: EURUSD closed at 1.08
# Row 1: GBPUSD closed at 1.25

# WARNING: iterrows() is SLOW for large DataFrames
# For production, use vectorized operations when possible
```

---

#### 5. Adding/Modifying Columns

```python
"""Creating and modifying columns."""

import pandas as pd

df = pd.DataFrame({
    'open': [1.08, 1.09],
    'close': [1.09, 1.10]
})

# Add new column
df['change'] = df['close'] - df['open']

print(df)
#    open  close  change
# 0  1.08   1.09    0.01
# 1  1.09   1.10    0.01

# Conditional column
df['direction'] = df['change'].apply(lambda x: 'UP' if x > 0 else 'DOWN')
```

---

### Common Pandas Gotchas

**1. `.any()` returns boolean, not numeric**
```python
import pandas as pd

s = pd.Series([0, 5, 0])

# WRONG:
if s.any() > 0:  # .any() is True/False, comparing bool > 0 is weird
    pass

# CORRECT:
if s.any():  # Just check the boolean directly
    pass

# OR check if values > 0:
if (s > 0).any():  # Check if ANY value is > 0
    pass
```

**2. Series arithmetic is element-wise**
```python
s = pd.Series([1, 2, 3])
result = s + 10  # Series([11, 12, 13])
```

**3. Column names must exist**
```python
df = pd.DataFrame({'a': [1, 2]})
print(df['b'])  # KeyError: 'b'
```

---

## Quick Reference Card

`

### Pandas Operations
```python
import pandas as pd

# Load CSV
df = pd.read_csv('file.csv')

# Check columns
df.columns  # Index(['col1', 'col2', ...])

# Access columns
df['col1']        # Series
df[['col1', 'col2']]  # DataFrame

# Check NaN
df.isna()         # DataFrame of True/False
df.isna().sum()   # Count per column
df.isna().sum().sum()  # Total NaN count

# Filter rows
df[df['col'] > 10]
df[(df['col'] > 10) & (df['col'] < 20)]  # Multiple conditions need ()

# Iterate
for idx, row in df.iterrows():
    print(row['col'])
```

---

## Exam Tips

**Pandas:**
- `.any()` returns boolean
- `.sum()` on boolean Series counts True values
- Multiple conditions need parentheses: `(condition1) & (condition2)`
- Use `&` for AND, `|` for OR (not `and`/`or`)
- `.isna()` returns DataFrame, `.isna().sum()` returns Series

---