# Week 12 Day 1 — Exceptions Deep Dive + All Gap Scaffolding
**Date:** 2026-03-30 | **Focus:** Exceptions (36% on real exam) + ALL identified gaps touched daily

---

## Task 1 — `type(e)` trap [Real exam Q11]

**TEACH:** `type(e)` returns the **actual class the object was raised as** — not the handler's label.
Catching with `BaseException` does NOT change what `type(e)` returns.
```python
# Mental model: cage labelled "Animal" still contains a dog.
# type() tells you what's IN the cage, not the cage label.
```

**A)** Predict the output of each:
```python
# Snippet 1
try:
    {}['missing']
except BaseException as e:
    print(type(e).__name__)

#KeyError
#if we printed e, it would be 'missing'

# Snippet 2
try:
    raise FileNotFoundError("gone")
except OSError as e:
    print(type(e).__name__) #FileNotFoundError
    print(isinstance(e, OSError)) #True
    print(isinstance(e, FileNotFoundError)) #True

#if we printed e, it would be 'gone'

# Snippet 3
try:
    int("abc")
except Exception as e:
    print(type(e) is ValueError) #True
    print(type(e) is Exception) #False
```

**B)** Which expression evaluates to `True` after this runs?
```python
try:
    1 / 0
except ArithmeticError as err:
    pass
```
- `type(err) is ArithmeticError` #False
- `type(err) is ZeroDivisionError` #True
- `type(err).__name__ == 'ArithmeticError'` #False
- `isinstance(err, ZeroDivisionError)` #True



Write your answers here:
```
A) Snippet 1: KeyError
   Snippet 2: FileNotFoundError, True, True
   Snippet 3: True, False

B) True expressions:
False, True, False, True (2, 4)

```

---

## Task 2 — `raise` inside `except` + bare `except` position [Real exam Q8, Q10]

**TEACH — `raiseX` no space:**
```python
raise ValueError    # statement — raises ValueError
raiseValueError     # name lookup — NameError if undefined (NOT SyntaxError!)
```
This looks syntactically valid — Python discovers the bug at RUNTIME.

**TEACH — bare `except` position:**
```python
# ILLEGAL — SyntaxError:
try: ...
except:    # bare except MUST be last
    pass
except ValueError:
    pass

# LEGAL — bare except last:
try: ...
except ValueError:
    pass
except:
    pass
```

**A)** Will each snippet raise an exception? If yes, which one and when (parse time vs runtime)?
```python
# Snippet 1
try:
    x = 1
except:
    pass
except ValueError:
    pass

#Yes, I think it's parse time error - a SyntaxError, as the bare except is first.


# Snippet 2
def foo():
    raiseRuntimeError

foo()

#NameError, undefined.
#But next time, I think it's a typo on my end and the gap is NOT connected with a lack of space - the space probably was there in the original.

# Snippet 3
try:
    raise IndexError
except TypeError:
    raiseValueError
except:
    print("caught")
```

**B)** What does this print? (This is Q10 from your real exam — trace it step by step)
```python
m = 0

def foo(n):
    global m
    assert m != 0 #I assumed THIS WOULD CAUSE AN AssertionError, as it's not even put in the try/except block. For some reason it doesn't trigger an assertion error or crash the code. Why?
    try:
        return 1/n
    except ArithmeticError:
        raise ValueError #This is MY TYPO - the original was with space, and I fixed that accordingly! The gap is not about space. Adjust that for every next time we address this and similar examples.

try:
    foo(0)
except ArithmeticError:
    m += 2
except:
    m += 1
print(m) #It returns 1, but I'm really not sure why.
#From my information, ZeroDivisonError is an ArithmethicError, so it should add 2 to m, and make it 2?
#What am I missing here? Why is that the case? How to avoid getting trapped in similar scenarios?
```

Write your answers here:
```
A) Snippet 1: SyntaxError 
   Snippet 2: NameError, but honestly THIS IS NOT THE REAL ISSUE. The space was in the original, I just made a typo there.
   Snippet 3: It prints caught - if we assume it's written correctly. It's weird for me though.

B) Output:
   Trace (step by step):

#It returns 1, but I'm really not sure why.
#First of all, I'd exdpect the AssertionError to trigger at assert m != 0, as it's literally 0
#From my information, ZeroDivisonError is an ArithmethicError, so it should add 2 to m, and make it 2?
#What am I missing here? Why is that the case? How to avoid getting trapped in similar scenarios?

```

---

## Task 3 — Custom exception class + `print(e)` vs `str(e)` vs `repr(e)` [Real exam Q7]

**TEACH:** When you define `__str__` on a custom exception:
- `print(e)` calls `__str__`
- `str(e)` calls `__str__`
- `repr(e)` calls `__repr__` (default: `ClassName(args)`)
- `print(type(e).__name__)` → class name string

**TEACH — Q7 from your real exam:**
```python
class E(Exception):
    def __init__(self, message):
        self.message = message     # NOT passed to super().__init__()!
    def __str__(self):
        return "it's nice to see you"
```
Notice: `super().__init__()` is NOT called with `message`. So `str(e)` uses your `__str__`, which returns the hardcoded string — NOT the message.

**A)** Predict the output:
```python
class AppError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.code = 500

    def __str__(self):
        return f"AppError[{self.code}]"

try:
    raise AppError("server down")
except AppError as e:
    print(e) #AppError[500]
    print(str(e)) #AppError[500]
    print(e.args[0]) #server down - this is very unintuitive
    print(type(e).__name__) #AppError
```

**B)** Now WITHOUT calling `super().__init__(msg)` — what changes?
```python
class AppError(Exception):
    def __init__(self, msg):
        self.code = 500          # no super().__init__()
    def __str__(self):
        return f"AppError[{self.code}]"

try:
    raise AppError("server down")
except AppError as e:
    print(e) #AppError[500] - it's literally the same, so what's the point in showing a difference here?
    print(e.args) #('server down',) - BUT WHAT ARE YOU TRYING TO SHOW HERE? Above example would print the same if we printed e.args - What's the fucking difference, as I see none...
```

**C)** Write a custom exception `InvalidPriceError` that:
- Takes `price` (float) and `reason` (str) in `__init__`
- Stores them as attributes
- `__str__` returns: `f"Invalid price {price}: {reason}"`
- Raise it with a negative price and catch it, printing the exception

Write your answers here:
```
A) Output:

B) Output + args:

C) Code:



class InvalidPriceError(Exception):
    def __init__(self, price: float, reason: str):
        self.reason = reason
        self.price = price
    
    def __str__(self):
        return f'Invalid price {self.price}: {self.reason}'
    

def mock_func(a, b):
    if a < 0 or b < 0:
        raise InvalidPriceError((a), 'Lol')

mock_func(-1, 5)

$ python practice.py
Traceback (most recent call last):
  File "C:\Users\HARDPC\Desktop\AL\projekty\python_pcap_agentic_learning\practice.py", line 12960, in <module>
    mock_func(-1, 5)
    ~~~~~~~~~^^^^^^^
  File "C:\Users\HARDPC\Desktop\AL\projekty\python_pcap_agentic_learning\practice.py", line 12958, in mock_func
    raise InvalidPriceError((a), 'Lol')
InvalidPriceError: Invalid price -1: Lol
(.venv) 

```

---

## Task 4 — `__bases__`, `__mro__`, `__dict__` [Real exam Q29]

**TEACH:**
```
__bases__  → tuple of DIRECT parents only
__mro__    → tuple of full resolution chain (includes object at end)
__dict__   → namespace dict — class attrs on class, instance attrs on instance
```
Real exam Q29 asked for the attribute storing superclasses → answer is `__bases__`, not `__super__` or `__ancestors__`.

**A)** Given:
```python
class A:
    x = 10
    def __init__(self):
        self.y = 20

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

d = D()
```
Predict True or False for each:
```python
print(A in D.__bases__)         #False
print(A in D.__mro__)           #True
print(len(D.__bases__))         # 2
print(len(D.__mro__))           # 5 (D - B - C - A - OBJECT)
print('x' in D.__dict__)        # False
print('x' in A.__dict__)        # True
print('y' in A.__dict__)        # #True - it's seen in static_attributes, not sure if this is meant
print('y' in d.__dict__)        # #True, clearly seen in a dict
```

