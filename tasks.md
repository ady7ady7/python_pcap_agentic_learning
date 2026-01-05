# Week 1, Day 1 - Modules & Packages Fundamentals

**Date:** 2026-01-05
**Topic:** Import Mechanisms, sys.path, Package Structure
**Target:** 6-8 Tasks Completed
**Rules:** PCAP Drills = Pure Python (no external libraries). Project Tasks = Pandas/NumPy allowed.

---

## Task 1: PCAP Warm-up - Import Variants (Pure Python)

Create a file `math_utils.py` with these functions following PEP 8:

```python
"""Basic mathematical utility functions for import practice."""

def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b

PI = 3.14159  # Module-level constant
```

Now create `test_imports.py` that demonstrates **4 different import styles**:
1. Import the entire module
2. Import specific functions only
3. Import with an alias
4. Import everything (use wildcard)

Print the result of `add(5, 3)` using each import style.

**Question:** What happens if you create a variable named `PI = 999` in `test_imports.py` BEFORE doing `from math_utils import *`? Test it.
#The pi variable is overwritten with the value imported from the module.

import math_utils

#task1
x1 = math_utils.add(3, 5)
print(x1)

#1.2
from math_utils import add
x2 = add(6, 10)
print(x2)

#1.3
import math_utils as mu
x3 = mu.add(10, 25)
print(x3)

#1.4

pi = 999
from math_utils import *

print(pi)
print(dir(math_utils))
x4 = math_utils.add(10, 7)
print(x4)


#The wildcard solution clearly creates issues and I'm not even able to properly execute the code with the standard logic
#I've also used different numbers for each import type to clearly see if they work


#Log:
$ python test_imports.py
16
35
3.14159
Traceback (most recent call last):
  File "C:\Users\HARDPC\Desktop\AL\projekty\python_pcap_agentic_learning\tasks_files\test_imports.py", line 24, in <module>
    print(dir(math_utils))
              ^^^^^^^^^^
NameError: name 'math_utils' is not defined



---

## Task 2: Theory Drill - sys.path Investigation (Pure Python)

Write a script `path_detective.py` that:
1. Prints the current working directory
2. Prints all paths in `sys.path` (one per line, numbered)
3. Creates a module `hidden.py` in a NEW subfolder `secret/`
4. Attempts to `import hidden` (this will FAIL)
5. Manually adds `secret/` to `sys.path`
6. Successfully imports `hidden`

**Deliverable:** The script should print "Success!" after the import works.

import sys
print(sys.path[0]) #current dir

num = 0
for path in sys.path:
    num += 1
    print(f'{num}: {path}')

sys.path.append(r'C:\Users\HARDPC\Desktop\AL\projekty\python_pcap_agentic_learning\tasks_files\secret')

mock_var = 3
import hidden
from hidden import * #If we use the wildcard import, we would also import the value of the mock_var in there
from hidden import mock_var #also works if we would like to import a single variable for whatever reason

num = 0
for path in sys.path:
    num += 1
    print(f'{num}: {path}')

print(mock_var)


#It works, if we put print('Imported with success') in the hidden.py, it will print as we import hidden

---

## Task 3: Refactor/Debug - Find the Circular Import (Pure Python)

You're given this broken package structure:

```
broken_pkg/
├── __init__.py
├── engine.py
└── utils.py
```

**engine.py:**
```python
from broken_pkg.utils import helper

def start():
    return helper()
```

**utils.py:**
```python
from broken_pkg.engine import start

def helper():
    return "Engine started: " + start()
```

**Task:**
1. Predict what error occurs when you run `from broken_pkg import engine`
2. Fix the circular dependency WITHOUT changing the function behavior
3. Explain your solution in a comment

#We'd get an error, as the engine.py depends on broken_pkg, and we're trying to import what's already in there, and we're trying to select the general scope from the specific file of this very scope, which is erratic. Same for utils.py.
# 
**engine.py:**
```python
from utils import helper

def start():
    return helper()

**utils.py:**
```python
from engine import start

