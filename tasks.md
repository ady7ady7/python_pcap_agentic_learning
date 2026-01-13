# Week 2, Day 2 Tasks - Polymorphism & Multiple Strategies

**Focus:** Polymorphism, implementing multiple concrete strategies, isinstance() patterns, composition vs inheritance

**Instructions:**
- Work in `practice.py` for experimentation
- Paste your FINAL solutions/answers below each task
- For project tasks, create/modify files in `algo_backtest/` as specified

---

## Task 1: PCAP Warm-up - Polymorphism Prediction

Predict the output WITHOUT running the code:

```python
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r ** 2

shapes = [Rectangle(5, 3), Circle(2), Rectangle(4, 4)]
total_area = sum(s.area() for s in shapes)
print(total_area)
```

**Your prediction:**
```
# Output:
`43.42



# Explanation (what is polymorphism and how does it work here?):
Each shape here uses the Shape class as the parent class, but their area calculations are different and yet they're calculated properly.

```

---

## Task 2: PROJECT - Implement LevelCrossStrategy

Create a concrete strategy that inherits from `BaseStrategy`.

**File:** `algo_backtest/strategies/level_cross_strategy.py`

**Requirements:**
1. Import `BaseStrategy` from `.base_strategy`
2. Create `LevelCrossStrategy` class that inherits from `BaseStrategy`
3. `__init__(self, level: float)`:
   - Call `super().__init__("Level Cross Strategy")`
   - Store `self.level = level`
4. Implement `generate_signal(self, price: float) -> str`:
   - Return `"BUY"` if `price > self.level`
   - Return `"SELL"` if `price < self.level`
   - Return `"HOLD"` if `price == self.level`
5. Add a method `get_level(self) -> float` that returns `self.level`
6. Type hints on ALL methods
7. Docstrings (Google style)

**Update:** `algo_backtest/strategies/__init__.py`
```python
from .base_strategy import BaseStrategy
from .level_cross_strategy import LevelCrossStrategy

__all__ = ['BaseStrategy', 'LevelCrossStrategy']
```

**Your solution:**
```python
# Paste your level_cross_strategy.py content here

from .base_strategy import BaseStrategy

class LevelCrossStrategy(BaseStrategy):
    '''
    A strategy based on crossing certain levels
    '''
    
    def __init__(self, level: float):
        '''Initializing the class with defined level'''
        super().__init__('Level Cross Strategy')
        self.level = level
        
    
    def generate_signal(self, price: float) -> str:
        '''
        Method used to generate signal based on a price you pass - this is a mock method mainly used to practice.
        
        It's an instance of a method that inherits abstract method from BaseStrategy (so it's mandatory).
        Signals for real strategies most likely will be more robust.
        '''
        if price > self.level:
            return 'BUY'
        elif price < self.level:
            return 'SELL'
        elif price == self.level:
            return 'HOLD'
    
    
    def get_level(self) -> float:
        '''Method used to return the set level'''
        return self.level


I also want you to explain the __init__.py file that we extended, what does it mean, why do we use it and what does this mean exactly?

__all__ = ['BaseStrategy', 'LevelCrossStrategy']

Is it an industry standard for Mid/Senior devs to do that? Why and what do we achieve by this?


```

---

## Task 3: PROJECT - Implement MovingAverageStrategy

Create another concrete strategy with different logic.

**File:** `algo_backtest/strategies/ma_strategy.py`

**Requirements:**
1. Import `BaseStrategy` and `List` type hint
2. Create `MovingAverageStrategy` class
3. `__init__(self, period: int)`:
   - Call `super().__init__(f"MA({period})")`
   - Store `self.period = period`
   - Initialize `self.price_history: List[float] = []`
4. Add method `add_price(self, price: float) -> None`:
   - Append price to `price_history`
   - Keep only last `period` prices (hint: slice or pop)
5. Implement `generate_signal(self, price: float) -> str`:
   - Add current price to history first
   - If not enough data (len < period), return `"HOLD"`
   - Calculate MA: `sum(self.price_history) / len(self.price_history)`
   - Return `"BUY"` if `price > ma`, `"SELL"` if `price < ma`, else `"HOLD"`
6. Type hints and docstrings

**Update:** `algo_backtest/strategies/__init__.py`
```python
from .base_strategy import BaseStrategy
from .level_cross_strategy import LevelCrossStrategy
from .ma_strategy import MovingAverageStrategy

__all__ = ['BaseStrategy', 'LevelCrossStrategy', 'MovingAverageStrategy']
```

**Your solution:**
```python
# Paste your ma_strategy.py content here



from .base_strategy import BaseStrategy
from typing import List

