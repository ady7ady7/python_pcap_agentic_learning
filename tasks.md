# Week 5, Day 2 - Tuesday
## Topic: datetime Practice & File I/O Applications

**Date:** 2026-02-03

**Lesson File:** [week3_5_stdlib_fileio.md](lessons/week3_5_stdlib_fileio.md)

**Target Difficulty:** 5/10

**Remember:** Work in `practice.py`, paste FINAL answers here for review.

---

## Task 1: datetime Coding Practice (No Theory!)

**Instructions:** Write working code for each scenario. Run and verify.

**Part A:** Create a function that calculates how many days until a given date.
```python
from datetime import date

def days_until(target_year: int, target_month: int, target_day: int) -> int:
    """Return number of days from today until target date. Negative if past."""
    # Your code:

# Test:
# print(days_until(2026, 12, 31))  # Days until end of year
# print(days_until(2026, 1, 1))    # Days since start of year (negative)
```

**Part B:** Create a function that formats a timestamp for trade logging.
```python
from datetime import datetime

def format_trade_timestamp(dt: datetime) -> str:
    """Return timestamp as 'YYYY-MM-DD HH:MM:SS' string."""
    # Your code (use strftime):

# Test:
# print(format_trade_timestamp(datetime(2026, 2, 14, 10, 30, 45)))
# Expected: "2026-02-14 10:30:45"
```

**Part C:** Create a function that parses a date string from CSV data.
```python
from datetime import datetime

def parse_csv_date(date_str: str) -> datetime:
    """Parse date string in format 'DD/MM/YYYY' to datetime object."""
    # Your code (use strptime):

# Test:
# dt = parse_csv_date("14/02/2026")
# print(dt.year, dt.month, dt.day)  # 2026 2 14
```

**Your code:**
```python

```

---

## Task 2: File I/O Coding Practice

**Instructions:** Write and run each exercise. Create actual files.

**Part A:** Write a function that counts lines in a file.
```python
def count_lines(filepath: str) -> int:
    """Return the number of lines in a file."""
    # Your code:

# Test with any file you have
```

**Part B:** Write a function that reads a file and returns non-empty lines only.
```python
from typing import List

def read_non_empty_lines(filepath: str) -> List[str]:
    """Return list of non-empty lines (stripped, no blank lines)."""
    # Your code:

# Test: Create a file with some blank lines, then read it
```

**Part C:** Write a function that appends a timestamped entry to a log file.
```python
from datetime import datetime

def log_entry(filepath: str, message: str) -> None:
    """Append '[YYYY-MM-DD HH:MM:SS] message' to file."""
    # Your code:

# Test:
# log_entry("app.log", "Application started")
# log_entry("app.log", "User logged in")
# Then read and print the file contents
```

**Your code:**
```python

```

---

## Task 3: CLOSURE + datetime Integration

**Instructions:** Combine closures with datetime (Week 4 + Week 5).

**Part A:** Create a `make_date_formatter` factory function.
```python
from datetime import datetime

def make_date_formatter(format_string: str):
    """
    Return a function that formats datetime objects using the given format.

    Example:
        us_format = make_date_formatter("%m/%d/%Y")
        eu_format = make_date_formatter("%d/%m/%Y")

        dt = datetime(2026, 2, 14)
        print(us_format(dt))  # "02/14/2026"
        print(eu_format(dt))  # "14/02/2026"
    """
    # Your code:

# Test with different formats
```

**Part B:** Create a `make_time_tracker` closure that tracks elapsed time.
```python
from datetime import datetime

def make_time_tracker():
    """
    Return a function that returns seconds elapsed since tracker was created.

    Example:
        tracker = make_time_tracker()
        # ... do some work ...
        print(tracker())  # e.g., 2.5 (seconds elapsed)
    """
    # Your code (hint: store start_time in closure):

# Test by creating tracker, sleeping briefly, then calling it
```

**Your code:**
```python

```

---

## Task 4: TradeLogger Enhancement (PROJECT)

**Instructions:** Extend your TradeLogger from Day 1 with new features.

