# PCAP Mock Exam - Week 2, Exam B

**Time Limit:** 65 minutes (simulates real exam pace)
**Questions:** 30
**Passing Score:** 70% (21/30)

**Instructions:**
- No external resources (notes, internet, IDE)
- Write your answer letter next to each question
- For code output questions, write the exact output

---

## Section 1: Inheritance & OOP (Questions 1-10)

**Question 1:** What is the output?

```python
class Vehicle:
    wheels = 4

class Bike(Vehicle):
    wheels = 2

b = Bike()
print(b.wheels, Vehicle.wheels)
```

A) 2 4
B) 4 4
C) 2 2
D) 4 2

**Your answer:**

---

**Question 2:** What does this code print?

```python
class A:
    def greet(self):
        return "Hello"

class B(A):
    def greet(self):
        return "Hi"

class C(B):
    pass

c = C()
print(c.greet())
```

A) Hello
B) Hi
C) HelloHi
D) Error

**Your answer:**

---

**Question 3:** What is method overriding?

A) Defining a method with the same name in a child class
B) Calling a method multiple times
C) Creating multiple methods with same name but different parameters
D) Deleting a parent method

**Your answer:**

---

**Question 4:** What is the output?

```python
class Parent:
    def __init__(self, x):
        self.x = x

class Child(Parent):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

c = Child(1, 2)
print(c.x, c.y)
```

A) Error
B) 1 2
C) None 2
D) 2 1

**Your answer:**

---

**Question 5:** Which is TRUE about `issubclass()`?

A) Every class is a subclass of itself
B) A class cannot be a subclass of `object`
C) `issubclass()` only works with direct parents
D) `issubclass()` checks instance type

**Your answer:**

---

**Question 6:** What is the output?

```python
class X:
    def method(self): return "X"

class Y:
    def method(self): return "Y"

class Z(Y, X):
    pass

z = Z()
print(z.method())
```

A) X
B) Y
C) XY
D) Error

**Your answer:**

---

**Question 7:** What is the MRO of class Z above?

A) Z → X → Y → object
B) Z → Y → X → object
C) Z → X → object → Y
D) Y → X → Z → object

**Your answer:**

---

**Question 8:** What is the output?

```python
class Counter:
    total = 0

    def __init__(self):
        Counter.total += 1
        self.total = 100

c1 = Counter()
c2 = Counter()
print(c1.total, Counter.total)
```

A) 100 2
B) 2 2
C) 100 100
D) 2 100

**Your answer:**

---

**Question 9:** What is the output?

```python
class A:
    pass

class B(A):
    pass

b = B()
print(isinstance(b, A), isinstance(b, object))
```

A) True True
B) True False
C) False True
D) False False

**Your answer:**

---

**Question 10:** What happens here?

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

s = Shape()
```

A) Creates an empty Shape object
B) TypeError: Can't instantiate abstract class
C) Returns None
D) Creates Shape with area = 0

**Your answer:**

---

## Section 2: Class & Static Methods (Questions 11-15)

**Question 11:** What is the output?

```python
class Calculator:
    value = 10

    @classmethod
    def double(cls):
        return cls.value * 2

    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.double())
print(Calculator.add(3, 4))
```

A) 20, 7
B) Error, 7
C) 20, Error
D) Error, Error

**Your answer:**

---

**Question 12:** Can you call a `@classmethod` on an instance?

A) No, only on the class
B) Yes, it still receives the class as first argument
C) Yes, but it receives the instance as first argument
D) It raises an error

**Your answer:**

---

**Question 13:** What is the output?

```python
class Demo:
    x = 5

    @classmethod
    def change(cls, val):
        cls.x = val

Demo.change(10)
d = Demo()
print(d.x, Demo.x)
```

A) 5 10
B) 10 10
C) 5 5
D) 10 5

**Your answer:**

---

**Question 14:** Which can access `self.attribute`?

A) Regular methods only
B) @classmethod only
C) @staticmethod only
D) Both @classmethod and @staticmethod

**Your answer:**

---

**Question 15:** What is the purpose of `@classmethod` factory methods?

A) To delete instances
B) To create instances in alternative ways
C) To make methods faster
D) To hide class attributes

**Your answer:**

---

## Section 3: Exception Handling (Questions 16-20)

**Question 16:** What is the output?

```python
try:
    print("A")
    raise ValueError()
