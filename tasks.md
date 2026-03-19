# Week 10, Day 3 — Module Drills + Mock Gap Closure
**Date:** 2026-03-19 | **Focus:** File I/O, os, datetime/time/calendar, + 10 targeted gap questions from mock 1

---

## Task 1 — Mock 1 gap drill: 10 questions (no code, write answers directly)

**Q1:** How many `except` blocks can execute for a single `try` block?
- A) One or more
- B) Not more than one
- C) Exactly one
- D) All matching ones

B


**Q2:** What is the output?
```python
try:
    raise ValueError("v")
except Exception:
    print("Exception")
except ValueError:
    print("ValueError")


Exception

```

**Q3:** What happens?
```python
try:
    raise ValueError
except:
    print("c")
except Exception:
    print("b")

SyntaxError - raw except CANNOT be the front except 
```

**Q4:** What is the output?
```python
for line in open('nonexistent_file.txt', 'rt'):
    print(line)
```
- A) SyntaxError — you can't iterate `open()` directly
- B) Nothing — open() returns None for missing files
- C) FileNotFoundError
- D) Reads line by line

D


**Q5:** Iterating a file object with `for line in f:` yields lines:
- A) Without the `\n` character
- B) Including the `\n` character
- C) As a list of characters
- D) As bytes

B


**Q6:** What is the output?
```python
import random
a = random.choice((0, 100, 3))
print(a == 6)
```
- A) True — `choice` returns a value from the range
- B) False — `choice` picks from the tuple, 6 is not in it
- C) Sometimes True
- D) TypeError

b


**Q7:** What is `len(x)`?
```python
x = '\\'

1

```

**Q8:** What is the output?
```python
print(chr(ord('a') + 3))

d

```

**Q9:** What is the output?
```python
class A:
    x = 10
    def __init__(self):
        self.y = 20

print(hasattr(A, 'x')) True
print(hasattr(A, 'y')) False
```

**Q10:** A file `utils.py` contains `print(__name__)`. It is imported by `main.py` with `import utils`. What is printed?


utils

---

## Task 2 — File I/O: 6 predict-the-output

**Q1:** What is the output?
```python
with open('test.txt', 'w') as f:
    f.write('hello\nworld\n')

with open('test.txt', 'r') as f:
    lines = f.readlines()

print(len(lines)) #2
print(repr(lines[0])) #'hello\n'
```

**Q2:** What is the output?
```python
with open('test.txt', 'w') as f:
    f.writelines(['a', 'b', 'c'])

with open('test.txt', 'r') as f:
    print(f.read())

'abc'
```

**Q3:** What is the output?
```python
with open('test.txt', 'w') as f:
    f.write('hello world')

with open('test.txt', 'r') as f:
    print(f.read(5))
    print(f.tell())
    f.seek(0)
    print(f.read(5))

'hello '
5
'hello '
```

**Q4:** Which mode raises `FileExistsError` if the file already exists?
- A) `'w'`
- B) `'a'`
- C) `'x'`
- D) `'r+'`

C

**Q5:** What is the output?
```python
with open('test.txt', 'w') as f:
    f.write('line1\nline2\nline3\n')

with open('test.txt', 'r') as f:
    line = f.readline()
    print(repr(line)) #'line1\n'


line1\n
```

**Q6:** What happens if you call `f.read()` on an already-exhausted file object (cursor at end)?
- A) `StopIteration`
- B) `IOError`
- C) Returns `''` (empty string)
- D) Returns `None`

C

---

## Task 3 — `os` module: 6 questions

**Q1:** What is the output?
```python
import os
print(type(os.environ))
print(os.environ.get('NONEXISTENT_KEY_XYZ', 'default'))

I don't know, we're printing a class environ
default



```

**Q2:** What is the difference between `os.mkdir('a/b/c')` and `os.makedirs('a/b/c')`?

In the first example we make dir c in directory a/b/
in the second example we make three dirs a, b, c in the current dir I guess


**Q3:** What is the output?
```python
import os
print(os.path.basename('/home/user/project/main.py'))
print(os.path.dirname('/home/user/project/main.py'))
print(os.path.splitext('data.csv'))

#main.py
#home/user/project
#('data', '.csv')


```

**Q4:** What is the output?
```python
import os
print(os.name)
```
- A) `'windows'`
- B) `'nt'` on Windows, `'posix'` on Linux/macOS
- C) `'win32'`
- D) The full OS name string