```python
from datetime import datetime, timedelta
from typing import List, Optional

class TradeLogger:
    """
    Enhanced TradeLogger with filtering capabilities.

    New methods to implement:
    1. get_trades_since(dt: datetime) -> List[str]
       - Return only trades logged after the given datetime
       - Hint: You'll need to parse the timestamp from each line

    2. get_trades_by_symbol(symbol: str) -> List[str]
       - Return only trades for a specific symbol (e.g., "AAPL")

    3. get_trade_count() -> int
       - Return total number of trades logged

    Keep existing methods: __init__, log_trade, get_trades, clear_log
    """

    def __init__(self, filepath: str):
        # Your existing code
        pass

    def log_trade(self, symbol: str, side: str, price: float, quantity: int):
        # Your existing code (fix format if needed)
        pass

    def get_trades(self) -> List[str]:
        # Your existing code (add .strip())
        pass

    def clear_log(self):
        # Your existing code
        pass

    # NEW METHODS:

    def get_trades_since(self, dt: datetime) -> List[str]:
        """Return trades logged after the given datetime."""
        # Your code:
        pass

    def get_trades_by_symbol(self, symbol: str) -> List[str]:
        """Return trades for a specific symbol."""
        # Your code:
        pass

    def get_trade_count(self) -> int:
        """Return total number of trades."""
        # Your code:
        pass

# Test:
logger = TradeLogger('test_trades.log')
logger.clear_log()
logger.log_trade('AAPL', 'BUY', 150.50, 100)
logger.log_trade('GOOGL', 'SELL', 2800.00, 10)
logger.log_trade('AAPL', 'SELL', 155.00, 50)

print(f"Total trades: {logger.get_trade_count()}")
print(f"AAPL trades: {logger.get_trades_by_symbol('AAPL')}")
```

**Your code:**
```python

```

---

## Task 5: PCAP Multiple Choice (6 Questions)

**Q1:** What is the output?
```python
from datetime import datetime, timedelta

dt = datetime(2026, 2, 28, 23, 30)
dt2 = dt + timedelta(hours=1)
print(dt2.day, dt2.month)
```
- A) 28 2
- B) 1 3
- C) 29 2
- D) Error

**Q2:** What is the output?
```python
with open('test.txt', 'w') as f:
    f.write('abc')
    f.write('def')

with open('test.txt', 'r') as f:
    print(f.readline())
```
- A) abc
- B) abcdef
- C) abc\ndef
- D) Error

**Q3:** What is the output?
```python
from datetime import date

d = date.today()
print(type(d.year).__name__)
```
- A) date
- B) int
- C) str
- D) datetime

**Q4:** What is the output?
```python
lines = []
with open('test.txt', 'w') as f:
    f.writelines(['a\n', 'b\n'])

with open('test.txt', 'r') as f:
    for line in f:
        lines.append(line.strip())
print(lines)
```
- A) ['a\n', 'b\n']
- B) ['a', 'b']
- C) ['ab']
- D) Error

**Q5:** What is the output?
```python
from datetime import datetime

dt1 = datetime(2026, 2, 1, 12, 0)
dt2 = datetime(2026, 2, 1, 14, 30)
diff = dt2 - dt1
print(type(diff).__name__)
```
- A) int
- B) float
- C) timedelta
- D) datetime

**Q6:** Which statement will raise an exception?
```python
# A:
with open('newfile.txt', 'w') as f:
    f.write('test')

# B:
with open('nonexistent.txt', 'r') as f:
    f.read()

# C:
with open('newfile.txt', 'a') as f:
    f.write('test')

# D:
with open('newfile.txt', 'x') as f:
    f.write('test')  # Assume file already exists
```
- A) Statement A
- B) Statement B
- C) Statement C
- D) Both B and D

**Your answers:**
```
Q1:
Q2:
Q3:
Q4:
Q5:
Q6:
```

---

## Task 6: Property + File I/O Integration

**Instructions:** Create a class that uses properties with file backing.

```python
from datetime import datetime
from typing import Optional

class ConfigManager:
    """
    A configuration manager that persists settings to a file.

    Properties:
    - last_updated (read-only): datetime of last config change
    - debug_mode: bool, with getter and setter
    - max_trades: int, with validation (must be > 0)

    The config file format (config.txt):
    debug_mode=True
    max_trades=100
    last_updated=2026-02-03 10:30:45
    """

    def __init__(self, filepath: str):
        self.filepath = filepath
        self._debug_mode = False
        self._max_trades = 10
        self._last_updated: Optional[datetime] = None
        self._load_config()

    def _load_config(self):
        """Load config from file if exists."""
        # Your code:
        pass

    def _save_config(self):
        """Save current config to file."""
        # Your code:
        pass

    @property
    def last_updated(self) -> Optional[datetime]:
        """Read-only: when config was last modified."""
        # Your code:
        pass

    @property
    def debug_mode(self) -> bool:
        # Your code:
        pass

    @debug_mode.setter
    def debug_mode(self, value: bool):
        # Your code (update _last_updated, save to file):
        pass

    @property
    def max_trades(self) -> int:
        # Your code:
        pass

    @max_trades.setter
    def max_trades(self, value: int):
        # Your code (validate > 0, update _last_updated, save):
        pass

# Test:
config = ConfigManager('config.txt')
config.debug_mode = True
config.max_trades = 50
print(f"Debug: {config.debug_mode}, Max: {config.max_trades}")
print(f"Last updated: {config.last_updated}")
```

**Your code:**
```python

```

---

## Task 7: Decorator + File I/O (Week 4 Review)

**Instructions:** Create a decorator that logs function calls to a file.

```python
from datetime import datetime
from functools import wraps

def log_to_file(filepath: str):
    """
    Decorator factory that logs function calls to a file.

    Log format: "YYYY-MM-DD HH:MM:SS | function_name(args) -> result"

    Example usage:
        @log_to_file("calls.log")
        def add(a, b):
            return a + b

        add(2, 3)  # Logs: "2026-02-03 10:30:45 | add(2, 3) -> 5"
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Your code:
            # 1. Call the original function
            # 2. Log the call to file
            # 3. Return the result
            pass
        return wrapper
    return decorator

# Test:
@log_to_file("function_calls.log")
def multiply(a, b):
    return a * b

@log_to_file("function_calls.log")
def greet(name):
    return f"Hello, {name}!"

multiply(3, 4)
multiply(5, 6)
greet("Alice")

# Read and print the log file
with open("function_calls.log", "r") as f:
    print(f.read())
```

**Your code:**
```python

```

---

## Task 8: timedelta Deep Practice

**Instructions:** Solve these practical datetime problems.

**Q1:** Write code to find all Mondays in February 2026.
```python
from datetime import date, timedelta

def mondays_in_month(year: int, month: int) -> list:
    """Return list of all Monday dates in the given month."""
    # Your code:

# Test:
print(mondays_in_month(2026, 2))
# Expected: [date(2026, 2, 2), date(2026, 2, 9), date(2026, 2, 16), date(2026, 2, 23)]
```

**Q2:** Write code to calculate trading days between two dates (exclude weekends).
```python
from datetime import date, timedelta

def trading_days_between(start: date, end: date) -> int:
    """Return count of weekdays (Mon-Fri) between start and end (exclusive)."""
    # Your code:

# Test:
print(trading_days_between(date(2026, 2, 2), date(2026, 2, 9)))  # Mon to Mon = 5 trading days
```

**Q3:** What is the output?
```python
from datetime import datetime, timedelta

start = datetime(2026, 1, 1)
deltas = [timedelta(days=30) for _ in range(3)]
current = start

for d in deltas:
    current += d
    print(current.strftime("%B"), end=" ")
```

**Your answers:**
```
Q1 code:

Q2 code:

Q3 output:
```

---

## Solutions Checklist

- [ ] Task 1: datetime coding practice (3 parts)
- [ ] Task 2: File I/O coding practice (3 parts)
- [ ] Task 3: Closure + datetime integration (2 parts)
- [ ] Task 4: PROJECT - TradeLogger enhancement
- [ ] Task 5: PCAP multiple choice (6 questions)
- [ ] Task 6: Property + File I/O integration
- [ ] Task 7: Decorator + File I/O (Week 4 review)
- [ ] Task 8: timedelta deep practice (3 questions)

---

## Feedback Section

**Time spent:** ___ minutes

**Difficulty (1-10):**

**What clicked today:**


**What's confusing:**


**Questions for mentor:**


---

**When complete:** Notify me for assessment.
