# Week 2, Day 4 Tasks - Position Sizing & Strategy Backtesting

**Focus:** Risk-based position sizing, strategy comparison, PCAP drills (more exam focus, less abstract OOP)

**Instructions:**
- Work in `practice.py` for experimentation
- Paste your FINAL solutions/answers below each task
- For project tasks, modify files in `algo_backtest/` as specified

---

## Task 1: PCAP Warm-up - Exception Handling Order

Predict the output WITHOUT running the code:

```python
def process_data(value):
    try:
        result = 10 / value
        data = [1, 2, 3]
        print(data[value])
    except ZeroDivisionError:
        return "Zero error"
    except IndexError:
        return "Index error"
    except Exception as e:
        return f"Other: {e}"
    else:
        return "Success"
    finally:
        print("Cleanup")

print(process_data(0))
print(process_data(5))
print(process_data(2))
```

**Your prediction:**
```
# Output:
#Zero error -> Cleanup
#Index error -> Cleanup
#Success -> Cleanup




# Explanation (what is the order of exception handling?):
It's arranged well, from specific to general and from the usual order they might occur.
The else block only executes if we don't get any errors, and finally block always executes.


```

---

## Task 2: PROJECT - Position Sizing from Risk

**This is actually useful!** Implement risk-based position sizing for your backtest engine.

**Concept:**
- You have $10,000 account
- You want to risk max 1% per trade ($100)
- Entry at $50, Stop Loss at $48 (distance = $2)
- **Position size = Risk $ / Distance = $100 / $2 = 50 shares**

**Requirements:**
1. Add `@classmethod` to `Position` class: `calculate_position_size(account_balance: float, risk_percent: float, entry_price: float, stop_loss: float) -> float`
2. Method should:
   - Calculate risk in dollars: `account_balance * (risk_percent / 100)`
   - Calculate distance: `abs(entry_price - stop_loss)`
   - Return position size: `risk_dollars / distance`
   - Handle edge case: if distance == 0, return 0
3. Add type hints and docstring

**Example usage:**
```python
# Risk 1% of $10,000 account = $100 max loss
# Entry $50, SL $48 (distance $2)
size = Position.calculate_position_size(10000, 1.0, 50.0, 48.0)
print(size)  # Should print 50.0
```

**Paste your code below:**
```python
# In algo_backtest/engine/position.py


    @classmethod
    def calculate_position_size(self,
                                account_balance: float,
                                risk_percent: float, 
                                entry_price: float, 
                                stop_loss_price: float) -> float:
        '''
        A class method used to calculate the position size based on a set risk %,
        entry + stop loss
        
        For now it uses a stop loss price - at some point I might decide to use distance instead - depends on our needs
        '''
        try:
            usd_risk = account_balance * (risk_percent / 100)
            distance = abs(entry_price - stop_loss_price)
            
            if distance != 0:
                position_size = usd_risk / distance
                return position_size
            else:
                print('The stop loss is set at the entry price, returning 0')
                return 0
            
        except Exception as e:
            print(f'Unexpected error: {str(e)}')

```

---

## Task 3: PCAP Drill - List Comprehensions with Conditionals

Predict the output WITHOUT running:

```python
prices = [100, 105, 98, 102, 110, 95]

# A
result_a = [p for p in prices if p > 100]

# B
result_b = [p * 2 if p > 100 else p for p in prices]

# C
result_c = [p for p in prices if p > 100 if p < 110]

print(result_a)
print(result_b)
print(result_c)
```

**Your answer:**
```
result_a = [105, 102, 110]

result_b = [100, 210, 98, 204, 220, 95]
 
result_c = [105, 102]

# Explanation (difference between filter-if and ternary-if):
Not sure what you mean by these name filter-if and ternary-if (you can explain), but the logic here is simple:
In result A - if serves as a filter to only get entries above 100 (p > 100)
In result B - there is an if-else structure - for entries above 100 (p > 100) we multiply them by 2, and others are returned normally (else p)
In result C - there is quite weird double if structure (never seen it before, as normally we'd probably use and or something like that) but the logic is simple as well we only fetch entries above 100 (p > 100) and the second if works as the second condition for entries below 110 (p < 110)


```

---

## Task 4: PROJECT - Strategy Backtesting Comparison

**This is actually useful!** Run multiple strategies on the same data and compare performance.

**Requirements:**
1. Create `algo_backtest/engine/backtest_comparison.py`
2. Implement `StrategyComparison` class with:
   - `__init__(self, strategies: List[BaseStrategy], prices: List[float])`
   - `run_backtest(self) -> Dict[str, Dict[str, float]]` that returns:
     ```python
     {
         "Level Cross Strategy": {
             "signals": ["BUY", "BUY", "HOLD", ...],
             "win_rate": 0.65,
             "total_trades": 20
         },
         "MovingAverage Strategy - ma 5": {
             "signals": ["HOLD", "BUY", "SELL", ...],
             "win_rate": 0.58,
             "total_trades": 18
         }
     }
     ```
   - Calculate win_rate as: (BUY signals + SELL signals) / total signals
   - Add type hints and docstrings

3. Create test script that compares LevelCrossStrategy and MovingAverageStrategy on sample prices

**Paste your code below:**
```python
# backtest_comparison.py

This is a great idea, but a too big knowledge gap for me at this point.
I want to actually learn to be able to do such a thing BUT I NEED TO BE UNDERSTANDING IT.
I don't want to use any form of cheating now, but WE SHOULD aim to create a similar file/code during the next two-three weeks, but I'm not ready for that now.

For that I'd like to:
- learn how these list imports of package strategies work - as a scaffolded approach, from very simple examples
- create a backtesting engine first - a one that will be thought over for my needs (scaffolded)
- after the backtesting engine is in place, we can think about a similar code to this that you require now.

But remember, the main goal for me is to understand everything I do, I do not want to jump gaps that are too big yet.

This task is a 9/10 difficulty for now, I'm not doing it and I'D LIKE YOU TO NOW TAKE AWAY POINTS FROM ME FOR THAT!


# Test script (practice.py or separate file)




```

---

## Task 5: PCAP Trap - Mutable Default Arguments

What's wrong with this code? Predict the output and explain the bug:

```python
def add_trade(trade, portfolio=[]):
    portfolio.append(trade)
    return portfolio

result1 = add_trade("AAPL")
result2 = add_trade("GOOGL")
result3 = add_trade("MSFT", [])

print(result1)
print(result2)
print(result3)
```

**Your answer:**
```
Output:

print(result1) 'AAPL'
print(result2) 'AAPL, GOOGL'
print(result3) 'MSFT'




Bug explanation:
There is a mutable default parameter - a list, which is problematic.
It works as if it was saved for every other object we create, unless we provide our own version of a default parameter, as in result 3.


How to fix it:

We shouldn't use an empty list as our parameter - there are solutions to that as using None as default parameter:

def add_trade(trade, portfolio = None): #This was the issue - mutable default parameter
    
    if portfolio is None:
        portfolio = []
    portfolio.append(trade)
    return portfolio


```

---

## Task 6: PCAP Drill - Class Methods vs Static Methods

What's the difference? When would you use each?

```python
class Strategy:
    default_risk = 0.01

    @classmethod
    def from_risk(cls, account_balance):
        return cls(account_balance * cls.default_risk)

    @staticmethod
    def validate_price(price):
        return price > 0

    def __init__(self, risk_amount):
        self.risk_amount = risk_amount
```

**Questions:**

1. What does `@classmethod` receive as first parameter?
2. What does `@staticmethod` receive as first parameter?
3. Can a `@classmethod` access `self.risk_amount`?
4. Can a `@staticmethod` access `cls.default_risk`?
5. When should you use `@classmethod` instead of `@staticmethod`?

**Your answers:**

Listen, again this is a knowledge gap - we didn't have staticmethod...
We also should have some notes on both classmethod and staticmethod in week2_classmethod_staticmethod with examples. I'll try to solve the questions anyway, as we've already had classmethod, and I'll use the web to find info on staticmethod, BUT WE NEED THE NOTES as I told you above.


```
1. It receives the class name

2. It receives price

3. Yes.

4. From what i've read, no - it doesn't have access to the class or instance.

5. When you want to have a separate class function used outside and for specific occasions, but you also need some of the class parameters or defined logic or whatever.

```

---

## Task 7: Multiple Choice - PCAP Focus

