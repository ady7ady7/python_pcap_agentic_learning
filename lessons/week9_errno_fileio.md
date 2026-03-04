# Week 9: File Streams, open() & Diagnosing Errors with `errno`

This lesson covers the full file I/O model — streams, open modes, binary vs text,
predefined streams, the `open()` function — and how Python exposes OS-level error
codes through `IOError.errno` and the `errno` module.

---

## Table of Contents

- [Files and streams](#files-and-streams)
- [Open modes](#open-modes)
- [Binary streams vs text streams](#binary-streams-vs-text-streams)
- [The open() function](#the-open-function)
- [Predefined streams](#predefined-streams)
- [Why errno exists](#why-errno-exists)
- [Reading errno from an exception](#reading-errno-from-an-exception)
- [The errno module](#the-errno-module)
- [Common errno constants](#common-errno-constants)
- [Practical pattern: branching on errno](#practical-pattern-branching-on-errno)
- [PCAP Traps](#pcap-traps)

---

## Files and streams

Before a program can process a file, the file must be **opened**. When you open a
file, Python associates it with a **stream** — an abstract representation of the
physical data stored on the media. When processing is finished, the file must be
**closed** to flush buffers and release the OS file descriptor.

```
Physical file on disk  ←→  Stream object in Python  ←→  Your program
```

The stream is the interface your code works with. You never touch the disk directly —
all reads and writes go through the stream.

---

## Open modes

Three open modes exist:

| Mode | Description |
|---|---|
| **read mode** | Only read operations are allowed. The file must already exist. |
| **write mode** | Only write operations are allowed. Creates the file if it doesn't exist; truncates if it does. |
| **update mode** | Both reads and writes are allowed. |

In `open()` these map to the `mode` argument:

| `mode` string | Meaning |
|---|---|
| `'r'` | Read (text). File must exist. |
| `'w'` | Write (text). Truncates or creates. |
| `'a'` | Append (text). Writes at end; creates if needed. |
| `'x'` | Exclusive create (text). Fails with `FileExistsError` if file exists. |
| `'r+'` | Update (read + write). File must exist. |
| `'rb'`, `'wb'`, `'ab'` | Binary equivalents of the above. |

---

## Binary streams vs text streams

Python uses two different class families depending on the file content:

| Class | Used for | What it handles |
|---|---|---|
| `BufferedIOBase` | **Binary streams** | Any file — images, executables, raw bytes |
| `TextIOBase` | **Text streams** | Human-readable text files divided into lines by newline markers |

When you call `open("file.txt", "r")` you get a `TextIOWrapper` (subclass of `TextIOBase`).
When you call `open("file.bin", "rb")` you get a `BufferedReader` (subclass of `BufferedIOBase`).

```python
f = open("data.txt", "r")
print(type(f))   # <class '_io.TextIOWrapper'>

g = open("data.bin", "rb")
print(type(g))   # <class '_io.BufferedReader'>
```

**Key rule:** Text streams handle encoding/decoding automatically and translate
newlines (`\n` ↔ `\r\n` on Windows). Binary streams pass raw bytes unchanged.

---

## The open() function

Full syntax:

```python
open(file_name, mode=open_mode, encoding=text_encoding)
```

- `file_name` — path to the file (string or path-like object)
- `mode` — open mode string (default: `'r'`)
- `encoding` — text encoding (default: platform-dependent, usually `'utf-8'`); only relevant for text mode

On success, `open()` returns a **stream object** and associates it with the named file.
On failure, it raises an `IOError` (which is `OSError`).

```python
# Always use a context manager — it closes the file automatically
with open("prices.csv", "r", encoding="utf-8") as f:
    content = f.read()
# File is guaranteed closed here, even if an exception occurred
```

Without `with`, you must call `f.close()` manually. Forgetting it leaks a file
descriptor — on long-running programs this causes `errno.EMFILE` (too many open files).

---

## Predefined streams

Three streams are already open when any Python program starts. They come from `sys`:

| Stream | Name | Default | Description |
|---|---|---|---|
| `sys.stdin` | Standard input | keyboard | `input()` reads from here |
| `sys.stdout` | Standard output | terminal | `print()` writes here |
| `sys.stderr` | Standard error | terminal | Error messages and tracebacks go here |

```python
import sys

sys.stdout.write("hello\n")   # same as print("hello")
sys.stderr.write("error!\n")  # goes to stderr, not stdout

line = sys.stdin.readline()   # reads one line from keyboard
```

These can be **redirected** at the OS level (e.g., `python script.py > output.txt`)
or reassigned in Python:

```python
import sys

sys.stdout = open("log.txt", "w")  # redirect all print() to a file
print("this goes to log.txt")
```

**PCAP note:** `sys.stdin`, `sys.stdout`, `sys.stderr` are text streams
(instances of `TextIOWrapper`). They are opened automatically — you never call
`open()` for them.

---

## Why errno exists

When an OS call fails (opening a file, writing to a stream, etc.), the operating system
sets a numeric error code describing what went wrong. Python surfaces this code through
the `errno` attribute on `OSError` (and its aliases `IOError`, `EnvironmentError`).

Knowing the exact numeric code lets you **branch your error handling** — responding
differently to "file not found" vs "permission denied" vs "disk full".

---

## Reading errno from an exception

```python
try:
    # Some stream operation
    with open("secret.txt", "w") as f:
        f.write("data")
except IOError as exc:
    print(exc.errno)      # integer error code, e.g. 13
    print(exc.strerror)   # human-readable message, e.g. "Permission denied"
    print(exc.filename)   # the file name involved, if any
```

`IOError` is an **alias** for `OSError` in Python 3 — they are the same class.
`EnvironmentError` is also an alias. All three catch the same exceptions.

```python
print(IOError is OSError)          # True
print(EnvironmentError is OSError) # True
```

---

## The errno module

```python
import errno
```

The `errno` module exposes symbolic constants that map to the OS numeric codes.
You compare `exc.errno` against these constants instead of hard-coding integers.

```python
import errno

try:
    open("missing.txt")
except IOError as exc:
    if exc.errno == errno.ENOENT:
        print("File does not exist — handle gracefully")
    elif exc.errno == errno.EACCES:
        print("No permission — inform the user")
    else:
        raise  # re-raise anything we don't specifically handle
```

---

## Common errno constants

| Constant | Value (Linux) | Meaning |
|---|---|---|
| `errno.EACCES` | 13 | **Permission denied** — tried to open a read-only file for writing, or access without rights |
| `errno.EBADF` | 9 | **Bad file number** — operating on a stream that is not open |
| `errno.EEXIST` | 17 | **File exists** — tried to create/rename a file to a name that already exists |
| `errno.EFBIG` | 27 | **File too large** — tried to write a file exceeding the OS maximum size |
| `errno.EISDIR` | 21 | **Is a directory** — used a directory path where an ordinary file was expected |
| `errno.EMFILE` | 24 | **Too many open files** — exceeded the OS limit on simultaneously open file descriptors |
| `errno.ENOENT` | 2 | **No such file or directory** — tried to access a path that does not exist |
| `errno.ENOSPC` | 28 | **No space left on device** — disk is full |

> **Note:** Numeric values differ between operating systems (Windows vs Linux vs macOS).
> Always use the **symbolic constant** (`errno.ENOENT`), never the raw integer.

---

## Practical pattern: branching on errno

```python
import errno

def safe_read(filepath: str) -> str | None:
    """Read a file and return its content, or None on known errors."""
    try:
        with open(filepath, "r") as f:
            return f.read()
    except IOError as exc:
        if exc.errno == errno.ENOENT:
            print(f"File not found: {filepath}")
        elif exc.errno == errno.EACCES:
            print(f"Permission denied: {filepath}")
        elif exc.errno == errno.EISDIR:
            print(f"Path is a directory, not a file: {filepath}")
        else:
            print(f"Unexpected IO error [{exc.errno}]: {exc.strerror}")
        return None
```

The `else` branch re-raises (or logs) anything not explicitly handled —
this is the **safe default**. Never silently swallow unknown errors.

---

## PCAP Traps

### Trap 1: `IOError`, `OSError`, `EnvironmentError` are the same class

```python
try:
    open("x.txt")
except OSError as exc:
    print(type(exc))  # <class 'FileNotFoundError'>
```

`FileNotFoundError` is a **subclass** of `OSError`. Catching `OSError` catches it.
Catching `IOError` also catches it. They are all the same parent.

Hierarchy (simplified):
```
BaseException
└── Exception
    └── OSError  (= IOError = EnvironmentError)
        ├── FileNotFoundError   (errno.ENOENT)
        ├── PermissionError     (errno.EACCES)
        ├── FileExistsError     (errno.EEXIST)
        ├── IsADirectoryError   (errno.EISDIR)
        └── BlockingIOError     (errno.EAGAIN)
```

Python 3.3+ introduced these **named subclasses** so you can catch them directly
without checking `errno` at all:

```python
# Modern Python 3.3+ style — preferred
try:
    open("missing.txt")
except FileNotFoundError:
    print("Not found")
except PermissionError:
    print("No access")
```

```python
# Classic style — still valid, required knowledge for PCAP
try:
    open("missing.txt")
except IOError as exc:
    if exc.errno == errno.ENOENT:
        print("Not found")
```

**PCAP tests both styles. Know them both.**

---

### Trap 2: `errno` attribute vs the `errno` module

These are two different things with the same name:

```python
import errno                  # the MODULE with symbolic constants

try:
    open("x.txt")
except IOError as exc:
    print(exc.errno)          # the ATTRIBUTE on the exception (an int)
    print(errno.ENOENT)       # the CONSTANT from the module (also an int)
    print(exc.errno == errno.ENOENT)  # True — this is how you compare
```

---

### Trap 3: `exc.errno` can be `None`

Not every `OSError` subclass sets `errno`. If the exception was raised manually
(e.g., `raise OSError("custom message")`), `exc.errno` is `None`.
Always guard if writing generic handlers:

```python
except IOError as exc:
    if exc.errno is not None and exc.errno == errno.ENOENT:
        ...
```

---

### Trap 4: except ordering with OSError subclasses

The same parent-before-child rule applies here. If you catch `OSError` before
`FileNotFoundError`, the child clause is **never reached**:

```python
# WRONG — FileNotFoundError is never reached
try:
    open("x.txt")
except OSError:
    print("OSError")          # catches FileNotFoundError here
except FileNotFoundError:
    print("FileNotFoundError")  # dead code

# CORRECT
try:
    open("x.txt")
except FileNotFoundError:
    print("FileNotFoundError")  # specific first
except OSError:
    print("OSError")            # generic fallback
```

---

### Trap 5: `open()` with mode `'x'` raises `FileExistsError`

```python
try:
    open("existing.txt", "x")  # exclusive create — fails if file exists
except FileExistsError:
    print("Already exists")    # errno.EEXIST under the hood
```

---

## Quick-reference card

```
errno constant      Named subclass (Py 3.3+)    Cause
─────────────────────────────────────────────────────────────────────────
errno.ENOENT   →  FileNotFoundError          File/dir does not exist
errno.EACCES   →  PermissionError            No read/write permission
errno.EEXIST   →  FileExistsError            File already exists
errno.EISDIR   →  IsADirectoryError          Dir used where file expected
errno.EBADF    →  (no direct subclass)       Operating on closed stream
errno.EFBIG    →  (no direct subclass)       File exceeds OS size limit
errno.EMFILE   →  (no direct subclass)       Too many open file descriptors
errno.ENOSPC   →  (no direct subclass)       Disk full
```

---

*Next: Apply `errno` knowledge in exception-handling exercises (Week 9 Day 3+).*
