# Week 13 Day 1 — Medium Volume: Gap Revisit
**Date:** 2026-04-07 | **Focus:** Custom __str__ trap, open() modes, raise-from, hasattr vs __dict__, random module, select-two patterns

---

## Task 1 — Custom `__str__` on exceptions: locked for good [Exam A Q4/Q5 gap]

**TEACH — the rule, once and for all:**
```
print(e)  →  calls e.__str__()
str(e)    →  calls e.__str__()
repr(e)   →  calls e.__repr__() — default is ClassName(args)
e.args    →  tuple from super().__init__() — unaffected by __str__
```

If `__str__` is defined, it **completely replaces** what `print(e)` shows.
The constructor argument (`"ignored arg"`) only affects `e.args` — NOT `print(e)`.

**Why Q4 confused you:** You saw `raise MyError("ignored arg")` and assumed `print(e)` would show that arg. It doesn't — `__str__` intercepts it entirely.

**A)** Predict ALL outputs — no shortcuts, trace each line:
```python
class AppError(Exception):
    def __init__(self, code, msg):
        super().__init__(msg)
        self.code = code

    def __str__(self):
        return f"[{self.code}] error occurred"

try:
    raise AppError(404, "not found")
except AppError as e:
    print(e)              # ?
    print(str(e))         # ?
    print(repr(e))        # ?
    print(e.args)         # ?
    print(e.code)         # ?
```

**B)** Now WITHOUT `__str__` — what changes?
```python
class AppError(Exception):
    def __init__(self, code, msg):
        super().__init__(msg)
        self.code = code

try:
    raise AppError(404, "not found")
except AppError as e:
    print(e)              # ?
    print(e.args)         # ?
```

**C)** Multiple choice — which is True?
```python
class E(Exception):
    def __str__(self):
        return "custom"

e = E("original arg")
```
- A: `str(e) == "original arg"`
- B: `str(e) == "custom"`
- C: `e.args == ()`
- D: `repr(e) == "custom"`

Write answers here:
```
A)
    print(e)              #[404] error occurred
    print(str(e))         #[404] error occurred
    print(repr(e))        #code: 404
    print(e.args)         #code: 404
    print(e.code)         # 404
B)
    print(e)              #'not found'
    print(e.args)         #('not found', ) #THIS FEELS STILL SUPER FUCKING DIFFICULT...
 
C) B, C
```

---

## Task 2 — `open()` modes: the complete map [Exam A Q19 gap]

**TEACH — pointer position matters:**
```
Mode   | Creates? | Truncates? | Pointer start | Read? | Write?
'r'    | No (fail)| No         | Beginning     | Yes   | No
'w'    | Yes      | Yes        | Beginning     | No    | Yes
'a'    | Yes      | No         | END           | No    | Yes
'x'    | No(fail) | No         | Beginning     | No    | Yes  ← exclusive create
'r+'   | No (fail)| No         | Beginning     | Yes   | Yes  ← read+write, no truncate
'w+'   | Yes      | Yes        | Beginning     | Yes   | Yes  ← truncates!
'a+'   | Yes      | No         | END (writes)  | Yes   | Yes  ← writes always at end
```

**Key distinctions:**
- `'r+'` vs `'w+'`: both read+write, but `'w+'` TRUNCATES, `'r+'` does NOT
- `'r+'` vs `'a+'`: both no-truncate, but `'a+'` pointer for writes is always END
- `'x'` raises `FileExistsError` if file exists — use for "create only if new"

**A)** True or False:
```
1. open('f', 'r+') truncates the file
2. open('f', 'w+') truncates the file
3. open('f', 'a+') allows reading
4. open('f', 'a') allows reading
5. open('f', 'r+') raises an error if the file doesn't exist
6. open('f', 'x') raises FileExistsError if file already exists
7. open('f', 'a') always writes at the end, regardless of seek()
8. open('f') is the same as open('f', 'r')
```

**B)** Match the description to the mode:
```
1. Read + write, no truncate, pointer at start, file must exist  → ?
2. Write only, always appends, creates if missing                → ?
3. Read + write, truncates first, creates if missing             → ?
4. Exclusive create, fails if exists                             → ?
5. Read + write + append, writes always go to end               → ?
```

Write answers here:
```
A) 1-8:
# 1. open('f', 'r+') truncates the file - NO
# 2. open('f', 'w+') truncates the file - Yes
# 3. open('f', 'a+') allows reading # Yes
# 4. open('f', 'a') allows reading #No
# 5. open('f', 'r+') raises an error if the file doesn't exist #Yes
# 6. open('f', 'x') raises FileExistsError if file already exists #Yes
# 7. open('f', 'a') always writes at the end, regardless of seek() #Yes
# 8. open('f') is the same as open('f', 'r') #Yes



B) 1-5:
# 1. Read + write, no truncate, pointer at start, file must exist  → r+
# 2. Write only, always appends, creates if missing                → a
# 3. Read + write, truncates first, creates if missing             → w+
# 4. Exclusive create, fails if exists                             → x
# 5. Read + write + append, writes always go to end               → a+
```

---

