# Week 4, Day 5 - Friday
## Topic: Final Functional Programming Review & Exam Prep

**Date:** 2026-01-30

**Purpose:** Final PCAP drills before weekend exams. Master Week 4 functional patterns.

**Target Difficulty:** 5/10

**Remember:** Work in `practice.py`, paste FINAL answers here for review.

---

## Task 1: Lambda Expression Mastery (6 Questions)

**Instructions:** Answer quickly - these are classic PCAP traps.

**Q1:** What is the output?
```python
f = lambda x, y, z=3: x + y * z
print(f(1, 2))

7
```

**Q2:** What is the output?
```python
funcs = [(lambda x: x + i) for i in range(3)]
print(funcs[0](10), funcs[1](10), funcs[2](10))

12, 12, 12
```

**Q3:** What is the output?
```python
funcs = [(lambda x, i=i: x + i) for i in range(3)]
print(funcs[0](10), funcs[1](10), funcs[2](10))

10, 11, 12
```

**Q4:** Which is valid?
- A) `lambda x: return x + 1`
- B) `lambda x: x + 1`
- C) `lambda: x = 5`
- D) `lambda x: print(x); x + 1`

B

**Q5:** What is the output?
```python
result = (lambda: (lambda x: x * 2)(5))()
print(result)

10
```

**Q6:** What is the output?
```python
g = lambda *args: sum(args)
print(g(1, 2, 3, 4))

10
```

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

## Task 2: Closure Deep Dive (4 Questions)

**Instructions:** Trace the execution carefully.

**Q1:** What is the output?
```python
def outer(n):
    def inner(x):
        return x ** n
    return inner

square = outer(2)
cube = outer(3)
print(square(4) + cube(2))

Answer: 24
```

**Q2:** What is the output?
```python
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    def get():
        return count
    return increment, get

inc, get = counter()
print(inc(), inc(), get())


Answer: 1, 2, 2
```

**Q3:** What is the output?
```python
def make_multipliers():
    return [lambda x, i=i: x * i for i in range(4)]

mults = make_multipliers()
print(mults[2](10))

Answer: 20
```

**Q4:** What is printed?
```python
def factory(start):
    value = start
    def add(x):
        nonlocal value
        value += x
        return value
    return add

adder1 = factory(10)
adder2 = factory(100)
print(adder1(5), adder2(5), adder1(5))

Answer: 15, 105, 20
```

**Your answers:**
```
Q1:
Q2:
Q3:
Q4:
```

---

## Task 3: map/filter/reduce Pipeline

**Instructions:** Build a complete data processing pipeline.

```python
from functools import reduce

transactions = [
    {"id": 1, "type": "BUY", "amount": 1000, "fee": 10},
    {"id": 2, "type": "SELL", "amount": 500, "fee": 5},
    {"id": 3, "type": "BUY", "amount": 2000, "fee": 20},
    {"id": 4, "type": "SELL", "amount": 800, "fee": 8},
    {"id": 5, "type": "BUY", "amount": 300, "fee": 3},
]

# Part A: Use map to add net_amount (amount - fee) to each transaction
# HINT: Create a function that returns a NEW dict with net_amount added

# Part B: Use filter to get only BUY transactions with net_amount > 500

# Part C: Use reduce to calculate total net_amount of filtered transactions

# Expected output:
# All transactions with net_amount: [990, 495, 1980, 792, 297]
# Filtered BUY transactions: [id=1, id=3]
# Total net amount: 2970
```

**Your code:**
```python

result = list(map(lambda t: {**t, 'net_amount': t['amount'] - t['fee']}, transactions))


new_trades = [] #Look, adding a new dict would be absolutely retarded, as we'd have to have a key for each trade, which doesn't make sense imo.
for transaction in result:
    new_trades.append(transaction)
    
filtered_buys = [t for t in new_trades if t['type'] == 'BUY' and t['net_amount'] > 500] #started with this, much simpler approach, but then I read your instructions and used filter below
filtered_buys = list(filter(lambda t: t['type'] == 'BUY' and t['net_amount'] > 500, new_trades))
print(filtered_buys)

total_net_amount = reduce(lambda acc, t: acc + t['net_amount'], filtered_buys, 0)
print(total_net_amount)


```

---

## Task 4: Decorator with Arguments

**Instructions:** Create a decorator that accepts arguments.

```python
def repeat(times):
    """
    Decorator that runs a function multiple times.

    Example:
        @repeat(3)
        def say_hello():
            print("Hello!")

        say_hello()
        # Output:
        # Hello!
        # Hello!
        # Hello!
    """
    # Your code here
    pass

# Test 1: Basic
@repeat(3)
def greet(name):
    print(f"Hi, {name}!")

greet("Alice")

# Test 2: With return value (should return last result)
@repeat(2)
def double(x):
    print(f"Doubling {x}")
    return x * 2

result = double(5)
print(f"Final result: {result}")
```