**B)** Multiple choice (real exam style): Which expression evaluates to True?
- `B in D.__bases__` #True
- `C in D.__bases__` #True
- `A in D.__bases__` #False
- `object in D.__bases__`  #False

Write answers here:
```
A) Results:

B) True expressions:

Already answered above.
```

---

## Task 5 — Lambda edge cases [Real exam Q34, Q36]

**TEACH — Q34 traps:**
```
"Cannot return None"              → FALSE — lambdas CAN return None
"Cannot be defined without params"→ FALSE — lambda: 42 is valid
"Must contain return keyword"     → FALSE — return is implicit
"Are anonymous functions"         → TRUE
"Can be defined without params"   → TRUE
```

**TEACH — Q36 naming trap:**
When a lambda is passed as an argument AND has the same param name as the outer function param, rename mentally:
```python
def foo(x, y, z):          # x here is the FUNCTION
    return x(y) - x(z)     # x(y) = call that function with y

print(foo(lambda x: x % 2, 2, 1))
# Rename: fn = lambda n: n%2, a=2, b=1
# fn(2) - fn(1) = 0 - 1 = -1
```

**A)** True or False:
```
1. lambda: 42               — valid Python? #Yes
2. lambda x: print(x)      — can this return None? #Supposedly, but I don't see it printing None
3. f = lambda: None; f()   — what does f() return? #It returns None
4. lambda x, y: x + y      — valid (multi-param)? #Yes
5. lambda x: return x + 1  — valid Python? #NO, THIS IS A SYNTAX ERROR!
6. result = (lambda x: x**2)(5) — what is result? #25

Although I'm still kinda puzzled in terms of what is an argument, waht is a parameter, what's the differene and how to remember that.
```

**B)** Predict the output:
```python
def apply(fn, a, b):
    return fn(a) + fn(b)

print(apply(lambda x: x ** 2, 3, 4)) #fn(3) + fn(4) = 9 + 16 = 25
print(apply(lambda x: x % 2, 7, 4)) #fn(7) + fn(4) = 1 + 0 = 1

#Now it looks much more clear, definitely we still need to practice this pattern
```

**C)** Predict the output (harder — Q36 exact pattern):
```python
def foo(x, y, z):
    return x(y) - x(z)

print(foo(lambda x: x % 2, 2, 1)) # foo(2) - foo(1) = 0 - 1 = -1
print(foo(lambda x: x * 3, 5, 2)) # foo(5) - foo(2) = 15 - 6 = 9
```

Write answers here:
```
A) 1-6:

B) Output:

C) Output:

Answers already given above
```

---

## Task 6 — List comprehension order + `open()` modes [Real exam Q35, Q39]

**TEACH — Q39 order trap:**
```python
range(4, 0, -1) → iterates: 4, 3, 2, 1 (DESCENDING)
# Result preserves ITERATION ORDER, not sorted order
# If you iterate 4→3→2→1 and pick odds: 3, 1 → output [3, 1] not [1, 3]
```

**TEACH — Q35 open() traps:**
```
Default mode    → 'r' (NOT 'w'!)
'w' mode        → truncates all previous content
'a' mode        → appends (safe for logs)
'x' mode        → fails if file already exists
'r+' mode       → read+write, file MUST exist
```

**A)** Predict the output:
```python
my_list = [0, 1, 2, 3, 4]
m = [my_list[i] for i in range(4, 0, -1) if my_list[i] % 2 != 0]
print(m) #[3, 1]
```

**B)** What does each print?
```python
evens = [x for x in range(10, 0, -2)]
print(evens) #[10, 8, 6, 4, 2]

squares = [x**2 for x in range(5, 0, -1) if x % 2 == 0]
print(squares) #[16, 4]
```

**C)** True or False about `open()`:
```
1. open('f.txt') is equivalent to open('f.txt', 'r') #Yes, because 'r' is the default mode
2. The default mode is 'w' #No!
3. open('f.txt', 'w') loses previous file contents #Yes
4. open('f.txt', 'a') creates the file if it doesn't exist #Yes
5. open('f.txt', 'x') fails if the file already exists #Yes
6. open('f.txt', 'r') raises FileNotFoundError if file missing #Yes
```

