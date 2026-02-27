# Week 8, Day 5 — Final PCAP Crunch + Week 8 Review
**Date:** 2026-02-27 | **Focus:** Closing remaining gaps before exams + Project: BacktestEngine polish

---

## Task 1 — PCAP Warm-up: Sort & isinstance traps (no code, 4 questions)

These are the exact two gaps from Day 4 — drill them until they are automatic.

**Q1:** What does `sorted([3, 1, 4, 1, 5], key=lambda x: -x)` return?

[5, 4, 3, 1, 1] - the values get sorted by their '-x' value (ascending), but shown in their standard form, which makes it work as descending sorting in the end.

**Q2:** What is the output?
```python
class Animal:
    pass

class Dog(Animal):
    pass

class Poodle(Dog):
    pass

p = Poodle()
print(isinstance(p, Animal), isinstance(p, Dog), isinstance(p, Poodle))

True, True, True
```

**Q3:** What is the output?
```python
xs = [10, 20, 30, 40, 50]
result = sorted(xs, key=lambda x: x % 3)
print(result)
```
Think carefully — what are the keys, and what values are returned?

1 2 0 1 2 -> the keys
Returned values: [30 10 40 20 50]


**Q4:** What is the output?
```python
class A: pass
class B(A): pass
class C(B): pass

obj = C()
print(issubclass(C, A), issubclass(A, C), isinstance(obj, A))

True, False, True
```

---

## Task 2 — PCAP Trap Gauntlet: 6 tricky snippets (no code)

Predict output + one-sentence explanation for each.

**Snippet A:**
```python
def f(x=[]):
    x.append(1)
    return x

print(f())
print(f())
print(f([]))
print(f())

[1]
[1, 1]
[1]
[1, 1, 1]

```

**Snippet B:**
```python
x = 5
def outer():
    x = 10
    def inner():
        print(x)
    return inner

outer()()

10
```

**Snippet C:**
```python
try:
    raise ValueError("bad")
except ValueError as e:
    result = str(e)
finally:
    result = "cleaned"

print(result)

cleaned
```

**Snippet D:**
```python
class Meta(type):
    def __new__(mcs, name, bases, namespace):
        namespace['greeting'] = 'hello'
        return super().__new__(mcs, name, bases, namespace)

class Foo(metaclass=Meta):
    pass

print(Foo.greeting)


hello
```

**Snippet E:**
```python
gen = (x * 2 for x in range(5))
print(3 in gen)
print(list(gen))


False
[]

```

**Snippet F:**
```python
a = (1,)
b = (1,)
print(a == b, a is b)

True, False
```

---

## Task 3 — PCAP Simulation (10 questions, 12 minutes)

Time yourself. No code runner.

**Q1:** What is the output?
```python
x = [1, 2, 3]
y = x[:]
y.append(4)
print(x, y)
```
- A) `[1, 2, 3] [1, 2, 3, 4]`
- B) `[1, 2, 3, 4] [1, 2, 3, 4]`
- C) `[1, 2, 3] [1, 2, 3]`
- D) `TypeError`

A

**Q2:** What is the output?
```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))
print(next(g))
g2 = iter(g)
print(g is g2)


```
- A) `1`, `2`, `True`
- B) `1`, `2`, `False`
- C) `1`, `1`, `True`
- D) `TypeError`

A

**Q3:** Which of the following raises `AttributeError`?
```python
# A
class C:
    @property
    def x(self): return 42
c = C(); c.x = 10

# B
class C:
    def __init__(self): self._x = 0
    @property
    def x(self): return self._x
    @x.setter
    def x(self, v): self._x = v
c = C(); c.x = 10

# C
class C:
    pass
c = C(); c.x = 10
```
- A) A only
- B) B only
- C) C only
- D) None of them

A

**Q4:** What is the output?
```python
from functools import reduce
xs = [2, 3, 4]
print(reduce(lambda acc, x: acc + x, xs, 10))
```
- A) `9`
- B) `19`
- C) `24`
- D) `TypeError`

B



**Q5:** What is the output?
```python
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner

f = outer()
g = outer()
print(f(), f(), g())
```
- A) `1 2 1`
- B) `1 2 3`
- C) `1 1 1`
- D) `NameError`

A

**Q6:** What is the output?
```python
class A:
    x = 10

class B(A):
    pass

B.x = 99
print(A.x, B.x)
```
- A) `99 99`
- B) `10 99`
- C) `10 10`
- D) `AttributeError`


