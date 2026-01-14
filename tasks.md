# Week 2, Day 3 Tasks - Composition, Advanced Polymorphism & MRO Practice

**Focus:** Composition vs Inheritance (HAS-A vs IS-A), MRO deep dive, mixins, strategy integration

**Instructions:**
- Work in `practice.py` for experimentation
- Paste your FINAL solutions/answers below each task
- For project tasks, create/modify files in `algo_backtest/` as specified

---

## Task 1: PCAP Warm-up - MRO Practice (CRITICAL!)

Yesterday you predicted "C" but the correct answer was "B". Let's practice MRO to solidify understanding.

**Predict the output WITHOUT running the code:**

```python
class Animal:
    def speak(self):
        return "generic sound"

class Mammal(Animal):
    def speak(self):
        return "mammal sound"

class Bird(Animal):
    def speak(self):
        return "chirp"

class Bat(Mammal, Bird):
    pass

class Platypus(Bird, Mammal):
    pass

bat = Bat()
platypus = Platypus()

print(bat.speak())
print(platypus.speak())
print(Bat.__mro__)
```

**Your prediction:**
```
# Output (3 lines):

print(bat.speak()) # -> 'mammal sound'
print(platypus.speak()) # -> 'chirp'
print(Bat.__mro__) # Mammal -> Bird -> Animal



# Explanation (why does order in class definition matter?):

Because the order is from bottom to the top and also from left to right, so its:
Platypus = Bird -> Mammal -> Animal
Bat = Mammal -> Bird -> Animal

```

---

## Task 2: Composition vs Inheritance - Theory

**Question:** When should you use composition (HAS-A) instead of inheritance (IS-A)?

Read the following scenario and decide which approach is better:

**Scenario A:** You're building a `Car` class. A car needs an engine to function.

**Option 1 - Inheritance:**
```python
class Engine:
    def start(self):
        return "Engine started"

class Car(Engine):  # Car IS-A Engine
    pass
```

**Option 2 - Composition:**
```python
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Car HAS-A Engine

    def start(self):
        return self.engine.start()
```

**Your answer:**
```
Which is better (Option 1 or Option 2)?


That really depends on the context, but here we would rather use option 2. 


Why?

CAR doesn't seem like it needs to be a subclass of Engine at all, it rather needs to use the features of Engine.


Give a real-world example where inheritance would be correct:

If we had a general class - like BaseStrategy, that would settle some variables that will or should be use in every strategy, but then each strategy might be very different and it needs a very specific extension of the BaseStrategy.


```

---

## Task 3: PROJECT - Position with Composition

Currently our `Position` class stores `ticker`, `entry_price`, `quantity`, etc. as primitive types.

**Task:** Refactor `Position` to use **composition** by creating a `PositionMetadata` class that holds non-price data.

**Requirements:**
1. Create a `PositionMetadata` class in `algo_backtest/engine/position_metadata.py`:
   - Attributes: `ticker: str`, `side: str`, `quantity: float`
   - Add `__str__` method: `"AAPL LONG 100 shares"`

2. Modify `Position` class in `algo_backtest/engine/position.py`:
   - Replace individual `ticker`, `side`, `quantity` attributes with `self.metadata: PositionMetadata`
   - Update `__init__` to accept `metadata: PositionMetadata` parameter
   - Update all methods to use `self.metadata.ticker`, `self.metadata.side`, etc.
   - Update `__str__` to use `self.metadata`

**Paste your code below:**
```python
# position_metadata.py



# position.py (modified parts only)



```

---

## Task 4: Mixin Pattern - LoggerMixin

A **mixin** is a small class that provides specific functionality via multiple inheritance. Mixins DON'T stand alone - they're meant to be combined with other classes.

**Task:** Create a `LoggerMixin` that adds logging capability to any class.

**Requirements:**
1. Create `LoggerMixin` class with a `log(message: str)` method that prints: `"[ClassName] message"`
2. Create a `Trade` class that inherits from BOTH `LoggerMixin` AND your base class
3. Demonstrate logging a trade execution

**Paste your code below:**
```python
# Your mixin implementation

# class LoggerMixin:
    
#     def __init__(self):
#         self.class_name = None
    
#     def log(self, message: str):
#         print(f'{self.class_name} message: {message}')
    


# class Trade(LoggerMixin):
    
#     def __init__(self):
#         super().__init__()
#         self.class_name = 'Trade Class'

# x = Trade()
# x.log('Test Xd')

# #LOG:
# $ python practice.py
# Trade Class message: Test Xd

# I didn't follow your reqs exactly, as I didn't want to clutter the code base but I've created a reusable Mixin class with log capabilities, and it works properly
```

---

## Task 5: PCAP Trap - MRO Edge Cases

**Predict which of these will raise an error and why:**

```python
# Case A
class A:
    pass

class B(A):
    pass

class C(A, B):
    pass

# Case B
class X:
    pass

class Y:
    pass

class Z(X, Y):
    pass

# Case C
class P:
    pass

class Q(P):
    pass

class R(Q):
    pass

class S(R, Q):
    pass
```

**Your answer:**
```
Case A (Error? Yes/No): Yes
Reason: B is inherited from A, and thefore A can't be inherited from B, it just doesn't make sense.


Case B (Error? Yes/No): No.
Reason: Everything is fine here, the classes are separate and then we create an inheritance order.


Case C (Error? Yes/No): No
Reason: It's a proper structure of inheritance and the final class that will take precedence is R.


```

