# Week 5, Day 5 - Friday
## Topic: Week Review & Exam Prep

**Date:** 2026-02-06

**Target Difficulty:** 5/10

**Focus:** Consolidate the week's topics, prep for weekend exams

**Remember:** Work in `practice.py`, paste FINAL answers here for review.

---

## Task 1: PCAP Warm-up (Pure Python)

**Q1:** What is the output?
```python
data = [1, 2, [3, 4]]
copy = data[:]
copy[2].append(5)
print(data)


Answer: [1, 2, [3, 4, 5]]
```

**Q2:** What is the output?
```python
def outer():
    x = 10
    def inner():
        nonlocal x
        x += 5
        return x
    return inner

f = outer()
print(f(), f())

Answer: 15, 20
```

**Your answers:**
```
Q1:
Q2:
```

---

## Task 2: Decorator Mastery Check

**Instructions:** Implement a `@retry` decorator factory.

```python
from functools import wraps

def retry(max_attempts: int):
    """
    Decorator factory that retries a function if it raises an exception.

    After max_attempts failures, re-raise the last exception.

    Example:
        @retry(3)
        def flaky_api():
            # might fail sometimes
            ...
    """
    # Your code (3 layers: retry -> decorator -> wrapper)

# Test:
attempt_count = 0

@retry(3)
def unstable_function():
    global attempt_count
    attempt_count += 1
    if attempt_count < 3:
        raise ValueError(f'Attempt {attempt_count} failed')
    return 'Success!'

print(unstable_function())
# Expected: "Success!" (after 2 failed attempts)
```

**Your code:**
```python

from functools import wraps

def retry(max_attempts: int):
    """
    Decorator factory that retries a function if it raises an exception.

    After max_attempts failures, re-raise the last exception.

    Example:
        @retry(3)
        def flaky_api():
            # might fail sometimes
            ...
    """
    
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_attempts):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    last_exception = e
            raise last_exception
        return wrapper
    return decorator

# Test:
attempt_count = 0


These decorators FEEL VERY DIFFICULT and I struggled with this one a lot and I couldn't figure out the proper patterna nd had to ask AI for aid. AS you know, I want to understand things instead of just copy-pasting stuff, so I'm not satisfied with that. We definitely ned to practice thsi mroe.

```

---

## Task 3: datetime + File I/O Combined

**Instructions:** Write a function that reads a log file and filters entries by date range.

```python
from datetime import datetime
from typing import List

def filter_log_by_date(filepath: str, start: datetime, end: datetime) -> List[str]:
    """
    Read a log file and return only lines where timestamp falls
    between start and end (inclusive).

    Log format per line: "YYYY-MM-DD HH:MM:SS | message"

    Steps:
    1. Open and read the file
    2. Parse the timestamp from each line
    3. Keep only lines within the date range
    4. Return as list of stripped strings
    """
    # Your code:

# Test:
# First create a test log
with open('test_filter.log', 'w') as f:
    f.write('2026-02-01 10:00:00 | Server started\n')
    f.write('2026-02-03 14:30:00 | Trade executed\n')
    f.write('2026-02-05 09:15:00 | Error occurred\n')
    f.write('2026-02-06 16:00:00 | Shutdown\n')

start = datetime(2026, 2, 2)
end = datetime(2026, 2, 5, 23, 59)
results = filter_log_by_date('test_filter.log', start, end)

for line in results:
    print(line)
# Expected:
# 2026-02-03 14:30:00 | Trade executed
# 2026-02-05 09:15:00 | Error occurred
```

**Your code:**
```python

from datetime import datetime
from typing import List

def filter_log_by_date(filepath: str, start: datetime, end: datetime) -> List[str]:
    '''Read a log file and return only lines where timestamp falls between stard and end (inclusive
    
      Log format per line "YYYY-MM-DD HH:MM:SS | message"
    )'''
    matching_logs = []
    with open(filepath, 'r') as r:
        for line in r:
            parts = line.split(' ')
            date = parts[0:2]
            date = str(' '.join(date))
            date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            
            if date > start and date < end:
                matching_logs.append(line)
    
    return matching_logs
            

```

