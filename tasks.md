# Week 10, Day 2 — PCAP Full Review
**Date:** 2026-03-18 | **Focus:** Exceptions, OOP, scope, generators, functional programming

---

## Task 1 — Exception hierarchy: 5 predict-the-output

**Q1:**
```python
try:
    raise ValueError("v")
except Exception as e:
    print(type(e).__name__)
    print(isinstance(e, BaseException))
    print(isinstance(e, Exception))

ValueError
True
True
```

**Q2:**
```python
try:
    1 / 0
except ArithmeticError:
    print("arithmetic")
except ZeroDivisionError:
    print("zero")

arithmetic
```

**Q3:**
```python
def f():
    try:
        return 1
    except Exception:
        return 2
    finally:
        return 3

print(f())

3
```

**Q4:**
```python
try:
    raise TypeError("t")
except (ValueError, TypeError) as e:
    print("caught:", e)
    raise

print("done")

caught: t
TypeError: t
```

**Q5:**
```python
try:
    try:
        raise ValueError("inner")
    except TypeError:
        print("inner handler")
except ValueError:
    print("outer handler")
finally:
    print("finally")

outer handler
finally
```

---

## Task 2 — OOP: 6 predict-the-output

**Q1:**
```python
class A:
    x = []

a = A()
b = A()
a.x.append(1)
print(b.x)
print(A.x)

[1]
[1]

```

**Q2:**
```python
class A:
    def __init__(self):
        self.__secret = 42

a = A()
print(a.__secret)


AttributeError

```

**Q3:**
```python
class A:
    def __init__(self):
        self.__secret = 42

a = A()
print(a._A__secret)


42
```

**Q4:**
```python
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

animals = [Dog(), Cat(), Animal()]
for a in animals:
    print(a.speak())

woof, meow, ...
```

**Q5:**
```python
class Counter:
    def __init__(self):
        self._count = 0

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        if value < 0:
            raise ValueError("negative")
        self._count = value

c = Counter()
c.count = 5
print(c.count)
c.count = -1

5
ValueError: negative


```

**Q6:**
```python
class A:
    def __str__(self):
        return "str_A"
    def __repr__(self):
        return "repr_A"

a = A()
print(a)
print(repr(a))
print([a])
print(f"{a}")

str_A
repr_A
[str_A]
{repr_A}
```

---

## Task 3 — Scope (LEGB + closures): 5 questions

**Q1:**
```python
x = "global"

def outer():
    x = "outer"
    def inner():
        x = "inner"
        return x
    return inner()

print(outer())
print(x)

inner
global

```

**Q2:**
```python
x = 0

def f():
    global x
    x += 10

f()
f()
print(x)

20

```

**Q3:**
```python
def make_multiplier(n):
    return lambda x: x * n

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5)) #10
print(triple(5)) #15
print(double(triple(2))) #12

10
15
12
```

**Q4:**
```python
fns = [lambda x: x + n for n in range(4)]
print([f(0) for f in fns])

[3, 3, 3, 3]

```

**Q5:**
```python
fns = [lambda x, n=n: x + n for n in range(4)]
print([f(0) for f in fns])

[0, 1, 2, 3]
```

---

## Task 4 — Generators and iterators: 5 questions

**Q1:**
```python
def gen():
    for i in range(3):
        yield i * 2

g = gen()
print(next(g)) #0
print(next(g)) #2
print(list(g)) #[4]

0
2
[4]
```

**Q2:**
```python
def gen():
    yield 1
    yield 2

g = gen()
print(list(g))
print(list(g))

[1, 2]
[]
```

**Q3:**
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print(sum(countdown(5)))


15
```

**Q4:**
```python
def gen():
    yield from [1, 2, 3]
    yield from range(3)

print(list(gen()))

[1, 2, 3, 0, 1, 2]


```

**Q5:**
```python
class Counter:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        self.current += 1
        return self.current

print(list(Counter(3)))

[1, 2, 3]
```

---

## Task 5 — Functional programming: 5 questions

**Q1:**
```python
nums = [1, 2, 3, 4, 5, 6]
result = list(filter(lambda x: x % 2 == 0, nums))
print(result)

[2, 4, 6]
```

**Q2:**
```python
nums = [1, 2, 3, 4]
result = list(map(lambda x: x ** 2, nums))
print(result)

[1, 4, 9, 16]
```

**Q3:**
```python
from functools import reduce

result = reduce(lambda acc, x: acc + x, [1, 2, 3, 4], 10)
print(result)

20
```

**Q4:**
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper

@decorator
def greet(name):
    print(f"hello {name}")

greet("Alice")

before
hello Alice
after

#this is a bit unintuitive, as we return the result after 'after', but it actually prints as we calculate the result here, as there's a print in our function

```