**Your code:**
```python

def repeat(times):
    """
    Decorator that runs a function multiple times.

    Example:
        @repeat(3)
        def say_hello():
            print("Hello!")

        say_hello()
        # Output:
        # Hello!
        # Hello!
        # Hello!
    """
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

#Although please mind, that this was very fdifficult and unintuitive for me and I had to check for materials.
#I'd like to practice decorators more, especially if they're PCAP relevant and generally used in Mid-Senior level programming or a good practice

```

---

## Task 5: PCAP Multiple Choice (8 Questions)

**Q1:** What does `map(str, [1, 2, 3])` return?
- A) `['1', '2', '3']`
- B) `<map object>`
- C) `('1', '2', '3')`
- D) Error


B

**Q2:** What is the output?
```python
from functools import reduce
print(reduce(lambda a, b: a - b, [10, 2, 3]))
```
- A) 5
- B) 15
- C) -5
- D) Error

A

**Q3:** What is the output?
```python
def deco(f):
    def wrapper():
        return f() * 2
    return wrapper

@deco
@deco
def five():
    return 5

print(five())
```
- A) 5
- B) 10
- C) 20
- D) Error

D

**Q4:** What is the output?
```python
x = 10
def outer():
    x = 20
    def inner():
        global x
        return x
    return inner()

print(outer())
```
- A) 10
- B) 20
- C) Error
- D) None

A

**Q5:** What is the output?
```python
nums = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2, nums))
print(result)
```
- A) `[2, 4]`
- B) `[1, 3, 5]`
- C) `[1, 2, 3, 4, 5]`
- D) `[]`

a

**Q6:** Which creates a closure?
- A) `def f(): return 42`
- B) `def f(x): return x + 1`
- C) `def f(n): def g(): return n; return g`
- D) `lambda x: x * 2`

C

**Q7:** What is the output?
```python
make_adder = lambda n: lambda x: x + n
add_five = make_adder(5)
print(add_five(10))
```
- A) 5
- B) 10
- C) 15
- D) Error

C

**Q8:** What is the output?
```python
from functools import reduce
words = ["a", "b", "c"]
result = reduce(lambda acc, w: acc + [w.upper()], words, [])
print(result)
```
- A) `['a', 'b', 'c']`
- B) `['A', 'B', 'C']`
- C) `ABC`
- D) Error

B

**Your answers:**
```
Q1:
Q2:
Q3:
Q4:
Q5:
Q6:
Q7:
Q8:
```

---

## Task 6: PROJECT - Strategy Signal Generator with Functional Patterns

**Instructions:** Create a signal generator using everything from Week 4.

```python
from functools import reduce
from typing import List, Dict, Callable

prices = [100, 102, 105, 103, 108, 106, 110, 112, 109, 115]

# Part A: Create a closure that generates crossover signals
def make_level_detector(level: float):
    """
    Returns a function that detects when price crosses a level.

    The returned function should:
    - Accept current_price and previous_price
    - Return "BUY" if price crosses UP through level
    - Return "SELL" if price crosses DOWN through level
    - Return "HOLD" otherwise

    Example:
        detect_105 = make_level_detector(105)
        detect_105(106, 104)  # Returns "BUY" (crossed up through 105)
        detect_105(104, 106)  # Returns "SELL" (crossed down through 105)
        detect_105(107, 106)  # Returns "HOLD" (didn't cross 105)
    """
    pass

# Part B: Use map to create price pairs [(prev, curr), ...]
# prices[0] has no previous, so start from index 1
# Result: [(100, 102), (102, 105), (105, 103), ...]

# Part C: Use the detector + map to generate signals for each pair

# Part D: Use filter to get only BUY and SELL signals (not HOLD)

# Part E: Use reduce to count total BUY signals

# Expected behavior:
# detect_105 = make_level_detector(105)
# Signals: ['HOLD', 'BUY', 'SELL', 'BUY', 'HOLD', 'HOLD', 'HOLD', 'SELL', 'BUY']
# Action signals (no HOLD): ['BUY', 'SELL', 'BUY', 'SELL', 'BUY']
# Total BUY signals: 3
```