---

## Task 4: PCAP Simulation (10 Questions — Exam Warmup)

**Q1:** What is the output?
```python
def deco(func):
    def wrapper():
        return func() + '!'
    return wrapper

@deco
@deco
def greet():
    return 'hi'

print(greet())
```
- A) hi!
- B) hi!!
- C) !hi!
- D) Error

B

**Q2:** What is the output?
```python
with open('x.txt', 'w') as f:
    f.write('abc\n')
    f.write('def\n')

with open('x.txt') as f:
    lines = f.readlines()
print(len(lines), lines[0].strip())
```
- A) 2 abc
- B) 1 abcdef
- C) 2 abc\n
- D) Error

A

**Q3:** What is the output?
```python
from datetime import date, timedelta
d = date(2026, 1, 31) + timedelta(days=1)
print(d.month, d.day)
```
- A) 1 32
- B) 2 1
- C) Error
- D) 2 0

B


**Q4:** What is the output?
```python
def make_counter():
    count = [0]
    def increment():
        count[0] += 1
        return count[0]
    return increment

c1 = make_counter()
c2 = make_counter()
print(c1(), c1(), c2())
```
- A) 1 2 3
- B) 1 2 1
- C) 1 1 1
- D) Error

B

**Q5:** What does `functools.wraps` NOT preserve?
- A) `__name__`
- B) `__doc__`
- C) `__module__`
- D) `__code__`


C

**Q6:** What is the output?
```python
try:
    f = open('nonexistent.txt', 'r')
except IOError:
    print('A', end=' ')
except FileNotFoundError:
    print('B', end=' ')
print('C')
```
- A) A C
- B) B C
- C) A B C
- D) Error

B

**Q7:** What is the output?
```python
from datetime import datetime
dt = datetime(2026, 2, 6)
print(dt.strftime('%d/%m/%y'))
```
- A) 06/02/2026
- B) 06/02/26
- C) 2/6/26
- D) 02/06/26

A

**Q8:** What is the output?
```python
def f(a, b=None):
    if b is None:
        b = []
    b.append(a)
    return b

print(f(1))
print(f(2))
```
- A) [1] [1, 2]
- B) [1] [2]
- C) [1, 2] [1, 2]
- D) Error

B

**Q9:** Which exception is the parent of FileNotFoundError?
- A) IOError
- B) ValueError
- C) TypeError
- D) RuntimeError

A

**Q10:** What is the output?
```python
x = 'hello'
print(x[::-1][1:4])
```
- A) oll
- B) lle
- C) lle
- D) olle

ERROR ON YOUR SIDE, both B and C are correct

**Your answers:**
```
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
```

---

## Task 5: PROJECT — BacktestEngine `__str__` Method

**Instructions:** Your test output showed `<...object at 0x...>`. Add a `__str__` method.

Open `algo_backtest/engine/backtest_engine.py` and add:

```python
def __str__(self) -> str:
    """
    Return a summary like:
    BacktestEngine: 2 open | 3 closed | PnL: $1500.00
    """
    # Your code:
```

**Your code:**
```python

def __str__(self) -> str:
    """
    Return a summary like:
    BacktestEngine: 2 open | 3 closed | PnL: $1500.00
    """
    
    return f'BacktestEngine: {(self.position_manager.get_position_count())} open | {len(self.completed_trades)} closed | PnL: ${self.total_pnl}'
```

---

## Task 6: Week 5 Self-Assessment

Answer honestly — this helps me calibrate next week.

**Q1:** Rate your comfort (1-5) with each topic:
```
Decorators (no args): 4
Decorators (with args): 3 (complicated/new decorators - 2)
File modes (w/a/r/x): 5
File read methods (read/readline/readlines): 4
datetime (strftime/strptime): 4
timedelta arithmetic: 5
Closures: 5
Properties: 5
```

**Q2:** Which topic from this week do you want on next week's exams?

Maybe decorators?

