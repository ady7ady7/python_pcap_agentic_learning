# Week 13 Day 2 — Heavy Gap Review
**Date:** 2026-04-08 | **Focus:** repr(e)/e.args deep drill, then all active gaps

---

## Task 1 — `repr(e)`, `e.args`, `str(e)`: heavy volume until it clicks

**TEACH — the three separate things, once and for all:**

```
e.args     → a TUPLE. Set by Exception.__init__() via super().__init__(*stuff).
             Whatever you pass to super().__init__() becomes e.args.
             If you don't call super().__init__(), e.args = ().

str(e)     → calls __str__. If you defined __str__, that runs.
print(e)   → same as str(e).
             If NO __str__ defined, Python falls back to str(e.args[0]) if len==1,
             or str(e.args) if multiple.

repr(e)    → calls __repr__. Default is: ClassName(arg1, arg2, ...)
             where the args come from e.args — NOT from __str__.
             __str__ has ZERO effect on repr().
```

**The key insight about `ClassName(args)` in repr:**
```python
# e.args = ('not found',)
# repr(e) → "AppError('not found')"
#            ^^^^^^^^  ^^^^^^^^^^^
#            class     e.args unpacked

# e.args = ('not found', 404)
# repr(e) → "AppError('not found', 404)"

# e.args = ()   (no super().__init__() called)
# repr(e) → "AppError()"
```

---

**Example 1 — no `__str__`, one arg passed to super():**
```python
class E1(Exception):
    def __init__(self, msg):
        super().__init__(msg)   # msg goes into e.args

e = E1("something broke")
print(str(e))     # 'something broke'   ← e.args[0] since len==1
print(repr(e))    # "E1('something broke')"
print(e.args)     # ('something broke',)
```

**Example 2 — with `__str__`, one arg:**
```python
class E2(Exception):
    def __init__(self, msg):
        super().__init__(msg)
    def __str__(self):
        return "CUSTOM MESSAGE"

e = E2("something broke")
print(str(e))     # 'CUSTOM MESSAGE'        ← __str__ wins
print(repr(e))    # "E2('something broke')" ← __str__ has NO effect on repr
print(e.args)     # ('something broke',)    ← unaffected by __str__
```

**Example 3 — two args passed to super():**
```python
class E3(Exception):
    def __init__(self, code, msg):
        super().__init__(code, msg)   # BOTH go into e.args

e = E3(404, "not found")
print(str(e))     # '(404, \'not found\')'  ← multiple args: str(e.args)
print(repr(e))    # "E3(404, 'not found')"  ← both args in repr
print(e.args)     # (404, 'not found')
```

**Example 4 — extra attributes, only msg to super():**
```python
class E4(Exception):
    def __init__(self, code, msg):
        super().__init__(msg)   # only msg goes to super → e.args = (msg,)
        self.code = code        # code is just an instance attr, NOT in e.args

e = E4(404, "not found")
print(str(e))     # 'not found'           ← e.args[0]
print(repr(e))    # "E4('not found')"     ← only msg in args
print(e.args)     # ('not found',)        ← code NOT here
print(e.code)     # 404                   ← separate instance attr
```

**Example 5 — NO super().__init__() call:**
```python
class E5(Exception):
    def __init__(self, msg):
        self.msg = msg          # super() NOT called → e.args = ()

e = E5("something broke")
print(str(e))     # ''                    ← empty args → empty str
print(repr(e))    # "E5()"               ← empty args
print(e.args)     # ()
print(e.msg)      # 'something broke'    ← only reachable as e.msg
```

---

**A)** Now predict — no peeking at the examples:

```python
class PriceError(Exception):
    def __init__(self, price, reason):
        super().__init__(reason)    # only reason goes to super
        self.price = price
    def __str__(self):
        return f"Bad price {self.price}: {self.args[0]}"

e = PriceError(-5, "negative")
print(str(e))
print(repr(e))
print(e.args)
print(e.price)
```

**B)** Predict:
```python
class ConnError(Exception):
    def __init__(self, host, port, msg):
        super().__init__(host, port, msg)   # all three to super

e = ConnError("localhost", 5432, "timeout")
print(str(e))
print(repr(e))
print(e.args)
print(len(e.args))
```

**C)** Predict:
```python
class SimpleError(Exception):
    pass   # no __init__, no __str__

e = SimpleError("oops")
print(str(e))
print(repr(e))
print(e.args)
```