**Your code:**
```python

def make_level_detector(level: float):
    """
    Returns a function that detects when price crosses a level.

    The returned function should:
    - Accept current_price and previous_price
    - Return "BUY" if price crosses UP through level
    - Return "SELL" if price crosses DOWN through level
    - Return "HOLD" otherwise

    Example:
        detect_105 = make_level_detector(105)
        detect_105(106, 104)  # Returns "BUY" (crossed up through 105)
        detect_105(104, 106)  # Returns "SELL" (crossed down through 105)
        detect_105(107, 106)  # Returns "HOLD" (didn't cross 105)
    """
    
    def generate_signal(current_price: float, previous_price: float):
        '''Closure used to generate signals based on previous price, current price and the set price level'''
        if previous_price <= level and current_price >= level:
            return 'BUY'
        elif previous_price >= level and current_price <= level:
            return 'SELL'
        elif (previous_price >= level and current_price >= level) or (previous_price <= level and current_price <= level):
            return 'HOLD'
              
    return generate_signal

prices = [100, 102, 105, 103, 108, 106, 110, 112, 109, 115]

price_pairs = list(map(lambda i: (prices[i-1], prices[i]), range(1, len(prices))))
print(price_pairs)
signals = []
for price_pair in price_pairs:
    result = detect_105(price_pair[1], price_pair[0]) #current, previous
    signals.append(result)

print(signals)

action_signals = list(filter(lambda signal: signal == 'BUY' or signal == 'SELL', signals))
print(action_signals)
buy_signals = reduce(lambda acc, x: acc + 1 if x == 'BUY' else acc, action_signals, 0)
print(buy_signals)

$ python practice.py
[(100, 102), (102, 105), (105, 103), (103, 108), (108, 106), (106, 110), (110, 112), (112, 109), (109, 115)]
['HOLD', 'BUY', 'SELL', 'BUY', 'HOLD', 'HOLD', 'HOLD', 'HOLD', 'HOLD']
['BUY', 'SELL', 'BUY']
2


#And your expectations are wrong, we're not CROSSING any level if the previous and the current price is already above a given level, so we have 2 buy signals and it's logically correct.
```

---

## Task 7: Decorator Stacking & Order

**Instructions:** Understand decorator execution order.

```python
def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

@bold
@italic
def greet(name):
    return f"Hello, {name}"

print(greet("World"))
```

**Q1:** What is the output?
- A) `<b><i>Hello, World</i></b>`
- B) `<i><b>Hello, World</b></i>`
- C) `<b>Hello, World</b>`
- D) `<i>Hello, World</i>`

B

**Q2:** In what order are the decorators applied?
- A) bold first, then italic
- B) italic first, then bold
- C) Both at the same time
- D) Depends on Python version


A

**Q3:** If we changed it to `@italic @bold`, what would the output be?

`<b><i>Hello, World</i></b>`

**Your answers:**
```
Q1:
Q2:
Q3:
```

---

## Task 8: Week 4 Self-Assessment & Exam Readiness

**Instructions:** Rate yourself honestly (1-5 scale) and identify weak spots.

| Concept | Rating (1-5) | Confident for Exam? |
|---------|--------------|---------------------|
| Lambda syntax - 4 - depends on the context
| Lambda with defaults 4-5 - depends on the context
| Late binding trap 4.5
| Late binding fix 2 - I don't get it yet, would appreciate a simple task with a few simple examples
| map() returns - 3, This is really weird and unnatural for me, I'd use list comprehension in 9/10 cases if I had a choice myself
| filter() returns - 3, same as above, definitely needs practice
| filter(None, ...) - 3, same as above - I find it unnatural, as normally we use filter to identify things with that feature and here we kinda elliminate them
| reduce() with initializer - 5, it's pretty easyt for me
| reduce() without initializer - 5, same - it makes the most sense out of lambda/map/filter concepts and I will likely use it
| Closure definition - 4, I could mix it up If I were to combine several functions within a closure
| nonlocal keyword - 5, I get it
| Factory functions - 3-4 - if we get 3 levels of nesting it gets really weird and I'm getting lost
| Basic decorators - 3-4, not feeling confident - too much output prediciton, not too much actual decorator creating practice - I'd appreciate that,  from simple exampl;es to more difficult, especially if it's PCAP relevant and mid-senior devs relevant
| Decorators with args - same as above
| functools.wraps - 3, same as above, I totally get the idea but could have issues applying it without looking it up
| Decorator stacking order - IDK, it's first time we stack decorators today

**Topics I need to review before the exam:**
```
1.
2.
3.
```

**Questions I still have:**
```

```

---

## Solutions Checklist

- [ ] Task 1: Lambda expressions (6 questions)
- [ ] Task 2: Closure deep dive (4 questions)
- [ ] Task 3: map/filter/reduce pipeline
- [ ] Task 4: Decorator with arguments
- [ ] Task 5: PCAP multiple choice (8 questions)
- [ ] Task 6: PROJECT - Signal generator
- [ ] Task 7: Decorator stacking order
- [ ] Task 8: Self-assessment

---

## Feedback Section

**Time spent:** ___ minutes

**Difficulty (1-10):**

**Ready for weekend exams?**
[ ] Yes - bring them on!
[ ] Need more practice on: _______________

**Questions for mentor:**


---

**When complete:** Notify me for assessment. Weekend = 2 PCAP Mock Exams (30 questions each)!