B


**Q5:** What is the output?
```python
import os
path = os.path.join('algo_backtest', 'data', 'prices.csv')
print(path)
```
(Answer for both Windows and Linux)

/algo_backtest/data/prices.csv



**Q6:** `os.rmdir('folder')` fails. What is the most likely reason?

Most likely the folder does not exist in the current working directory.


---

## Task 4 — `datetime` / `time` / `calendar`: 8 questions

**Q1:** What is the output?
```python
from datetime import datetime
dt = datetime(2026, 3, 19, 14, 30, 0)
print(dt.strftime("%A, %d %B %Y"))
print(dt.strftime("%H:%M"))

#Thursday, 19 March 2026
#14:30


```

**Q2:** What is the output?
```python
from datetime import datetime
s = "19/03/2026 14:30"
dt = datetime.strptime(s, "%d/%m/%Y %H:%M")
print(dt.year, dt.month, dt.day)

#2026 3 19
```

**Q3:** What is the output?
```python
from datetime import timedelta
delta = timedelta(days=2, hours=3, seconds=30)
print(delta.days)
print(delta.seconds)
print(delta.total_seconds())

2
10830
183630.0

Although I ran that code - it's a stupid question to assume I'd know it or calculate by heart. It's weird.


```

**Q4:** What is the output?
```python
import time
t = time.localtime()
print(type(t).__name__)
print(t.tm_wday)   # assuming today is Wednesday
```
- What type is returned?
- What does `tm_wday` value mean? (Monday = ?)

time
2


**Q5:** What is the output?
```python
import time
print(type(time.time()))

float
```

**Q6:** What is the output?
```python
import calendar
print(calendar.weekday(2026, 3, 19))
print(calendar.THURSDAY)
print(calendar.isleap(2026))

3
3
False

```

**Q7:** What is the output?
```python
import calendar
first_day, num_days = calendar.monthrange(2024, 2)
print(first_day, num_days)

3 29

Again I had to run this code to check it as there's no way to know that without that...
I'm just a human being

```

**Q8:** What is the output?
```python
import calendar
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.weekheader(2)

Su Mo Tu We Th Fr Sa
```

---

## Task 5 — Mixed PCAP simulation: 10 questions

**Q1:** What is the output?
```python
x = "hello"
print(x[1:4])
print(x[-2:])
print(x[::-1])

ell
lo
olleh

```

**Q2:** What is the output?
```python
class A:
    count = 0
    def __init__(self):
        A.count += 1

a1 = A()
a2 = A()
a3 = A()
print(A.count)
print(a1.count)


3
3

```

**Q3:** What is the output?
```python
def f(x, items=[]):
    items.append(x)
    return items

print(f(1))
print(f(2, []))
print(f(3))

[1]
[2]
[1, 3]

```

**Q4:** What is the output?
```python
print(bool(""))
print(bool("0"))
print(bool([]))
print(bool([0]))

False
True
False
True

```

**Q5:** What is the output?
```python
x = (1, 2, 3)
y = x
y += (4,)
print(x)
print(y)

(1, 2, 3, 4)
(1, 2, 3, 4)
```

**Q6:** What is the output?
```python
try:
    raise ValueError("v")
except ValueError as e:
    msg = str(e)
print(msg)
```
- A) `ValueError: v`
- B) `v`
- C) `NameError`
- D) `<class 'ValueError'>`

A

**Q7:** What is the output?
```python
def outer():
    x = 10
    def inner():
        return x * 2
    x = 20
    return inner()

print(outer())


40

```

**Q8:** What is the output?
```python
a, *b, c = [1, 2, 3, 4, 5]
print(type(b))
print(b)
print(c)

tuple
(2, 3, 4)
5

```

**Q9:** What is the output?
```python
xs = [1, 2, 3]
ys = xs[:]
ys[0] = 99
print(xs[0])
print(ys[0])

1
99



```

**Q10:** What is the output?
```python
print(__name__)
```
- A) `__main__` always
- B) The filename without `.py`
- C) `__main__` if run directly, module name if imported
- D) `None`


C


---

## Answers

### Task 1
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

### Task 2
Q1:
Q2:
Q3:
Q4:
Q5:
Q6:

### Task 3
Q1:
Q2:
Q3:
Q4:
Q5:
Q6:

### Task 4
Q1:
Q2:
Q3:
Q4:
Q5:
Q6:
Q7:
Q8:

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