**D)** Multiple choice — given `class E(Exception): def __str__(self): return "hi"` and `e = E("ignored")`:
- A: `repr(e) == "hi"`
- B: `e.args == ("ignored",)`
- C: `e.args == ()`
- D: `str(e) == "ignored"`

Write answers here:


```
A) str, repr, args, price:
print(str(e)) #Bad price -5: negative
print(repr(e)) #PriceError('negative')
print(e.args) #('negative',)
print(e.price) #-5

B) str, repr, args, len:
print(str(e)) #('localhost', 5432, 'timeout)
print(repr(e)) #ConnError('localhost', 5432, 'timeout)
print(e.args) #('localhost', 5432, 'timeout)
print(len(e.args)) #3



C) str, repr, args:

# class SimpleError(Exception): #this example is very unintuitive still
#     pass   # no __init__, no __str__

# e = SimpleError("oops")
# print(str(e)) #oops
# print(repr(e)) #SimpleError('oops')
# print(e.args) #('oops',)


D)
A: False
B: True
C: False
D: False

```

---

## Task 2 — `rfind` vs `rindex` — one clean drill

**Rule:** `rfind`/`rindex` are identical to `find`/`index` except they search from the RIGHT (return the last occurrence index).

```
find   → last occurrence? No. First. Returns -1 if not found.
rfind  → last occurrence. Returns -1 if not found.    ← NO raise
index  → first occurrence. Raises ValueError if not found.
rindex → last occurrence. Raises ValueError if not found. ← DOES raise
```

**A)** Predict each — output or exception:
```python
s = "abracadabra"
print(s.find('a'))      # first 'a'
print(s.rfind('a'))     # last 'a'
print(s.index('a'))     # first 'a'
print(s.rindex('a'))    # last 'a'
print(s.find('z'))      # not found
print(s.rfind('z'))     # not found
print(s.index('z'))     # not found
print(s.rindex('z'))    # not found
```

Write answers here:
```
A)
print(s.find('a'))      #0
print(s.rfind('a'))     #10
print(s.index('a'))     #0
print(s.rindex('a'))    #10
print(s.find('z'))      #-1
print(s.rfind('z'))     #-1
print(s.index('z'))     #valueError
print(s.rindex('z'))    #valueError

```

---

## Task 3 — Name mangling: compile-time resolution drill [recurring gap]

**A)** Predict — 3-level chain, no `get()` in C:
```python
class X:
    __val = 'x'
    def show(self): return self.__val

class Y(X):
    __val = 'y'
    def show(self): return self.__val

class Z(Y):
    __val = 'z'

obj = Z()
print(obj.show())          # which show() runs? what does it return?
print(obj._Z__val)
print(obj._Y__val)
print(obj._X__val)
```

**B)** True or False:
```python
print(hasattr(Z, 'show'))       # ?
print('show' in Z.__dict__)     # ?
print('show' in Y.__dict__)     # ?
print(Z.__bases__ == (Y,))      # ?
print(Y in Z.__mro__)           # ?
```

Write answers here:
```
A) 
print(obj.show())   #y
print(obj._Z__val) #'z'
print(obj._Y__val) #'y'
print(obj._X__val) #'x'

B)
print(hasattr(Z, 'show'))       #False
print('show' in Z.__dict__)     #False
print('show' in Y.__dict__)     #True
print(Z.__bases__ == (Y,))      #True
print(Y in Z.__mro__)           #True

```

---

## Task 4 — Assert propagation + exception routing [Q10 real exam pattern]

**A)** Trace and predict output — 3 variants:

```python
# Variant 1
result = 0
def compute(n):
    assert n > 0
    try:
        return 100 / n
    except ZeroDivisionError:
        raise RuntimeError("div fail")

try:
    compute(0)
except RuntimeError:
    result = 1
except AssertionError:
    result = 2
except:
    result = 3
print(result)
```

```python
# Variant 2
result = 0
def compute(n):
    assert n > 0
    try:
        return 100 / n
    except ZeroDivisionError:
        raise RuntimeError("div fail")

try:
    compute(-1)
except RuntimeError:
    result = 1
except AssertionError:
    result = 2
except:
    result = 3
print(result)
```

```python
# Variant 3
result = 0
def compute(n):
    assert n > 0
    try:
        return 100 / n
    except ZeroDivisionError:
        raise RuntimeError("div fail")

try:
    compute(5)
except RuntimeError:
    result = 1
except AssertionError:
    result = 2
except:
    result = 3
print(result)
```