**Q5:**
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper

@decorator
@decorator
def greet(name):
    print(f"hello {name}")

greet("Bob")


before
before
hello Bob
after
after

```

---

## Task 6 — Strings and slicing: 5 questions

**Q1:**
```python
s = "Python"
print(s[1:4])
print(s[-3:])
print(s[::2])
print(s[::-1])


```

**Q2:**
```python
s = "hello world"
print(s.upper())
print(s.capitalize())
print(s.title())
```

**Q3:**
```python
s = "  hello  "
print(len(s))
print(len(s.strip()))
```

**Q4:**
```python
s = "a,b,,c,d"
parts = s.split(",")
print(len(parts))
print(parts)
```

**Q5:**
```python
print("{}{}{}".format(1, 2, 3))
print("{2}{0}{1}".format("a", "b", "c"))
print(f"{'hello':>10}")
```


s = "Python"
print(s[1:4]) #yth
print(s[-3:]) #hon
print(s[::2]) #Pto
print(s[::-1]) #nohtyP


s = "hello world"
print(s.upper()) #HELLO WORLD
print(s.capitalize()) #Hello world
print(s.title()) #Hello World

s = "  hello  "
print(len(s)) #9
print(len(s.strip())) #5



s = "a,b,,c,d"
parts = s.split(",") #
print(len(parts)) #5
print(parts) #['a', 'b', '', 'c', 'd']



print("{}{}{}".format(1, 2, 3)) #123
print("{2}{0}{1}".format("a", "b", "c")) #cab
print(f"{'hello':>10}") #i don't know - this synthax is weird and we didn't use it I think. Neither it looks relevant


---

## Task 7 — Mixed PCAP simulation: 8 questions (10 minutes)

**Q1:** What is the output?
```python
x = [1, 2, 3]
print(x[10:20])
```
- A) `IndexError`
- B) `[]`
- C) `[3]`
- D) `None`

B

**Q2:** What is the output?
```python
def f(*args, **kwargs):
    print(len(args), len(kwargs))

f(1, 2, 3, a=4, b=5)
```
- A) `5 0`
- B) `3 2`
- C) `2 3`
- D) `TypeError`

B

**Q3:** What is the output?
```python
class A:
    pass

a = A()
a.x = 10
print(a.__dict__)
```
- A) `{}`
- B) `{'x': 10}`
- C) `AttributeError`
- D) `{'A': {'x': 10}}`

B

**Q4:** What is the output?
```python
xs = [1, 2, 3]
ys = xs[:]
ys.append(4)
print(xs)
print(ys)
```
- A) `[1,2,3,4]`, `[1,2,3,4]`
- B) `[1,2,3]`, `[1,2,3,4]`
- C) `[1,2,3]`, `[1,2,3]`
- D) `TypeError`

B

**Q5:** What is the output?
```python
print(bool(0), bool(""), bool([]), bool(None))
print(bool(1), bool("0"), bool([0]))
```
- A) `False False False False` / `True True True`
- B) `False False False False` / `True False True`
- C) `True True True True` / `True True True`
- D) `False False False False` / `False True True`

B

**Q6:** What is the output?
```python
d = {"a": 1, "b": 2}
for k, v in d.items():
    d[k] = v * 2

print(d)

```
- A) `RuntimeError: dictionary changed size during iteration`
- B) `{"a": 2, "b": 4}`
- C) `{"a": 1, "b": 2}`
- D) `{"a": 2, "b": 2}`

B

**Q7:** What is the output?
```python
def f(a, b=2, *args, **kwargs):
    print(a, b, args, kwargs)

f(1, 3, 4, 5, x=6)
```
- A) `1 2 (3, 4, 5) {'x': 6}`
- B) `1 3 (4, 5) {'x': 6}`
- C) `1 3 (3, 4, 5) {'x': 6}`
- D) `TypeError`

B

**Q8:** What is the output?
```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
shallow[0].append(99)

print(original)
print(shallow)
```
- A) `[[1,2],[3,4]]`, `[[1,2,99],[3,4]]`
- B) `[[1,2,99],[3,4]]`, `[[1,2,99],[3,4]]`
- C) `[[1,2],[3,4]]`, `[[1,2],[3,4]]`
- D) `TypeError`

B

---

## Answers

### Task 1
Q1:
Q2:
Q3:
Q4:
Q5:

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

### Task 4
Q1:
Q2:
Q3:
Q4:
Q5:

### Task 5
Q1:
Q2:
Q3:
Q4:
Q5:

### Task 6
Q1:
Q2:
Q3:
Q4:
Q5:

### Task 7
Q1:
Q2:
Q3:
Q4:
Q5:
Q6:
Q7:
Q8:
