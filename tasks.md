# Week 5, Day 3 - Wednesday
## Topic: Decorator Mastery & File Modes Deep Dive

**Date:** 2026-02-04

**Lesson File:** [week3_5_stdlib_fileio.md](lessons/week3_5_stdlib_fileio.md)

**Target Difficulty:** 6/10

**Focus Areas:** Decorator patterns, file modes, type hint contracts

**Remember:** Work in `practice.py`, paste FINAL answers here for review.

---

## Task 1: File Mode Drill (Reinforce 'w' vs 'a')

**Instructions:** Predict the output WITHOUT running. Then verify.

**Q1:**
```python
with open('test.txt', 'w') as f:
    f.write('first')

with open('test.txt', 'w') as f:
    f.write('second')

with open('test.txt', 'r') as f:
    print(f.read())
```

**Q2:**
```python
with open('test.txt', 'w') as f:
    f.write('first')

with open('test.txt', 'a') as f:
    f.write('second')

with open('test.txt', 'r') as f:
    print(f.read())
```

**Q3:**
```python
# File doesn't exist yet
with open('new.txt', 'a') as f:
    f.write('hello')

with open('new.txt', 'r') as f:
    print(f.read())
```

**Q4:** You want to create a log file that accumulates entries over time. Which mode?
- A) 'w'
- B) 'a'
- C) 'r'
- D) 'x'

**Your answers:**
```
Q1:
Q2:
Q3:
Q4:
```

---

## Task 2: Decorator Pattern Practice

**Instructions:** Fix each broken decorator. Explain what was wrong.

**Part A:** This decorator should log every call, but it only shows the last call.
```python
from functools import wraps

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('calls.log', 'w') as f:  # BUG HERE
            f.write(f'{func.__name__} called\n')
        return result
    return wrapper

@log_calls
def greet(name):
    return f'Hello, {name}'

greet('Alice')
greet('Bob')
greet('Charlie')

# Expected in calls.log:
# greet called
# greet called
# greet called

# Actual in calls.log:
# greet called  (only one!)
```
**Fix and explain:**
```python

```

**Part B:** This decorator calls the function twice (wasteful!). Fix it.
```python
from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with {args}')
        print(f'Result: {func(*args, **kwargs)}')  # First call
        return func(*args, **kwargs)  # Second call!
    return wrapper

@debug
def expensive_operation(n):
    print('Doing expensive work...')
    return n * 2

expensive_operation(5)
# Prints "Doing expensive work..." TWICE!
```
**Fix and explain:**
```python

```

---

## Task 3: Decorator with Arguments (Corrected Pattern)

**Instructions:** Implement a working `@log_to_file` decorator.

```python
from datetime import datetime
from functools import wraps

def log_to_file(filepath: str):
    """
    Decorator factory that logs function calls to a file.

    Requirements:
    1. APPEND to file (don't overwrite)
    2. Call wrapped function ONCE only
    3. Format: "TIMESTAMP | func_name(args) -> result"
    4. Preserve function metadata with @wraps
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # YOUR CODE HERE
            pass
        return wrapper
    return decorator

# Test:
@log_to_file('operations.log')
def add(a, b):
    return a + b

@log_to_file('operations.log')
def multiply(a, b):
    return a * b

# Clear log first
open('operations.log', 'w').close()

add(2, 3)
add(10, 20)
multiply(4, 5)

# Print the log
with open('operations.log', 'r') as f:
    print(f.read())

# Expected output (3 lines):
# 2026-02-04 10:30:45 | add(2, 3) -> 5
# 2026-02-04 10:30:45 | add(10, 20) -> 30
# 2026-02-04 10:30:45 | multiply(4, 5) -> 20
```

**Your code:**
```python

```

---

## Task 4: Type Hint Contracts

**Instructions:** The function signature tells you what types to expect. Don't re-convert!

**Q1:** What's wrong with this code?
```python
from datetime import datetime

def format_date(dt: datetime) -> str:
    """Format datetime as string."""
    parsed = datetime.strptime(dt, '%Y-%m-%d')  # ???
    return parsed.strftime('%B %d, %Y')
```

**Q2:** Fix the function:
```python
from datetime import datetime

def format_date(dt: datetime) -> str:
    """Format datetime as string."""
    # Your fix:
```

**Q3:** What's wrong here?
```python
def process_count(count: int) -> str:
    num = int(count)  # ???
    return f'Count is {num}'
```

**Your answers:**
```
Q1 explanation:

Q2 code:

Q3 explanation:
```

---

## Task 5: PROJECT - BacktestEngine Start

**Instructions:** Begin the core backtesting engine for AlgoBacktest.