B

**Q7:** What is the output?
```python
xs = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, xs)
print(list(evens))
print(list(evens))
```
- A) `[2, 4]` then `[2, 4]`
- B) `[2, 4]` then `[]`
- C) `[1, 3, 5]` then `[]`
- D) `TypeError`

B

**Q8:** What is the output?
```python
def f(*args, **kwargs):
    print(type(args), type(kwargs))

f(1, 2, a=3)
```
- A) `<class 'list'> <class 'dict'>`
- B) `<class 'tuple'> <class 'dict'>`
- C) `<class 'tuple'> <class 'list'>`
- D) `TypeError`

B



**Q9:** What is the output?
```python
class C:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x

a = C(1)
b = C(1)
c = a
print(a == b, a is b, a is c)
```
- A) `True False True`
- B) `True True True`
- C) `False False True`
- D) `TypeError`

A

**Q10:** What is the output?
```python
import sys
xs = list(range(1000))
gen = (x for x in range(1000))
print(sys.getsizeof(xs) > sys.getsizeof(gen))
```
- A) `True`
- B) `False`
- C) `TypeError`
- D) Depends on Python version


A

---

## Task 4 — PROJECT: `__repr__` on BacktestEngine

Open [algo_backtest/engine/backtest_engine.py](algo_backtest/engine/backtest_engine.py).

The engine has `__str__` but no `__repr__`. When you type `engine` in a REPL or put the engine inside a list, Python falls back to the default `<BacktestEngine object at 0x...>`.

Add a `__repr__` that returns the same string as `__str__`. One rule: `__repr__` must call `self.__str__()` — do not duplicate the format string.

Verify: `repr(engine)` and `str(engine)` produce the same output.

Added and verified:

repr: BacktestEngine: 0 open | 4 closed | PnL: $260.0
str: BacktestEngine: 0 open | 4 closed | PnL: $260.0

---

## Task 5 — PCAP Final Gap: Decorators + Exception flow (5 questions, no code)

**Q1:** What is the output?
```python
def deco(f):
    def wrapper(*args, **kwargs):
        print("before")
        result = f(*args, **kwargs)
        print("after")
        return result
    return wrapper

@deco
def greet(name):
    print(f"hello {name}")

greet("Ada")


before
Hello Ada
after

```

**Q2:** What is the output?
```python
def deco_a(f):
    def wrapper():
        print("A in")
        f()
        print("A out")
    return wrapper

def deco_b(f):
    def wrapper():
        print("B in")
        f()
        print("B out")
    return wrapper

@deco_a
@deco_b
def hello():
    print("hello")

hello()


A in
B in
hello
B out
A out


```

**Q3:** What is the output?
```python
try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print(type(e).__name__)
else:
    print("no error")
finally:
    print("done")


ValueError
done
```

**Q4:** What is the output?
```python
def f():
    try:
        return 1
    finally:
        return 2

print(f())


2
```

**Q5:** What is the output?
```python
class CustomError(Exception):
    pass

try:
    raise CustomError("oops")
except Exception as e:
    print(isinstance(e, CustomError), isinstance(e, Exception))


True, True
```

---

## Task 6 — Week 8 Self-Assessment

No code. Answer honestly.

Rate yourself 1-5 on each topic (1 = shaky, 5 = exam-ready):

1. OOP: properties, encapsulation, `__dunder__` methods: depends, 3.5/5
2. Inheritance, MRO, super() - 4/5
3. Closures, nonlocal, late binding - 5/5
4. Decorators (simple + parameterised + stacking) 4/5
5. Generators, iterators, `iter(gen) is gen` 4/5
6. Logging (two-gate filtering, exception(), __name__) 4/5
7. Exceptions (hierarchy, try/except/else/finally flow) - 5
8. Built-ins: sorted/filter/map/reduce, zip, enumerate - 4/5

Which single topic are you least confident about going into the weekend exams?

Still some complex inheritance / generators and someimtes exceptions.
Also, it would be useful to review more basic concepts like lambdas etc.


---

## Answers

### Task 1
Q1:
Q2:
Q3:
Q4:

### Task 2
Snippet A:
Snippet B:
Snippet C:
Snippet D:
Snippet E:
Snippet F:

### Task 3
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

### Task 4
Done / notes:

### Task 5
Q1:
Q2:
Q3:
Q4:
Q5:

### Task 6
Ratings:
Weakest topic:
