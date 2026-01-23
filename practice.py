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

# from algo_backtest.engine.trade import Trade

# trade1 = Trade("EURUSD", "BUY", 1.08, 1.09, 10000, "2024-01-01 09:00", "2024-01-01 09:30", "TP")
# trade2 = Trade("GBPUSD", "SELL", 1.25, 1.26, 5000, "2024-01-01 10:00", "2024-01-01 10:15", "SL")
# trade3 = Trade("USDJPY", "BUY", 110.00, 110.50, 2000, "2024-01-01 11:00", "2024-01-01 11:45", "TP")

# trades = [trade1, trade2, trade3]
# win_rate = Trade.calculate_win_rate(trades)
# print(f"Win rate: {win_rate:.1f}%")  # Expected: 66.7%
# print(trades)

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


# class Test:
#     items = []

#Start 11:32
#W2 D1 T1

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Some sound"

# class Dog(Animal):
#     def speak(self):
#         return "Woof"

# d = Dog("Buddy")
# print(d.name)
# print(d.speak())


#W2 D1 T2 - a child class SavingsAccount adding to the class we created last week


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
    
    
    
# class SavingsAccount(BankAccount):
        
#     '''A child class of BankAccount with added interest_rate
#     and add_interest method that allows for interest compounding'''
    
#     def __init__(self, owner: str, balance: float, interest_rate: float):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate
#         self.balance = balance
    
#     def __str__(self):
#         return f'SavingsAccount(balance = ${super().get_balance()}, rate = {self.interest_rate}%)'
        
#     def add_interest(self):
#         '''Compounds the interest based on set interest_rate'''
#         self.balance += self.interest_rate * self.balance
#         return self.balance
        
        
# savings = SavingsAccount(owner="Alice", balance=1000.0, interest_rate=0.05)
# print(savings)  # SavingsAccount(balance=$1000.00, rate=5.0%)
# savings.add_interest()
# print(savings.get_balance())  # 1050.0
# savings.add_interest()
# print(savings.get_balance())


#W2 D1 T3

# class Strategy:
#     '''A strategy class used to generate trades based on set signals + child classes with specific strategies'''
#     def __init__(self, name: str):
#         self.name = name
        
#     def generate_signal(self, price: float) -> str:
#         return 'HOLD'
    
# class LevelCrossStrategy(Strategy):
#     def __init__(self, level: float):
#         super().__init__('Level Cross')
#         self.level = level
        
#     def generate_signal(self, price: float) -> str:
        
#         if price > self.level:
#             return 'BUY'
#         elif price < self.level:
#             return 'SELL'
#         else:
#             return 'HOLD'
        
# strategy = LevelCrossStrategy(100.0)
# print(strategy.generate_signal(105))  # "BUY"
# print(strategy.generate_signal(95))   # "SELL"
# print(strategy.generate_signal(100))  # "HOLD"


#W2 D1 T4 - bug hunting

#original
# class Vehicle:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year

# class Car(Vehicle):
#     def __init__(self, brand, year, doors):
#         self.doors = doors

# car = Car("Toyota", 2023, 4)
# print(car.brand)  # What happens here?

#Bug - brand, year in child class should be plugged from the parent class with super()
#Fix:

# class Vehicle:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year

# class Car(Vehicle):
#     def __init__(self, brand, year, doors):
#         super().__init__(brand, year)
#         self.doors = doors
        

# car = Car("Toyota", 2023, 4)
# print(car.brand)


#W2 D1 T5

# class Animal:
#     pass

# class Mammal(Animal):
#     pass

# class Dog(Mammal):
#     pass

# dog = Dog()

# print(isinstance(dog, Dog))           # A  -> True
# print(isinstance(dog, Mammal))        # B -> True
# print(isinstance(dog, Animal))        # C -> True
# print(isinstance(dog, object))        # D (TRICKY!) -> True

# print(issubclass(Dog, Mammal))        # E -> True
# print(issubclass(Dog, Animal))        # F -> False
# print(issubclass(Dog, Dog))           # G (TRICKY!) -> True
# print(issubclass(Animal, Dog))        # H -> False


#W2 D1 T6 - abstract base class - `algo_backtest/strategies/base_strategy.py`


# '''Abstract Method Class - base strategy'''

# from abc import ABC, abstractmethod

# class BaseStrategy(ABC):
#     '''A class with abstract method used to generate trading signal'''
#     def __init__(self, name: str):
#         self.name = name
        
#     @abstractmethod
#     def generate_signal(self, price: float) -> str:
#         pass
    
#     def get_name(self) -> str:
#         '''inherited method to fetch a given strategy name'''
#         return self.name


#import also added to strategies/init.py
# from .base_strategy import BaseStrategy

# __all__ = ['BaseStrategy']


#W1 D1 T8 - code review/issue detection

#original:
# class strategy:
#     def init(self, name):
#         name = name

#     def signal(self, price):
#         return HOLD

# class MovingAverageStrategy(strategy):
#     def init(self, ma_period):
#         self.ma_period = ma_period

#     def signal(self, price):
#         result = super().signal(price)
#         if price > 100:
#             return "buy"
#         return result

# strat = MovingAverageStrategy(20)
# print(strat.name)


#ISSUES:\
# 1. Uncapitalized class name
# 2. Lack of floor symbols __ next to init
# 3. name in init has local scope instead of being self.name
# 4. HOLD in signal in parent class will trigger a TypeError, as it's not defined in anyway, and it's not a string either
# 5. lack of super() to get the parent class parameters in init
# 6. with current logic in signal in both classes, we only get to have a 'buy' or 'hold' signal (from the parent class), and no sell at all
# 7. the class is called without a name
# 8. Lack of type hints

#fixed version:

# class Strategy:
#     '''a base strategy for creating strategies'''
#     def __init__(self, name: str):
#         self.name = name

#     def signal(self):
#         pass

# class MovingAverageStrategy(Strategy):
#     '''a child-class of strategy class with its separate signal generating logic'''
#     def __init__(self, name: str, ma_period: float):
#         super().__init__(name)
#         self.ma_period = ma_period

#     '''Signal class used to generate signals for the moving average strategy (mock, as you can see :))'''
#     def signal(self, price: float):
#         if price > 100:
#             return 'Buy'
#         elif price < 100:
#             return 'Hold'
        
# strat = MovingAverageStrategy('Strategy1', 20)
# print(strat.name)

#finish 12:38

#W2 D2 T2 - creating a mock strategy inherited from BaseStrategy (w/ abstract method for generate_signal in BaseStrategy)

# from .base_strategy import BaseStrategy

# class LevelCrossStrategy(BaseStrategy):
#     '''
#     A strategy based on crossing certain levels
#     '''
    
#     def __init__(self, level: float):
#         '''Initializing the class with defined level'''
#         super().__init__('Level Cross Strategy')
#         self.level = level
        
    
#     def generate_signal(self, price: float) -> str:
#         '''
#         Method used to generate signal based on a price you pass - this is a mock method mainly used to practice.
        
