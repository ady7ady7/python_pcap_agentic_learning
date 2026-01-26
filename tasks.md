# Week 4, Day 2 - Tuesday
## Topic: Closures & Factory Functions

**Date:** 2026-01-27

**IMPORTANT:** Re-read the **Closures** section in `lessons/week4_lambda_closures.md` before starting!

**Target Difficulty:** 5/10

**Remember:** Work in `practice.py`, paste FINAL answers here for review.

---

## Task 1: Closure Basics (PCAP Warm-up)

**Instructions:** Answer after reading the closures section.

**Q1:** What is the output?
```python
def outer(x):
    def inner(y):
        return x + y
    return inner

add_5 = outer(5)
print(add_5(3))
```

**Q2:** What is the output?
```python
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10), triple(10))
```

**Q3:** True or False: The inner function in a closure can access variables from the outer function even after the outer function has finished executing.

**Q4:** What does this print?
```python
def outer():
    message = "Hello"
    def inner():
        return message
    return inner

greet = outer()
print(greet())
```

**Your answers:**
```
Q1:
Q2:
Q3:
Q4:
```

---

## Task 2: Create a Closure - make_counter

**Instructions:** Create a factory function that creates counters.

```python
def make_counter(start=0):
    """
    Create a counter that remembers its count.

    Args:
        start: Initial count value (default 0)

    Returns:
        A function that increments and returns the count
    """
    # Your code here
    pass

# Test:
counter_a = make_counter(0)
counter_b = make_counter(100)

print(counter_a())  # 1
print(counter_a())  # 2
print(counter_a())  # 3

print(counter_b())  # 101
print(counter_b())  # 102
```

**Hint:** You'll need the `nonlocal` keyword to modify the outer variable.

**Your code:**
```python

```

**Test output:**
```

```

---

## Task 3: nonlocal vs global

**Q1:** What is the output?
```python
x = 10

def outer():
    x = 20

    def inner():
        nonlocal x
        x = 30

    inner()
    print("outer x:", x)

outer()
print("global x:", x)
```

**Q2:** What would happen if we used `global x` instead of `nonlocal x` in the inner function?

**Q3:** When do you use `nonlocal` vs `global`?

**Your answers:**
```
Q1:

Q2:

Q3:
```

---

## Task 4: Closure Trap - Late Binding

**Instructions:** This is a PCAP trap. Predict the output, then explain why.

```python
functions = []
for i in range(3):
    functions.append(lambda: i)

print(functions[0]())
print(functions[1]())
print(functions[2]())
```

**Q1:** What is the output?

**Q2:** Why does this happen? (Explain the "late binding" trap)

**Q3:** How do you fix it? Write the corrected version.

**Your answers:**
```
Q1 Output:

Q2 Explanation:

Q3 Fixed code:

```

---

## Task 5: PROJECT - make_price_validator

**Instructions:** Create a closure that validates prices against a threshold.

```python
def make_price_validator(min_price: float, max_price: float):
    """
    Create a price validator function.

    Args:
        min_price: Minimum acceptable price
        max_price: Maximum acceptable price

    Returns:
        A function that takes a price and returns (is_valid, message)
    """
    # Your code here
    pass

# Test:
validate_stock = make_price_validator(0.01, 10000.0)
validate_crypto = make_price_validator(0.0001, 100000.0)

print(validate_stock(150.50))     # (True, "Price 150.5 is valid")
print(validate_stock(-5.0))       # (False, "Price -5.0 below minimum 0.01")
print(validate_stock(50000.0))    # (False, "Price 50000.0 above maximum 10000.0")

print(validate_crypto(0.00001))   # (False, "Price 1e-05 below minimum 0.0001")
print(validate_crypto(45000.0))   # (True, "Price 45000.0 is valid")
```

**Your code:**
```python

```

**Test output:**
```

```

---

## Task 6: PCAP Multiple Choice

**Q1:** What is a closure?
- A) A function that closes files automatically
- B) A function that remembers variables from its enclosing scope
- C) A function that cannot be called
- D) A function with no parameters

**Q2:** What keyword is used to modify a variable in an enclosing (non-global) scope?
- A) `global`
- B) `local`
- C) `nonlocal`
- D) `outer`

**Q3:** What is the output?
```python
def make_adder(n):
    return lambda x: x + n

add10 = make_adder(10)
print(add10(5))
```
- A) `5`
- B) `10`
- C) `15`
- D) `TypeError`

**Q4:** In the late binding trap, why do all functions return the same value?
- A) Python has a bug
- B) The lambda captures the variable reference, not the value at creation time
- C) Lists cannot store functions
- D) Lambda functions don't work in loops

**Your answers:**
```
Q1:
Q2:
Q3:
Q4:
```

---

## Task 7: PROJECT - make_trade_logger

**Instructions:** Create a closure that logs trades with a customizable prefix.

```python
def make_trade_logger(prefix: str):
    """
    Create a trade logger with a specific prefix.

    The logger should also track the total number of trades logged.

    Args:
        prefix: String prefix for log messages (e.g., "INFO", "TRADE")

    Returns:
        A tuple of (log_trade, get_count) functions
    """
    # Your code here
    pass

# Test:
log_trade, get_count = make_trade_logger("TRADE")

log_trade("AAPL", "BUY", 150.0)   # [TRADE] AAPL BUY @ $150.00
log_trade("GOOGL", "SELL", 2800.0) # [TRADE] GOOGL SELL @ $2800.00
log_trade("MSFT", "BUY", 300.0)   # [TRADE] MSFT BUY @ $300.00

print(f"Total trades: {get_count()}")  # Total trades: 3

# Create another logger with different prefix
log_error, error_count = make_trade_logger("ERROR")
log_error("TSLA", "FAILED", 0.0)  # [ERROR] TSLA FAILED @ $0.00
print(f"Errors: {error_count()}")  # Errors: 1
```

**Your code:**
```python

```

**Test output:**
```

```

---

## Task 8: Closure vs Class

**Instructions:** The closure pattern can sometimes replace simple classes. Compare these two approaches.

**Closure approach:**
```python
def make_account(initial_balance):
    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if amount <= balance:
            balance -= amount
            return balance
        raise ValueError("Insufficient funds")

    def get_balance():
        return balance

    return deposit, withdraw, get_balance
```

**Class approach:**
```python
class Account:
    def __init__(self, initial_balance):
        self._balance = initial_balance

    def deposit(self, amount):
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return self._balance
        raise ValueError("Insufficient funds")

    def get_balance(self):
        return self._balance
```

**Questions:**

**Q1:** What are the advantages of the closure approach?

**Q2:** What are the advantages of the class approach?

**Q3:** When would you prefer closures over classes?

**Your answers:**
```
Q1 (Closure advantages):

Q2 (Class advantages):

Q3 (When to use closures):

```

---

## Solutions Checklist

- [ ] Task 1: Closure basics (4 questions)
- [ ] Task 2: make_counter closure
- [ ] Task 3: nonlocal vs global (3 questions)
- [ ] Task 4: Late binding trap
- [ ] Task 5: PROJECT - make_price_validator
- [ ] Task 6: PCAP Multiple choice (4 questions)
- [ ] Task 7: PROJECT - make_trade_logger
- [ ] Task 8: Closure vs Class comparison

---

## Feedback Section

**Time spent:** ___ minutes

**Difficulty (1-10):**

**What clicked:**


**What's confusing:**


**Questions for mentor:**


---

**When complete:** Fill out feedback section and notify me for assessment.