## Task 3 — `random` module [Real exam Q6 pattern]

**TEACH:**
```python
import random
random.seed(n)          # set seed → reproducible sequence
random.random()         # float in [0.0, 1.0)  — NEVER >= 1
random.randint(a, b)    # int in [a, b] inclusive — CAN return b
random.choice(seq)      # random element from non-empty sequence
random.sample(seq, k)   # k unique elements from seq, returns list
random.shuffle(lst)     # shuffles list IN PLACE, returns None
```

**Key traps:**
```python
random.seed(1); v1 = random.random()
random.seed(1); v2 = random.random()
v1 == v2   # True — same seed → same sequence

random.random() >= 1   # ALWAYS False — range is [0.0, 1.0)
random.choice([1,2,3]) >= 1  # ALWAYS True — min value is 1
len(random.sample([1,2,3], 2)) > 2  # ALWAYS False — len==2
```

**A)** True or False — which always evaluate to True?
```python
import random
random.seed(99)
a = random.random()
random.seed(99)
b = random.random()

print(a == b)                           # ?
print(a < 1)                            # ?
print(a >= 0)                           # ?
print(random.choice([5, 10, 15]) >= 5) # ?
print(len(random.sample([1,2,3], 2)) == 3)  # ?
```

**B)** Multiple choice — which TWO always evaluate to True?
```python
random.seed(7)
x = random.randint(1, 6)
```
- A: `x == 1`
- B: `x >= 1`
- C: `x <= 6`
- D: `x > 6`

Write answers here:
```
A) 5 results:

print(a == b)                           #True
print(a < 1)                            #False
print(a >= 0)                           #True
print(random.choice([5, 10, 15]) >= 5) #True
print(len(random.sample([1,2,3], 2)) == 3)  #False


B) Two that are always True:
B, C
```

---

## Task 4 — PCAP select-two simulation [Real exam format]

Answer exactly as on the real exam — select two answers per question.

**Q1.** Which of the following expressions always evaluate to True? (Select two)
```python
import random
random.seed(0)
v = random.random()
```
- A: `v >= 1`
- B: `v == random.random()`
- C: `v < 1`
- D: `random.choice([1, 2, 3]) >= 1`

D, C


**Q2.** Which of the following are valid? (Select two)
- A: `'hello'.find('xyz')` returns `-1`
- B: `'hello'.index('xyz')` returns `-1`
- C: `'hello'.rindex('l')` returns `3`
- D: `'hello'.rfind('xyz')` raises `ValueError`

A, D

**Q3.** Which expressions evaluate to True? (Select two)
```python
s = 'PCAP'[:2:]
s = s[-1] + s[::-1] #C + CP
```
- A: `len(s) == 3`
- B: `s[0] == 'A'`
- C: `s[-1] == 'P'`
- D: `s == 'APC'`  ← wait, trace it yourself


A, C

**Q4.** What is true about lambda functions? (Select two)
- A: They are anonymous functions
- B: They cannot return `None`
- C: They can be defined without parameters
- D: They must use the `return` keyword

**Q5.** Which are true about `__bases__` and `__mro__`? (Select two)
```python
class A: pass
class B(A): pass
class C(B): pass
```
- A: `C.__bases__ == (B,)`
- B: `A in C.__bases__`
- C: `object in C.__mro__`
- D: `len(C.__mro__) == 2`

Write answers here:
```
Q1: D, C
Q2: A, D
Q3: A, C
Q4: A, C
Q5: A, C
```

---

## Task 5 — `hasattr` vs `__dict__`: final nail [recurring gap]

One more exposure — same concept, new code.

**A)** Given:
```python
class Engine:
    horsepower = 200
    def start(self): pass

class Car(Engine):
    def __init__(self, brand):
        self.brand = brand
    def drive(self): pass

c = Car('Toyota')
```
Answer True or False:
```python
hasattr(c, 'horsepower')          # ?
hasattr(c, 'start')               # ?
hasattr(Car, 'start')             # ?
'start' in Car.__dict__           # ?
'start' in Engine.__dict__        # ?
'horsepower' in Car.__dict__      # ?
'brand' in Car.__dict__           # ?
'brand' in c.__dict__             # ?
'drive' in Car.__dict__           # ?
```

**B)** One-line rule — complete the sentence:
> `hasattr(X, 'name')` returns True if `'name'` exists anywhere in the mro
> `'name' in X.__dict__` returns True only if `'name'` is defined in a given Class instance

Write answers here:
```
A) 9 results:
print(hasattr(c, 'horsepower'))          #True
print(hasattr(c, 'start'))               #True
print(hasattr(Car, 'start'))            #True
print('start' in Car.__dict__)           #False
print('start' in Engine.__dict__)        #True
print('horsepower' in Car.__dict__)      #False
print('brand' in Car.__dict__)          #False
print('brand' in c.__dict__)           #True
print('drive' in Car.__dict__)          #True


B)

> `hasattr(X, 'name')` returns True if `'name'` exists anywhere in the mro
> `'name' in X.__dict__` returns True only if `'name'` is defined in a given Class instance
```
