# PCAP-31-03 Lessons Archive

---

## Week 1: Modules, Packages & PIP

**Learning Objectives:**
- Understand the module/package hierarchy in Python
- Master import mechanisms (import, from...import, as)
- Navigate sys.path and package resolution
- Use pip for dependency management
- Recognize namespace collision traps

### Theory

**1. Modules vs Packages:**
- **Module**: A single `.py` file containing Python code
- **Package**: A directory containing `__init__.py` + multiple modules
- **Namespace Package** (PEP 420): Directories without `__init__.py` (Python 3.3+)

**2. Import Mechanisms:**

```python
"""Demonstration of Python import mechanisms."""

# Absolute Import (Most Explicit)
import math
print(math.sqrt(16))  # 4.0

# Selective Import (Import only what you need)
from math import sqrt, pi
print(sqrt(16))  # 4.0

# Alias Import (Industry standard for common libraries)
import numpy as np  # Convention: np for NumPy
import pandas as pd  # Convention: pd for Pandas
from collections import Counter as C

# Wildcard Import (AVOID in production! PEP 8 discourages this)
from math import *  # Pollutes namespace, unclear dependencies
```

**PEP 8 Best Practice:** Use absolute imports. Avoid wildcards except in interactive sessions.

**3. sys.path Resolution:**
Python searches for modules in this order:
1. Current directory
2. PYTHONPATH environment variable
3. Standard library directories
4. Site-packages (pip installs)

```python
import sys
print(sys.path)  # View search paths
```

**4. Package Structure:**
```
my_package/
├── __init__.py      # Makes it a package (can be empty or contain initialization)
├── module_a.py      # Regular module
└── subpackage/
    ├── __init__.py
    └── module_b.py
```

**Example `__init__.py`:**
```python
"""My Package - A professional Python package."""

__version__ = "1.0.0"
__author__ = "Your Name"

# Optionally expose key functions at package level
from .module_a import key_function  # Relative import within package
```

**Importing from packages:**
```python
"""Example of importing from a package structure."""

from my_package import module_a  # Import module
from my_package.subpackage import module_b  # Import from subpackage
from my_package import key_function  # Import exposed function
```

**5. pip Essentials:**
```bash
pip install pandas          # Install
pip install pandas==2.0.0   # Specific version
pip freeze > requirements.txt  # Export dependencies
pip install -r requirements.txt  # Install from file
```

---

### PCAP TRAPS & GOTCHAS

**Trap 1: Circular Imports**
```python
# module_a.py
"""Module A with circular dependency issue."""

from module_b import func_b


def func_a() -> str:
    """Function that depends on module_b."""
    return func_b()


# module_b.py
"""Module B with circular dependency issue."""

from module_a import func_a  # ERROR! Circular dependency


def func_b() -> str:
    """Function that depends on module_a."""
    return func_a()
```

**Solutions:**
1. **Restructure:** Move shared logic to a third module
2. **Lazy Import:** Import inside the function
```python
def func_a() -> str:
    """Lazy import to break circular dependency."""
    from module_b import func_b  # Import at runtime, not module load
    return func_b()
```
3. **Type Hints Only:** Use `from __future__ import annotations` (Python 3.7+)

---

**Trap 2: Shared Mutable State in `__init__.py`**
```python
# __init__.py
"""Package with shared mutable state - DANGEROUS!"""

cache = []  # WARNING: Shared across ALL imports!


# module_a.py
"""Module A modifying shared state."""

from my_package import cache

cache.append(1)  # Modifies the shared list


# module_b.py
"""Module B observing shared state."""

from my_package import cache

print(cache)  # [1] - Surprise! State from module_a persists
```

**Best Practice:** Avoid mutable globals. Use proper state management patterns (Singleton, dependency injection) or configuration objects.

---

**Trap 3: Name Shadowing (Module Name Collision)**
```python
# BAD: Naming your file "random.py" in your project
# random.py
"""Custom random utilities - SHADOWS stdlib module!"""


def my_func() -> None:
    """Some custom function."""
    pass


# main.py
"""Main script that tries to use stdlib random."""

import random  # Imports YOUR random.py from current directory, not stdlib!

print(random.randint(1, 10))  # AttributeError: module has no attribute 'randint'
```

**PEP 8 Warning:** Never name your modules after standard library modules (`random`, `string`, `math`, `sys`, etc.). This shadows stdlib and breaks imports.

**Fix:** Rename your module to something descriptive like `custom_random_utils.py`

---

**Trap 4: `__init__.py` Execution Behavior**
```python
# __init__.py
"""Package initialization code runs ONCE on first import."""

print("Package initialized!")  # Runs on FIRST import only


# main.py
"""Demonstrating __init__.py execution behavior."""

import my_package  # Prints "Package initialized!"
import my_package  # (Silent - module already in sys.modules cache)
```

**Key Concept:** Python caches imported modules in `sys.modules`. The `__init__.py` executes only once, even with multiple imports.

**Professional Use:** Place initialization logic here (logging setup, configuration loading), but keep it lightweight!

---

**Trap 5: Relative vs Absolute Imports**
```python
# Inside package/subpackage/module.py
"""Demonstrating import styles within a package."""

# Absolute Import (PREFERRED by PEP 8)
from package.module_a import func  # Clear, explicit, works everywhere


# Relative Import (Use with caution)
from ..module_a import func  # ".." means parent package
from .sibling_module import other_func  # "." means current package

# DANGER: Relative imports fail if module is run directly as script
# python package/subpackage/module.py  # ValueError: attempted relative import
```

**PEP 8 Recommendation:**
- Use **absolute imports** for clarity and maintainability
- Relative imports are acceptable for complex package hierarchies
- Never run package modules directly; use `python -m package.subpackage.module`

**Type Hint Import Pattern:**
```python
"""Module showing type hint import best practice."""

from typing import List, Dict
from package.models import User  # Absolute import for type hints


def process_users(users: List[User]) -> Dict[str, int]:
    """Process users with proper type hints."""
    return {user.name: user.id for user in users}
```

---

### Exam Tips

**Critical Concepts for PCAP:**
1. **`sys.modules`**: Dictionary of already-imported modules (cached)
   ```python
   import sys
   print('math' in sys.modules)  # Check if math is imported
   ```

2. **`__name__` == "__main__"`**: Guard for executable scripts
   ```python
   """Module that can be imported or run directly."""

   def main() -> None:
       """Entry point when run as script."""
       print("Running as script")


   if __name__ == "__main__":
       main()  # Only runs when executed directly, not when imported
   ```

3. **`dir(module)`**: Lists all attributes/functions in a module
   ```python
   import math
   print(dir(math))  # Shows all available functions/constants
   ```

4. **Dotted imports**: `from a.b.c import d` - Know the lookup order!
   - Python searches in order: current dir → PYTHONPATH → stdlib → site-packages

5. **Import Statement Evaluation**: Imports execute code! Be aware of side effects.

---

### Professional Standards Recap

**For Project Code (AlgoBacktest):**
- ✅ Always use type hints: `def load_data(file_path: str) -> pd.DataFrame:`
- ✅ Add docstrings: Module, class, and function level
- ✅ Follow PEP 8: `snake_case` for functions, `PascalCase` for classes
- ✅ Use absolute imports for clarity
- ✅ Meaningful names: `price_dataframe` not `df`

**For PCAP Drills:**
- Focus on pure Python behavior and edge cases
- Understand import mechanics deeply (when/how code executes)
- Know the traps and gotchas listed above

---
