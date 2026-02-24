# Week 8, Day 2 — Exam Crunch
**Date:** 2026-02-24 | **Focus:** OOP deep drills + PCAP simulation

---

## Task 1 — Predict the Output (no code, 8 questions)

**Q1:**
```python
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        super().__init__()
        self.y = 2

b = B()
print(b.x, b.y)

1, 2
```

**Q2:**
```python
class A:
    def __init__(self):
        self.x = 1

class B(A):
    def __init__(self):
        self.y = 2

b = B()
print(b.x, b.y)


AttributeError
```

**Q3:**
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2
    return wrapper

@decorator
@decorator
def get_five():
    return 5

print(get_five())

20
```

**Q4:**
```python
class C:
    _x = 0

    @classmethod
    def increment(cls):
        cls._x += 1

    @staticmethod
    def description():
        return "I am C"

C.increment()
C.increment()
print(C._x, C.description())


2, I am C
```

**Q5:**
```python
try:
    x = int("abc")
except (ValueError, TypeError) as e:
    print(type(e).__name__)


ValueError

```

**Q6:**
```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node(1)
b = Node(2)
a.next = b
b.next = a

print(a.next.next.val)

None

```

**Q7:**
```python
xs = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, map(lambda x: x + 1, xs)))
print(result)

[2, 4, 6]


```

**Q8:**
```python
def f(x=[]):
    x.append(1)
    return len(x)

print(f(), f(), f())

1 2 3
```

---

## Task 2 — OOP Drill: Inheritance & super()

The following class chain has **two bugs**. Find them, explain why each is a bug, and write the corrected version in `practice.py`.

```python
class Animal:
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound

    def speak(self) -> str:
        return f"{self.name} says {self.sound}"


class Dog(Animal):
    def __init__(self, name: str, breed: str):
        self.breed = breed

    def speak(self) -> str:
        return super().speak() + f" (breed: {self.breed})"


class GuideDog(Dog):
    def __init__(self, name: str, breed: str, owner: str):
        super().__init__(name, breed)
        self.owner = owner

    def speak(self) -> str:
        return super().speak() + f" [guide dog for {self.owner}]"


gd = GuideDog("Rex", "Labrador", "Alice")
print(gd.speak())
```

Paste corrected code + bug explanations in the answer box.

# #Erratic class chain - bug identification
# class Animal:
#     def __init__(self, name: str, sound: str):
#         self.name = name
#         self.sound = sound

#     def speak(self) -> str:
#         return f"{self.name} says {self.sound}"
# #everything ok up to this point

# class Dog(Animal):
#     def __init__(self, name: str, breed: str): #sound missing
#         #ISSUE 1 - WE'RE NOT fetching anything from our parent class - this will be an issue
#         self.breed = breed

#     def speak(self) -> str:
#         return super().speak() + f" (breed: {self.breed})"


# class GuideDog(Dog):
#     def __init__(self, name: str, breed: str, owner: str): #sound missing as well...
#         super().__init__(name, breed)
#         self.owner = owner

#     def speak(self) -> str:
#         return super().speak() + f" [guide dog for {self.owner}]"


# gd = GuideDog("Rex", "Labrador", "Alice")
# print(gd.speak())



#FIX
class Animal:
    def __init__(self, name: str, sound: str):
        self.name = name
        self.sound = sound

    def speak(self) -> str:
        return f"{self.name} says {self.sound}"
#everything ok up to this point

class Dog(Animal):
    def __init__(self, name, sound, breed: str):
        super().__init__(name, sound)
        self.breed = breed

    def speak(self) -> str:
        return super().speak() + f" (breed: {self.breed})"
    
#fixed this now


class GuideDog(Dog):
    def __init__(self, name: str, sound: str, breed: str, owner: str):
        super().__init__(name, breed, sound)
        self.owner = owner

    def speak(self) -> str:
        return super().speak() + f" [guide dog for {self.owner}]"


dog = Dog('Johny', 'Woof', 'Labrador')
print(dog.speak())

gd = GuideDog("Rex", 'Woof', "Labrador", "Alice")
print(gd.speak())

It's fixed and it works properly now


---

## Task 3 — PCAP Simulation (12 questions, 15 minutes)

Time yourself. No code runner.

**Q1:** What is the output?
```python
x = 10
def f():
    global x
    x += 5
