# Week 2, Day 5 Tasks - Week Review & Integration (Friday)

**Focus:** Week 2 review, PCAP drills, consolidation of OOP concepts

**Target Difficulty:** 5-6/10 (no brick walls!)

**Instructions:**
- Work in `practice.py` for experimentation
- Paste your FINAL solutions/answers below each task

---

## Task 1: Quick Fire Review (Week 2 Concepts)

Answer these questions without looking at notes:

**Q1:** In `class D(B, C)`, which parent's method is used if both B and C have `method()`?

**Q2:** What's the difference between `@classmethod` and `@staticmethod` first parameter?

**Q3:** What pattern should you use instead of `def func(items=[])` to avoid the mutable default trap?

**Q4:** When should you use composition (HAS-A) instead of inheritance (IS-A)?

**Q5:** What does `super().__init__()` do? Does Python call it automatically?

**Q6:** What does `__all__` in `__init__.py` control?

**Your answers:**
```
Q1: B

Q2: For @class method it's cls, for staticmethod the first parameter will depend on a given method (not determined).

Q3: items = None, and then we can set items = 0 if items == None.

Q4: When a subclass is stricly an extension of the base class - e.g. it's a specific trading strategy and the parent class is a general strategy.

Q5: It imports/fetches the init parameters from the parent class.

Q6: It controls all of the classes that can be interacted with/imported from a given package/module (folder). It lists all available classes that we can later import and use in other folders/files.

```

---

## Task 2: PCAP Drill - Inheritance Output Prediction

Predict the output WITHOUT running the code:

```python
class Vehicle:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

    def describe(self):
        return f"{self.brand} with {self.wheels} wheels"

class Motorcycle(Vehicle):
    wheels = 2

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self.doors = doors

    def describe(self):
        return f"{super().describe()}, {self.doors} doors"

# What prints?
m = Motorcycle("Honda")
c = Car("Toyota", 4)

print(m.describe())
print(c.describe())
print(m.wheels, c.wheels)
```

**Your prediction:**
```
# Output (3 lines):

Honda with 2 wheels
Toyota with 4 wheels, 4 doors
2 4

# Explanation:
What's there to explain - it's all very simple - we pass relevant parameters and shared class attribute takes precedence, unless it's modified on purpose (as in motorcycle).


```

---

## Task 3: PCAP Drill - Exception Handling

Predict the output WITHOUT running:

```python
def risky_operation(x):
    try:
        if x == 0:
            raise ValueError("Zero not allowed")
        result = 10 / x
    except ValueError as e:
        print(f"Caught: {e}")
        return -1
    except ZeroDivisionError:
        print("Division by zero!")
        return -2
    else:
        print(f"Success: {result}")
        return result
    finally:
        print("Cleanup done")

print(risky_operation(0))
print("---")
print(risky_operation(2))
```

**Your prediction:**
```
# Output:
#1 - Caught: Zero not allowed. Cleanup done. -1
#2 - Success: 5.0 Cleanup done. 5.0




# Explanation (order of execution):
I was uncertain whether we will see the raise ValueError's message or excepts' ValueError's message - I definitely need to practice nad remember this.

As for the general rule -> try -> (OPTIONALLY) else (if we don't encounter an error) -> finally (always)

```

---

## Task 4: PCAP Drill - @classmethod and @staticmethod

Predict the output WITHOUT running:

```python
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def validate(value):
        return value > 0

# What happens?
print(Counter.get_count())
c1 = Counter()
c2 = Counter()
print(Counter.get_count())
print(c1.get_count())
print(Counter.validate(-5))
print(c2.validate(10))
```

**Your prediction:**
```
# Output (5 lines):


# What happens?
print(Counter.get_count()) #0
c1 = Counter() #2
c2 = Counter() #2
print(Counter.get_count()) #2
print(c1.get_count()) #5
print(Counter.validate(-5))#False
print(c2.validate(10)) #True


# Explanation:

When we create actual class objects, the count value is increased with init.
As classmethod doesn't include actually creating any object, it doesn't use the init - it doesn't increase the count value, but it's obviously able to fetch it, and since it's a shared class attribute, we get the last value.

When creating a new class object (as c1, c2), we increase that count value by 1, as it's a shared class attribute.

```

---

## Task 5: Code Integration - Position with Risk Sizing

Yesterday you implemented `calculate_position_size`. Now let's use it in practice.

**Task:** Write a simple script that:
1. Creates a Position using the position sizing calculation
2. Uses account balance = $10,000, risk = 2%, entry = $100, stop_loss = $95
3. Prints the calculated position size
4. Creates a Position object with that size
5. Prints the Position using `__str__`

