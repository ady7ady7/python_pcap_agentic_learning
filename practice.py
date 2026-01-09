import pandas as pd #added on W1 D4, and I will be definitely using both pd/np
import numpy as np


#This file will be used for me to test the code and complete the tasks - but it will not be checked by the agent,
#it's just for me


#Week1 Day1 Task1

'''tasks_files/math_utils.py'''

# '''Mock file for practicing imports with some basic functions'''

# def add(a, b):
#     '''add nums and receive the result'''
#     return a + b

# def multiply(a, b):
#     '''multiply nums and receive the result'''
#     return a * b

# pi = 3.14159 #module-level ocnstant

# '''tasks_files/test_imports.py'''

# import math_utils

# #task1
# x1 = math_utils.add(3, 5)
# print(x1)


#W1 D1 Task2
# import sys
# print(sys.path[0]) #current dir

# num = 0
# for path in sys.path:
#     num += 1
#     print(f'{num}: {path}')

# sys.path.append(r'C:\Users\HARDPC\Desktop\AL\projekty\python_pcap_agentic_learning\tasks_files\secret')

# mock_var = 3
# import hidden
# from hidden import * #If we use the wildcard import, we would also import the value of the mock_var in there
# from hidden import mock_var #also works if we would like to import a single variable for whatever reason

# num = 0
# for path in sys.path:
#     num += 1
#     print(f'{num}: {path}')

# print(mock_var)

#W1 D1 Task3
# You're given this broken package structure:

# ```
# broken_pkg/
# ├── __init__.py
# ├── engine.py
# └── utils.py
# ```

# **engine.py:**
# ```python
# from broken_pkg.utils import helper

# def start():
#     return helper()
# ```

# **utils.py:**
# ```python
# from broken_pkg.engine import start

# def helper():
#     return "Engine started: " + start()

# **Task:**
# 1. Predict what error occurs when you run `from broken_pkg import engine`
# 2. Fix the circular dependency WITHOUT changing the function behavior
# 3. Explain your solution in a comment

#We'd get an error, as the engine.py depends on broken_pkg, and we're trying to import what's already in there, and we're trying to select the general scope from the specific file of this very scope, which is erratic. Same for utils.py.
# 
# **engine.py:**
# ```python
# from utils import helper

# def start():
#     return helper()

# **utils.py:**
# ```python
# from engine import start

# def helper():
#     return "Engine started: " + start()

#We simply import the respective modules from the current folder we're in, no need to do circular imports here
#Python automatically checks the current directory first when importing modules


#W1 D1 Task 5

# '''Module used to check dependencies''' 
# /algo_backtest/check_dependencies.py

# def check_deps():
#     try:
#         import pandas as pd
#         import numpy as np
        
#     except ImportError as e:
#         print(f'Import error: {str(e)}')
#     except ModuleNotFoundError as e:
#         print(f'Module not found: {str(e)}')
#     except Exception as e:
#         print(f'Unexpected error: {str(e)}')
        
#     else:
#         print('Imports succeeded!')
#         print(f'Pandas version: {pd.__version__}')
#         print(f'Numpy version: {np.__version__}')


#W1 D2 T1

# s = "PCAP Exam"
# ```

# Predict the output of each expression (write answers in `practice.py`, paste here):

# 1. `s[100:]`
# 2. `s[-100:]`
# 3. `s[5:3]`
# 4. `s[::-1]`
# 5. `s[::2]`
# 6. `s[-4:-1]`

# **Question:** Why does `s[100:]` return an empty string instead of raising an `IndexError`?
#As slicing never returns an index error.

#empty string
#PCAP Exam
#empty string
#maxE PACP
#PA xm
#Exa

#W1 D2 T2
# print(s.find('E'))
# print(s.index('e'))

# s = "   ,  TEST, TEXT ,SUPER TEXT,    "

# strip = s.strip()
# print(strip)

# lstrip = s.lstrip()
# print(lstrip)

# rstrip = s.rstrip()
# print(rstrip)

# split_no_arg = s.split()
# print(split_no_arg)

# split_arg = s.split(' ')
# print(split_arg)

#W1 D2 T3

# def safe_divide(a: float, b: float) -> float:
    
#     try:
#         result = a / b
    
#     except ZeroDivisionError as e:
#         print(f'Cannot divide by zero! {str(e)}')
#     except TypeError as e:
#         print(f'Wrong data type, use float (e.g. 0.64, 6.4, 64.4). {str(e)}')
#     except Exception as e:
#         print(f'Unexpected error: {str(e)}')
        