#         It's an instance of a method that inherits abstract method from BaseStrategy (so it's mandatory).
#         Signals for real strategies most likely will be more robust.
#         '''
#         if price > self.level:
#             return 'BUY'
#         elif price < self.level:
#             return 'SELL'
#         elif price == self.level:
#             return 'HOLD'
    
    
#     def get_level(self) -> float:
#         '''Method used to return the set level'''
#         return self.level

#W2 D2 T3 - Another mock strategy built with BaseStrategy inheritance

# from .base_strategy import BaseStrategy
# from typing import List

# class MovingAverageStrategy(BaseStrategy):
    
#     def __init__(self, ma_period: int):
#         '''Initialization of the class, inheriting the base init from the BaseStrategy and extending it'''
#         super().__init__(f'MovingAverage Strategy - ma {ma_period}')
#         self.ma_period = ma_period
#         self.price_history: List[float] = []
    
#     def add_price(self, price: float):
#         '''Method used to add a price to the self.price_history list'''
#         self.price_history.append(price)
#         if len(self.price_history) > self.ma_period:
#             self.price_history.remove([0])
            
#     def generate_signal(self, price: float) -> str:
#         '''Method used to check whether the list has enough entries to be able to calculate the MA properly'''
#         if len(self.price_history) < self.ma_period:
#             print(f'Not enough data entries to properly count ma {self.ma_period}. Currently we only have {len(self.price_history)} entries.')
#             return 'HOLD'
        
#         else:
#             ma_value = sum(self.price_history) / self.ma_period
#             if price > ma_value:
#                 return 'BUY'
#             else:
#                 return 'SELL'        


#W2 D2 T4 - testing the strategies with a function

# from algo_backtest.strategies import MovingAverageStrategy, LevelCrossStrategy

# '''Test script used to check if our strategies work properly'''

# def test_strategy(strategy, prices: list[float]) -> None:
#     """Test a strategy with a list of prices.

#     Args:
#         strategy: Any strategy that has generate_signal method
#         prices: List of prices to test
#     """
#     print(f"\nTesting: {strategy.get_name()}")
#     for price in prices:
#         signal = strategy.generate_signal(price)
#         print(f"  Price {price}: {signal}")


# strat1 = MovingAverageStrategy(5)
# strat2 = LevelCrossStrategy(100.5)

# strat1.add_price(430)
# strat1.add_price(230)
# strat1.add_price(450)
# strat1.add_price(470)
# strat1.add_price(490)
# strat1.add_price(530)
# test_strategy(strat1, [430, 450, 520, 550, 570, 460, 430, 320])
# test_strategy(strat2, [120, 105, 90, 20])


#W2 D2 T5


# from algo_backtest.strategies import BaseStrategy, LevelCrossStrategy, MovingAverageStrategy

# def analyze_strategy(strategy: BaseStrategy) -> str:
#     """Analyze a strategy and return description based on its type.

#     Args:
#         strategy: Any strategy instance

#     Returns:
#         Description string
#     """
    
#     if isinstance(strategy, LevelCrossStrategy):
#         return f"{strategy.name} with level={strategy.level}"
#     elif isinstance(strategy, MovingAverageStrategy):
#         return f"{strategy.name} with period={strategy.ma_period}"
#     else:
#         return strategy.name

# # Test cases
# strat1 = LevelCrossStrategy(100.0)
# strat2 = MovingAverageStrategy(5)

# print(analyze_strategy(strat1))
# # Expected: "Level Cross Strategy with level=100.0"

# print(analyze_strategy(strat2))


#W2 D2 T8 - Bug bounty

#THE BUGGY ORIGINAL:
# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

#     def start(self):
#         return "Starting vehicle"

# class Car(Vehicle):
#     def start(self):
#         return f"Starting {self.brand} car"

# class Motorcycle(Vehicle):
#     pass

# def start_all_vehicles(vehicles):
#     for v in vehicles:
#         print(v.start())

# vehicles = [
#     Car("Toyota"),
#     Motorcycle("Harley"),
#     Vehicle("Generic")
# ]

# start_all_vehicles(vehicles)


#issues:
#1. Lack of docstrings/typehints
#2. Car has a missing init and it doesn't use super() - perhaps it's okay as the code still works, but it just looks weird to me
#3. The Motorcycle class is empty, so what's the point of even having it there when it does nothing different compared to the parent class?
#4. As a consequence of the above, the start_all_vehicles will not be able to work properly and list all the vehicles.

#fix

# class Vehicle:
#     '''Parent class used to start a vehicle'''
#     def __init__(self, brand):
#         self.brand = brand

#     def start(self):
#         return "Starting vehicle"

# class Car(Vehicle):
#     '''A polimorphic variant of a Vehicle that is designed specifically for cars'''
#     def __init__(self, brand: str, doors: int):
#         super().__init__(brand)
#         self.doors = doors
    
#     def start(self):
#         return f"Starting {self.brand} car with {self.doors} doors"

# class Motorcycle(Vehicle):
#     '''A polimorphic variant of a Vehicle extended specifically for motorcycles'''
#     def __init__(self, brand, horsepower: int):
#         super().__init__(brand)
#         self.horsepower = horsepower
        
#     def start(self):
#         return f'Starting a {self.brand} motorcycle with {self.horsepower} horsepower'

# def start_all_vehicles(vehicles):
#     for v in vehicles:
#         print(v.start())

# vehicles = [
#     Car("Toyota", 4),
#     Motorcycle("Harley", 50),
#     Vehicle("Generic")
# ]

# start_all_vehicles(vehicles)


#W2 D3 T1 -> MRO predictions

# class Animal:
#     def speak(self):
#         return "generic sound"

# class Mammal(Animal):
#     def speak(self):
#         return "mammal sound"

# class Bird(Animal):
#     def speak(self):
#         return "chirp"

# class Bat(Mammal, Bird):
#     pass

# class Platypus(Bird, Mammal):
#     pass

# bat = Bat()
# platypus = Platypus()

# print(bat.speak()) # -> 'mammal sound'
# print(platypus.speak()) # -> 'chirp'
# print(Bat.__mro__) # Mammal -> Bird -> Animal

#W2 D3 T4

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

#W2 D3 T5 - error prediction


# Case A -> Error, B is inherited from A, and it doesn't make sense to later make A inherited from B 
# class A:
#     pass

# class B(A):
#     pass

# class C(A, B):
#     pass

# # Case B -> No error, everything's fine here and we kind of 'appoint' the inheritance structure in Z class
# class X:
#     pass

# class Y:
#     pass

# class Z(X, Y):
#     pass

# # Case C -> No error, It's a proper structure of inheritance -> It doesn't change much, but it works.
# class P:
#     pass

# class Q(P):
#     pass

# class R(Q):
#     pass

# class S(R, Q):
#     pass


#W2 D3 T8 - # Identifying issues

# class Database:
#     def __init__(self, connection_string):
#         self.connection_string = connection_string

#     def connect(self):
#         return f"Connected to {self.connection_string}"

#     def query(self, sql):
#         return f"Executing: {sql}"

# class UserManager(Database):  # IS-A relationship
#     def __init__(self, connection_string):
#         super().__init__(connection_string)

#     def get_user(self, user_id):
#         return self.query(f"SELECT * FROM users WHERE id={user_id}")

# class ProductManager(Database):  # IS-A relationship
#     def __init__(self, connection_string):
#         super().__init__(connection_string)

#     def get_product(self, product_id):
#         return self.query(f"SELECT * FROM products WHERE id={product_id}")
#
#Issues:
#1. UserManager shouldn't be a subclass of Database - it could use Database method's instead (connect + query), but it's not an extended Database version, but rather it uses 2 methods from the Database.
#2. Same for ProductManager, there's no need to inherit Database class, but rather simply use the query method.
#3. And as for both - for these two subclasses, we could simply write two extra methods to the Database method and it would be much more nice and neat, if it's only about changing the product_id or user_id. It's just weird to invent a new class for that.


#Option 1 - IMHO very clear and not overengineered
# class Database:
#     def __init__(self, connection_string):
#         self.connection_string = connection_string

#     def connect(self):
#         return f"Connected to {self.connection_string}"

#     def query(self, sql):
#         return f"Executing: {sql}"

#     def get_user(self, user_id):
#         return (f"SELECT * FROM users WHERE id={user_id}")
    
#     def get_product(self, product_id):
#         return (f"SELECT * FROM products WHERE id={product_id}")


# #Option 2 - A bit more tricky but with perhaps clearer structure if we're planning to extend the new classes much further

# class Database:
#     def __init__(self, connection_string):
#         self.connection_string = connection_string

#     def connect(self):
#         return f"Connected to {self.connection_string}"

#     def query(self, sql):
#         return f"Executing: {sql}"

# class UserManager():  # IS-A relationship
#     def __init__(self, connection_string):
#         self.connection = Database(connection_string)

#     def get_user(self, user_id):
#         return self.connection.query(f"SELECT * FROM users WHERE id={user_id}")

# class ProductManager():  # IS-A relationship
#     def __init__(self, connection_string):
#         self.connection = Database(connection_string)

#     def get_product(self, product_id):
#         return self.connection.query(f"SELECT * FROM products WHERE id={product_id}")


#W2 D4 T1
# def process_data(value):
#     try:
#         result = 10 / value
#         data = [1, 2, 3]
#         print(data[value])
#     except ZeroDivisionError:
#         return "Zero error"
#     except IndexError:
#         return "Index error"
#     except Exception as e:
#         return f"Other: {e}"
#     else:
#         return "Success"
#     finally:
#         print("Cleanup")

# print(process_data(0))
# print(process_data(5))
# print(process_data(2))


# Output prediction:
#Zero error -> Cleanup
#Index error -> Cleanup
#Success -> Cleanup

# The exception order is arranged well, from specific to general.
# The else block only executes if we don't get any errors, and the finally block always executes.

#W2 D4 T2 - classmethod in position.py for calculating position size

#     @classmethod
#     def calculate_position_size(self,
#                                 account_balance: float,
#                                 position_type: str,
#                                 risk_percent: float, 
#                                 entry_price: float, 
#                                 stop_loss_price: float) -> float:
#         '''
#         A class method used to calculate the position size based on a set risk %,
#         with given position type and entry + stop loss
        
#         For now it uses a stop loss price - at some point I might decide to use distance instead - depends on our needs
#         '''
#         try:
#             usd_risk = account_balance * (risk_percent / 100)
            
#             if position_type.upper() == 'BUY':
#                 distance = abs(entry_price - stop_loss_price)
#             else:
#                 distance = abs(entry_price + stop_loss_price)
            
#             if distance != 0:
#                 position_size = usd_risk / distance
#                 return position_size
#             else:
#                 print('The stop loss is set at the entry price, returning 0')
#                 return 0
            
#         except Exception as e:
#             print(f'Unexpected error: {str(e)}')


# from algo_backtest.engine.position_manager import Position

# size = Position.calculate_position_size(10000, 'buy', 0.5, 50.0, 48.0)
# print(size)

#W4 D4 T3 - Output prediction - list comprehensions review

# prices = [100, 105, 98, 102, 110, 95]
# # A
# result_a = [p for p in prices if p > 100]
# # B
# result_b = [p * 2 if p > 100 else p for p in prices]
# # C
# result_c = [p for p in prices if p > 100 if p < 110]

# print(result_a) #-> [105, 102, 110] 
# print(result_b) #-> [100, 210, 98, 204, 220, 95]
# print(result_c) #-> [105, 102]

#W4 D4 T5 - bug fix

# def add_trade(trade, portfolio=[]): #This is the issue - mutable default parameter
#     portfolio.append(trade)
#     return portfolio

# result1 = add_trade("AAPL")
# result2 = add_trade("GOOGL")
# result3 = add_trade("MSFT", [])

# print(result1) 'AAPL'
# print(result2) 'AAPL, GOOGL'
# print(result3) 'MSFT'

#FIX:

# def add_trade(trade, portfolio = None): #This is the issue - mutable default parameter
    
#     if portfolio is None:
#         portfolio = []
#     portfolio.append(trade)
#     return portfolio

# result1 = add_trade("AAPL")
# result2 = add_trade("GOOGL")
# result3 = add_trade("MSFT", [])

# print(result1) #'AAPL'
# print(result2) #'AAPL, GOOGL'
# print(result3) #'MSFT'


#W2 D4 T8 - Code Review / Code Fix

# class RiskCalculator:
#     def __init__(self, account_balance):
#         self.account_balance = account_balance

#     def calculate_position_size(self, risk_percent, entry, stop_loss):
#         risk_dollars = self.account_balance * risk_percent  # Bug 1
#         distance = entry - stop_loss  # Bug 2
#         position_size = risk_dollars / distance  # Bug 3
#         return position_size

#     def get_risk_amount(risk_percent):  # Bug 4
#         return self.account_balance * (risk_percent / 100)

# # Test
# calc = RiskCalculator(10000)
# size = calc.calculate_position_size(1, 50, 48)  # Should be 50 shares
# print(size)

# 1. No type hints/ docstrings
# 2. Lack of self in get_risk_amount method
# 3. That really depends on how we ask and present our data, but risk_percent and multiplying it by our acc balance like that might be tricky.
#If somebody gives the percent value like 5, we'd get our balance by 5 instead of 5% of our balance. But this depends, as we could also state percents as 0.05.
# 4. I've chosen more descriptive variants for entry and stop_loss



# class RiskCalculator:
#     '''Class used to calculate risk - both position size and the risk amount'''
    
    
    
    
#     def __init__(self, account_balance: float):
#         self.account_balance = account_balance
        
#     def calculate_position_size(self, 
#                                 risk_percent: float, 
#                                 entry_price: float, 
#                                 stop_loss_price: float) -> float:
        
#         '''Method used to calculate position size - check args, as this is IMPORTANT:
        
#         risk_percent - GIVE THE ACTUAL PERCENT VALUE here (e.g. 0.5 for 0.5%, 5 for 5%, 20 for 20%)
#         entry - provide the entry price e.g. 2053.43
#         stop_loss_price - as above,

        
#         '''
        
#         risk_dollars = self.account_balance * (risk_percent / 100)
#         distance = abs(entry_price - stop_loss_price)  #More descriptive variant + abs for both BUY/SELL
#         position_size = risk_dollars / distance  #This should be correct now if we assume that above is correct
#         return position_size

#     def get_risk_amount(self, risk_percent):
#         '''Get the risk amount per position'''
#         return self.account_balance * (risk_percent / 100)

# # Test
# calc = RiskCalculator(10000)
# size = calc.calculate_position_size(1, 50, 48)  # Should be 50 shares
# print(size)

#W2 D5 T2 - Output prediction

# class Vehicle:
#     wheels = 4

#     def __init__(self, brand):
#         self.brand = brand

#     def describe(self):
#         return f"{self.brand} with {self.wheels} wheels"

# class Motorcycle(Vehicle):
#     wheels = 2

# class Car(Vehicle):
#     def __init__(self, brand, doors):
#         super().__init__(brand)
#         self.doors = doors

#     def describe(self):
#         return f"{super().describe()}, {self.doors} doors"

# # What prints?
# m = Motorcycle("Honda")
# c = Car("Toyota", 4)

# print(m.describe()) #-> Honda with 2 wheels
# print(c.describe()) #-> Toyota with 4 wheels, 4 doors
# print(m.wheels, c.wheels) #-> 2 4


#W2 D5 T3 - Predict the output
# def risky_operation(x):
#     try:
#         if x == 0:
#             raise ValueError("Zero not allowed")
#         result = 10 / x
#     except ValueError as e:
#         print(f"Caught: {e}")
#         return -1
#     except ZeroDivisionError:
#         print("Division by zero!")
#         return -2
#     else:
#         print(f"Success: {result}")
#         return result
#     finally:
#         print("Cleanup done")

# print(risky_operation(0))
# print("---")
# print(risky_operation(2))

# #1 - Caught: Zero not allowed. Cleanup done. -1
# #2 - Success: 5.0 Cleanup done. 5.0


#W2 D5 T4 - Output prediction

# class Counter:
#     count = 0

#     def __init__(self):
#         Counter.count += 1

#     @classmethod
#     def get_count(cls):
#         return cls.count

#     @staticmethod
#     def validate(value):
#         return value > 0

# print(Counter.get_count()) #0
# c1 = Counter() #2
# c2 = Counter() #2
# print(Counter.get_count()) #2
# print(c1.get_count()) #5
# print(Counter.validate(-5))#False
# print(c2.validate(10)) #True

'''

When we create actual class objects, the count value is increased with init.
As classmethod doesn't include actually creating any object, it doesn't use the init - it doesn't increase the count value, but it's obviously able to fetch it, and since it's a shared class attribute, we get the last value.

When creating a new class object (as c1, c2), we increase that count value by 1, as it's a shared class attribute.

'''

#W2 D5 T5

# from algo_backtest.engine.position import Position

# position_size = Position.calculate_position_size(10000, 2, 100, 95)
# print(position_size)
# position = Position('DAX', 'Buy', 25100, position_size, 24900, 25300)
# print(str(position))


#W2 D5 T7 - Bug fix

# class Strategy:
#     active_count = 0

#     def __init__(self, name):
#         self.name = name
#         active_count += 1  # Bug 1

#     @classmethod
#     def get_active(self):  # Bug 2
#         return cls.active_count

#     @staticmethod
#     def validate_name(name):
#         return len(name) > 0 and self.name.isalpha()  # Bug 3

#     def describe():  # Bug 4
#         return f"Strategy: {self.name}"
    
# #1. We will not increase active_count as it's in local scope
# #2 Class method CANNOT use self, it uses cls instead
# #3 static_method DOES NOT have access to class attributes, it's a self standing function only with its own attributes
# #4 Lack of self in describe method
# #5 - lack of docs/typehints - not a bug, but a bad practice

#FIXED VERSION BELOW:

# class Strategy:
#     '''Mock docstring'''
#     active_count = 0

#     def __init__(self, name: str):
#         self.name = name
#         Strategy.active_count += 1

#     @classmethod
#     def get_active(cls) -> int:  
#         '''Returns count of active strategies'''
#         return cls.active_count

#     @staticmethod
#     def validate_name(name) -> bool:
#         '''A standalone method/function that allows to validate any name'''
#         return len(name) > 0 and name.isalpha()

#     def describe(self) -> str:  
#         '''Returns the name of a given strategy'''
#         return f"Strategy: {self.name}"



#W3 D1 T2 - Output prediction

# class Secret:
#     def __init__(self):
#         self._protected = "visible"
#         self.__private = "hidden"

#     def reveal(self):
#         return self.__private

# s = Secret()
# print(s._protected) #visible
# print(s.reveal()) #hidden
# print(hasattr(s, '__private')) #False
# print(hasattr(s, '_Secret__private')) #True

#W3 D1 T3 - Output prediction

# class Temperature:
#     def __init__(self, celsius):
#         self._celsius = celsius

#     @property
#     def celsius(self):
#         return self._celsius

#     @property
#     def fahrenheit(self):
#         return self._celsius * 9/5 + 32

# t = Temperature(25) 
# print(t.celsius) #25
# print(t.fahrenheit) # 77
# t.celsius = 30  # What happens here? Error - there's no such attribute as 'celsius' in the Temperature class.

#W3 D1 T4 - Code impl

# Create a `Price` class that:
# 1. Has a protected `_value` attribute
# 2. Has a `value` property (getter)
# 3. Has a `value` setter that validates: value must be >= 0
# 4. Raises `ValueError` with message "Price cannot be negative" if validation fails

# class Price:
#     '''A mock docstring of a mock class used for practice'''
    
#     def __init__(self, value: float):
#         self._value = value
    
#     @property
#     def value(self) -> float:
#         return self._value
    
#     @value.setter
#     def value(self, value: float) -> None:
#         if value >= 0:
#             self._value = value
#         else:
#             raise ValueError('Price cannot be negative!')


# # Test it:
# p = Price(100)
# print(p.value)      # Should print: 100
# p.value = 150       # Should work
# print(p.value)      # Should print: 150
# p.value = -10       # Should raise ValueError
#works.



#W3 D1 T5 -  modifying Trade class in algo_backtest/engine/trade.py - protected attributes, pnl as a property, is_winner property

# In practice.py - paste your test code and output
# from algo_backtest.engine.trade import Trade

# # Create a winning BUY trade
# t1 = Trade("AAPL", "buy", 100.0, 110.0, 10)
# print(t1)           # Should show: BUY AAPL: +100.00 (WIN)
# print(t1.pnl)       # Should show: 100.0
# print(t1.is_winner) # Should show: True

# # Create a losing SELL trade
# t2 = Trade("TSLA", "sell", 200.0, 220.0, 5)
# print(t2)           # Should show: SELL TSLA: -100.00 (LOSS)


#Updated Trade class pasted here as well:

# """Trade management for completed positions."""
# from typing import Optional

# class Trade:
#     '''
#     Represents a completed trade
    
#     Attributes:
#         ticker: Trading symbol.
#         side: 'BUY' or 'SELL'.
#         entry_price: Entry price.
#         exit_price: Exit price.
#         quantity: Number of units.
#         entry_time: Entry timestamp (string or datetime).
#         exit_time: Exit timestamp (string or datetime).
#         pnl: Profit/Loss (calculated automatically).
#         exit_reason: 'SL', 'TP', or 'MANUAL'.
#     '''
    
#     def __init__(self,
#                  ticker: str,
#                  side: str,
#                  entry_price: float,
#                  exit_price: float,
#                  quantity: float,
#                  entry_time: Optional[str] = None,
#                  exit_time: Optional[str] = None,
#                  exit_reason: Optional[str] = None
#                  ):
        
#         """Initialize a completed trade and calculate P&L."""
        
#         self._ticker = ticker
#         self._side = side.upper()
#         self._entry_price = entry_price
#         self._exit_price = exit_price
#         self._quantity = quantity
#         self._entry_time = entry_time
#         self._exit_time = exit_time
        
#         if exit_reason is not None:
#             self._exit_reason = exit_reason.upper()
#         else:
#             self._exit_reason = ''

#         #Properties - is_winner + pnl
#         self.__pnl: Optional[float] = None
#         self.__is_winner: Optional[bool] = None
        
#     def __str__(self):
#         """
#         User-friendly representation.

#         Format: [WIN/LOSS] SIDE QUANTITY TICKER: ENTRY -> EXIT (REASON) | P&L: $X.XX
#         Example: [WIN] BUY 10000 EURUSD: 1.0800 -> 1.0850 (TP) | P&L: $500.00
#         """
        
#         if self.is_winner == True:
#             result = '[WIN]'
#         else:
#             result = '[LOSS]'
        
#         return (f'''{result} {self._side} {self._quantity} {self._ticker}: 
#                 {self._entry_price} -> {self._exit_price} {self._exit_reason}
#                 | P&L: ${self.pnl:.2f}''')
    
#     def __repr__(self):
        
        
#         return (f'Trade(ticker = {self._ticker!r}, side = {self._side!r},'
#                 f'entry_price = {self._entry_price}, exit_price = {self._exit_price}'
#                 f'quantity = {self._quantity}, pnl = {self.pnl:.2f}, exit_reason = {self._exit_reason!r}'
#         )
    
    
#     @property
#     def pnl(self) -> float:
#         '''
#         Calculate profit/loss based on side.

#         Returns:
#             P&L in currency units.
#         '''
#         if self._side != 'BUY' and self._side != 'SELL':
#             print('Incorrect side, it should be either BUY or SELL (case insensitive)')
#             return None
#         elif self._exit_price < 0 or self._entry_price < 0:
#             print('Incorrect exit price or entry price, it should be above 0!')
#             return None
        
#         if self._side == 'BUY':
#             self.__pnl = (self._exit_price - self._entry_price) * self._quantity
#             return self.__pnl
#         elif self._side == 'SELL':
#             self.__pnl = (self._entry_price - self._exit_price) * self._quantity
#             return self.__pnl
        
#     @property 
#     def is_winner(self) -> bool:
#         """A property created to check if trade was profitable."""
#         if self.pnl > 0:
#             self.__is_winner = True
#         else:
#             self.__is_winner = False
            
#         return self.__is_winner
        
    
#     @classmethod
#     def calculate_win_rate(cls, trades: list['Trade']) -> float:
#         """
#         Calculate win rate from list of trades.

#         Args:
#             trades: List of Trade objects.

#         Returns:
#             Win rate as percentage (0-100).
#             Returns 0 if no trades.
#         """

#         if trades is not None:
#             trades_profits = [trade.pnl() for trade in trades]
#             winners = [profit for profit in trades_profits if profit > 0]
#             print(trades_profits)
#             return (len(winners) / len(trades_profits)) * 100
            
#         else:
#             return 0


#W3 D1 T6 - Property output prediction

# class Counter:
#     def __init__(self):
#         self._count = 0

#     @property
#     def count(self):
#         self._count += 1
#         return self._count

# c = Counter()
# print(c.count) #1
# print(c.count) #2
# print(c.count) #3


#W3 D1 T8 - it was supposed to be just a script to integrate Position with Trade,
#As a result of a natural flow I quickly moved to an idea of creating another class

# from typing import Optional
# from algo_backtest.engine.position import Position
# from algo_backtest.engine.trade import Trade


# class PositionTrade:
#     '''My practice class which integrates both Position and Trade classes
    
#        Mainly done for practice purposes for now, but we will see.
#     '''
    
#     def __init__(self,
#     acc_size: float,
#     risk_percent: float,
#     entry_price: float,
#     asset_name: str,
#     position_side: str,
#     sl: Optional[float] = None,
#     tp: Optional[float] = None,
#     ):
#         self.acc_size = acc_size
#         self.risk_percent = risk_percent
#         self.entry_price = entry_price
#         self.asset_name = asset_name
#         self.position_side = position_side
        
#         self.sl = sl
#         self.tp = tp
        
#         self.position = None
#         self.trade = None
        

#     def create_trade(self):
        
#         '''A method used to integrate the Position class and create an instance of an active position'''

#         try:
#             self.position_size = Position.calculate_position_size(self.acc_size, self.risk_percent, self.entry_price, self.sl)
#             self.position = Position(self.asset_name, self.position_side, self.entry_price, self.position_size, self.sl, self.tp)
            
#         except Exception as e:
#             print(f'Unexpected error: {str(e)}')
            
#     def check_trade(self, price):
        
#         '''A method used to check if the position should close and IF IT SHOULD, we integrate the Trade class'''
        
#         if self.position is not None and price > 0:
#             check, reason = self.position.should_close(price)
#             if check is True:
#                 print('Time to close the position!')
#                 self.trade = Trade(self.asset_name, self.position_side, self.entry_price, price, self.position_size, None, None, reason)
                
#                 print(self.trade)
#                 print(self.position)
#             else:
#                 print('Position still open')
#         else:
#             print('There is no position or the given price is below 0')
            
            

# x = PositionTrade(10000, 2, 50, 'DAX', 'Buy', 48, 55)
# x.create_trade()
# x.check_trade(55)


#W3 D2 T2 - random testing

# import random

# random.seed(100)
# a = random.randint(1, 10)

# random.seed(100)
# b = random.randint(1, 10)

# random.seed(200)
# c = random.randint(1, 10)

# print(a == b) #True
# print(a == c) #False


#W3 D2 T3

# class Percentage:
#     def __init__(self, value):
#         self._value = value
    
#     @property
#     def value(self):
#         return self._value
    
#     @value.setter
#     def value(self, setter):
#         if setter in range(0, 101):
#             self._value = setter
#         else:
#             raise ValueError('Percentage must be between 0 and 100!')
    
#     @property
#     def as_decimal(self):
#         return self._value / 100
    
# p = Percentage(50)
# print(p.value)      # 50
# print(p.as_decimal) # 0.5
# p.value = 75
# print(p.value)      # 75
# p.value = 150  

#W3 D2 T4 - before the attribute was unprotected and caused RecursionError

# class BadExample:
#     def __init__(self, value):
#         self._value = value

#     @property
#     def value(self):
#         return self._value

#     @value.setter
#     def value(self, new_value):
#         self._value = new_value

# obj = BadExample(10)


#W3 D2 T5 - updating the Trade class - added tp/sl as optional init values + risk_reward_ratio and return_percent as properties
# from algo_backtest.engine.trade import Trade

# trade = Trade(
#     ticker="EURUSD",
#     side="BUY",
#     entry_price=1.1000,
#     exit_price=1.1050,
#     quantity=10000,
#     stop_loss=1.0950,
#     take_profit=1.1100
# )
# print(f"P&L: ${trade.pnl:.2f}")
# print(f"Return: {trade.return_percent:.2f}%")
# print(f"R:R Ratio: {trade.risk_reward_ratio:.2f}")



#W3 D2 T6

# import random
# random.seed(42)
# result = random.choice(['A', 'B', 'C'])
# print(result)

# picks = [random.choice(items) for _ in range(3)]

# picks = random.sample(items, 3)

# import random
# prices = [random.randrange(0, 400) for i in range(10)]
# print(prices)
# sample = random.sample(prices, 3)
# print(sample)


# class Example:
#     def __init__(self):
#         self.__data = [1, 2, 3]

#     @property
#     def data(self):
#         return self.__data

# e = Example()
# e.data.append(4)
# print(len(e.data))

#W3 D2 T8 - Risk Validator class

# from typing import Tuple

# class RiskValidator:
    
#     def __init__(self, max_risk_percent: float, max_position_size: float):
        
#         self.__max_risk_percent = max_risk_percent
#         self.__max_position_size = max_position_size
        
#     @property
#     def max_risk_percent(self) -> float:
#         '''Property max_risk_percent with validation'''
#         if self.__max_risk_percent < 0.1 or self.__max_risk_percent > 10:
#             raise ValueError('Max risk percent should be between 0.1 and 10.0!')
#         else:
#             return self.__max_risk_percent

#     @property
#     def max_position_size(self) -> float:
#         '''Property max_position_size with validation'''
#         if self.__max_position_size < 0:
#             raise ValueError('Max position size should be above 0!')
#         else:
#             return self.__max_position_size
        
#     def validate_position(self, position) -> Tuple[bool, str]:
#         if position.quantity > self.__max_position_size:
#             return (False, 'Position size exceeds maximum')
#         else:
#             return (True, 'Position valid!')
        

# validator = RiskValidator(max_risk_percent=2.0, max_position_size=100.0)
# print(validator.max_risk_percent)  # 2.0


# from algo_backtest.engine.position import Position

# large_position = Position(
#     ticker="AAPL",
#     side="BUY",
#     quantity=150.0,
#     entry_price=150.0
# )


# valid, message = validator.validate_position(large_position)
# print(f"Valid: {valid}, Message: {message}")


#W3 D2 T9 - Random trade generator

# import random
# from typing import List
# from algo_backtest.engine.trade import Trade

# def generate_random_trades(n: int, tickers: List[str]) -> List[Trade]:
#     '''A function used to generate a number of random trades
    
#     Args: 
#     n - the number of trades you want to generate
#     tickers - the list of tickers you want to use in the generator
    
#     Returns:
#     - a list of generated trades
#     '''
    
#     trades = []
    
#     for i in range(n):
#         ticker = random.choice(tickers)
#         side = random.choice(['BUY', 'SELL'])
#         entry_price = random.uniform(120.0, 200.0)
#         exit_price = entry_price * random.uniform(0.95, 1.05)
#         quantity = random.randint(1, 100)
        
#         trade = Trade(ticker, side, entry_price, exit_price, quantity)
#         trades.append(trade)
        
#     return trades


# tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN']
# trades = generate_random_trades(5, tickers)
# for trade in trades:
#     print(trade)

#W3 D3 T1

# try:
#     x = int("abc")
# except Exception as e:
#     print(type(e).__name__)
    
#W3 D3 T2

# class BankAccount:
#     def __init__(self, owner: str, initial_balance: float = 0.0):
#         self.__owner = owner
#         self.initial_balance = initial_balance
#         self.__balance = self.initial_balance
        
#     def __str__(self):
#         return f'{__class__.__name__}(owner = {self.__owner}, balance = {self.__balance})'
        
#     @property
#     def owner(self) -> str:
#         return self.__owner
    
#     @property
#     def balance(self) -> float:
#         if self.initial_balance < 0:
#             raise ValueError('Initial balance cannot be below 0!')
#         else:
#             return self.__balance
        
#     def deposit(self, amount: float):
#         self.__balance += amount
    
#     def withdraw(self, amount: float):
#         if amount > self.__balance:
#             print(f'The current balance is lower than the amount you want to withdraw!')
#             return False
#         else:
#             self.__balance -= amount
#             print(f'Successfully withdrawn ${amount:.2f} from the account.')
#             return True
    
    
    
# acc = BankAccount("Alice", 100.0)
# print(acc.owner)          # Alice
# print(acc.balance)        # 100.0
# acc.deposit(50.0)
# print(acc.balance)        # 150.0
# success = acc.withdraw(200.0)
# print(success)            # False (insufficient funds)
# print(acc.balance)        # 150.0 (unchanged)
# acc.owner = "Bob"         # AttributeError (read-only)
# print(acc)


#W3 D3 T3

# class Point:
#     def __init__(self, x: int, y: int):
#         self.x = x
#         self.y = y

#     def __str__(self) -> str:
#         '''Simplified string representation if anybody wants to print a class instance'''
#         return f'{__class__.__name__} at ({self.x}, {self.y})'
    
#     def __repr__(self) -> str:
#         '''Unambigous representation for devs'''
#         return f'{__class__.__name__!r}(x = {self.x}, y = {self.y})'
    
    

# p = Point(3, 5)
# print(p)           # Which method? str
# print([p])         # Which method?
# print(f"{p}")      # Which method?
# print(f"{p!r}")    # Which method? -> repr

#W3 D3 T4

# from typing import List
# from algo_backtest.engine.trade import Trade

# class TradeManager:
#     '''Mock class used to manage trades with the Trade class, we can calculate the win rate, total pnl etc.
#        Requires Trade class import from algo_backtest/engine/trade.py'''
    
#     def __init__(self):
#         self._trades = []
#         self.__total_pnl: float = 0.0
#         self.__win_rate: float = 0.0
#         self.__trade_count: int = 0
        
#         self.winning_trades = 0
        
#     def __len__(self):
#         '''Length dunder method'''
#         return len(self._trades)

#     def __iter__(self):
#         '''Iter dunder method, making the objects in the TradeManager iterable'''
#         return iter(self._trades)
    
#     @property 
#     def trade_count(self):
#         return self.__trade_count
    
#     @property
#     def total_pnl(self):
#         return self.__total_pnl
    
#     @property
#     def win_rate(self):
#         self.__win_rate = (self.winning_trades / self.__trade_count * 100)
#         return self.__win_rate
        
    
#     def add_trade(self, trade: Trade) -> None:
#         '''A method used to add trades created with a Trade class'''
#         self._trades.append(trade)
#         self.__trade_count += 1
#         self.__total_pnl += trade.pnl
#         if trade.pnl > 0:
#             self.winning_trades += 1
        
