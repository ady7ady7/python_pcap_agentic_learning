# Week 6, Day 5 - Friday
## Topic: Exam Gap Closure — Iterator Identity, `in` on Generators, @wraps Stacking, Closure Names

**Date:** 2026-02-13

**Target Difficulty:** 7/10

**Focus:** Day 4 Tasks 7-8 exposed 6 specific PCAP gaps. Today targets each one surgically. You know the concepts — the issue is applying them under exam pressure.

**Remember:** Work in `practice.py`, paste FINAL answers here for review.

---

#Start 14:05

## Task 1: PCAP Warm-up — The `in` Operator on Generators

**Context:** Day 4 Task 8 Q3 — you answered C (False, False). The correct answer was A (True, True). The `in` operator on a generator **consumes elements sequentially** until it finds a match or exhausts.

**Q1:** Predict the output — trace element-by-element:
```python
gen = (x for x in range(5))
print(2 in gen)
print(3 in gen)
print(1 in gen)

True True False
```

**Hint:** `in` on a generator works like calling `next()` repeatedly until it finds the value or hits StopIteration. Once consumed, those elements are gone.

**Q2:** Predict the output:
```python
gen = (x for x in range(5))
print(0 in gen)   # Line A
print(0 in gen)   # Line B
print(4 in gen)   # Line C

True False False
```

**Q3:** What about lists — same behavior?
```python
nums = [0, 1, 2, 3, 4]
print(2 in nums)
print(2 in nums)

True True
```

**Your answers:**
```
Q1:


Q2:


Q3:


```

---

## Task 2: Identity Check — `iter(obj) is obj`

**Context:** Day 4 Task 8 Q2 — you answered D (`True`, `[1,2,3]`, `[1,2,3]`). The correct answer was A (`False`, `[1,2,3]`, `[1,2,3]`).

**Key rule:** When `__iter__` returns `self` → `iter(obj) is obj` is **True** (it's an iterator).
When `__iter__` returns something else (like `iter(self.items)`) → `iter(obj) is obj` is **False** (it's an iterable, not an iterator).

**Q1:** Predict `True` or `False`:
```python
class Alpha:
    def __init__(self):
        self.data = [1, 2, 3]
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= len(self.data): raise StopIteration
        self.i += 1
        return self.data[self.i - 1]

a = Alpha()
print(iter(a) is a)  # ?

True
```

**Q2:** Predict `True` or `False`:
```python
class Beta:
    def __init__(self):
        self.data = [1, 2, 3]
    def __iter__(self):
        return iter(self.data)

b = Beta()
print(iter(b) is b)  # ?

False
```

**Q3:** Predict `True` or `False`:
```python
nums = [1, 2, 3]
it = iter(nums)
print(iter(it) is it)  # ?

True
```

**Q4:** Now the full Day 4 question — predict ALL THREE lines:
```python
class Data:
    def __init__(self):
        self.items = [1, 2, 3]
    def __iter__(self):
        return iter(self.items)

d = Data()
it = iter(d)
print(it is d)      # Line 1
print(list(d))      # Line 2
print(list(it))     # Line 3

False
[1, 2, 3]
[1, 2, 3]

```

**Your answers:**
```
Q1:
Q2:
Q3:
Q4 Line 1:
Q4 Line 2:
Q4 Line 3:
```

---

## Task 3: Resettable Iterators — `__iter__` Reset Pattern

**Context:** Day 4 Task 7 Q1 — you answered C (`[0,1,2]` then `[]`). The correct answer was A (`[1,2,3]` then `[1,2,3]`). Two mistakes in one:
1. Missed that `__next__` increments BEFORE returning (`current += 1; return current` yields 1, not 0)
2. Missed that `__iter__` resets `self.current = 0`, making it reusable

**Q1:** Trace this carefully. What does `__next__` return on the FIRST call?
```python
class Counter:
    def __init__(self, max_val):
        self.max_val = max_val

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current >= self.max_val:
            raise StopIteration
        self.current += 1
        return self.current
```
- When `list()` is called, Python calls `__iter__` first → `self.current = 0`
- Then `__next__`: `current` is 0, check `0 >= 3`? No. Increment to 1. Return 1.
- Then `__next__`: `current` is 1, check `1 >= 3`? No. Increment to 2. Return 2.
- Continue tracing...

What is `list(Counter(3))`?

**Q2:** What happens on the SECOND `list()` call? Think about what `__iter__` does.
```python
c = Counter(3)
print(list(c))  # ? [1, 2, 3]
print(list(c))  # ? [1, 2, 3]
```

**Q3:** Now compare — what if `__iter__` did NOT reset?
```python
class CounterNoReset:
    def __init__(self, max_val):
        self.max_val = max_val
        self.current = 0

    def __iter__(self):
        return self  # NO reset!

    def __next__(self):
        if self.current >= self.max_val:
            raise StopIteration
        self.current += 1
        return self.current

c = CounterNoReset(3)
print(list(c))  # ? [1, 2, 3]
print(list(c))  # ? []
```

**Your answers:**
```
Q1: list(Counter(3)) = ?

Q2: First list() = ?  Second list() = ?

Q3: First list() = ?  Second list() = ?
```

---

## Task 4: `__name__` — Functions vs Variables vs @wraps

**Context:** Day 4 Task 8 Q4 — you answered C (`make_multiplier`). Correct was B (`multiplier`). Also Task 8 Q1 — you answered C (`Called wrapper`, `Called foo`). Correct was B (`Called foo` twice).

**Rule:** `func.__name__` is the name from the `def` statement, NOT the variable it's assigned to. `@wraps` copies `__name__` from the original function to the wrapper.

**Q1:** What is printed?
```python
def outer():
    def inner():
        pass
    return inner

f = outer()
print(f.__name__)
```
- A) `outer`
- B) `inner`
- C) `f`
- D) Error