```python
from datetime import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class Trade:
    """Represents a single trade."""
    symbol: str
    side: str  # 'BUY' or 'SELL'
    entry_price: float
    quantity: int
    entry_time: datetime
    exit_price: Optional[float] = None
    exit_time: Optional[datetime] = None

    @property
    def is_closed(self) -> bool:
        """Return True if trade has been exited."""
        # Your code:
        pass

    @property
    def pnl(self) -> Optional[float]:
        """
        Calculate profit/loss if trade is closed.
        BUY: (exit_price - entry_price) * quantity
        SELL: (entry_price - exit_price) * quantity
        Return None if trade is still open.
        """
        # Your code:
        pass


class BacktestEngine:
    """
    Simple backtesting engine that tracks trades and calculates performance.
    """

    def __init__(self):
        self._trades: List[Trade] = []
        self._start_time: Optional[datetime] = None

    def start(self) -> None:
        """Start the backtest session."""
        self._start_time = datetime.now()
        self._trades = []

    def open_trade(self, symbol: str, side: str, price: float, quantity: int) -> Trade:
        """
        Open a new trade and add it to the list.
        Return the created Trade object.
        """
        # Your code:
        pass

    def close_trade(self, trade: Trade, exit_price: float) -> None:
        """
        Close an existing trade by setting exit_price and exit_time.
        """
        # Your code:
        pass

    @property
    def open_trades(self) -> List[Trade]:
        """Return list of trades that haven't been closed."""
        # Your code:
        pass

    @property
    def closed_trades(self) -> List[Trade]:
        """Return list of trades that have been closed."""
        # Your code:
        pass

    @property
    def total_pnl(self) -> float:
        """Return sum of PnL from all closed trades."""
        # Your code:
        pass

# Test:
engine = BacktestEngine()
engine.start()

# Open some trades
trade1 = engine.open_trade('AAPL', 'BUY', 150.0, 100)
trade2 = engine.open_trade('GOOGL', 'SELL', 2800.0, 10)

print(f'Open trades: {len(engine.open_trades)}')  # 2
print(f'Closed trades: {len(engine.closed_trades)}')  # 0

# Close trades
engine.close_trade(trade1, 155.0)  # BUY at 150, SELL at 155 = +500
engine.close_trade(trade2, 2750.0)  # SELL at 2800, BUY at 2750 = +500

print(f'Open trades: {len(engine.open_trades)}')  # 0
print(f'Closed trades: {len(engine.closed_trades)}')  # 2
print(f'Total PnL: ${engine.total_pnl}')  # $1000.0
```

**Your code:**
```python

```

---

## Task 6: PCAP Multiple Choice (6 Questions)

**Q1:** What is the output?
```python
def outer(func):
    def inner(*args):
        print('before')
        result = func(*args)
        print('after')
        return result
    return inner

@outer
def say(msg):
    print(msg)
    return msg.upper()

x = say('hello')
print(x)
```
- A) hello, HELLO
- B) before, hello, after, HELLO
- C) hello, before, after, HELLO
- D) before, after, hello, HELLO

**Q2:** What does `@wraps(func)` do?
- A) Calls the wrapped function
- B) Preserves the original function's metadata (__name__, __doc__)
- C) Makes the function run faster
- D) Prevents the function from being called twice

**Q3:** What is the output?
```python
with open('test.txt', 'w') as f:
    result = f.write('hello')
print(result)
```
- A) None
- B) 'hello'
- C) 5
- D) True

**Q4:** Which correctly implements a decorator with arguments?
```python
# A:
def deco(arg):
    def wrapper(func):
        return func
    return wrapper

# B:
def deco(func, arg):
    def wrapper():
        return func()
    return wrapper

# C:
def deco(func):
    def wrapper(arg):
        return func(arg)
    return wrapper
```
- A) Option A
- B) Option B
- C) Option C
- D) None of the above

**Q5:** What is the output?
```python
from datetime import datetime, timedelta

dt = datetime(2026, 3, 1, 0, 0)
dt2 = dt - timedelta(hours=1)
print(dt2.month, dt2.day)
```
- A) 3 1
- B) 2 28
- C) 2 29
- D) Error

**Q6:** What happens when you open a file with mode 'x' and the file already exists?
- A) The file is overwritten
- B) Content is appended
- C) FileExistsError is raised
- D) FileNotFoundError is raised

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

## Task 7: Missing Function from Day 2

**Instructions:** Implement the function you missed yesterday.

```python
from typing import List

def read_non_empty_lines(filepath: str) -> List[str]:
    """
    Read a file and return only non-empty lines.

    Requirements:
    1. Strip whitespace from each line
    2. Skip lines that are empty after stripping
    3. Return as a list of strings (without newlines)

    Example:
        File contents:
        "hello\n"
        "\n"
        "  \n"
        "world\n"

        Returns: ['hello', 'world']
    """
    # Your code:

# Test:
# Create test file
with open('test_lines.txt', 'w') as f:
    f.write('hello\n\n   \nworld\n  python  \n')

result = read_non_empty_lines('test_lines.txt')
print(result)  # ['hello', 'world', 'python']
```

**Your code:**
```python

```

---

## Task 8: Closure + Decorator Integration

**Instructions:** Create a decorator factory using closure concepts.

```python
def rate_limiter(max_calls: int):
    """
    Decorator factory that limits how many times a function can be called.

    After max_calls, the function returns None without executing.

    Example:
        @rate_limiter(3)
        def greet(name):
            return f'Hello, {name}'

        print(greet('A'))  # Hello, A
        print(greet('B'))  # Hello, B
        print(greet('C'))  # Hello, C
        print(greet('D'))  # None (limit reached)

    Hint: Use a list to track call count (closure trick from Week 4)
    """
    # Your code:

# Test:
@rate_limiter(3)
def expensive_api_call(query):
    return f'Results for: {query}'

print(expensive_api_call('python'))  # Results for: python
print(expensive_api_call('java'))    # Results for: java
print(expensive_api_call('rust'))    # Results for: rust
print(expensive_api_call('go'))      # None
print(expensive_api_call('c++'))     # None
```

**Your code:**
```python

```

---

## Solutions Checklist

- [ ] Task 1: File mode drill (4 questions)
- [ ] Task 2: Decorator bug fixes (2 parts)
- [ ] Task 3: log_to_file decorator (corrected)
- [ ] Task 4: Type hint contracts (3 questions)
- [ ] Task 5: PROJECT - BacktestEngine
- [ ] Task 6: PCAP multiple choice (6 questions)
- [ ] Task 7: read_non_empty_lines (Day 2 makeup)
- [ ] Task 8: rate_limiter decorator

---

## Feedback Section

**Time spent:** ___ minutes

**Difficulty (1-10):**

**What clicked today:**


**What's confusing:**


**Questions for mentor:**


---

**When complete:** Notify me for assessment.