#     def remove_trade(self, ticker: str) -> bool:
#         '''A method used to remove trades and return a T/F'''
#         for trade in self._trades:
#             if trade.ticker == ticker:
#                 self._trades.remove(trade)
#                 return True
#         print('Did not find a trade with requested ticker')
#         return False

#     def get_trades_by_side(self, side: str) -> List[Trade]:
#         '''Gets all of the trades that are either 'BUY' or 'SELL' '''
#         filtered_trades = []
        
#         for trade in self._trades:
#             if trade.side == side:
#                 filtered_trades.append(trade)
        
#         return filtered_trades



# manager = TradeManager()
# manager.add_trade(Trade("AAPL", "BUY", 100, 110, 10))   # +100 PnL
# manager.add_trade(Trade("GOOGL", "SELL", 200, 190, 5))  # +50 PnL
# manager.add_trade(Trade("MSFT", "BUY", 50, 45, 20))     # -100 PnL

# print(f"Total P&L: ${manager.total_pnl:.2f}")  # $50.00
# print(f"Win Rate: {manager.win_rate:.1f}%")    # 66.7%
# print(f"Trade Count: {manager.trade_count}")   # 3
# print(f"Length: {len(manager)}")               # 3

# for trade in manager:
#     print(trade)

#W3 D3 T5
# class A:
#     def __init__(self):
#         self.x = 1

# class B(A):
#     def __init__(self):
#         self.y = 2

# b = B()
# print(hasattr(b, 'x'), hasattr(b, 'y'))


# class MyClass:
#     @property
#     def value(self):
#         return self._value

# obj = MyClass()
# print(obj.value) #Attribute Error - object has no attribute '_value'

# class Counter:
#     count = 0

#     def __init__(self):
#         Counter.count += 1
#         self.id = Counter.count

# c1 = Counter()
# c2 = Counter()
# c3 = Counter()
# print(c1.id, c2.id, c3.id)

#W3 D3 T6 - Debugging

#Original:
# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self._price = price

#     @property
#     def price(self):
#         return self.price  # Bug 1

#     @price.setter
#     def price(self, value):
#         if value > 0:
#             self._price = value
#         # Bug 2: What if value <= 0?

#     def apply_discount(self, percent):
#         self._price = self._price * (1 - percent)  # Bug 3

#     def __str__(self)
#         return f"Product: {self.name}, ${self._price}"  # Bug 4
    
    
    # 1. Wrong property name
    # 2. We aren't properly handling negative values here, which should be the msot logical step
    # 3. Whatever number we put as percent here (if it's an integer), we'd end up with a negative number most likely
    # 4. Lack of :
    
    #Fixed version:
    
    
# class Product:
#     '''Mock class for exercise purpose'''
#     def __init__(self, name: str, price: float):
#         self.name = name
#         self._price = price
    
#     def __str__(self):
#         return f'Product: {self.name}, ${self._price}'    
    
#     @property
#     def price(self):
#         if self._price < 0:
#             raise ValueError('Price cannot be negative!')
#         else:
#             return self._price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError('Price cannot be negative!')
#         else:
#             self._price = value
            
#     def apply_discount(self, percent):
#         self._price = self._price * (1 - percent / 100)


#W3 D3 T7 - dunder methods hash + eq added to  algo_backtest/engine/position.py

# from algo_backtest.engine.position import Position

# p1 = Position("AAPL", "BUY", 100.0, 10)
# p2 = Position("AAPL", "BUY", 100.0, 10)
# p3 = Position("AAPL", "SELL", 100.0, 10)

# print(p1 == p2)  # True
# print(p1 == p3)  # False

# # Can use in set
# positions = {p1, p2, p3}
# print(len(positions))  # 2 (p1 and p2 are duplicates)
# print(positions)

#W3 D3 T8 - Mutable def argument trap

# def add_item(item, items=[]):
#     items.append(item)
#     return items

# print(add_item("a"))
# print(add_item("b"))
# print(add_item("c"))

#Q1 Base Output:
#[a], [a, b], [a, b, c]

#Fixed version:
# from typing import List

# def add_item(item: str, items: List = None) -> List:
    
#     if items is None:
#         items = []
#     items.append(item)
#     return items

# print(add_item("a"))
# print(add_item("b"))
# print(add_item("c"))

# from platform import python_implementation, python_version_tuple

# print(python_implementation())

# for atr in python_version_tuple():
#     print(atr)

#W3 D4 T1


# class Parent:
#     def __init__(self):
#         self.x = 1
#         print("Parent __init__ ran")

# class Child(Parent):
#     def __init__(self):
#         super().__init__() #WITHOUT THIS LINE WE'D GET AN ATTRIBUTE ERROR - parent's init doesn't RUN AUTOMATICALLY
#         self.y = 2
#         print("Child __init__ ran")
        

# c = Child()
# # Output: "Child __init__ ran"  (Parent never ran!)

# print(c.y)  # 2 - works
# print(c.x)  # AttributeError: 'Child' has no attribute 'x'



### Example 3: NO `__init__` in Child -> The INIT inheritance is automatic!

# class Parent:
#     def __init__(self):
#         self.x = 1
#         print("Parent __init__ ran")

# class Child(Parent):
#     pass  # No __init__ defined

# c = Child()
# # Output: "Parent __init__ ran"  (Automatically uses Parent's!)

# print(c.x)  # 1 - works!


#W4 D4 T2 - creating child class for the Base class Account:


# class Account:
#     def __init__(self, owner: str, balance: float = 0.0):
#         self._owner = owner
#         self._balance = balance

#     @property
#     def balance(self) -> float:
#         return self._balance

#     def deposit(self, amount: float) -> None:
#         if amount > 0:
#             self._balance += amount



# class MarginAccount(Account):
#     '''A child class with margin and buying power added'''

#     def __init__(self, owner: str, balance: float, leverage: float):
#         super().__init__(owner, balance)
#         self._leverage = leverage
#         self._buying_power = 0.0
        
#     def __str__(self):
#         return f'{__class__.__name__}(owner = {self._owner}, balance = {self._balance}, leverage = {self._leverage})'
    
#     @property
#     def buying_power(self) -> float:
#         '''A property that calculates the current buying power'''
#         self._buying_power = self._leverage * self._balance
#         return self._buying_power
    
#     @property
#     def leverage(self) -> float:
#         '''A property that describes leverage (read-only)'''
#         return self._leverage


# acc = MarginAccount("Alice", 1000.0, leverage=2.0)
# print(acc.balance)       # 1000.0
# print(acc.leverage)      # 2.0
# print(acc.buying_power)  # 2000.0
# acc.deposit(500)
# print(acc.buying_power)  # 3000.0
# print(acc)               # MarginAccount(owner='Alice', balance=1500.00, leverage=2.0)


#W4 D4 T4 - price generator function

# import random

# def price_generator(start_price: float, num_ticks: int, volatility: int = 5):
#     """
#     Generate simulated price ticks.

#     Args:
#         start_price: Starting price
#         num_ticks: Number of price updates to generate
#         volatility: Max percentage change per tick (1 = 1%)