Write answers here:
```
A) Output: [3, 1]

B) evens: [10, 8, 6, 4, 2]
   squares: [16, 4]

C) 1-6:
True, False, True, True, True, True


```

---

## Task 7 — `2.` float syntax + numeric literals + `platform` [Real exam Q1, Q32]

**TEACH — Q32 trap:**
`2.` is VALID Python — same as `2.0`. The exam uses it to make you think it's a SyntaxError.

**TEACH — All valid numeric literals:**
```python
2.          # float: 2.0       ← real exam trap
1_000_000   # int with underscores
0xFF        # hex int: 255
0o77        # octal int: 63
0b1010      # binary int: 10
3+2j        # complex number
```

**TEACH — Q1 platform trap:**
```python
platform.platform()      # full platform string: 'Windows-10-...'
platform.system()        # just OS name: 'Windows'
platform.uname()         # namedtuple with ALL info — NOT just platform name
platform.python_version()# Python version: '3.11.4'
```
Q1 asked "underlying platform name" → `platform.platform()`, NOT `platform.uname()`

**A)** Valid or SyntaxError?
```python
x = 2.          # ?
y = .5          # ?
z = 1_000_000   # ?
a = 0xFF        # ?
b = 0o79        # ?  ← careful #This is False, but I had to check it. Honestly I doubt this will be at REAL PCAP exam. The float trap and maybe bytes is maximum we can get.
c = 0b1020      # ?  ← careful
d = 3+2j        # ?

This is a bit too much.
We need to know the float trap + bytes potentially, with bytearray and potential traps there though.

```

**B)** Predict the output:
```python
x = 8 ** (1/3)
y = 2. if x < 2.3 else 3.
print(y)
print(type(y))
```

**C)** Multiple choice — which platform function returns the platform name string (not a tuple/namedtuple)?
- `platform.platform()`
- `platform.uname()`
- `platform.system()`
- `platform.processor()`

Write answers here:
```
A) x, y, z, a, b, c, d: This is a bit too much - an overkill. We need to know the FLOAT trap, maybe also the 1_000_00 trap, as it's a bit sneaky + bytes (with bytearray), as they are included in the file I/O seciton. Make sure we adapt to that next time. But do not take away points for this 

B) Output: 2.0, float

C) Answer: #platform.platform()
But we still definitely need to practice all of these, not just platform.platform(), with information and same about os. There might be questions about different commands, functions etc.
```

---

## Task 8 — Name mangling + inheritance [Real exam Q24]

**TEACH — this was Q24 on your real exam:**
Name mangling is resolved at **compile time** based on where the **method is defined**, NOT where the instance is created.

```python
class A:
    __x = 1           # stored as _A__x
    def get(self): return self.__x   # compiled: self._A__x

class B(A):
    __x = 2           # stored as _B__x
    def get(self): return self.__x   # compiled: self._B__x

class C(B):
    __x = 3           # stored as _C__x
    # NO get() method defined here!
```

`C` has no `get()`. MRO: C → B → A. `obj_c.get()` resolves to `B.get()`.
Inside `B.get()`, `self.__x` was compiled as `self._B__x` = **2**.
Python does NOT re-mangle at runtime based on the instance's class.

**A)** Predict output:
```python
class A:
    __VarA = 1
    def get(self): return self.__VarA

class B(A):
    __VarA = 2
    def get(self): return self.__VarA

class C(B):
    __VarA = 3

obj_a = A()
obj_b = B()
obj_c = C()

print(obj_a.get())
print(obj_b.get())
print(obj_c.get())       # KEY QUESTION — what is this?
print(obj_c._C__VarA)
print(obj_c._B__VarA)
```

**B)** True or False (real exam Q24 options):
```
1. hasattr(B, 'get')                  # True
2. obj_c.get() == 2                   # True
3. isinstance(obj_b, C)               # False
4. C._C__VarA == 3                    # True
5. obj_c._A__VarA == 1                # True
```

Write answers here:
```
A) Output: 1, 2, 2, 3, 2
 
B) 1-5: True, True, False, True, True
```