#     else:
#         print('Operation successful')
#         return result
    
#     finally:
#         print('Operation complete')
    

# print(safe_divide(5, 0))
# print(safe_divide(40, 25))

#W1 D2 T4 - REFACTOR/DEBUG

# def process_data(value):
#     try:
#         result = int(value) / 10
#         return result
    
#     except ValueError:
#         print("Invalid number format")
#         return None
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#         return None
#     except Exception as e:
#         print(f"Generic error: {e}")
#         return None

#the exception handling instances were put in the wrong order, from general to specific, and it would always end up with a basic Exception handling

#W1 D1 T5

# from algo_backtest.data.data_loader import DataLoader

# loader = DataLoader('ohlc_mock_data.csv')
# data = loader.load_data()
# if data is not None:
#     print(data.head())
#     print(f"Loaded {len(data)} rows")
    

#/algo_backtest/data/data_loader.py
#     '''
# Data loading module for AlgoBacktest
# '''


# from typing import Optional
# import pandas as pd


# class DataLoader:
#     '''
#     Class used to load and validate data
    
#     Attributes:
#         file_path: path to the csv file with trading data
    
#     '''

#     def __init__(self, file_path: str) -> None:
#         '''Initialize the DataLoader class with file path'''
#         print('DataLoader initialized.')
#         self.filepath = file_path
    
    
#     def load_data(self) -> Optional[pd.DataFrame]:
#         '''
#         Load CSV data with error handling.

#         Returns:
#             DataFrame with columns: timestamp, ticker, open, high, low, close, volume (and DF index)
#             Returns None if file not found.

#         Raises:
#             ValueError: If CSV format is invalid or missing required columns.
#             FileNotFoundError: If file is missing or file name is wrong.
#             Pandas Parser Error: If there are any issues with data parsing.
#         '''
        
#         try:
#             data = pd.read_csv(self.filepath)
#             data.columns = ['timestamp', 'ticker', 'open', 'high', 'low', 'close', 'volume']
            
        
#         except FileNotFoundError as e:
#             print(f'File not found: {str(e)}')
#             return None
#         except ValueError as e:
#             print(f'Value Error! {str(e)}')
#         except pd.errors.ParserError as e:
#             print(f'Pandas Parser Error: {str(e)}')
#             return None
#         except Exception as e:
#             print(f'Unexpected error: {str(e)}')
            
        
#         else:
#             print('Data loading succeeded')
#             return data
        
#         finally:
#             print('Data loading operation ended.')
        
        
#W1 D1 T6

# from algo_backtest.data.data_loader import DataLoader

# loader = DataLoader('ohlc_mock_data.csv')
# data = loader.load_data()
# if data is not None:
#     print(data.head())
#     print(f"Loaded {len(data)} rows")
    
# x = loader.validate_data(data)
# print(x)


#     def validate_data(self, df: pd.DataFrame) -> bool:
#         '''
#         Docstring for validate_data

#         :param df: Description
#         :type df: pd.DataFrame
#         :return: Description
#         :rtype: bool
#         '''

#         req_columns = ['timestamp', 'ticker', 'open', 'high', 'low', 'close', 'volume']
#         #ohlc_columns = ['open', 'high', 'low', 'close']


#         missing_columns = set(df.columns) - set(df.columns)
#         if missing_columns:
#             print(f'Missing columns: {missing_columns}')
#             is_valid = False
    
#         nan_values = df[req_columns].isna().sum()
#         if nan_values.any():
#             print(f'Missing values found: {nan_values}')
#             is_valid = False

#         invalid_rows = df[df['high'] < df['low']]
#         if not invalid_rows.empty:
#             print(f'Found {len(invalid_rows)} invalid rows: {invalid_rows}')
#             is_valid = False

#         return is_valiD


        
#W1 D1 T7


# Write a function `read_config(file_path: str) -> dict` that:

# **Handles these edge cases:**
# 1. File doesn't exist (return empty dict)
# 2. File exists but is empty (return empty dict)
# 3. File has permission error (print error, return empty dict)
# 4. File contains valid data (return parsed dict - assume each line is `key=value`)

# def read_config(file_path: str) -> dict:
#     try:
#         with open(file_path, 'r') as f:
#             content = f.read()
            