f()
print(x)
```
- A) `10`
- B) `15`
- C) `UnboundLocalError`
- D) `NameError`

B

**Q2:** Which of the following is true about `@abstractmethod`?
- A) A class with abstract methods can be instantiated if at least one method is implemented
- B) A subclass that doesn't implement all abstract methods raises `TypeError` on instantiation
- C) `@abstractmethod` can only be used on `__init__`
- D) Abstract methods must have an empty body

B

**Q3:** What is the output?
```python
a = [1, 2, 3]
b = a[:]
a[0] = 99
print(b[0])
```
- A) `99`
- B) `1`
- C) `None`
- D) `TypeError`

B #it creates a new object essentially

**Q4:** What is the output?
```python
class A:
    def method(self):
        return "A"

class B(A):
    pass

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

print(D().method())
```
- A) `"A"`
- B) `"B"`
- C) `"C"`
- D) `AttributeError`

C



**Q5:** What is the output?
```python
s = {1, 2, 3}
s.add(2)
s.add(4)
print(len(s))
```
- A) `3`
- B) `4`
- C) `5`
- D) `TypeError`

B

**Q6:** What is the output?
```python
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g), next(g))
print(list(g))


A
```
- A) `1 2` then `[3]`
- B) `1 2` then `[1, 2, 3]`
- C) `1 2` then `[]`
- D) `StopIteration`

**Q7:** What is the output?
```python
class Meta(type):
    pass

class MyClass(metaclass=Meta):
    pass

print(type(MyClass))
```
- A) `<class 'type'>`
- B) `<class '__main__.Meta'>`
- C) `<class '__main__.MyClass'>`
- D) `TypeError`

B - but it's my speculation - WE DIDN'T HAVE THAT!

**Q8:** What is the output?
```python
x = "hello world"
print(x.split()[1].upper()[:3])
```
- A) `"WOR"`
- B) `"hel"`
- C) `"WO"`
- D) `"wor"`

A

**Q9:** What is the output?
```python
def f(a, b, /, c, d):
    return a + b + c + d

print(f(1, 2, c=3, d=4))
```
- A) `10`
- B) `TypeError`
- C) `SyntaxError`
- D) `NameError`

A

**Q10:** Which is true about `__eq__` and `__hash__`?
- A) Defining `__eq__` automatically defines `__hash__`
- B) Defining `__eq__` without `__hash__` sets `__hash__` to `None`, making the object unhashable
- C) `__hash__` is never needed if `__eq__` is defined
- D) Both are optional and independent

B

**Q11:** What is the output?
```python
d = {"a": 1, "b": 2, "c": 3}
print({v: k for k, v in d.items()})
```
- A) `{"a": 1, "b": 2, "c": 3}`
- B) `{1: "a", 2: "b", 3: "c"}`
- C) `TypeError`
- D) `{("a", 1), ("b", 2), ("c", 3)}`

B

**Q12:** What is the output?
```python
class A:
    def __init__(self):
        self.__x = 10

    def get_x(self):
        return self.__x