**Question 1:** What happens when you inherit from a class but don't call `super().__init__()`?

A) Syntax error
B) Parent's `__init__` doesn't run, parent attributes not initialized
C) Automatically calls parent's `__init__` anyway
D) TypeError at runtime

**Your answer:** 
C

---

**Question 2:** Which exception is raised when you divide by zero?

A) ValueError
B) ZeroDivisionError
C) ArithmeticError
D) DivisionError

**Your answer:** B

---

**Question 3:** What does `try/except/else/finally` do?

A) `else` runs if exception occurs, `finally` runs always
B) `else` runs if no exception, `finally` runs always
C) `else` runs always, `finally` runs if exception
D) `else` runs if no exception, `finally` runs only on success

**Your answer:** B

---

## Task 8: Code Review - Fix the Risk Calculator

This code has bugs. Find them and fix it:

```python
class RiskCalculator:
    def __init__(self, account_balance):
        self.account_balance = account_balance

    def calculate_position_size(self, risk_percent, entry, stop_loss):
        risk_dollars = self.account_balance * risk_percent  # Bug 1
        distance = entry - stop_loss  # Bug 2
        position_size = risk_dollars / distance  # Bug 3
        return position_size

    def get_risk_amount(risk_percent):  # Bug 4
        return self.account_balance * (risk_percent / 100)

# Test
calc = RiskCalculator(10000)
size = calc.calculate_position_size(1, 50, 48)  # Should be 50 shares
print(size)
```

**Bugs found:**
```
# 1. No type hints/ docstrings
# 2. Lack of self in get_risk_amount method
# 3. That really depends on how we ask and present our data, but risk_percent and multiplying it by our acc balance like that might be tricky.
#If somebody gives the percent value like 5, we'd get our balance by 5 instead of 5% of our balance. But this depends, as we could also state percents as 0.05.
# 4. I've chosen more descriptive variants for entry and stop_loss

```

**Corrected code:**
```python

class RiskCalculator:
    '''Class used to calculate risk - both position size and the risk amount'''
    
    
    
    
    def __init__(self, account_balance: float):
        self.account_balance = account_balance
        
    def calculate_position_size(self, 
                                risk_percent: float, 
                                entry_price: float, 
                                stop_loss_price: float) -> float:
        
        '''Method used to calculate position size - check args, as this is IMPORTANT:
        
        risk_percent - GIVE THE ACTUAL PERCENT VALUE here (e.g. 0.5 for 0.5%, 5 for 5%, 20 for 20%)
        entry - provide the entry price e.g. 2053.43
        stop_loss_price - as above,

        
        '''
        
        risk_dollars = self.account_balance * (risk_percent / 100)
        distance = abs(entry_price - stop_loss_price)  #More descriptive variant + abs for both BUY/SELL
        position_size = risk_dollars / distance  #This should be correct now if we assume that above is correct
        return position_size

    def get_risk_amount(self, risk_percent):
        '''Get the risk amount per position'''
        return self.account_balance * (risk_percent / 100)

# Test
calc = RiskCalculator(10000)
size = calc.calculate_position_size(1, 50, 48)  # Should be 50 shares
print(size)


```

---

## Task 9: BONUS - Portfolio P&L Tracking

Extend Task 4 to track actual P&L if strategies were traded.

**Requirements:**
- For each strategy, calculate hypothetical P&L assuming:
  - BUY at current price → profit if next price is higher
  - SELL at current price → profit if next price is lower
  - HOLD → no trade
- Return total P&L for each strategy
- Compare which strategy performed best

**Paste your code below:**
```python
# Extended backtest_comparison.py

SKIPPED FOR THE REASONS STATED IN TASK4 - I want to be able to get to the stage where I can comfortably create similar things, but I NEED TO UNDERSTAND THEM, and the road to that is through a step-by-step understanding process and building blocks, not jumping suhc a huge bricks. It's not a gap created in this task though, it's the gap in task 4, as this task seems rather simple if we had task 4 completed. I still expect YOU WILL NOT TAKE AWAY MY points for this.




```

---

## Feedback Section

**Time spent:** 60 minutes

**Difficulty (1-10):**
5-9

**What clicked:**


**What's confusing:**
Task 4 is definitely a LEAP too big for today and it doesn't make sense.

**Questions:**


