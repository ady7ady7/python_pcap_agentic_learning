# Week 11, Day 2 — 2026-03-24

**Topic:** File I/O | os module | datetime | Generators | Gap closure
**Mode:** PCAP drills — Pure Python only | Heavy volume

---

## Task 1 — Predict the output: yield + early return (gap from Day 1)

```python
def gen():
    return
    yield 1
    yield 2

g = gen()
print(type(g).__name__)
print(list(g))
```

And a follow-up — what does this print?

```python
def gen2():
    yield
    return
    yield 1

print(list(gen2()))
```

---

## Task 2 — Predict the output: IOError / OSError (gap from Day 1)

```python
print(IOError is OSError)
print(issubclass(FileNotFoundError, OSError))
print(issubclass(FileNotFoundError, IOError))
```

What are the three outputs?

---

## Task 3 — File I/O: predict the output

```python
with open("test.txt", "w") as f:
    f.write("line1\n")
    f.write("line2\n")

with open("test.txt", "r") as f:
    lines = f.readlines()

print(len(lines))
print(repr(lines[0]))
print(repr(lines[-1]))
```

What is the output?

---

## Task 4 — File I/O: predict the output

```python
with open("test.txt", "w") as f:
    f.write("hello")

with open("test.txt", "r") as f:
    print(repr(f.read(3)))
    print(repr(f.read(3)))
    print(repr(f.read(3)))
```

What is the output?

---

## Task 5 — File I/O: predict the output

```python
with open("test.txt", "w") as f:
    f.write("alpha\nbeta\ngamma\n")

with open("test.txt", "r") as f:
    line = f.readline()
    print(repr(line))
    line = f.readline()
    print(repr(line))
```

What is the output?

---

## Task 6 — os module: predict the output

```python
import os

path = "/home/user/docs/report.pdf"
print(os.path.basename(path))
print(os.path.dirname(path))
print(os.path.split(path))
print(os.path.splitext(path))
```

What is the output?

---

## Task 7 — os module: multiple choice

```python
import os

result = os.path.join("home", "user", "file.txt")
print(result)
```

On Linux/POSIX, what is the output?

- A) `home\user\file.txt`
- B) `home/user/file.txt`
- C) `/home/user/file.txt`
- D) `TypeError`

---

## Task 8 — datetime: predict the output

```python
from datetime import datetime, timedelta

dt = datetime(2026, 3, 24, 10, 30, 0)
delta = timedelta(days=3, hours=2)
result = dt + delta

print(result.day)
print(result.hour)
```

What is the output?

---

## Task 9 — datetime: predict the output

```python
from datetime import timedelta

td = timedelta(days=1, seconds=3600)
print(td.days)
print(td.seconds)
print(td.total_seconds())
```

What is the output?

---

## Task 10 — datetime: multiple choice

```python
from datetime import datetime

dt = datetime(2026, 3, 24)
print(dt.strftime("%Y-%m-%d %H:%M"))
```

- A) `2026-03-24 00:00`
- B) `2026-24-03 00:00`
- C) `2026-03-24`
- D) `ValueError`

---

## Task 11 — Generators: predict the output

```python
def evens(limit):
    n = 0
    while n <= limit:
        yield n
        n += 2

gen = evens(6)
print(next(gen))
print(next(gen))
print(list(gen))
```

What is the output?

---

## Task 12 — Generators: predict the output

```python
def gen():
    yield from [1, 2, 3]
    yield from range(3)

result = list(gen())
print(result)
print(len(result))
```

What is the output?

---

## Task 13 — Generators: multiple choice

```python
def squares():
    for i in range(5):
        yield i ** 2

g = squares()
list(g)
print(next(g))
```

- A) `0`
- B) `16`
- C) `StopIteration` is raised
- D) `None`

---

## Task 14 — Mixed: exception + file I/O

```python
import errno

try:
    f = open("no_such_file.txt", "r")
except OSError as e:
    print(e.errno)
    print(type(e).__name__)
```

What is the output? (Assume the file does not exist.)

---

## Task 15 — Scope + closure (gap reinforcement)

```python
def outer():
    x = 10
    def inner():
        x += 1
        return x
    return inner

f = outer()
print(f())
```

What happens? What is the fix?

---

## Answers

### Task 1
```
gen():
gen2():
```

### Task 2
```
output:
```

### Task 3
```
output:
```

### Task 4
```
output:
```

### Task 5
```
output:
```

### Task 6
```
output:
```

### Task 7
Answer:

### Task 8
```
output:
```

### Task 9
```
output:
```

### Task 10
Answer:

### Task 11
```
output:
```

### Task 12
```
output:
```

### Task 13
Answer:

### Task 14
```
output:
```

### Task 15
```
what happens:
fix:
```