Write answers here:
```
Variant 1 trace + output:
result = 0
def compute(n):
    assert n > 0 #1.This assertion fails inside -> raises AssertionError
    try:
        return 100 / n
    except ZeroDivisionError:
        raise RuntimeError("div fail")

try:
    compute(0) # 2. The error is unhandled inside the compute function, so it propagates to the outside
except RuntimeError:
    result = 1
except AssertionError: # 3. This handle handles the AssertionError
    result = 2
except:
    result = 3
print(result) #2


Variant 2 trace + output:

basically the same as above, why?
The result is 2 again.

Variant 3 trace + output:
result = 0
def compute(n):
    assert n > 0 #1. this time the assertion is correct
    try:
        return 100 / n #This works properly, returning the result (20)
    except ZeroDivisionError:
        raise RuntimeError("div fail")

try:
    compute(5) 
except RuntimeError:
    result = 1
except AssertionError:
    result = 2
except:
    result = 3
print(result) #0, the result is not updated with the result of compute() function

```

---

## Task 5 — String comparison + list comp: combined PCAP patterns

**A)** Predict True or False:
```python
print('abc' > 'ABC')          # ?
print('abc' == 'ABC'.lower()) # ?
print('Z' > 'a')              # ?
print('' < 'a')               # ?
print('aa' == 'aa ')          # ?
print('1abc' < 'abc')         # ?
```

**B)** Predict the output — real exam list comp patterns:
```python
lst = [i for i in range(6)]
result = [lst[i] for i in range(5, -1, -1) if lst[i] % 2 == 0]
print(result)
```

```python
result = [x ** 2 for x in range(4, 0, -1) if x % 2 != 0]
print(result)
```

Write answers here:
```
A) 6 results:
print('abc' > 'ABC')          # True
print('abc' == 'ABC'.lower()) # True
print('Z' > 'a')              # False
print('' < 'a')               # True
print('aa' == 'aa ')          # False
print('1abc' < 'abc')         # True


B) result 1: [4, 2, 0]
   result 2: [9, 1]
```

---

## Task 6 — PCAP select-two: full mixed simulation

**Q1.** Which expressions always evaluate to True? (Select two)
```python
import random
random.seed(5)
v = random.random()
```
- A: `v >= 1`
- B: `v < 1`
- C: `v >= 0`
- D: `v == 1`

**Q2.** Which of the following are true about exception classes? (Select two)
```python
class AppError(Exception):
    def __init__(self, msg):
        super().__init__(msg)
    def __str__(self):
        return "app error"

e = AppError("details")
```
- A: `str(e) == "app error"`
- B: `e.args == ()`
- C: `repr(e) == "app error"`
- D: `e.args == ("details",)`

**Q3.** Which expressions evaluate to True? (Select two)
```python
class A: pass
class B(A): pass
class C(B): pass
```
- A: `B in C.__bases__`
- B: `A in C.__bases__`
- C: `A in C.__mro__`
- D: `object in C.__bases__`

**Q4.** Which are valid Python? (Select two)
- A: `lambda: 42`
- B: `lambda x: return x`
- C: `lambda x, y=0: x + y`
- D: `lambda x: x if x > 0 else -x`

**Q5.** What is true about the following code? (Select two)
```python
class P:
    __x = 1
    def get(self): return self.__x

class Q(P):
    __x = 2

obj = Q()
```
- A: `obj.get() == 1`
- B: `obj.get() == 2`
- C: `obj._P__x == 1`
- D: `obj._Q__x == 1`

Write answers here:
```
Q1: B, C
Q2: A, D
Q3: A, C
Q4: A, D (a bit confusing though, how about C?)
Q5: A, C
```

---

## Task 7 — `type(e)` + `isinstance` combined [real exam Q11 pattern]

**A)** Predict each:
```python
try:
    {}['missing']
except Exception as e:
    print(type(e).__name__)           # ?
    print(isinstance(e, KeyError))    # ?
    print(isinstance(e, Exception))   # ?
    print(type(e) is Exception)       # ?
    print(type(e) is KeyError)        # ?
```

**B)** Multiple choice — which TWO are True after:
```python
try:
    open('no_such_file_xyz.txt')
except OSError as e:
    pass
```
- A: `type(e) is OSError`
- B: `type(e) is FileNotFoundError`
- C: `isinstance(e, OSError)`
- D: `isinstance(e, FileNotFoundError)`

Write answers here:
```
A) 5 results:
    print(type(e).__name__)           # KeyError
    print(isinstance(e, KeyError))    # True
    print(isinstance(e, Exception))   # True
    print(type(e) is Exception)       # False
    print(type(e) is KeyError)        # True


B) Two True:
B, D
```
