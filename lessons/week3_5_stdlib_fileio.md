# Weeks 3-5: Standard Library Modules & File I/O

This lesson covers essential modules from Python's standard library. These are **built-in** - no installation required.

---

## Table of Contents

| Module | Description |
|--------|-------------|
| [`random`](#the-random-module) | Pseudo-random number generation |
| [`platform`](#the-platform-module) | System and hardware information |
| [`sys`](#the-sys-module) | Python interpreter interaction |
| [`os`](#the-os-module) | Operating system interaction |
| [`datetime`](#the-datetime-module) | Date and time manipulation |
| [File I/O](#file-io) | Reading and writing files |

---

## The `random` Module

The `random` module provides functions for generating pseudo-random numbers and making random selections.

```python
import random
```

---

### `random.random()` - Float between 0 and 1

Returns a random float in the range `[0.0, 1.0)` (includes 0, excludes 1).

```python
import random

print(random.random())  # e.g., 0.7134589023
print(random.random())  # e.g., 0.2918374651
```

---

### `random.seed()` - Reproducible Results

The `seed()` function initializes the random number generator. Using the same seed produces the same sequence of "random" numbers.

```python
import random

random.seed(42)
print(random.random())  # Always: 0.6394267984578837

random.seed(42)
print(random.random())  # Always: 0.6394267984578837 (same!)
```

**Use case:** Testing - when you need predictable "random" values for debugging.

---

### `random.randint(a, b)` - Random Integer (Inclusive)

Returns a random integer N such that `a <= N <= b` (both endpoints included).

```python
import random

print(random.randint(1, 6))   # Dice roll: 1, 2, 3, 4, 5, or 6
print(random.randint(0, 100)) # Random percentage: 0 to 100
```

**PCAP Trap:** Both `a` and `b` are **inclusive**. `randint(1, 6)` can return 6.

---

### `random.randrange(start, stop, step)` - Random from Range

Returns a random element from `range(start, stop, step)`. The `stop` value is **excluded** (like `range()`).

```python
import random

print(random.randrange(10))        # 0 to 9 (stop only)
print(random.randrange(1, 7))      # 1 to 6 (like randint but stop excluded)
print(random.randrange(0, 100, 5)) # 0, 5, 10, 15, ..., 95
```

**Key difference from `randint`:**
- `randint(1, 6)` → can return 1, 2, 3, 4, 5, **6**
- `randrange(1, 7)` → can return 1, 2, 3, 4, 5, 6 (same result, different syntax)

---

### `random.choice(sequence)` - Pick One Element

Returns a single random element from a non-empty sequence.

```python
from random import choice

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(choice(my_list))  # e.g., 4

colors = ['red', 'green', 'blue']
print(choice(colors))   # e.g., 'green'

word = "Python"
print(choice(word))     # e.g., 'h'
```

---

### `random.sample(sequence, k)` - Pick Multiple Unique Elements

Returns a list of `k` unique elements chosen from the sequence. The elements are placed in **random order**.

```python
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))       # e.g., 4
print(sample(my_list, 5))    # e.g., [3, 1, 8, 9, 10]
print(sample(my_list, 10))   # e.g., [10, 8, 5, 1, 6, 4, 3, 9, 7, 2]
```

**Critical rule:** `k` must not be greater than `len(sequence)`.

```python
sample(my_list, 15)  # ValueError: Sample larger than population
```

**Key property:** `sample()` returns **unique** elements - no duplicates. This is different from calling `choice()` multiple times, which can return the same element twice.

```python
# choice() can repeat:
[choice(my_list) for _ in range(5)]  # e.g., [3, 3, 7, 1, 3]

# sample() never repeats:
sample(my_list, 5)                    # e.g., [3, 7, 1, 9, 2] (all unique)
```

---

### `random` Quick Reference

| Function | Returns | Range/Behavior |
|----------|---------|----------------|
| `random()` | float | [0.0, 1.0) |
| `seed(n)` | None | Sets generator state |
| `randint(a, b)` | int | a <= N <= b (inclusive) |
| `randrange(start, stop, step)` | int | Like range(), stop excluded |
| `choice(seq)` | element | Single random element |
| `sample(seq, k)` | list | k unique elements, random order |

### `random` PCAP Traps

1. **`randint` is inclusive on both ends** - `randint(1, 10)` can return 10
2. **`randrange` excludes stop** - `randrange(1, 10)` cannot return 10
3. **`sample(seq, k)` requires `k <= len(seq)`** - otherwise ValueError
4. **`sample()` returns unique elements** - no duplicates possible
5. **`random()` excludes 1.0** - range is [0.0, 1.0), never exactly 1.0

---

## The `platform` Module

The `platform` module provides access to information about the underlying system - the hardware, OS, and Python interpreter.

```python
import platform
```

### Understanding the Execution Layers

When your Python code runs, it goes through several layers:

```
┌─────────────────────────────┐
│      Your Python Code       │  ← You write this
├─────────────────────────────┤
│    Python Interpreter       │  ← Executes your code
├─────────────────────────────┤
│    Operating System (OS)    │  ← Windows, Linux, macOS
├─────────────────────────────┤
│         Hardware            │  ← CPU, RAM, etc.
└─────────────────────────────┘
```

The `platform` module lets you query information from each of these layers. This is useful when:
- Writing cross-platform code that behaves differently on Windows vs Linux
- Debugging environment-specific issues
- Logging system information for diagnostics

**Note:** You may not need this module often, but understanding how your code interacts with the system is valuable knowledge.

---

### `platform.platform()` - Full System Description

Returns a single string identifying the underlying platform with as much useful information as possible.

```python
import platform

print(platform.platform())
# Example outputs:
# Windows: 'Windows-10-10.0.19041-SP0'
# Linux:   'Linux-5.4.0-42-generic-x86_64-with-glibc2.31'
# macOS:   'macOS-12.0-arm64-arm-64bit'
```

**Parameters:**
- `aliased` (default `False`) - If `True`, uses common aliases (e.g., "Windows" instead of "Windows-10")
- `terse` (default `False`) - If `True`, returns minimal information

```python
print(platform.platform(aliased=True))   # May use aliases
print(platform.platform(terse=True))     # Minimal output
```

---

### Common `platform` Functions

```python
import platform

# Operating System
print(platform.system())        # 'Windows', 'Linux', 'Darwin' (macOS)
print(platform.release())       # '10' (Windows 10), '5.4.0' (Linux kernel)
print(platform.version())       # Detailed OS version string

# Hardware
print(platform.machine())       # 'AMD64', 'x86_64', 'arm64'
print(platform.processor())     # CPU info (may be empty on some systems)

# Python Interpreter
print(platform.python_version())           # '3.10.4'
print(platform.python_implementation())    # 'CPython', 'PyPy', etc.
print(platform.python_version_tuple())     # ('3', '10', '4')
```

---

### Practical Example: Cross-Platform Code

```python
import platform

if platform.system() == 'Windows':
    path_separator = '\\'
    clear_command = 'cls'
else:
    path_separator = '/'
    clear_command = 'clear'

print(f"Running on {platform.system()}")
print(f"Python version: {platform.python_version()}")
```

---

### `platform` Quick Reference

| Function | Returns | Example |
|----------|---------|---------|
| `platform()` | Full platform string | 'Windows-10-10.0.19041-SP0' |
| `system()` | OS name | 'Windows', 'Linux', 'Darwin' |
| `release()` | OS release | '10', '5.4.0' |
| `machine()` | Hardware architecture | 'AMD64', 'x86_64' |
| `processor()` | CPU info | 'Intel64 Family 6...' |
| `python_version()` | Python version string | '3.10.4' |
| `python_implementation()` | Interpreter type | 'CPython' |

---

## The `sys` Module

The `sys` module provides access to variables and functions that interact with the **Python interpreter** itself. It's essential for understanding how Python runs your code.

```python
import sys
```

### Key Use Cases

1. **Command-line arguments** - Access arguments passed to your script
2. **Module search path** - Control where Python looks for imports
3. **Standard streams** - Access stdin, stdout, stderr
4. **Interpreter information** - Version, platform, recursion limits
5. **Script termination** - Exit the program with a status code

---

### `sys.argv` - Command Line Arguments

A list containing the script name and any arguments passed to it.

```python
# script.py
import sys

print(f"Script name: {sys.argv[0]}")
print(f"Arguments: {sys.argv[1:]}")
print(f"Total args: {len(sys.argv)}")

# Run: python script.py hello world 123
# Output:
# Script name: script.py
# Arguments: ['hello', 'world', '123']
# Total args: 4
```

**PCAP Trap:** `sys.argv[0]` is always the script name, actual arguments start at index 1.

---

### `sys.path` - Module Search Path

A list of directories where Python looks for modules when you use `import`.

```python
import sys

# See where Python looks for modules
for path in sys.path:
    print(path)

# Add a custom directory (temporarily)
sys.path.append('/my/custom/modules')

# Now Python will also search there for imports
```

**Windows Paths - Backslash Escaping:**

On Windows, paths use backslashes (`\`). Since `\` is normally used to escape characters in strings (e.g., `\n` = newline, `\t` = tab), you must **escape the backslash** with another backslash:

```python
# WRONG - \U and \p are interpreted as escape sequences
sys.path.append('C:\Users\user\py\modules')  # SyntaxError or wrong path!

# CORRECT - Double backslash escapes properly
sys.path.append('C:\\Users\\user\\py\\modules')

# ALTERNATIVE - Raw string (prefix with r)
sys.path.append(r'C:\Users\user\py\modules')
```

**How Python resolves imports:**
1. Current directory (usually first)
2. PYTHONPATH environment variable directories
3. Standard library directories
4. Site-packages (third-party packages)

---

### `sys.exit()` - Exit the Program

Terminates the script with an optional exit code.

```python
import sys

def main():
    if some_error:
        print("Error occurred!", file=sys.stderr)
        sys.exit(1)  # Non-zero = error

    print("Success!")
    sys.exit(0)  # Zero = success (optional, default)
```

**Exit codes:**
- `0` = Success (default)
- `1-255` = Error (convention: different codes for different errors)

---

### `sys.stdin`, `sys.stdout`, `sys.stderr` - Standard Streams

The three standard I/O streams:

```python
import sys

# Normal output (what print() uses)
sys.stdout.write("Hello\n")

# Error output (separate stream)
sys.stderr.write("Error message\n")

# Read input (what input() uses)
data = sys.stdin.readline()
```

**Why separate stderr?** Allows redirecting normal output while keeping errors visible:
```bash
python script.py > output.txt  # stdout to file, stderr still on screen
```

---

### `sys.version` and `sys.version_info` - Python Version

```python
import sys

print(sys.version)
# '3.10.4 (main, Mar 31 2022, 08:41:55) [GCC 7.5.0]'

print(sys.version_info)
# sys.version_info(major=3, minor=10, micro=4, releaselevel='final', serial=0)

# Check minimum version
if sys.version_info < (3, 8):
    sys.exit("Python 3.8+ required")
```

---

### `sys.getrecursionlimit()` / `sys.setrecursionlimit()` - Recursion Control

```python
import sys

print(sys.getrecursionlimit())  # Default: usually 1000

# Increase if needed (be careful!)
sys.setrecursionlimit(2000)
```

**Warning:** Setting too high can crash Python with a stack overflow.

---

### `sys` Quick Reference

| Function/Variable | Description | Example |
|-------------------|-------------|---------|
| `sys.argv` | Command-line arguments | `['script.py', 'arg1']` |
| `sys.path` | Module search paths | `['/home/user', ...]` |
| `sys.exit(code)` | Exit program | `sys.exit(1)` |
| `sys.version` | Python version string | `'3.10.4 ...'` |
| `sys.version_info` | Version as named tuple | `(3, 10, 4, ...)` |
| `sys.stdin/stdout/stderr` | Standard I/O streams | File-like objects |
| `sys.getrecursionlimit()` | Max recursion depth | `1000` |

---

## The `os` Module

The `os` module provides functions for interacting with the **operating system**. It's essential for file/directory operations and environment variables.

```python
import os
```

### Key Use Cases

1. **File/directory operations** - Create, delete, rename, list
2. **Path manipulation** - Join paths, get file info
3. **Environment variables** - Access system configuration
4. **Process management** - Run commands, get current directory

---

### `os.getcwd()` and `os.chdir()` - Working Directory

```python
import os

# Get current working directory
print(os.getcwd())  # '/home/user/project'

# Change directory
os.chdir('/home/user/other_folder')
print(os.getcwd())  # '/home/user/other_folder'
```

---

### `os.listdir()` - List Directory Contents

```python
import os

# List files and folders in current directory
files = os.listdir('.')
print(files)  # ['file1.py', 'folder1', 'data.csv']

# List specific directory
files = os.listdir('/home/user/documents')
```

---

### `os.mkdir()` and `os.makedirs()` - Create Directories

```python
import os

# Create single directory
os.mkdir('new_folder')

# Create nested directories (like mkdir -p)
os.makedirs('parent/child/grandchild', exist_ok=True)
# exist_ok=True prevents error if already exists
```

---

### `os.remove()` and `os.rmdir()` - Delete Files/Directories

```python
import os

# Delete a file
os.remove('unwanted_file.txt')

# Delete an EMPTY directory
os.rmdir('empty_folder')

# For non-empty directories, use shutil.rmtree()
import shutil
shutil.rmtree('folder_with_contents')
```

---

### `os.path` - Path Manipulation (Submodule)

The `os.path` submodule is crucial for cross-platform path handling:

```python
import os

# Join paths (handles OS-specific separators)
path = os.path.join('folder', 'subfolder', 'file.txt')
# Windows: 'folder\\subfolder\\file.txt'
# Linux:   'folder/subfolder/file.txt'

# Check if path exists
os.path.exists('some_file.txt')  # True/False

# Check if it's a file or directory
os.path.isfile('data.csv')      # True if it's a file
os.path.isdir('my_folder')      # True if it's a directory

# Get file name from path
os.path.basename('/home/user/file.txt')  # 'file.txt'

# Get directory from path
os.path.dirname('/home/user/file.txt')   # '/home/user'

# Split into directory and filename
os.path.split('/home/user/file.txt')  # ('/home/user', 'file.txt')

# Get file extension
os.path.splitext('data.csv')  # ('data', '.csv')

# Get absolute path
os.path.abspath('relative/path')  # '/full/absolute/path'
```

---

### `os.environ` - Environment Variables

```python
import os

# Get an environment variable
home = os.environ.get('HOME')  # '/home/user' (Linux/Mac)
path = os.environ.get('PATH')  # System PATH variable

# Get with default if not set
debug = os.environ.get('DEBUG', 'False')

# Set an environment variable (for this process only)
os.environ['MY_VAR'] = 'some_value'
```

**Common environment variables:**
- `HOME` / `USERPROFILE` - User's home directory
- `PATH` - Executable search paths
- `PYTHONPATH` - Additional Python module paths

---

### `os.name` - Operating System Name

```python
import os

print(os.name)
# 'nt'     - Windows
# 'posix'  - Linux, macOS, Unix
```

---

### Practical Example: Cross-Platform Script

```python
import os
import sys

def setup_project():
    # Get project directory (where script is located)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Create data directory if it doesn't exist
    data_dir = os.path.join(script_dir, 'data')
    os.makedirs(data_dir, exist_ok=True)

    # Check if config file exists
    config_path = os.path.join(script_dir, 'config.ini')
    if not os.path.exists(config_path):
        print(f"Warning: {config_path} not found", file=sys.stderr)
        sys.exit(1)

    print(f"Project setup complete in {script_dir}")

if __name__ == '__main__':
    setup_project()
```

---

### `os` Quick Reference

| Function | Description | Example |
|----------|-------------|---------|
| `os.getcwd()` | Get current directory | `'/home/user'` |
| `os.chdir(path)` | Change directory | `os.chdir('/tmp')` |
| `os.listdir(path)` | List directory contents | `['file1', 'file2']` |
| `os.mkdir(path)` | Create directory | `os.mkdir('new')` |
| `os.makedirs(path)` | Create nested directories | `os.makedirs('a/b/c')` |
| `os.remove(path)` | Delete file | `os.remove('file.txt')` |
| `os.rmdir(path)` | Delete empty directory | `os.rmdir('empty')` |
| `os.path.join()` | Join path components | `'a/b/c'` or `'a\\b\\c'` |
| `os.path.exists()` | Check if path exists | `True/False` |
| `os.path.isfile()` | Check if it's a file | `True/False` |
| `os.path.isdir()` | Check if it's a directory | `True/False` |
| `os.environ` | Environment variables dict | `os.environ['HOME']` |
| `os.name` | OS type | `'nt'` or `'posix'` |

---

---

## The `datetime` Module

The `datetime` module provides classes for working with dates and times.

```python
from datetime import date, time, datetime, timedelta
```

### `date` - Date Objects

```python
from datetime import date

# Create a date
d = date(2026, 2, 2)  # year, month, day
print(d)  # 2026-02-02

# Today's date
today = date.today()

# Access components
print(today.year)   # 2026
print(today.month)  # 2
print(today.day)    # 2

# Day of week (Monday = 0, Sunday = 6)
print(today.weekday())     # 0 (Monday)
print(today.isoweekday())  # 1 (Monday = 1)
```

### `time` - Time Objects

```python
from datetime import time

# Create a time
t = time(14, 30, 45)  # hour, minute, second
print(t)  # 14:30:45

# Access components
print(t.hour)    # 14
print(t.minute)  # 30
print(t.second)  # 45
```

### `datetime` - Combined Date and Time

```python
from datetime import datetime

# Create datetime
dt = datetime(2026, 2, 2, 14, 30, 45)
print(dt)  # 2026-02-02 14:30:45

# Current datetime
now = datetime.now()

# From timestamp (Unix time)
dt = datetime.fromtimestamp(1738500000)

# To timestamp
ts = now.timestamp()
```

### `strftime` and `strptime` - Formatting

```python
from datetime import datetime

now = datetime.now()

# strftime = "string format time" → datetime to string
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
# '2026-02-02 14:30:45'

# strptime = "string parse time" → string to datetime
dt = datetime.strptime("2026-02-02", "%Y-%m-%d")

# Common format codes:
# %Y - 4-digit year (2026)
# %m - 2-digit month (02)
# %d - 2-digit day (02)
# %H - 24-hour (14)
# %M - minute (30)
# %S - second (45)
# %A - weekday name (Monday)
# %B - month name (February)
```

**PCAP Trap:** `strftime` vs `strptime`
- strftime = **f**ormat → datetime to string
- strptime = **p**arse → string to datetime

### `timedelta` - Date Arithmetic

```python
from datetime import datetime, timedelta

now = datetime.now()

# Create timedelta
delta = timedelta(days=7, hours=3, minutes=30)

# Add/subtract
future = now + delta
past = now - delta

# Difference between datetimes
dt1 = datetime(2026, 2, 10)
dt2 = datetime(2026, 2, 2)
diff = dt1 - dt2
print(diff.days)  # 8
print(diff.total_seconds())  # 691200.0
```

### `datetime` Quick Reference

| Class/Function | Description | Example |
|----------------|-------------|---------|
| `date(y, m, d)` | Create date | `date(2026, 2, 2)` |
| `date.today()` | Current date | `date(2026, 2, 2)` |
| `time(h, m, s)` | Create time | `time(14, 30, 45)` |
| `datetime(...)` | Create datetime | `datetime(2026, 2, 2, 14, 30)` |
| `datetime.now()` | Current datetime | Current timestamp |
| `strftime(fmt)` | Format to string | `"%Y-%m-%d"` |
| `strptime(s, fmt)` | Parse from string | String to datetime |
| `timedelta(...)` | Duration | `timedelta(days=7)` |

---

## File I/O

### Opening Files - The `with` Statement

```python
# ALWAYS use context manager (auto-closes file)
with open('file.txt', 'r') as f:
    content = f.read()
# File automatically closed here

# WITHOUT context manager (NOT recommended)
f = open('file.txt', 'r')
content = f.read()
f.close()  # Easy to forget!
```

### File Modes

```python
'r'   # Read (default) - file must exist
'w'   # Write - creates new or TRUNCATES existing
'a'   # Append - creates new or appends to existing
'x'   # Exclusive create - fails if file exists

'rb'  # Read binary
'wb'  # Write binary

'r+'  # Read and write (file must exist)
'w+'  # Write and read (truncates)
```

### Reading Files

```python
# Read entire file as string
with open('file.txt', 'r') as f:
    content = f.read()

# Read specific number of characters
with open('file.txt', 'r') as f:
    chunk = f.read(100)  # First 100 chars

# Read one line (includes \n!)
with open('file.txt', 'r') as f:
    line = f.readline()

# Read all lines as list
with open('file.txt', 'r') as f:
    lines = f.readlines()  # ['line1\n', 'line2\n', ...]

# Iterate line by line (MEMORY EFFICIENT!)
with open('file.txt', 'r') as f:
    for line in f:
        print(line.strip())  # Remove trailing \n
```

### Writing Files

```python

#We can create an empty file like that - using w.write() WOULD cause a TypeError
with open(self.filepath, 'w') as w:
    pass

# Write string
#Also remember that 'w' mode OVERWRITES previous data - so we might consider using append if we want to add content
with open('file.txt', 'w') as f:
    f.write('Hello, World!\n')

# Write multiple lines
with open('file.txt', 'w') as f:
    lines = ['line1\n', 'line2\n', 'line3\n']
    f.writelines(lines)  # Does NOT add \n automatically!

# Append to file
with open('file.txt', 'a') as f:
    f.write('Appended line\n')
```

### File Position

```python
with open('file.txt', 'r') as f:
    pos = f.tell()  # Get current position (0 at start)

    f.read(10)
    pos = f.tell()  # Now 10

    f.seek(0)       # Go back to start
    f.seek(0, 2)    # Go to end (offset 0 from end)
```

### PCAP Traps - File I/O

```python
# TRAP 1: read() vs readline() vs readlines()
f.read()       # Entire file as ONE string
f.readline()   # ONE line (with \n)
f.readlines()  # ALL lines as list

# TRAP 2: writelines() does NOT add newlines
f.writelines(['a', 'b', 'c'])  # Writes 'abc', not 'a\nb\nc\n'

# TRAP 3: 'w' mode TRUNCATES existing files
with open('existing.txt', 'w') as f:  # File is now EMPTY
    f.write('new content')

# TRAP 4: readline() includes \n
line = f.readline()  # 'hello\n'
line = line.strip()  # 'hello' (use strip() to remove)
```

### File I/O Quick Reference

| Function | Description | Returns |
|----------|-------------|---------|
| `open(path, mode)` | Open file | File object |
| `f.read()` | Read entire file | String |
| `f.read(n)` | Read n characters | String |
| `f.readline()` | Read one line | String (with \n) |
| `f.readlines()` | Read all lines | List of strings |
| `f.write(s)` | Write string | Number of chars |
| `f.writelines(lst)` | Write list of strings | None |
| `f.tell()` | Get position | Integer |
| `f.seek(pos)` | Move to position | New position |
| `f.close()` | Close file | None |

---

## PCAP Traps - All Modules

1. **`sys.argv[0]`** is the script name, not the first argument
2. **`sys.exit()`** without argument exits with code 0 (success)
3. **`os.path.join()`** is preferred over string concatenation for paths
4. **`os.makedirs()`** creates all intermediate directories, `os.mkdir()` doesn't
5. **`os.rmdir()`** only works on EMPTY directories
6. **`os.environ.get()`** is safer than `os.environ[]` (returns None vs raises KeyError)
7. **`strftime`** = format (dt→str), **`strptime`** = parse (str→dt)
8. **`f.read()`** reads entire file, **`f.readline()`** reads ONE line
9. **`f.writelines()`** does NOT add newlines automatically
10. **`'w'` mode TRUNCATES** existing files - use `'a'` to append
