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


#W1 D1 Task6