---

## Task 6: PROJECT - Strategy Factory with Polymorphism

Create a `StrategyFactory` class that creates strategies based on string identifiers. This demonstrates **polymorphism** (returning different types through same interface) and **factory pattern**.

**Requirements:**
1. Create `algo_backtest/strategies/strategy_factory.py`
2. Implement `StrategyFactory` class with static method `create(strategy_type: str, **kwargs) -> BaseStrategy`
3. Support creating:
   - `"level_cross"` → returns `LevelCrossStrategy(level=kwargs['level'])`
   - `"moving_average"` → returns `MovingAverageStrategy(ma_period=kwargs['ma_period'])`
4. Raise `ValueError` if `strategy_type` is unknown
5. Add type hints and docstrings

**Paste your code below:**
```python
# strategy_factory.py




```

---

## Task 7: Multiple Choice - Advanced OOP

**Question 1:** What is the main advantage of composition over inheritance?

A) Composition is faster
B) Composition allows runtime flexibility (you can change components)
C) Composition uses less memory
D) Composition is required for polymorphism

**Your answer:** B

---

**Question 2:** In `class D(B, C)`, if both B and C define `method()`, which one does D inherit?

A) C's method (rightmost parent)
B) B's method (leftmost parent)
C) Both (D has two methods)
D) Neither (raises AttributeError)

**Your answer:** B

---

**Question 3:** What is a mixin?

A) A class that mixes data types
B) A small class designed to provide specific functionality via multiple inheritance
C) A function that modifies class behavior
D) A decorator for methods

**Your answer:** B

---

## Task 8: Code Review - Composition vs Inheritance Abuse

The following code works but violates good OOP design. Identify issues and rewrite using composition.

```python
class Database:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def connect(self):
        return f"Connected to {self.connection_string}"

    def query(self, sql):
        return f"Executing: {sql}"

class UserManager(Database):  # IS-A relationship
    def __init__(self, connection_string):
        super().__init__(connection_string)

    def get_user(self, user_id):
        return self.query(f"SELECT * FROM users WHERE id={user_id}")

class ProductManager(Database):  # IS-A relationship
    def __init__(self, connection_string):
        super().__init__(connection_string)

    def get_product(self, product_id):
        return self.query(f"SELECT * FROM products WHERE id={product_id}")
```

**Issues identified:**
```
#1. UserManager shouldn't be a subclass of Database - it could use Database method's instead (connect + query), but it's not an extended Database version, but rather it uses 2 methods from the Database.
#2. Same for ProductManager, there's no need to inherit Database class, but rather simply use the query method.
#3. And as for both - for these two subclasses, we could simply write two extra methods to the Database method and it would be much more nice and neat, if it's only about changing the product_id or user_id. It's just weird to invent a new class for that.

```

**Your refactored code (using composition):**
#Option 1 - IMHO very clear and not overengineered
class Database:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def connect(self):
        return f"Connected to {self.connection_string}"

    def query(self, sql):
        return f"Executing: {sql}"

    def get_user(self, user_id):
        return (f"SELECT * FROM users WHERE id={user_id}")
    
    def get_product(self, product_id):
        return (f"SELECT * FROM products WHERE id={product_id}")


#Option 2 - A bit more tricky but with perhaps clearer structure if we're planning to extend the new classes much further

class Database:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def connect(self):
        return f"Connected to {self.connection_string}"

    def query(self, sql):
        return f"Executing: {sql}"

class UserManager():  # IS-A relationship
    def __init__(self, connection_string):
        self.connection = Database(connection_string)

    def get_user(self, user_id):
        return self.connection.query(f"SELECT * FROM users WHERE id={user_id}")

class ProductManager():  # IS-A relationship
    def __init__(self, connection_string):
        self.connection = Database(connection_string)

    def get_product(self, product_id):
        return self.connection.query(f"SELECT * FROM products WHERE id={product_id}")

#Evaluate both solutions and argument which one would be better here, and in general.

```

---

## Task 9: BONUS - Advanced Strategy with Composition

Create a `CompositeStrategy` that combines multiple strategies using composition (NOT inheritance).

**Requirements:**
- Inherits from `BaseStrategy`
- Constructor accepts `List[BaseStrategy]`
- `generate_signal()` calls all sub-strategies and returns:
  - `"BUY"` if majority say BUY
  - `"SELL"` if majority say SELL
  - `"HOLD"` otherwise
- Use `isinstance()` to validate all strategies are `BaseStrategy` instances

**Paste your code below:**
```python
# composite_strategy.py


What the hell, how would I be able to do that considering that each strategy has its own parameters like level, period etc? That's a really weird task and I didn't know what did you expect here.

```

---

## Feedback Section

**Time spent:** 60 minutes

**Difficulty (1-10):** 8 - some really weird tasks + unclear bonus task with difficult and not understandable requirements, unrealistic

**What clicked:**
-

**What's confusing:**
A lot of things - mixins, calling a list of strategies (bonus tasks), and HAS-A vs IS-A (when to use which option) - we need to practice this definitely. Yet the main objective is PCEP, do not forget


**Questions:**