def helper():
    return "Engine started: " + start()

#We simply import the respective modules from the current folder we're in, no need to do circular imports here



---

## Task 4: PROJECT TASK - Setup AlgoBacktest Structure (Pandas/NumPy Allowed)

Create the following directory structure:

```
algo_backtest/
├── __init__.py
├── data/
│   └── __init__.py
├── engine/
│   └── __init__.py
├── strategies/
│   └── __init__.py
└── main.py
```

In `algo_backtest/__init__.py`, add:
```python
"""AlgoBacktest Core - Professional backtesting framework for algorithmic trading strategies."""

__version__ = "0.1.0"
__author__ = "Your Name"
```

In `main.py`, write code that:
1. Imports `sys`
2. Prints the package version by importing from `algo_backtest`
3. Prints "AlgoBacktest Core - Ready"

**PEP 8 Requirements:**
- Add a module-level docstring at the top of `main.py`
- Use proper spacing (2 blank lines between top-level definitions)
- Follow naming conventions

**Run it:** `python algo_backtest/main.py` should work without errors.


main.py

'''

This is the main.py for my professional backtesting framework for algotrading strategies
I'm working on this project as a part of my daily Python PCAP practice routine, using the small steps methodology

'''


import sys
from __init__ import __version__


if __name__ == '__main__':
    print(f'Current version: {__version__}')
    print('AlgoBacktest Core - Ready')

$ python algo_backtest/main.py
Current version: 0.1.0
AlgoBacktest Core - Ready


---

## Task 5: PROJECT TASK - Create requirements.txt + Dependency Checker (Industry Standard)

Create `requirements.txt` in the project root with:
```
pandas>=2.0.0
numpy>=1.24.0
```

**Task:** Write a script `check_deps.py` that:
1. Attempts to import pandas and numpy
2. Prints their `__version__` attributes
3. If import fails, prints "Missing dependency: [name]"

**Professional Standards:**
- Add module docstring
- Use meaningful variable names (e.g., `required_packages` not `deps`)
- Add type hints: `def check_dependency(package_name: str) -> bool:`
- Follow PEP 8 spacing and formatting
- Use proper exception handling with specific exception types

**Hint:** Use try/except blocks for `ImportError` or `ModuleNotFoundError`.

$ python algo_backtest/main.py
Imports succeeded!
Pandas version: 2.3.2
Numpy version: 2.2.5
Current version: 0.1.0
AlgoBacktest Core - Ready

#Look, you wanted me to actually pass package_name, but every time I try to check an import for a given package_name, IT IMPORTS package_name literally, which sucks. I've read that we could use ImportLib to deal with that, BUT YOU HAVEN'T TAUGHT me that at all, so I simply used my way of dealing with that with basic 'hardcoded' version of check_dependencies.

If you want me to deal with that using the Importlib, we can do it next time, BUT MAKE SURE YOU add it to lessons.md and explain why we use it!

'''Module used to check dependencies''' 
# /algo_backtest/check_dependencies.py

def check_deps():
    try:
        import pandas as pd
        import numpy as np
        
    except ImportError as e:
        print(f'Import error: {str(e)}')
    except ModuleNotFoundError as e:
        print(f'Module not found: {str(e)}')
    except Exception as e:
        print(f'Unexpected error: {str(e)}')
        
    else:
        print('Imports succeeded!')
        print(f'Pandas version: {pd.__version__}')
        print(f'Numpy version: {np.__version__}')


---

## Task 6: Edge Case Hunt - Name Shadowing Trap (Pure Python)

Create a file named `string.py` with this code (intentionally minimal for the trap):
```python
"""Custom string utilities - WARNING: Shadows stdlib module."""

def reverse(text: str) -> str:
    """Reverse a string using slicing."""
    return text[::-1]
```

Now create `main_app.py` that:
1. Tries to `import string` (stdlib module)
2. Calls `string.ascii_lowercase` (should print alphabet)