#             if not content.strip(): #the file is empty
#                 return {}
            
#             config = {}
#             for line in content.strip().split('\n'):
#                 key, value = line.split('=', 1)
#                 config[key] = value

#             return config
#     except FileNotFoundError:
#         print(f'File not found - either it does not exist or the file name is wrong!')
#         return {}
#     except PermissionError as e:
#         print(f'Permission error: {str(e)}')

        
#W1 D2 Bonus Task

# def format_trade_summary(ticker: str, price: float, volume: int, side: str) -> str:
#     '''
#     Function used to return the trade in nice format
    
#     args:
#     ticker: str, 
#     price: float, 
#     volume: int, 
#     side: str
    
#     Returns:
#     A nicely formatted trade string, example:
#     "EURUSD: BUY @ 103.25 | Vol: 25,000"
#     '''
    
#     print(f'{ticker}: {side.upper()} @ {price:.2f} | Vol: {volume}')
    
# format_trade_summary('GBPUSD', 120.64, 100, 'buy')


#W1 D3 T1

# class Counter:
#     def __init__(self, start):
#         self.value = start

#     def increment(self):
#         self.value += 1

#     def get_value(self):
#         return self.value

# c1 = Counter(10)
# c2 = Counter(20)

# c1.increment()
# c1.increment()
# c2.increment()

# print(c1.get_value())
# print(c2.get_value())

# **Your answer:**
# - Line 1 output: `12`
# - Line 2 output: `21`

# **Explain:** Why do `c1` and `c2` have different values even though they're both `Counter` objects?

# **Answer here:**

# They are different objects, the Counter is only a blueprint for creating them. 
# C1 starts with 10 as a starting value and c2 with 20, and the number only gets incremented 
# as we call the increment() method (not function, as it's a class - method) only for the given object.


#W1 D3 T2

# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name):
#         self.name = name

# dog1 = Dog("Buddy")
# dog2 = Dog("Max")

# print(dog1.name)
# print(dog2.name)
# print(dog1.species)
# print(dog2.species)

# Dog.species = "Canis lupus"

# print(dog1.species)
# print(dog2.species)


# **Your predictions:**
# 1. `dog1.name` → `Buddy`
# 2. `dog2.name` → `Max`
# 3. `dog1.species` (first time) → `Canis familiaris`
# 4. `dog2.species` (first time) → `Canis familiaris`
# 5. `dog1.species` (after change) → 'Canis lupus`
# 6. `dog2.species` (after change) → Canis lupus`

# **Question:** What's the difference between `self.name` and `species` in this class?

# **Answer here:**
# Self.name is an attribute of a given class object - dog1/dog2.
# If we create a dog1 as an instance of the Dog class, chosen self.name 
# will only reference to this particular object, instance.

# Species, however, is a class attribute of class Dog, 
# and it relates to the whole class, including all of the instances of it.

#W1 D3 T3

# class BankAccount:
    
#     """
#     Represents a simple bank account.

#     Attributes:
#         owner: Account owner's name.
#         balance: Current account balance.
#     """
    
    
#     def __init__(self, owner: str, balance: float = 0.0):
#         """Constructor used to initialize account with owner and optional starting balance."""
#         self.owner = owner
#         self.balance = balance
    
#     def deposit(self, amount: float) -> None:
#         '''
#         Method used to deposit a given amount in the account
#         Only accepts positive amount values
#         '''
        
#         if amount > 0:
#             self.balance += amount
#         else:
#             print(f'Only positive amounts accepted for deposit!')
    
#     def withdraw(self, amount: float) -> bool:
#         '''
#         Method used to withdraw a given amount from the account
#         Only accepts withdraw if:
        
#         1. The withdrawn amount is above 0.
#         2. There is a sufficient balance in the account.
        
#         Returns True if the withdraw is successful, otherwise it returns False.
#         '''
        
#         if amount < 0:
#             print('Cannot withdraw NEGATIVE amounts!')
#             return False
#         elif self.balance < amount:
#             print(f'Cannot withdraw ${amount:.2f} as the current balance is below that amount!')
#             return False
#         else:
#             self.balance -= amount
#             print(f'${amount} withdrawn successfully.')
#             return True
    
#     def get_balance(self) -> float:
#         '''
#         Checks the current balance of the account
#         '''
        
#         return self.balance


# account = BankAccount("Alice", 100.0)
# account.deposit(50.0)
# print(account.get_balance())  # Should print 150.0
# account.withdraw(30.0)
# print(account.get_balance())  # Should print 120.0
# account.withdraw(200.0)       # Should fail (insufficient funds)
# print(account.get_balance())  # Should still be 120.0


#W1 D3 T4 - find the bug

# class TodoList:
#     tasks = []

#     def __init__(self, owner):
#         self.owner = owner

#     def add_task(self, task):
#         self.tasks.append(task)

#     def get_tasks(self):
#         return self.tasks

# alice_todos = TodoList("Alice")
# bob_todos = TodoList("Bob")

# alice_todos.add_task("Buy groceries")
# bob_todos.add_task("Walk dog")

# print(f"Alice's tasks: {alice_todos.get_tasks()}")
# print(f"Bob's tasks: {bob_todos.get_tasks()}")

# Bug: All of the instances - alice and bob todos will share the same list of tasks, 
# as they used class attribute tasks, 
# which is shared across all of the class instances.

#FIX:

# class TodoList:
    
#     def __init__(self, owner: str):
#         self.owner = owner
#         self.tasks = [] #instead of using list as a default argument, we initiate it here

#     def add_task(self, task):
#         self.tasks.append(task)

#     def get_tasks(self):
#         return self.tasks

# alice_todos = TodoList("Alice")
# bob_todos = TodoList("Bob")

# alice_todos.add_task("Buy groceries")
# bob_todos.add_task("Walk dog")

# print(f"Alice's tasks: {alice_todos.get_tasks()}")
# print(f"Bob's tasks: {bob_todos.get_tasks()}")

#W1 D3 T5 - I created algo_backtest/engine/position.py

# from algo_backtest.engine.position import Position

# long_pos = Position('FDAX', 'buy', 25100, 10, 25050, 25350)
# print(long_pos.calculate_pnl(25250.0))  # 1000.0
# print(long_pos.should_close(25090.0))  # True (hit SL)

# short_pos = Position("GBPUSD", 'SELL', entry_price=120.0, quantity=-500, stop_loss=121.0, take_profit=118.0)
# print(short_pos.calculate_pnl(119.0))  # 500.0
# print(short_pos.should_close(117.5))  # True (hit TP)


#W1 D3 T6 - fixes in ago_backtest/data/data_loader - 
#added context manager to load_data() - with open() as f: pd.read_csv(f),
#added missing return statement in ValueError + logic error in validate_data for missing cols

# from algo_backtest.data.data_loader import DataLoader

# loader = DataLoader('ohlc_mock_data.csv')
# data = loader.load_data()
# if data is not None:
#     is_valid = loader.validate_data(data)
#     print(f"Data valid: {is_valid}")  # Should print True


#W1 D3 T7


# What is the output of this code?
#
# class Test:
#     value = 10

#     def __init__(self):
#         self.value = 20

# obj = Test()
# print(obj.value)
# print(Test.value)
# ```

# **Choices:**
# A) `20` then `20`
# B) `10` then `10`
# C) `20` then `10`
# D) `10` then `20`

# **Your answer with explanation:**
#A,
# In the first print we print the attribute value of the object, 
# which is self.value, 20;
# In the second print however we print the class attribute, 
# is shared across all the class instances, and it's 10.

# What happens when you run this code?

# class Person:
#     def __init__(self, name):
#         self.name = name
#         return self

# p = Person("Alice")
# ```

# **Choices:**
# A) Works fine, `p.name` is `"Alice"`
# B) `TypeError: __init__() should return None`
# C) `AttributeError: 'NoneType' object has no attribute 'name'`
# D) `NameError: self is not defined`

# **Your answer with explanation:**
# B, init should return None!


#W1 D3 T8
#Enhance the `OHLCCandle` class from the lesson with new methods.

# class OHLCCandle:
#     """Represents a single OHLC candle."""

#     def __init__(self, timestamp: str, ticker: str, open_price: float,
#                  high: float, low: float, close: float, volume: int) -> None:
#         self.timestamp = timestamp
#         self.ticker = ticker
#         self.open = open_price
#         self.high = high
#         self.low = low
#         self.close = close
#         self.volume = volume

#     def is_bullish(self) -> bool:
#         """Check if candle closed higher than it opened."""
#         return self.close > self.open

#     def get_body_size(self) -> float:
#         """Calculate candle body size."""
#         return abs(self.close - self.open)

#     def get_range(self) -> float:
#         """Calculate candle range (high - low)."""
#         return self.high - self.low
    
#     def is_doji(self, threshold: float = 0.1) -> bool:
#         if abs(self.close - self.open) / (self.high - self.low) < threshold:
#             return True
#         elif self.high - self.low == 0:
#             return True
#         else:
#             return False
#     def get_upper_wick(self) -> float:
#         max_price = max(self.open, self.close)
#         return self.high - max_price
    
#     def get_lower_wick(self) -> float:
#         min_price = min(self.open, self.close)
#         return min_price - self.low
    

# candle = OHLCCandle(
#     timestamp="2024-01-01 09:00:00",
#     ticker="EURUSD",
#     open_price=100.5,
#     high=101.0,
#     low=100.0,
#     close=100.6,
#     volume=5000
# )

# print(f"Is doji? {candle.is_doji()}")  # Should be False (body is significant)
# print(f"Upper wick: {candle.get_upper_wick():.2f}")  # 101.0 - 100.6 = 0.40
# print(f"Lower wick: {candle.get_lower_wick():.2f}")  # 100.5 - 100.0 = 0.50

#W1 D3 Bonus task
#Employee class that assigns unique IDs to each employee using a class attribute counter

# class Employee:
#     """
#     Employee with auto-incrementing ID.

#     Class Attributes:
#         total_employees: Counter for total employees created.

#     Instance Attributes:
#         name: Employee name.
#         employee_id: Unique ID assigned automatically.
#     """

#     total_employees = 0

#     def __init__(self, name: str):
#         Employee.total_employees += 1
#         self.name = name
#         self.employee_id = Employee.total_employees

# emp1 = Employee("Alice")
# emp2 = Employee("Bob")
# emp3 = Employee("Charlie")

# print(emp1.employee_id)  # 1
# print(emp2.employee_id)  # 2
# print(emp3.employee_id)  # 3
# print(Employee.total_employees)  # 3


#W1 D4 T1
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __repr__(self):
#         return f"Product(name={self.name!r}, price={self.price})"

#     def __str__(self):
#         return f"{self.name}: ${self.price:.2f}"

# product = Product("Laptop", 999.99)

# print(str(product)) #`Laptop: $999.99`
# print(repr(product)) #`Product(name = 'Laptop'), price = 999.99`
# print(product)       #`Laptop: $999.99`

#W1 D4 T2
# class Counter:
#     def __init__(self, value):
#         self.value = value

#     def __str__(self):
#         return f"Counter: {self.value}"

# counter = Counter(10)
# result = str(counter)
# print(f"Result: {result}")


#W1 D4 T3 - updates of __repr__ and __str__ in algo_backtest/engine/position.py
# from algo_backtest.engine.position import Position

# pos = Position("EURUSD", "BUY", 1.0850, 10000, stop_loss=1.0800, take_profit=1.0950)
# print(repr(pos))  # Should show Position(ticker='EURUSD', ...)
# print(str(pos))   # Should show BUY 10000 EURUSD @ 1.0850 [SL=1.0800, TP=1.0950]
# print(pos)        # Should use __str__

# pos_no_sl = Position("GBPUSD", "SELL", 1.2500, 5000)
# print(pos_no_sl)  # Should show SELL 5000 GBPUSD @ 1.2500 [No SL, No TP]


#W1 D4 T4 - checking for NaN values in Pandas


# df = pd.DataFrame({
#     'ticker': ['EURUSD', 'GBPUSD', 'USDJPY'],
#     'open': [1.08, 1.25, np.nan],
#     'close': [1.09, np.nan, 110.5],
#     'volume': [1000, 1500, 2000]
# })

# check_nan1 = df.isna().sum().sum() #returns a total sum of NaNs in our DF
# print(check_nan1)

# check_nan2 = df.isna().sum() #returns a nice breakthrough of all columns and the number of NaNs in each
# print(check_nan2)

# check_nan3 = df.isna().any().any() #returns True
# print(check_nan3)

#W1 D4 T5 - Pandas practice

# df = pd.DataFrame({
#     'timestamp': ['2024-01-01 09:00', '2024-01-01 09:01', '2024-01-01 09:02', '2024-01-01 09:03'],
#     'ticker': ['EURUSD', 'EURUSD', 'EURUSD', 'EURUSD'],
#     'open': [1.0800, 1.0820, 1.0850, 1.0830],
#     'high': [1.0850, 1.0870, 1.0900, 1.0880],
#     'low': [1.0790, 1.0810, 1.0840, 1.0820],
#     'close': [1.0820, 1.0850, 1.0830, 1.0850],
#     'volume': [1000, 1500, 2000, 1200]
# })