B

**Q2:** What is printed?
```python
def make_greeter(greeting):
    def greeter(name):
        return f"{greeting}, {name}!"
    return greeter

hello = make_greeter("Hello")
print(hello.__name__)

greeter
```

**Q3:** Now with `@wraps` — what is printed?
```python
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args):
        return func(*args)
    return wrapper

@decorator
def add(a, b):
    return a + b

print(add.__name__)

add
```

**Q4:** Stacked decorators with `@wraps` — the Day 4 question revisited:
```python
from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args):
        print(f"Called {func.__name__}")
        return func(*args)
    return wrapper

@trace
@trace
def foo(x):
    return x * 2

foo(5)


Called foo, called foo
```

Trace the decoration process step by step:
1. Inner `@trace` wraps `foo` → creates `wrapper` but `@wraps(func)` copies `foo.__name__` onto it → this wrapper's `__name__` = ?
2. Outer `@trace` wraps that wrapper → `func` is now the inner wrapper → `func.__name__` = ? (thanks to @wraps)
3. So what gets printed?

**Your answers:**
```
Q1:
Q2:
Q3:
Q4 Step-by-step:
  Inner wrapper __name__ = ?
  Outer func.__name__ = ?
  Output = ?
```

---

## Task 5: Independent Generator Instances

**Context:** Day 4 Task 7 Q3 — you answered C (`1, 2, 1`). Correct was A (`1, 1, 2`). Each call to a generator FUNCTION creates a completely independent generator OBJECT.

**Q1:** Predict the output:
```python
def count():
    yield 10
    yield 20
    yield 30

a = count()
b = count()
print(next(a))
print(next(b))
print(next(a))


10 10 20
```

**Q2:** Now compare with `iter()` on the same generator:
```python
def count():
    yield 10
    yield 20
    yield 30

g = count()
x = iter(g)
y = iter(g)
print(x is y)     # ?
print(next(x))    # ?
print(next(y))    # ?

False
10
10
```

**Q3:** And with a list:
```python
nums = [10, 20, 30]
x = iter(nums)
y = iter(nums)
print(x is y)     # ?
print(next(x))    # ?
print(next(y))    # ?

False
10
10
```

**Quick rule recap:**
- Calling `gen_func()` twice → two **independent** generators
- Calling `iter(generator)` twice → **same** object (generators return self)
- Calling `iter(list)` twice → two **independent** iterators

**Your answers:**
```
Q1:

Q2:

Q3:

```

---

## Task 6: PCAP Simulation — Exam Pressure Round (6 Questions, 8 Minutes)

**Instructions:** Time yourself. 8 minutes max. No running code. Trust your tracing.