**Questions:**
- Does it work? Why/why not?
- How would you fix it WITHOUT renaming `string.py`?
- Test your solution.

**PEP 8 Note:** Even though this task demonstrates bad practice (shadowing), write clean code with docstrings and type hints to maintain professional habits.

1. Traceback (most recent call last):
  File "C:\Users\HARDPC\Desktop\AL\projekty\python_pcap_agentic_learning\algo_backtest\main.py", line 20, in <module>
    string.ascii_lowercase
AttributeError: module 'string' has no attribute 'ascii_lowercase'

It causes the error, as our string DOESN'T have the ascii_lowercase module obviously, but reverse only.

2. Honestly, leaving it without renaming that WOULDN'T be wise, as it's a very bad practice, and I'm NOT SURE how to fix it in the current state.

I've tried doing direct import:
    from string import ascii_lowercase
    print(ascii_lowercase)
But it still drops an ImportError, ImportError: cannot import name 'ascii_lowercase' from 'string' (C:\Users\HARDPC\Desktop\AL\projekty\python_pcap_agentic_learning\algo_backtest\string.py)


---

## Task 7: PCAP Simulation - Multiple Choice

**Question:**
What is the output of this code?

```python
# package/__init__.py
x = 10

# package/module.py
x = 20

# main.py
from package import x as a
from package.module import x as b
print(a, b)
```

**Choices:**
A) `10 20`
B) `20 20`
C) `10 10`
D) `NameError`

Write your answer in `task7_answer.txt` with a 2-sentence explanation.

Asking me to write the answer in a separate file is just retarded, WE DON'T WANT TO CLUTTER our filebase with 32494329 unnecessary files. I want it to BE CLEAN AND NEAT and reduce teh number of files to the MINIMUM, and I'll be answering in tasks.md

Answer: A, while the __init__ runs only once, we still get the x value saved as a, and in module.py it's different, but we save the x value in a separate object, so In my opinion it remains 10, 20 respectively.

---

## Task 8: Integration - Lazy Import Pattern (Pure Python)

Create `expensive_module.py`:
```python
"""Simulates a heavy module with expensive initialization."""

print("Heavy computation loading...")
import time

time.sleep(2)  # Simulate expensive setup


def calculate() -> int:
    """Perform expensive calculation."""
    return 42
```

Now create `smart_loader.py` that:
1. Defines a function `get_result() -> int` with type hint
2. ONLY imports `expensive_module` INSIDE the function (lazy import)
3. Returns the result of `calculate()`
4. Add proper docstring explaining the lazy import pattern

**Test:**
```python
# main.py (add docstring here too!)
from smart_loader import get_result

print("App started")  # Should print IMMEDIATELY
result = get_result()  # Now the 2-second delay happens
print(result)
```

**Question:** Why is lazy importing useful? Write answer as a docstring in `smart_loader.py` explaining the pattern.

**Professional Note:** This is a real-world optimization technique used in production systems.


'''Simulates an easy to load smart module'''

def get_result() -> int:
    '''It lazy imports the expensive_module and returns the result of the calculate function of that module'''
    import expensive_module
    return expensive_module.calculate()

I'm really unsure why this would be useful, as it seems a bit overengineered, but perhaps if we want to split two modules for whatever reason (maybe clarity or different scopes/areas that are covered by them), and then for whatever reason we need to use them together again, but we don't want to do so in main, we could use them in a separate module. But I'd still love to see your explanation for that


---

## Self-Assessment

After completing all tasks, rate yourself:

- **Score:** 8/8 tasks completed
- **Difficulty:** (Easy/Medium/Hard) - Medium - Hard (depends)
- **Time Spent:** ___ hours
- **Sticking Points:** (What was confusing?)

Document this in `feedback.md` (I'll create the template next).

---

**Next Session Preview:**
Tomorrow we dive into **relative imports** and build the `DataLoader` class for AlgoBacktest using Pandas!