# # 1. Filter rows where `close > open` (bullish candles)
# # 2. Filter rows where `volume > 1200` AND `close > 1.0840`
# # 3. Get the `high` values (as a Series) where `close > open`
# # 4. Count how many candles are bullish (close > open)

# bullish_candles = df[df['close'] > df['open']]
# filtered_rows = df[(df['volume'] > 1200) & (df['close'] > 1.0840)]
# high_series = pd.Series(df['high'][df['close'] > df['open']])
# bullish_candles_count = len(df[df['close'] > df['open']])
# print(bullish_candles_count)

#W1 D4 T6 - creating Trade Class in algo_backtest/engine/trade.py
# from algo_backtest.engine.trade import Trade

# # Winning BUY trade
# trade1 = Trade(
#     ticker="EURUSD",
#     side="BUY",
#     entry_price=1.0800,
#     exit_price=1.0850,
#     quantity=10000,
#     entry_time="2024-01-01 09:00",
#     exit_time="2024-01-01 09:30",
#     exit_reason="TP"
# )

# print(trade1)
# # Expected: [WIN] BUY 10000 EURUSD: 1.0800 -> 1.0850 (TP) | P&L: $50.00

# # Losing SELL trade
# trade2 = Trade(
#     ticker="GBPUSD",
#     side="SELL",
#     entry_price=1.2500,
#     exit_price=1.2550,
#     quantity=5000,
#     entry_time="2024-01-01 10:00",
#     exit_time="2024-01-01 10:15",
#     exit_reason="SL"
# )

# print(trade2)
# Expected: [LOSS] SELL 5000 GBPUSD: 1.2500 -> 1.2550 (SL) | P&L: $-25.00


#W1 D4 T7

# df = pd.DataFrame({'a': [1, 2, 3]})
# #result = df['a'] > 2 and df['a'] < 5 #ERROR, ValueError - doesn't work like that with Series

# result = df[(df['a'] > 2) & (df['a'] < 5)] #correct application
# print(result)

#W1 D4 T8 - modifying algo_backtest/data/data_loader.py - classmethod

from algo_backtest.engine.trade import Trade

trade1 = Trade("EURUSD", "BUY", 1.08, 1.09, 10000, "2024-01-01 09:00", "2024-01-01 09:30", "TP")
trade2 = Trade("GBPUSD", "SELL", 1.25, 1.26, 5000, "2024-01-01 10:00", "2024-01-01 10:15", "SL")
trade3 = Trade("USDJPY", "BUY", 110.00, 110.50, 2000, "2024-01-01 11:00", "2024-01-01 11:45", "TP")

trades = [trade1, trade2, trade3]
win_rate = Trade.calculate_win_rate(trades)
print(f"Win rate: {win_rate:.1f}%")  # Expected: 66.7%
print(trades)

#W1 D5 T1

# **Answer these short questions to test your Week 1 retention:**

# 1. What's the difference between `import math` and `from math import sqrt`?
# 2. What does `"PCAP"[10:20]` return? (No IndexError!)
# 3. In exception handling, why must specific exceptions come before general ones?
# 4. What's the difference between an instance attribute and a class attribute?
# 5. When does Python call `__repr__` vs `__str__`?
# 6. What operator do you use for multiple conditions in Pandas filtering? (`and`/`or` or `&`/`|`?)

# **Your answers:**

# 1. Two differences - in the first example we import all the relevant functions from math that are set to be imported there by default if we use this general import (this is also the best practice, as we're not occupying the namespace), but to use them we have to call math.module_name; In the second example we only import the sqrt function and we can call it by naming it sqrt. It's not the best practice as we're also occupying the namespace and may cause naming conflicts, especially if our codebase is large and we import a lot of functions like that.
# 2. Empty string
# 3. Because otherwise we would always catch the general exception catch, and it would block the other exception handling cases (so effectively, they would be pointless)
# 4. Instance attribute is tied to a given instance of a class, while a class attribute is shared among all instances of a given class.
# 5. It calls __str__ by default if it's available and if we do print(class_name); __repr__ would be called instead if __str__ is not available. We can also simply explicitly call both methods as in print(repr(class_name)) or print(str(class_name))
# 6. For single elements comparison, we use and/or operators, and for series we use & / | instead, so in this case the answer is `&`/`|`.