except ValueError:
    print("B")
else:
    print("C")
finally:
    print("D")
```

A) A B D
B) A B C D
C) A C D
D) B D

**Your answer:**

---

**Question 17:** What is the output?

```python
def test():
    try:
        return "try"
    except:
        return "except"
    finally:
        print("finally")

result = test()
print(result)
```

A) try
B) finally try
C) finally
D) try finally

**Your answer:**

---

**Question 18:** Which is the correct exception hierarchy (most specific to most general)?

A) Exception → ValueError → ArithmeticError
B) ValueError → Exception → BaseException
C) BaseException → Exception → ValueError
D) ValueError → ArithmeticError → Exception

**Your answer:**

---

**Question 19:** What is the output?

```python
try:
    x = int("abc")
except ValueError:
    print("A")
except:
    print("B")
else:
    print("C")
```

A) A
B) B
C) A B
D) C

**Your answer:**

---

**Question 20:** What does `finally` guarantee?

A) The code runs only if no exception
B) The code runs only if exception occurs
C) The code always runs, even with return/exception
D) The code runs only after else

**Your answer:**

---

## Section 4: List Comprehensions & Iterables (Questions 21-25)

**Question 21:** What is the output?

```python
result = [i ** 2 for i in range(4)]
print(result)
```

A) [1, 4, 9, 16]
B) [0, 1, 4, 9]
C) [0, 1, 2, 3]
D) [1, 2, 3, 4]

**Your answer:**

---

**Question 22:** What is the difference between these?

```python
a = [x for x in range(5) if x > 2]
b = [x if x > 2 else 0 for x in range(5)]
```

A) `a` filters, `b` transforms
B) `a` transforms, `b` filters
C) Both filter
D) Both transform

**Your answer:**

---

**Question 23:** What is the output?

```python
def make_list(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

print(make_list(1))
print(make_list(2))
```

A) [1] [1, 2]
B) [1] [2]
C) [1, 2] [1, 2]
D) Error

**Your answer:**

---

**Question 24:** What is the output?

```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in matrix for x in row]
print(flat)
```

A) [[1, 2], [3, 4], [5, 6]]
B) [1, 2, 3, 4, 5, 6]
C) [[1, 3, 5], [2, 4, 6]]
D) Error

**Your answer:**

---

**Question 25:** What is the output?

```python
result = {x: x**2 for x in [1, 2, 3]}
print(result)
```

A) [1, 4, 9]
B) {1: 1, 2: 4, 3: 9}
C) [(1, 1), (2, 4), (3, 9)]
D) Error

**Your answer:**

---

## Section 5: Mixed Topics (Questions 26-30)

**Question 26:** What is composition in OOP?

A) A class inheriting from multiple classes
B) A class containing instances of other classes
C) A class that cannot be instantiated
D) A class with only static methods

**Your answer:**

---

**Question 27:** What is the output?

```python
class Outer:
    class Inner:
        value = 42

print(Outer.Inner.value)
```

A) Error
B) 42
C) None
D) Outer.Inner.value

**Your answer:**

---

**Question 28:** What is `__name__` when a script is run directly?

A) The filename
B) `"__main__"`
C) `"script"`
D) Empty string

**Your answer:**

---

**Question 29:** What is the output?

```python
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super().__init__()
        self.x = 2
        self.y = 3

b = B()
print(hasattr(b, 'x'), hasattr(b, 'y'))
```

A) True True
B) False True
C) True False
D) False False

**Your answer:**

---

**Question 30:** Why is this code problematic?

```python
class Manager(Database):  # Database has connect() and query()
    def get_users(self):
        return self.query("SELECT * FROM users")
```

A) Nothing wrong, it's correct
B) Should use composition instead (Manager HAS-A Database)
C) Missing super().__init__()
D) query() should be a static method

**Your answer:**

---

## Answer Key (Check after completing!)

Write your answers in order:

```
1:    2:    3:    4:    5:
6:    7:    8:    9:    10:
11:   12:   13:   14:   15:
16:   17:   18:   19:   20:
21:   22:   23:   24:   25:
26:   27:   28:   29:   30:
```

**Total Score:** ___/30

---

*Complete this exam without any resources, then check your answers with the mentor.*
