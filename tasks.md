# Week 9, Day 1 — Exam B Gap Closure
**Date:** 2026-03-02 | **Focus:** Drilling the 5 Exam B gaps. Short session — 4 tasks only.

---

## Task 1 — Warm-up: 5 predictions (no code)

Each one is a direct re-drill of an Exam B miss.

**Q1:** What is the output?
```python
class Base:
    items = []

class Child(Base):
    pass

Base.items.append("a")
Child.items.append("b")
print(Base.items, Child.items)


['a', 'b'], ['a', 'b']

```

**Q2:** What is the output?
```python
class C:
    @property
    def value(self):
        return self.value

c = C()
print(c.value)


Recursion ERROR

```

**Q3:** What is the output?
```python
xs = [1, 2, 3]
ys = [4, 5]
zs = [6, 7, 8, 9]
print(list(zip(xs, ys, zs)))

[(1, 4, 6), (2, 5, 7)]
```

**Q4:** What is the output?
```python
def f(*args):
    print(type(args), args)

a = [1, 2]
b = [3, 4]
f(*a, *b)

tuple, (1, 2, 3, 4)

```

**Q5:** What is the output?
```python
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.warning("watch out")

DEBUG: watch out
```

---

## Task 2 — PCAP Trap: Name mangling outside the class

Predict the output of each snippet and explain why.

**Snippet A:**
```python
class C:
    def __init__(self):
        self.__x = 10

    def get(self):
        return self.__x

c = C()
c.__x = 99
print(c.get()) 10
print(c.__x) 99
print(c._C__x) 10



```

**Snippet B:**
```python
class C:
    def __init__(self):
        self.__x = 10

c = C()
print(hasattr(c, '__x')) #False
print(hasattr(c, '_C__x')) #True


```

---

## Task 3 — PCAP Simulation: 6 questions (8 minutes)

**Q1:** What is the output?
```python
class A:
    data = [1, 2, 3]

class B(A):
    pass

B.data = B.data + [4]
print(A.data, B.data)
```
- A) `[1, 2, 3] [1, 2, 3, 4]`
- B) `[1, 2, 3, 4] [1, 2, 3, 4]`
- C) `[1, 2, 3] [1, 2, 3]`
- D) `AttributeError`

A

**Q2:** What is the output?
```python
xs = [1, 2, 3]
ys = [4, 5]
print(list(zip(xs, ys)), len(list(zip(xs, ys))))
```
- A) `[(1, 4), (2, 5), (3, None)] 3`
- B) `[(1, 4), (2, 5)] 2`
- C) `TypeError`
- D) `[(1, 4), (2, 5)] 3`

B

**Q3:** What is the output?
```python
import logging
fmt = '%(levelname)s - %(message)s'
logging.basicConfig(format=fmt, level=logging.INFO)
logging.info("started")
logging.debug("verbose")
```
- A) `INFO - started` and `DEBUG - verbose`
- B) `INFO - started` only
- C) `INFO:root:started` only
- D) Nothing printed

A

**Q4:** What is the output?
```python
def f(*args, **kwargs):
    return args, kwargs

xs = [1, 2]
d = {'a': 3}
print(f(*xs, **d))
```
- A) `([1, 2], {'a': 3})`
- B) `((1, 2), {'a': 3})`
- C) `(1, 2, {'a': 3}), {}`
- D) `TypeError`

A

**Q5:** Which raises `RecursionError`?
```python
# A
class C:
    @property
    def x(self):
        return self._x

# B
class C:
    @property
    def x(self):
        return self.x

# C
class C:
    @property
    def x(self):
        return 42
    @x.setter
    def x(self, v):
        self.x = v
```
- A) A only
- B) B only
- C) C only
- D) B and C

D

**Q6:** What is the output?
```python
class A:
    def method(self): return "A"

class B(A):
    def method(self): return "B"

class C(A):
    def method(self): return "C"

class D(B, C): pass
class E(C, B): pass

print(D().method(), E().method())
```
- A) `B C`
- B) `C B`
- C) `A A`
- D) `B B`

A

---

## Task 4 — Self-check

One sentence each — no code:

1. Why does `Child.items.append("x")` also appear in `Base.items`? 
2. Why does `@property` returning `self.value` cause `RecursionError` and not `AttributeError`?
3. What is the difference between `f(*a, *b)` and `f(a, b)` — what does `f` receive in each case?


1. Because it applies to a class attribute, not instance attribute, and it's a parent class.
2. Because it causes infinite loop of recursion, self referencing each other and finally exceeding the allowed number of recursions.
3. The second case assumes that we receive exactly two arguments, while the first one gives us freedom of assignment.

---

## Answers

### Task 1
Q1:
Q2:
Q3:
Q4:
Q5:

### Task 2
Snippet A:
Snippet B:

### Task 3
Q1:
Q2:
Q3:
Q4:
Q5:
Q6:

### Task 4
1.
2.
3.