#     Yields:
#         float: Next price value
#     """

#     prices = []
#     for i in range(num_ticks):
#         price = start_price * (1 - (random.uniform(-volatility, volatility) / 100))
#         prices.append(price)
    
#     return prices


# prices = price_generator(100, 10, 5)
# print(prices)

# class Parent:
#     class_var = "parent"

# class Child(Parent):
#     pass

# Child.class_var = "child"
# print(Parent.class_var, Child.class_var)


#W3 D4 T6  - DEBUGGING

# class Vehicle:
#     def __init__(self, brand: str, year: int):
#         self.brand = brand
#         self.year = year

#     def info(self) -> str:
#         return f"{self.year} {self.brand}"

# class Car(Vehicle):
#     def __init__(self, brand: str, year: int, doors: int):
#         super().__init__(brand, year)
#         self.doors = doors

#     def info(self) -> str:
#         return f"{super().info()} with {self.doors} doors"

# car = Car("Toyota", 2020, 4)
# print(car.info())  # Expected: "2020 Toyota with 4 doors"

# #The child class has init, so it won't automatically inherit the attributes from the parent class,
# #yet it doesn't use the super().__init__() so it won't actually be able to ge the brand, and year attributes.

#W3 D5 T1

# def gen():
#     yield 1
#     yield 2
#     yield 3

# g = gen()
# print(next(g))
# print(next(g))

# def simple():
#     yield 1

# g = simple()
# next(g)
# next(g)  # What happens here?



#W3 D5 T2

# def countdown(n):
#     for num in range(n, 0, -1): #I assume we want to include 1
#         yield num

# # Test it:
# for num in countdown(5):
#     print(num)


#W3 D5 T3
# A) Convert this list comprehension to a generator expression
# squares_list = [x**2 for x in range(10)]

# # Your generator expression (hint: change [ ] to ( ))
# squares_gen = (x ** 2 for x in range (10))

# # B) Convert this filtered list comprehension to a generator expression
# evens_list = [x for x in range(20) if x % 2 == 0]

# # Your generator expression:
# evens_gen = (x for x in range (20) if x % 2 == 0)

# # C) Predict the output:
# gen = (x * 2 for x in [1, 2, 3])
# print(next(gen)) # 2
# print(next(gen)) # 4
# print(list(gen))  # What remains? [6]


#W3 D5 T4

# import random

# def price_ticks(start_price: float, num_ticks: int):
#     """
#     Generate simulated price movements.

#     Each tick moves the price by -1% to +1% randomly.

#     Args:
#         start_price: Starting price
#         num_ticks: Number of prices to generate

#     Yields:
#         float: Each new price (rounded to 2 decimals)
#     """

#     for num in range(num_ticks):
#         exit_price = round(random.uniform(start_price * 0.99, start_price * 1.01), 2)
#         yield exit_price

# # Test:
# random.seed(42)  # For reproducible results
# for price in price_ticks(100.0, 5):
#     print(f"${price:.2f}")

#W3 D5 T5


# class Portfolio:
#     """
#     A portfolio that holds cash and tracks transactions.

#     Requirements:
#     1. __init__(self, initial_cash: float) - store as _cash (protected)
#     2. cash property (read-only) - returns current cash
#     3. _transactions list (protected) - stores all deposit/withdrawal amounts
#     4. deposit(amount) - adds to cash, appends amount to transactions
#     5. withdraw(amount) - subtracts from cash (raise ValueError if insufficient), appends negative amount
#     6. __len__ - returns number of transactions
#     7. __iter__ - iterates over transactions
#     8. __str__ - returns "Portfolio: $X.XX (N transactions)"
#     """

#     def __init__(self, initial_cash: float):
#         self._cash = initial_cash
#         self._transactions_list = []
        
#     def __str__(self) -> str:
#         return f'{__class__.__name__}: ${self._cash:.2f}, ({len(self._transactions_list)} transactions)'
        
#     def __len__(self) -> int:
#         '''Dunder method that allows to check the current length of the transactions list'''
#         return len(self._transactions_list)
    
#     def __iter__(self) -> iter:
#         '''Dunder method that allows us to iterate over transactions'''
#         return iter(self._transactions_list)
        
#     @property
#     def cash(self) -> float:
#         '''A read-only property which returns the current amount of cash'''
#         return self._cash
    
    
#     def deposit(self, amount):
#         '''A method used to deposit any positive amount into our account'''
#         if amount < 0:
#             raise ValueError('The deposited amount has to be above 0!')
#         else:
#             self._cash += amount
#             self._transactions_list.append(('deposit', amount))
    
#     def withdraw(self, amount):
#         '''A method used to withdraw funds if there is a sufficient amount available'''
#         if amount > self._cash:
#             raise ValueError('Deposit impossible, not enough funds')
#         else:
#             self._cash -= amount
#             self._transactions_list.append(('withdraw', -amount))
    
    

# # Test:
# p = Portfolio(1000.0)
# p.deposit(500.0)
# p.withdraw(200.0)
# print(p)              # Portfolio: $1300.00 (2 transactions)
# print(len(p))         # 2
# for t in p:
#     print(t)          # Should print: 500.0, then -200.0


#W3 D5 T6

# gen = (x for x in [1, 2, 3])
# list(gen)  # Consumes it
# for item in gen:
#     print(item) #Prints nothing, empty loop

# def gen():
#     yield 1
#     return "done"
#     yield 2

# g = gen()
# print(next(g))
# print(next(g)) -> Stop iteration error


#W3 D5 T7 - error fix

# def even_numbers(limit):
#     """Generate even numbers from 0 up to (not including) limit."""
#     n = 0
#     while n < limit:
#         if n % 2 == 0:
#             return n  # BUG - IT WILL STOP THE LOOP
#         n += 1
        
        

# def even_numbers(limit):
#     """Generate even numbers from 0 up to (not including) limit."""
#     n = 0
#     while n < limit:
#         if n % 2 == 0:
#             yield n  # BUG - IT WILL STOP THE LOOP
#         n += 1
        
# for num in even_numbers(10):
#     print(num)
# # Should print: 0, 2, 4, 6, 8



#W3 D5 T8

# import random

# class SimpleTradeManager:
#     """Simplified version for this exercise."""

#     def __init__(self):
#         self._trades = []  # List of (ticker, pnl) tuples

#     def add_trade(self, ticker: str, pnl: float):
#         self._trades.append((ticker, pnl))

#     def profitable_trades(self):
#         """
#         Generator that yields only profitable trades.

#         Yields:
#             tuple: (ticker, pnl) where pnl > 0
#         """
        
#         profitable_trades = ((trade[0], trade[1]) for trade in self._trades if trade[1] > 0)
#         return profitable_trades
        

# # Test:
# tm = SimpleTradeManager()
# tm.add_trade("AAPL", 100.0)
# tm.add_trade("GOOGL", -50.0)
# tm.add_trade("MSFT", 200.0)
# tm.add_trade("TSLA", -75.0)

# print("Profitable trades:")
# for ticker, pnl in tm.profitable_trades():
#     print(f"  {ticker}: ${pnl}")