a = A()
print(a.get_x(), a._A__x)
```
- A) `10 AttributeError`
- B) `AttributeError AttributeError`
- C) `10 10`
- D) `10 None`

C

---

## Task 4 — Write: Custom Iterator

Write a class `Countdown` in `practice.py` that:
- Takes a `start: int` in `__init__`
- Implements the full iterator protocol (`__iter__`, `__next__`)
- Yields values from `start` down to `1` inclusive
- After reaching `1`, raises `StopIteration`
- Can be reset by calling `.reset()` which restores the counter to `start`

Demonstrate it works by:
1. Using it in a `for` loop — prints `3 2 1`
2. Calling `reset()` and doing `list(countdown)` — confirms reusability

Paste final code in the answer box.

class Countdown:
    '''A practice iterator class which takes the following args:
    
    start: int
    
    It yields values from start down to 1 inclusive, and then raises StopIteration,
    but the value can be reset by calling .reset() method.
    '''
    
    def __init__(self, start: int):
        self.start = start
        self.current = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < 1:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value
    
    def reset(self):
        self.current = self.start
        print('Restored the current value to the starting value.')
    
    

for x in Countdown(5):
    print(x)

print(list(Countdown(4)))
print(list(Countdown(7)))

Done it, but IT DOESN'T FEEL like a strongly rooted concept - I had to look things up to make sure it works.



---

## Task 5 — Refactor: Exception Handling

The following code runs but has **three professional-quality issues** (not syntax errors — style and logic problems). Identify them all, then write a corrected version.

```python
def load_price(filepath):
    try:
        f = open(filepath)
        data = f.read()
        f.close()
        return float(data.strip())
    except:
        return None
```

def load_price(filepath):
    try:
        with open(filepath, 'r') as r:
            data = r.read()
            return float(data.strip())
    except FileNotFoundError:
        print('File not found!')
    except Exception as e:
        print(f'Unexpected exception: {str(e)}')

---

## Task 6 — PCAP Trap: Spot the Difference

Both snippets look similar. Predict what each prints and explain why they differ.

**Snippet A:**
```python
class Account:
    balance = 0

a1 = Account()
a2 = Account()
a1.balance += 100
print(a1.balance, a2.balance)


100, 0

balance here is a class attribute, shared by all instances of the class as a new instance is created, but if we instantiate the balance and then change it in a given class instance, IT WILL BE in that class instance only. Anyway, this is rather weird approach in this case.

```

**Snippet B:**
```python
class Account:
    balance = 0

a1 = Account()
a2 = Account()
Account.balance += 100
print(a1.balance, a2.balance)

100 100

Here we're changing the whole class attribute, not the instance attribute only.
```

---

## Task 7 — PROJECT: Docstrings on Position and Trade

Open [algo_backtest/engine/position.py](algo_backtest/engine/position.py) and [algo_backtest/engine/trade.py](algo_backtest/engine/trade.py).

For each file, add:
1. A module-level docstring (one sentence is enough)
2. A proper class docstring with `Attributes:` section
3. Docstrings on any public methods that currently lack them

You already know what format you prefer — use it consistently. This is the final documentation pass for the core engine classes.

Edit the files directly. Paste a note here confirming it's done and mention anything interesting you found.


I think this is a completely wrong choice of tasks, as both files HAVE these docstrings, and in the format you asked for with Attributes section.

This is a misguided task that I don't need to do, and I DON'T WANT YOU TO TAKE AWAY POINTS FROM ME FOR TODAY.

As for the future progress and GOALS of my backtesting repo, I need the following things:
- I want to calculate the R profit, based on a risk unit rather than P/L in $, as it's more important for me, and we might always calculate the equity curve based on the risk amount per risk unit, starting balance etc. Beside that, it would be nice to calculate sharpe ratio and profit factor.


- I'd like to be able to test several strategies at once, which means that each position should also contain information about given strategy that it implements if applicable - what is more, I might be testing the same strategy that uses the same basic constraints or base factors, but with a twist as slightly different SL/TP settings etc., and it still should be distinguished, so have a different strategy_id. This modularity/objectification is very important.
- In the end, we should have a nice and clear raporting of all strategies performance (in R values) together and separately. This is the total endgoal.

---

```
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

### Task 2
Bugs:
Corrected code:

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
Q11:
Q12:

### Task 4
Code:

### Task 5
Issues:
Corrected code:

### Task 6
Snippet A output + explanation:
Snippet B output + explanation:

### Task 7
Notes:
```