**Q3:** Which topic do you NEVER want to see again (because you've nailed it)?

Thre's no such topic, it's always useful to reinforce and revise topics, as Python is very broad and I might forget something with time

**Your answers:**
```
Q1:

Q2:

Q3:
```

---

## Task 7: Predict the Output — Decorator Stacking

**Instructions:** Trace carefully. No running!

**Q1:**
```python
def bold(func):
    def wrapper():
        return '<b>' + func() + '</b>'
    return wrapper

def italic(func):
    def wrapper():
        return '<i>' + func() + '</i>'
    return wrapper

@bold
@italic
def say_hello():
    return 'hello'

print(say_hello())
```

**Q2:** Now reverse the order:
```python
@italic
@bold
def say_hello():
    return 'hello'

print(say_hello())
```

**Hint:** Remember: `@bold @italic def f()` = `f = bold(italic(f))`

**Your answers:**
```
Q1: <b><i>text<i><b>
Q2: <i><b>text<b><i>
```

---

## Task 8: Exception Handling + File I/O

**Instructions:** Write a function that safely reads multiple files and collects results.

```python
from typing import Dict

def read_multiple_files(filepaths: list) -> Dict[str, str]:
    """
    Attempt to read each file in the list.

    Returns:
        Dict mapping filepath -> contents (for successful reads)

    Files that don't exist or can't be read should be skipped
    (not crash the program). Print a warning for each skipped file.

    Example:
        result = read_multiple_files(['exists.txt', 'missing.txt', 'also_exists.txt'])
        # Prints: "Warning: could not read missing.txt"
        # Returns: {'exists.txt': 'contents...', 'also_exists.txt': 'contents...'}
    """
    # Your code:

# Test:
# Create some test files
with open('file_a.txt', 'w') as f:
    f.write('content A')
with open('file_c.txt', 'w') as f:
    f.write('content C')

result = read_multiple_files(['file_a.txt', 'file_b.txt', 'file_c.txt'])
print(result)
# Expected:
# Warning: could not read file_b.txt
# {'file_a.txt': 'content A', 'file_c.txt': 'content C'}
```

**Your code:**
```python

from typing import Dict

def read_multiple_files(filepaths: list) -> Dict[str, str]:
    """
    Attempt to read each file in the list.

    Returns:
        Dict mapping filepath -> contents (for successful reads)

    Files that don't exist or can't be read should be skipped
    (not crash the program). Print a warning for each skipped file.

    Example:
        result = read_multiple_files(['exists.txt', 'missing.txt', 'also_exists.txt'])
        # Prints: "Warning: could not read missing.txt"
        # Returns: {'exists.txt': 'contents...', 'also_exists.txt': 'contents...'}
    """
    
    contents = {}
    for filepath in filepaths:
        try: 
            with open(filepath, 'r') as r:
                text = r.read()
                contents[filepath] = {text}
                    
        except Exception as e:
            print(f'Warning, an exception {str(e)} occured within filepath {filepath}, continuing.')
            continue   
    
    return contents

Everything went as expected:

$ python practice.py
Warning, an exception [Errno 2] No such file or directory: 'file_b.txt' occured within filepath file_b.txt, continuing
{'file_a.txt': {'content A'}, 'file_c.txt': {'content C'}}
(.venv) 


```

---

## Solutions Checklist

- [ ] Task 1: PCAP warm-up (2 questions)
- [ ] Task 2: @retry decorator
- [ ] Task 3: filter_log_by_date function
- [ ] Task 4: PCAP simulation (10 questions)
- [ ] Task 5: BacktestEngine __str__
- [ ] Task 6: Week 5 self-assessment
- [ ] Task 7: Decorator stacking prediction
- [ ] Task 8: Exception handling + File I/O

---

## Feedback Section

**Time spent:** ___ minutes

**Difficulty (1-10):**

**Ready for weekend exams?** yes/no

---

**Weekend:** Complete Week5_Exam_A.md and Week5_Exam_B.md (will be generated after assessment)

**When complete:** Notify me for assessment + exam generation.