#W1 D5 T2- updated algo_backtest/main.py to import data_loader and trade 
# and do a mock backtest of 3 manually added trades

#W1 D5 T3


# class Portfolio:
#     total_portfolios = 0

#     def __init__(self, name):
#         self.name = name
#         Portfolio.total_portfolios += 1

#     def __str__(self):
#         return f"Portfolio: {self.name}"

#     def __repr__(self):
#         return f"Portfolio({self.name!r})"

# p1 = Portfolio("Tech Stocks")
# p2 = Portfolio("Bonds")

# print(p1)
# print(repr(p2))
# print(f"Total: {Portfolio.total_portfolios}")

# portfolios = [p1, p2]
# print(portfolios)

# **Your predictions:**
# - Line 1 (`print(p1)`): `Portfolio: Tech Stocks`
# - Line 2 (`print(repr(p2))`): `Portfolio('Bonds')`
# - Line 3 (`print(f"Total: ...")`): `Total: 2`
# - Line 4 (`print(portfolios)`): `[Portfolio('Tech Stocks'), Portfolio('Bonds')]`

#W1 D5 T4

# from typing import Optional, List
# from algo_backtest.data.data_loader import DataLoader
# from algo_backtest.engine.trade import Trade


# def safe_backtest_runner(filepath: str) -> Optional[List[Trade]]:
#     """
#     Safely run backtest with error handling.

#     Args:
#         filepath: Path to OHLC data CSV.

#     Returns:
#         List of Trade objects if successful, None if any error occurs.

#     Error Handling:
#         - FileNotFoundError: Data file missing
#         - ValueError: Invalid data format
#         - KeyError: Missing required columns
#         - Exception: Catch-all for unexpected errors
#     """

#     try:
        
#         trades = []
#         loader = DataLoader(filepath)
#         data = loader.load_data()
#         x = loader.validate_data(data)
        
#         if x:
#             trade1 = Trade(data.iloc[0]['ticker'],     #ticker
#                            'BUY',                      #side     
#                            data.iloc[15]['open'],      #entry_price
#                            data.iloc[34]['close'],     #exit_price
#                            15000,                      #quantity
#                            data.iloc[15]['timestamp'], #entry_time
#                            data.iloc[35]['timestamp'], #exit_time
#                            '')                         #reason (nie wrzucam nic na razie)
            
            
#             trade2 = Trade(data.iloc[0]['ticker'],     #jw.
#                            'SELL',
#                            data.iloc[18]['open'],
#                            data.iloc[27]['close'],
#                            15000,
#                            data.iloc[18]['timestamp'],
#                            data.iloc[28]['timestamp'],
#                            '')
#             trades = [trade1, trade2]

#     except FileNotFoundError as e:
#         print(f'File not found: {str(e)}')
#         return None

#     except ValueError as e:
#         print(f'Wrong value: {str(e)}')
#         return None

#     except KeyError as e:
#         print(f'Key not found: {str(e)}')
#         return None
    
#     except Exception as e:
#         print(f'Unexpected error: {str(e)}')
#         return None
    
#     else:
#         print('Trades added successfully, returning the list of trades.')
#         return trades

#     finally:
#        print('Operation finished')

# # Test 1: Valid file
# result = safe_backtest_runner('ohlc_mock_data.csv')
# print(f"Valid file: {result is not None}")  # Should be True

# # Test 2: Missing file
# result = safe_backtest_runner('nonexistent.csv')
# print(f"Missing file: {result is None}")  # Should be True


#W1 D5 T5
# data = pd.read_csv('ohlc_mock_data.csv')

# import numpy as np
# # Question 1: What's the average close price for bullish candles only?
# # Your code here
# avg_bullish_close = np.mean([data['close'][data['close'] > data['open']]])
# print(avg_bullish_close)
# # Question 2: Find the candle with the highest volume
# # Return the entire row as a Series
# # Your code here
# highest_vol = np.max([data['volume']])
# highest_vol_candle = data[data['volume'] == highest_vol]
# print(highest_vol_candle)
# # Question 3: Calculate the total volume for candles where close > 100.5
# # Your code here

# total_vol_candles = sum(data['volume'][data['close'] > 100.5])
# print(total_vol_candles)

