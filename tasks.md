# Week 2, Day 1 Tasks - Inheritance Fundamentals

**Focus:** Basic inheritance, `super()`, method overriding, `isinstance()`/`issubclass()`

**Instructions:**
- Work in `practice.py` for experimentation
- Paste your FINAL solutions/answers below each task
- For project tasks, create/modify files in `algo_backtest/` as specified

---

## Task 1: PCAP Warm-up - Predict the Output

Predict the output of the following code WITHOUT running it first. Then explain WHY.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

d = Dog("Buddy")
print(d.name)
print(d.speak())
```

**Your prediction:**
```
# Output:
'Buddy'
'Woof'


# Explanation:
As for the name, we simply use the parent class architecture, so 'Buddy' is the name assigned to the Dog class instance, based on parent's init.

As for 'woof' instead of 'Some sound' - simply the code from the child overwrites the code from the parent.

```

---

## Task 2: Basic Inheritance - BankAccount Hierarchy

Create a **child class** `SavingsAccount` that inherits from the `BankAccount` class you created in Week 1.

Requirements:
- Inherit from `BankAccount`
- Add a new attribute `interest_rate` (float) in `__init__`
- Use `super().__init__()` to initialize parent attributes
- Add a method `add_interest()` that adds interest to the balance (balance * interest_rate)
- Add a method `__str__()` that returns: `"SavingsAccount(balance=$X, rate=Y%)"`

Test your implementation:
```python
savings = SavingsAccount(owner="Alice", balance=1000.0, interest_rate=0.05)
print(savings)  # SavingsAccount(balance=$1000.00, rate=5.0%)
savings.add_interest()
print(savings.get_balance())  # 1050.0
```

**Your solution:**
```python
# Paste your SavingsAccount class here


    
    
    
class SavingsAccount(BankAccount):
        
    '''A child class of BankAccount with added interest_rate
    and add_interest method that allows for interest compounding'''
    
    def __init__(self, owner: str, balance: float, interest_rate: float):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
        self.balance = balance
    
    def __str__(self):
        return f'SavingsAccount(balance = ${super().get_balance()}, rate = {self.interest_rate}%)'
        
    def add_interest(self):
        '''Compounds the interest based on set interest_rate'''
        self.balance += self.interest_rate * self.balance
        return self.balance
        

```

---

## Task 3: Method Overriding - Strategy Pattern

Create a simple trading strategy hierarchy:

1. **Parent class `Strategy`**:
   - `__init__(self, name: str)` - store strategy name
   - `generate_signal(self, price: float) -> str` - returns `"HOLD"` (default implementation)

2. **Child class `LevelCrossStrategy(Strategy)`**:
   - `__init__(self, level: float)` - store level and call parent with name="Level Cross"
   - Override `generate_signal(self, price: float)`:
     - Returns `"BUY"` if `price > self.level`
     - Returns `"SELL"` if `price < self.level`
     - Returns `"HOLD"` otherwise

Test:
```python
strategy = LevelCrossStrategy(100.0)
print(strategy.generate_signal(105))  # "BUY"
print(strategy.generate_signal(95))   # "SELL"
print(strategy.generate_signal(100))  # "HOLD"
```

**Your solution:**
```python
# Paste your Strategy and LevelCrossStrategy classes here

class Strategy:
    '''A strategy class used to generate trades based on set signals + child classes with specific strategies'''
    def __init__(self, name: str):
        self.name = name
        
    def generate_signal(self, price: float) -> str:
        return 'HOLD'
    
class LevelCrossStrategy(Strategy):
    def __init__(self, level: float):
        super().__init__('Level Cross')
        self.level = level
        
    def generate_signal(self, price: float) -> str:
        
        if price > self.level:
            return 'BUY'
        elif price < self.level:
            return 'SELL'
        else:
            return 'HOLD'



```

---

## Task 4: PCAP Trap Hunt - Find the Bug

The following code has a BUG. Identify the bug, explain why it causes an error, and provide the FIX.

```python
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        self.doors = doors

car = Car("Toyota", 2023, 4)
print(car.brand)  # What happens here?
```

**Your answer:**
```
Bug:
AttributeError: 'Car' object has no attribute 'brand'

Why it fails:
Brand and year attributes in child class should be plugged from the parent class with super(). By the way, are these attributes or parameters? What is the difference between attribute and parameter?

Fix:
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors
        

car = Car("Toyota", 2023, 4)
print(car.brand)

```

---

## Task 5: isinstance() and issubclass() Practice

Given this class hierarchy:

```python
class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

dog = Dog()
```

**Without running the code**, predict the output of each:

```python
print(isinstance(dog, Dog))           # A
print(isinstance(dog, Mammal))        # B
print(isinstance(dog, Animal))        # C
print(isinstance(dog, object))        # D (TRICKY!)