**Paste your code below:**
```python
# Your integration script



from algo_backtest.engine.position import Position

position_size = Position.calculate_position_size(10000, 2, 100, 95)
print(position_size)
position = Position('DAX', 'Buy', 25100, position_size, 24900, 25300)
print(str(position))

#LOG:

# $ python practice.py
# 40.0
# BUY 40.0 @ 25100 [SL = 24900, TP = 25300]
# (.venv) 

```

---

## Task 6: PCAP Multiple Choice - Week 2 Review

**Question 1:** What is Method Resolution Order (MRO)?

A) The order methods are defined in a class
B) The order Python searches for methods in inheritance hierarchy
C) The order constructors are called
D) The order attributes are initialized

**Your answer:**
B

---

**Question 2:** Which decorator creates a method that can access class attributes but not instance attributes?

A) @property
B) @staticmethod
C) @classmethod
D) @abstractmethod

**Your answer:**
C


---

**Question 3:** What happens if a child class doesn't call `super().__init__()`?

A) Python raises TypeError
B) Parent's `__init__` runs automatically
C) Parent's attributes are not initialized
D) The child class cannot be instantiated

**Your answer:**
C

---

**Question 4:** What is the output of `[x*2 if x > 5 else x for x in [3, 6, 9]]`?

A) [3, 12, 18]
B) [6, 12, 18]
C) [3, 6, 9]
D) [6, 6, 9]

**Your answer:**
A

---

**Question 5:** In `class C(A, B)`, what is the MRO?

A) C → B → A → object
B) C → A → B → object
C) A → B → C → object
D) B → A → C → object

**Your answer:**

D
In other words, as this can is a bit ambiguous and can be interpreted in different ways:
The C is dominant and final, but it inherits everything from A, which inherits from B.
But in the final execution we will overwrite everything from B with A, and we will overwrite everything from A with C - that's what I mean in my answer.

---

## Task 7: Code Review - Find the Bugs

This code has 4 bugs. Find and fix them:

```python
class Strategy:
    active_count = 0

    def __init__(self, name):
        self.name = name
        active_count += 1  # Bug 1

    @classmethod
    def get_active(self):  # Bug 2
        return cls.active_count

    @staticmethod
    def validate_name(name):
        return len(name) > 0 and self.name.isalpha()  # Bug 3

    def describe():  # Bug 4
        return f"Strategy: {self.name}"
```

**Bugs found:**
```
#1. We will not increase active_count as it's in local scope
#2 Class method CANNOT use self, it uses cls instead
#3 static_method DOES NOT have access to class attributes, it's a self standing function only with its own attributes
#4 Lack of self in describe method

```

**Corrected code:**
```python

class Strategy:
    '''Mock docstring'''
    active_count = 0

    def __init__(self, name: str):
        self.name = name
        Strategy.active_count += 1

    @classmethod
    def get_active(cls) -> int:  
        '''Returns count of active strategies'''
        return cls.active_count

    @staticmethod
    def validate_name(name) -> bool:
        '''A standalone method/function that allows to validate any name'''
        return len(name) > 0 and name.isalpha()

    def describe(self) -> str:  
        '''Returns the name of a given strategy'''
        return f"Strategy: {self.name}"




```

---

## Task 8: Week 2 Self-Assessment

Rate your understanding of each topic (1-5, where 5 = fully confident):

```
Inheritance basics (class Child(Parent)):        5/5
super().__init__() usage:                        5/5
Method overriding:                               5/5
MRO (Method Resolution Order):                   5/5
@classmethod:                                    4/5
@staticmethod:                                   4/5
Composition vs Inheritance (HAS-A vs IS-A):      4/5
Mutable default arguments trap:                  5/5
List comprehensions (filter-if vs ternary-if):   5/5
try/except/else/finally flow:                    5/5

Topics I need more practice on:

classmethod/staticmethod + potential other types of special methods if there are any (and if they're relevant now/relevant to PCAP requirements, as PCAP is the MOST IMPORTANT GOAL)
importing and calling them with different types of arguments/parameters (also including lists, Pandas Dataframes etc.), 
creating them as well,
packaging and using _all_ with init.py,

- I also definitely need to practice / come back to basic data manipulations, defaultdict etc. as we study the current topics, so that I will be able to reinforce the past topics as well.


Topics I feel confident about:
I listed them, feeling confident with most of these topics.


```

---

## Feedback Section

**Time spent:** 60 minutes

**Difficulty (1-10):**
4
**What clicked:**
Almost everything

**What's confusing:**

Class method vs staticmethod perhaps needs a bit more practice

**Questions:**