class MovingAverageStrategy(BaseStrategy):
    
    def __init__(self, ma_period: int):
        '''Initialization of the class, inheriting the base init from the BaseStrategy and extending it'''
        super().__init__(f'MovingAverage Strategy - ma {ma_period}')
        self.ma_period = ma_period
        self.price_history: List[float] = []
    
    def add_price(self, price: float):
        '''Method used to add a price to the self.price_history list'''
        self.price_history.append(price)
        if len(self.price_history) > self.ma_period:
            self.price_history.remove(self.price_history[0])
            
    def generate_signal(self, price: float) -> str:
        '''Method used to check whether the list has enough entries to be able to calculate the MA properly'''
        if len(self.price_history) < self.ma_period:
            print(f'Not enough data entries to properly count ma {self.ma_period}. Currently we only have {len(self.price_history)} entries.')
            return 'HOLD'
        
        else:
            ma_value = sum(self.price_history) / self.ma_period
            if price > ma_value:
                return 'BUY'
            else:
                return 'SELL'        



```

---

## Task 4: Polymorphism in Action - Strategy Testing

Write a script that demonstrates polymorphism by using different strategies interchangeably.

**File:** Create `test_strategies.py` in the project root (not inside algo_backtest)

**Requirements:**
```python
"""Test polymorphism with multiple strategies."""

from algo_backtest.strategies import LevelCrossStrategy, MovingAverageStrategy

def test_strategy(strategy, prices: list[float]) -> None:
    """Test a strategy with a list of prices.

    Args:
        strategy: Any strategy that has generate_signal method
        prices: List of prices to test
    """
    print(f"\nTesting: {strategy.get_name()}")
    for price in prices:
        signal = strategy.generate_signal(price)
        print(f"  Price {price}: {signal}")

# Test with different strategies
prices = [95.0, 100.0, 105.0, 102.0, 98.0]

level_strat = LevelCrossStrategy(level=100.0)
test_strategy(level_strat, prices)

ma_strat = MovingAverageStrategy(period=3)
test_strategy(ma_strat, prices)
```

Run the script and paste the output below.

**Your output:**
```
# Paste the actual output from running test_strategies.py here


from algo_backtest.strategies import MovingAverageStrategy, LevelCrossStrategy

'''Test script used to check if our strategies work properly'''

def test_strategy(strategy, prices: list[float]) -> None:
    """Test a strategy with a list of prices.

    Args:
        strategy: Any strategy that has generate_signal method
        prices: List of prices to test
    """
    print(f"\nTesting: {strategy.get_name()}")
    for price in prices:
        signal = strategy.generate_signal(price)
        print(f"  Price {price}: {signal}")


if __name__ == '__main__':
    strat1 = MovingAverageStrategy(5)
    strat2 = LevelCrossStrategy(100.5)
    
    strat1.add_price(430)
    strat1.add_price(230)
    strat1.add_price(450)
    strat1.add_price(470)
    strat1.add_price(490)
    strat1.add_price(530)
    test_strategy(strat1, [430, 450, 520, 550, 570, 460, 430, 320])
    test_strategy(strat2, [120, 105, 90, 20])


Testing: MovingAverage Strategy - ma 5
  Price 430: SELL
  Price 450: BUY
  Price 520: BUY
  Price 550: BUY
  Price 570: BUY
  Price 460: BUY
  Price 430: SELL
  Price 320: SELL

Testing: Level Cross Strategy
  Price 120: BUY
  Price 105: BUY
  Price 90: SELL
  Price 20: SELL

I need to make it a bit more robust and add prices first before we could test the MA strategy.


```

---

## Task 5: isinstance() Patterns - Type Checking

Complete the following function that works differently based on strategy type:

```python
from typing import Union
from algo_backtest.strategies import BaseStrategy, LevelCrossStrategy, MovingAverageStrategy

def analyze_strategy(strategy: BaseStrategy) -> str:
    """Analyze a strategy and return description based on its type.

    Args:
        strategy: Any strategy instance

    Returns:
        Description string
    """
    # TODO: Implement this logic:
    # 1. All strategies should print their name
    # 2. If it's a LevelCrossStrategy, also print the level
    # 3. If it's a MovingAverageStrategy, also print the period
    # 4. Use isinstance() to check types

    pass  # Replace with your implementation

# Test cases
strat1 = LevelCrossStrategy(100.0)
strat2 = MovingAverageStrategy(5)

print(analyze_strategy(strat1))
# Expected: "Level Cross Strategy with level=100.0"

print(analyze_strategy(strat2))
# Expected: "MA(5) with period=5"
```

**Your solution:**
```python
# Paste your complete analyze_strategy function here



from algo_backtest.strategies import BaseStrategy, LevelCrossStrategy, MovingAverageStrategy
def analyze_strategy(strategy: BaseStrategy) -> str:
    """Analyze a strategy and return description based on its type.

    Args:
        strategy: Any strategy instance

    Returns:
        Description string
    """
    
    if isinstance(strategy, LevelCrossStrategy):
        return f"{strategy.name} with level={strategy.level}"
    elif isinstance(strategy, MovingAverageStrategy):
        return f"{strategy.name} with period={strategy.ma_period}"
    else:
        return strategy.name


        
# Test cases
strat1 = LevelCrossStrategy(100.0)
strat2 = MovingAverageStrategy(5)

print(analyze_strategy(strat1))
# Expected: "Level Cross Strategy with level=100.0"

print(analyze_strategy(strat2))


# LOG:

# $ python practice.py
# Strategy Level Cross Strategy with level = 100.0
# Strategy MovingAverage Strategy with ma period = 5
```

---

## Task 6: PCAP Trap - Method Resolution Order (MRO)

Predict the output:

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    pass

obj = D()
print(obj.method())
print(D.__mro__)
```

**Your prediction:**
```
# Output:
C
The mro in mock is written as D -> C -> B -> A (from inner to outer)

# Explanation (what is MRO and how does Python determine which method to call?):
It's called the Method Resolution Order and Python check the methods order and it always goes to the inner one as the last one, which takes the precedence in the order. In practice, method B overwrites method A, and then method C overwrites method B. Method D should overwrite B, C, but it's empty, it only has pass so it does nothing. So if the C is the last written method, it will overwrite every previous one and we will see the output from C.
```

---

## Task 7: PCAP Multiple Choice

### Question 1
What is polymorphism?

A) The ability to create multiple classes
B) The ability to use objects of different types through the same interface
C) The ability to inherit from multiple parents
D) The ability to override methods

**Your answer:** B

---

### Question 2
What is the output?

```python
class Animal:
    def speak(self):
        return "sound"

class Dog(Animal):
    def speak(self):
        return "woof"

def make_sound(animal: Animal):
    return animal.speak()

d = Dog()
print(make_sound(d))
```

A) `"sound"`
B) `"woof"`
C) `TypeError`
D) `AttributeError`

**Your answer:** B

---

### Question 3
When should you use composition over inheritance?

A) Never, inheritance is always better
B) When you have a "HAS-A" relationship instead of "IS-A"
C) When you want polymorphism
D) When you need to reuse code

**Your answer:** B

---

## Task 8: Code Review - Fix the Polymorphism Bug

This code is supposed to demonstrate polymorphism but has issues. Find ALL bugs (aim for 5+) and fix them:

```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return "Starting vehicle"

class Car(Vehicle):
    def start(self):
        return f"Starting {self.brand} car"

class Motorcycle(Vehicle):
    pass

def start_all_vehicles(vehicles):
    for v in vehicles:
        print(v.start())

vehicles = [
    Car("Toyota"),
    Motorcycle("Harley"),
    Vehicle("Generic")
]

start_all_vehicles(vehicles)
```

**Your findings:**
```
Issues found:
#1. Lack of docstrings/typehints
#2. Car has a missing init and it doesn't use super() - perhaps it's okay as the code still works, but it just looks weird to me
#3. The Motorcycle class is empty, so what's the point of even having it there when it does nothing different compared to the parent class?
#4. As a consequence of the above, the start_all_vehicles will not be able to work properly and list all the vehicles or make us see any difference between them.



What would the actual output be with the bugs?

$ python practice.py
Starting Toyota car
Starting vehicle
Starting vehicle

What SHOULD the output be?

It should be specific for every type of the class and extended somehow, otherwise what's the point of having different classes and cluttering the codebase?


Corrected code:


class Vehicle:
    '''Parent class used to start a vehicle'''
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return "Starting vehicle"

class Car(Vehicle):
    '''A polimorphic variant of a Vehicle that is designed specifically for cars'''
    def __init__(self, brand: str, doors: int):
        super().__init__(brand)
        self.doors = doors
    
    def start(self):
        return f"Starting {self.brand} car with {self.doors} doors"

class Motorcycle(Vehicle):
    '''A polimorphic variant of a Vehicle extended specifically for motorcycles'''
    def __init__(self, brand, horsepower: int):
        super().__init__(brand)
        self.horsepower = horsepower
        
    def start(self):
        return f'Starting a {self.brand} motorcycle with {self.horsepower} horsepower'

def start_all_vehicles(vehicles):
    for v in vehicles:
        print(v.start())

vehicles = [
    Car("Toyota", 4),
    Motorcycle("Harley", 50),
    Vehicle("Generic")
]

start_all_vehicles(vehicles)


```python


```
```

---

## Task 9: Bonus Challenge - Strategy Factory Pattern

Implement a factory function that creates strategies based on a string name:

```python
from typing import Union
from algo_backtest.strategies import BaseStrategy, LevelCrossStrategy, MovingAverageStrategy

def create_strategy(name: str, **kwargs) -> BaseStrategy:
    """Factory function to create strategies by name.

    Args:
        name: Strategy type ("level_cross" or "ma")
        **kwargs: Parameters for the strategy

    Returns:
        Strategy instance

    Raises:
        ValueError: If strategy name is unknown
    """
    # TODO: Implement factory logic
    pass

# Test cases
strat1 = create_strategy("level_cross", level=100.0)
print(strat1.generate_signal(105))  # Should print "BUY"

strat2 = create_strategy("ma", period=5)
print(strat2.get_name())  # Should print "MA(5)"

try:
    strat3 = create_strategy("unknown")
except ValueError as e:
    print(f"Error: {e}")  # Should print error message
```

**Your solution:**
```python
# Paste your create_strategy function here


```

---

## Feedback Section

**Difficulty (1-10):** ___

**Time spent:** ___ minutes

**What clicked:**


**What's still confusing:**


**Questions for mentor:**


---

**When done, save this file and notify your mentor for assessment.**