print(issubclass(Dog, Mammal))        # E
print(issubclass(Dog, Animal))        # F
print(issubclass(Dog, Dog))           # G (TRICKY!)
print(issubclass(Animal, Dog))        # H
```

**Your answers:**
```
A: True
B: True
C: True
D: True
E: True
F: False
G: True
H: False

# Explanation for D and G:

D -> dog is certainly an object, an instance of a class, but a separate object nevertheless
G -> Dog is a class and I believe it's also a subclass of it's own class

```

---

## Task 6: PROJECT - Create BaseStrategy ABC

Create an **Abstract Base Class** for the AlgoBacktest project.

**File:** `algo_backtest/strategies/base_strategy.py` (create new file)

Requirements:
1. Import `ABC` and `abstractmethod` from `abc`
2. Create `BaseStrategy` class that inherits from `ABC`
3. `__init__(self, name: str)` - store strategy name
4. Abstract method `generate_signal(self, price: float) -> str` - no implementation
5. Concrete method `get_name(self) -> str` - returns `self.name`
6. Add type hints to ALL methods
7. Add docstrings (Google style)

**File:** `algo_backtest/strategies/__init__.py` (create if doesn't exist)
```python
from .base_strategy import BaseStrategy

__all__ = ['BaseStrategy']
```

**Your solution:**
```python
# Paste your base_strategy.py content here



'''Abstract Method Class - base strategy'''

from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    '''A class with abstract method used to generate trading signal'''
    def __init__(self, name: str):
        self.name = name
        
    @abstractmethod
    def generate_signal(self, price: float) -> str:
        pass
    
    def get_name(self) -> str:
        '''inherited method to fetch a given strategy name'''
        return self.name

```

---

## Task 7: PCAP Multiple Choice

### Question 1
What does `super().__init__()` do?

A) Creates a new parent object
B) Calls the parent class's `__init__` method
C) Overrides the parent class
D) Deletes the parent class

**Your answer:** B

---

### Question 2
What is the output?

```python
class A:
    def method(self):
        return "A"

class B(A):
    pass

b = B()
print(b.method())
```

A) `"A"`
B) `"B"`
C) `AttributeError`
D) `None`

**Your answer:** A

---

### Question 3
Which is TRUE about abstract methods?

A) They must have an implementation in the parent class
B) Child classes are required to implement them
C) They can only be used in built-in classes
D) They are deprecated in Python 3

**Your answer:** B

---

## Task 8: Code Review - Fix the Strategy Implementation

Review this code and identify ALL issues (aim for 5-7 issues):

```python
class strategy:
    def init(self, name):
        name = name

    def signal(self, price):
        return HOLD

class MovingAverageStrategy(strategy):
    def init(self, ma_period):
        self.ma_period = ma_period

    def signal(self, price):
        result = super().signal(price)
        if price > 100:
            return "buy"
        return result

strat = MovingAverageStrategy(20)
print(strat.name)
```

**Your findings:**
```
Issues found:
# 1. Uncapitalized class name
# 2. Lack of floor symbols __ next to init
# 3. name in init has local scope instead of being self.name
# 4. HOLD in signal in parent class will trigger a TypeError, as it's not defined in anyway, and it's not a string either
# 5. lack of super() to get the parent class parameters in init
# 6. with current logic in signal in both classes, we only get to have a 'buy' or 'hold' signal (from the parent class), and no sell at all. Also this whole logic is really weird - we're calling the signal logic from the parent class, but there's no signal logic there, this logic is incomplete etc.
# 7. the class is called without a name
# 8. Lack of type hints andd or docs

Corrected code:
```python

class Strategy:
    '''a base strategy for creating strategies'''
    def __init__(self, name: str):
        self.name = name

    def signal(self):
        pass

class MovingAverageStrategy(Strategy):
    '''a child-class of strategy class with its separate signal generating logic'''
    def __init__(self, name: str, ma_period: float):
        super().__init__(name)
        self.ma_period = ma_period

    '''Signal class used to generate signals for the moving average strategy (mock, as you can see :))'''
    def signal(self, price: float):
        if price > 100:
            return 'Buy'
        elif price < 100:
            return 'Hold'
        
strat = MovingAverageStrategy('Strategy1', 20)
print(strat.name)

```
```

---

## Feedback Section

**Difficulty (1-10):** 5

**Time spent:** 66 minutes

**What clicked:**
Generally everything I think, but it all needs refinement and regular practice


**What's still confusing:**


**Questions for mentor:**


---

**When done, save this file and notify your mentor for assessment.**