# # Question 4: Create a new column 'candle_type' with values 'bullish' or 'bearish'
# # based on close vs open
# # Your code here
# for index, row in data.iterrows():
#     row['candle_type'] = 'bullish' if row['close'] > row['open'] else 'bearish'
#     print(row)
# #Here we iterate, creating a copy of each row, so we don't add anything to the original df

# data['candle_type'] = data.apply(lambda row: 'bullish' if row['open'] > row['close'] else 'bearish',
#                                          axis = 1)
# print(data)

# # Question 5: Get all candles where high is in the top 10 highest values
# # Hint: Use .nlargest()
# # Your code here
# top_10_highs = data.nlargest(10, 'high')
# print(top_10_highs)


#W1 D5 T6 - created algo_backtest/engine/position_manager to manage multiple positions

# from algo_backtest.engine.position_manager import PositionManager
# from algo_backtest.engine.position import Position

# manager = PositionManager()

# # Add positions
# pos1 = Position("EURUSD", "BUY", 1.0800, 10000, stop_loss=1.0750, take_profit=1.0900)
# pos2 = Position("GBPUSD", "SELL", 1.2500, 5000, stop_loss=1.2550, take_profit=1.2450)

# manager.add_position(pos1)
# manager.add_position(pos2)

# print(manager)  # PositionManager: 2 open positions

# # Check P&L at current price
# current_price = 1.0850
# total_pnl = manager.get_total_pnl(current_price)
# print(total_pnl)

# # Check for triggered positions
# closed = manager.close_triggered_positions(1.0900)
# print(f"Closed {len(closed)} positions")
# print(manager)  # Should show 1 open position now

#W1 D5 T8 - Bug hunter 

#I'm leaving the original version in its oriignal form 

# """Broken trading simulator - find all bugs!"""

# class trade:
#     def __init__(self, Ticker, side, entry, exit, qty):
#         self.ticker = Ticker
#         self.Side = side
#         self.entry = entry
#         self.exit = exit
#         self.qty = qty

#     def __str__(self):
#         print(f"{self.Side} {self.ticker}")

#     def calc_pnl(self):
#         if self.Side == "BUY":
#             return (self.exit - self.entry) * self.qty
#         else:
#             return (self.entry - self.exit) * self.qty

# trades = []

# import pandas as pd
# df = pd.read_csv("data.csv")

# for i in range(len(df)):
#     row = df.iloc[i]
#     t = trade(row['ticker'], 'BUY', row['open'], row['close'], 1000)
#     trades.append(t)

# total = 0
# for t in trades:
#     total = total + t.calc_pnl()

# print(f"Total PNL: {total}")

#**List of all issues I found:**

# 1. uncapitalized class name - trade
# 2. capitalized parameter name - Ticker
# 3. capitalized self.Side 
# 4. it would be nice to also add .upper to side to account for potential case issues
# 5. weird __str__ representation with unclear information (missing data) AND an error - it uses print instead of return
# 6. wrong place to import pandas module
# 7. general lack of exception handling
# 8. wrong total_pnl calculation

#Fixed version:

# '''
# Fixed trade simulator
# '''

# import pandas as pd

# class Trade:
#     def __init__(self, ticker, side, entry, exit, qty):
#         '''init constructor for the Trade class'''
#         self.ticker = ticker
#         self.side = side.upper()
#         self.entry = entry
#         self.exit = exit
#         self.qty = qty
        
#     def __str__(self):
#         '''A clear representation of a class if anybody decides to use print(Trade)'''
#         return f"{self.side} {self.qty} {self.ticker} @ {self.entry}, EXIT @ {self.exit}"
    
#     def calc_pnl(self):
#         '''Method used to calculate profit of a given position
        
#         Returns the pnl value, depending on the side (buy or sell)
#         '''
#         if self.qty < 0 or self.entry < 0 or self.exit < 0:
#             print(f'Wrong value, it should be above 0!')
#             return None
        
#         if self.side == "BUY":
#             return (self.exit - self.entry) * self.qty
#         else:
#             return (self.entry - self.exit) * self.qty
    

# trades = []
# filepath = 'ohlc_mock_data.csv'

# df = pd.read_csv(filepath)

# for i in range(len(df)):
#     row = df.iloc[i]
#     t = Trade(row['ticker'], 'BUY', row['open'], row['close'], 1000)
#     trades.append(t)

# total = 0
# for t in trades:
#     total += t.calc_pnl()

# print(f"Total PNL: {total}")