**Q1:** What is the output?
```python
class Seq:
    def __init__(self, n):
        self.n = n
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        self.i += 1
        return self.i * 10

s = Seq(3)
print(list(s))
print(list(s))
```
- A) `[10, 20, 30]` then `[10, 20, 30]`
- B) `[10, 20, 30]` then `[]`
- C) `[0, 10, 20]` then `[0, 10, 20]`
- D) `[0, 10, 20]` then `[]`

A


**Q2:** What is the output?
```python
gen = (x * 2 for x in range(4))
print(4 in gen)
print(6 in gen)
```
- A) `True` `True`
- B) `True` `False`
- C) `False` `True`
- D) `False` `False`

A

**Q3:** What is the output?
```python
def make_adder(x):
    def adder(y):
        return x + y
    return adder

add5 = make_adder(5)
print(add5(3))
print(add5.__name__)
```
- A) `8` `add5`
- B) `8` `adder`
- C) `8` `make_adder`
- D) Error

B

**Q4:** What is the output?
```python
def gen():
    yield 'a'
    yield 'b'
    yield 'c'

g1 = gen()
g2 = gen()
print(next(g1))
print(next(g1))
print(next(g2))
```
- A) `a` `b` `c`
- B) `a` `b` `a`
- C) `a` `a` `a`
- D) Error

B

**Q5:** What is the output?
```python
class Box:
    def __init__(self, items):
        self.items = items
    def __iter__(self):
        return iter(self.items)

b = Box([10, 20, 30])
it = iter(b)
print(it is b)
next(it)
print(list(b))
print(list(it))
```
- A) `False` `[10, 20, 30]` `[20, 30]`
- B) `False` `[10, 20, 30]` `[10, 20, 30]`
- C) `True` `[10, 20, 30]` `[20, 30]`
- D) `True` `[20, 30]` `[20, 30]`

A

**Q6:** What is the output?
```python
from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args):
        print(f"Running {func.__name__}")
        return func(*args)
    return wrapper

@log
@log
def double(x):
    return x * 2

result = double(5)
print(result)
```
- A) `Running double` `Running double` `10`
- B) `Running wrapper` `Running double` `10`
- C) `Running double` `10`
- D) `Running double` `Running double` `20`

A

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

## Task 7: Week 6 Cumulative — Concept Map

**Fill in the blanks** (no code, just understanding):

1. An **iterator** has both `next` and `iter` methods.

2. An **iterable** has `next` but NOT necessarily `iter`.

3. When `__iter__` returns `self`, the object is a `one-shot` (one-shot/reusable?).

4. When `__iter__` uses `yield`, each call creates `an iterator`, making the object `reusable` (one-shot/reusable?).

5. `iter(generator) is generator` evaluates to `True` because generators are `one-shot`.

6. `iter(list) is list` evaluates to `False` because lists are `independent` not `dependent`.

7. The `in` operator on a generator `yields` elements until it finds a match. Those consumed elements are `lost for later checks`.

8. `func.__name__` reflects the name from the `def` statement, not the `outer function/wrapper or whatever` it's assigned to.

9. `@wraps(func)` copies `function name` (and other metadata) from `func` to the wrapper.

10. Calling a generator function 3 times creates `3` independent generator objects.

**Your answers:**
```
1:
2:
3:
4:
5:
6:
7:
8:
9:
10:
```

---

**Key Focus Areas for Today:**
1. `in` on generators — sequential consumption (Task 1)
2. `iter(obj) is obj` — identity tells you iterator vs iterable (Task 2)
3. Resettable iterators — `__iter__` reset pattern (Task 3)
4. `__name__` and `@wraps` stacking (Task 4)
5. Independent generator instances (Task 5)
6. Timed PCAP simulation (Task 6)
7. Concept consolidation (Task 7)

**Day 4 gaps targeted:**
- Task 7 Q1 wrong (resettable iterator + increment-before-return) → Tasks 3, 6 Q1
- Task 7 Q3 wrong (independent generators) → Task 5, 6 Q4
- Task 8 Q1 wrong (@wraps stacking) → Task 4 Q4, 6 Q6
- Task 8 Q2 wrong (iter identity) → Task 2, 6 Q5
- Task 8 Q3 wrong (`in` on generators) → Task 1, 6 Q2
- Task 8 Q4 wrong (closure `__name__`) → Task 4 Q1-Q2, 6 Q3
