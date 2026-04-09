# Week 13 Day 3 — Gap Closure + PCAP Exam Traps
**Date:** 2026-04-09 | **Focus:** hasattr/MRO (3x gap), sys internals, lambda traps, str(obj) default, open() modes, project fix

---

## Task 1 — `hasattr` vs `__dict__` — FINAL closure [appeared 3 sessions running]

**THE RULE:**
```
hasattr(X, 'name')     → searches the FULL MRO chain. Returns True if found ANYWHERE.
'name' in X.__dict__   → searches ONLY X's own namespace. Inherited attrs = False.
'name' in obj.__dict__ → searches the INSTANCE's own namespace. Class attrs = False.
```

**A)** Predict each — no peeking:
```python
class Animal:
    legs = 4
    def breathe(self): pass

class Dog(Animal):
    def bark(self): pass

class Poodle(Dog):
    pass

p = Poodle()
p.name = "Fifi"
```

For each, write True or False:
```
print(hasattr(Poodle, 'bark'))       # True
print(hasattr(Poodle, 'breathe'))    # #True
print(hasattr(Poodle, 'legs'))       # #True
print('bark' in Poodle.__dict__)     # False
print('breathe' in Poodle.__dict__)  # #False
print('legs' in Poodle.__dict__)     # #False
print('bark' in Dog.__dict__)        # #True
print('name' in p.__dict__)          # #True
print('bark' in p.__dict__)          # #False
print('legs' in p.__dict__)          # #False
```

**B)** Multiple choice — which TWO are True after the code in A?
- A: `hasattr(p, 'name')` → True
- B: `'name' in Poodle.__dict__` → True
- C: `hasattr(p, 'breathe')` → True
- D: `'breathe' in p.__dict__` → True

A, C

**C)** One-line rule — complete the blank:
```
hasattr() checks ____ MRO chain | __dict__ checks ____ namespace only
```

Write answers here:
```
A) 10 results:
print(hasattr(Poodle, 'bark'))       # True
print(hasattr(Poodle, 'breathe'))    # #True
print(hasattr(Poodle, 'legs'))       # #True
print('bark' in Poodle.__dict__)     # False
print('breathe' in Poodle.__dict__)  # #False
print('legs' in Poodle.__dict__)     # #False
print('bark' in Dog.__dict__)        # #True
print('name' in p.__dict__)          # #True
print('bark' in p.__dict__)          # #False
print('legs' in p.__dict__)          # #False


B) Two True:
A, C


C) Rule:
WHOLE MRO chain, given object/class namespace only (depending on how we call it)
```

---

## Task 2 — `sys` internals: `sys.path`, `sys.modules`, `sys.argv` [Q5 and recurring]

**THE RULES:**
```
sys.path      → list[str]   — directories where Python searches for modules
sys.modules   → dict        — maps module name (str) → module object (already imported)
sys.argv      → list[str]   — argv[0] = script name, argv[1:] = arguments
sys.argv[0]   → always the script name, even if no args passed
```

**A)** Predict True or False — pure type checks:
```python
import sys
print(type(sys.path) is list)
print(type(sys.modules) is dict)
print(isinstance(sys.path, list))
print(type(sys.argv) is list)
print(type(sys.argv[0]) is str)



```

**B)** Given: script run as `python myscript.py alpha 42`

Predict:
```python
import sys
print(sys.argv[0])         #myscript.py
print(sys.argv[1])         #alpha
print(sys.argv[2])         #42
print(type(sys.argv[2]))   #str
print(len(sys.argv))       #3
```

**C)** True or False:
```python
import sys
# 'sys' is already imported
print('sys' in sys.modules)          # ?
print('os' in sys.modules)           # ?  ← hint: not imported yet
import os
print('os' in sys.modules)           # ?  ← now?


```

**D)** Multiple choice — which statement is correct?
- A: `sys.path` is a tuple
- B: `sys.modules` is a list of module names
- C: `sys.argv[0]` is always the script filename
- D: `sys.modules` contains only standard library modules



Write answers here:
```
A) 5 results:
print(type(sys.path) is list) #True
print(type(sys.modules) is dict) #True
print(isinstance(sys.path, list)) #True
print(type(sys.argv) is list) #True
print(type(sys.argv[0]) is str) #True

B) 5 results:
print(sys.argv[0])         #myscript.py
print(sys.argv[1])         #alpha
print(sys.argv[2])         #42
print(type(sys.argv[2]))   #str
print(len(sys.argv))       #3

C) 3 results:
True, False, True



D) Answer:
C, D
```

---

## Task 3 — `str(obj)` default output + `__str__` vs `__repr__` [Q20 trap]

**THE RULES:**
```
Default __str__(obj)   → '<ClassName object at 0x7f...>'  (NOT the var name, NOT class name alone)
Default __repr__(obj)  → same as __str__ if __repr__ not defined
str(obj) == 'obj'      → ALWAYS False (default repr is memory address, not variable name)

When __str__ IS defined: str(obj) calls it, repr(obj) does NOT use it (uses __repr__).
```

**A)** Predict True or False:
```python
class Box:
    pass

b = Box()
print(str(b) == 'b')                  # ?
print(str(b) == 'Box')                # ?
print('Box' in str(b))                # ? ← careful
print('object' in str(b))             # ?
print(str(b) == repr(b))              # ? ← when neither __str__ nor __repr__ defined
```

**B)** Predict the output:
```python
class Animal:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Animal({self.name})"

a = Animal("cat")
print(str(a))          # ?
print(repr(a))         # ? ← __repr__ NOT defined
print(str(a) == repr(a))  # ?
```

**C)** Multiple choice — which TWO are True?
```python
class Foo:
    x = 1

obj = Foo()
```
- A: `str(obj) == 'obj'`
- B: `'Foo' in str(obj)`
- C: `type(obj) is Foo`
- D: `str(obj) == 'Foo'`

Write answers here:
```
A) 5 results:
print(str(b) == 'b')                  #False
print(str(b) == 'Box')                #False
print('Box' in str(b))                #True <Box object at ....>
print('object' in str(b))             #True
print(str(b) == repr(b))              #True


B) 3 results:
print(str(a))          #Animal(cat)
print(repr(a))         #<main.Animal object at ...>
print(str(a) == repr(a))  #False



C) Two True:
B, C

```

---

## Task 4 — Lambda: all valid forms + return None trap [Q34]

**THE RULES:**
```
lambda           → valid, zero params: lambda: 42
lambda x:        → must have body: lambda x: x
lambda x, y=0:   → default args valid: lambda x, y=0: x + y
lambda *args:    → *args valid: lambda *args: sum(args)
return keyword   → FORBIDDEN inside lambda body (SyntaxError)
lambda CAN return None → lambda: None is perfectly valid
```

**A)** Valid or SyntaxError? Write V or S:
```python
f1 = lambda: 42
f2 = lambda x: return x
f3 = lambda x, y=0: x + y
f4 = lambda x: x if x > 0 else -x
f5 = lambda x, y: x * y
f6 = lambda: None
f7 = lambda x: print(x)
```

**B)** Predict the output:
```python
fns = [lambda x, n=n: x + n for n in range(3)]
print(fns[0](10))
print(fns[1](10))
print(fns[2](10))
```

```python
fns = [lambda x: x + n for n in range(3)]
print(fns[0](10))
print(fns[2](10))
```

**C)** Multiple choice — which TWO are true about lambda?
- A: A lambda is an anonymous function
- B: A lambda can be defined without parameters
- C: A lambda cannot return `None`
- D: A lambda must use the `return` keyword

**D)** What does this evaluate to?
```python
f = lambda: None
print(f() is None)    # ?
print(f() == None)    # ?
print(bool(f()))      # ?
```

Write answers here:
```
A) f1-f7:
f1 = lambda: 42 #Valid
f2 = lambda x: return x #Invalid
f3 = lambda x, y=0: x + y #Valid
f4 = lambda x: x if x > 0 else -x #Valid
f5 = lambda x, y: x * y #Valid
f6 = lambda: None #Valid
f7 = lambda x: print(x) #valid


B) result 1 (3 outputs):
10, 11, 12

   result 2 (2 outputs):
12, 12


C) Two True:
A, B


D) 3 results:
print(f() is None)    #True
print(f() == None)    #True
print(bool(f()))      #False
```

---

## Task 5 — `open()` modes: the full table drill [recurring gap]

**THE TABLE:**
```
Mode | Creates? | Truncates? | Pointer start | Read? | Write?
-----|----------|------------|---------------|-------|-------
'r'  | No (error)| No        | Start         | Yes   | No
'r+' | No (error)| No        | Start         | Yes   | Yes
'w'  | Yes       | Yes        | Start         | No    | Yes
'w+' | Yes       | Yes        | Start         | Yes   | Yes
'a'  | Yes       | No         | END           | No    | Yes
'a+' | Yes       | No         | END (writes)  | Yes   | Yes (at end)
'x'  | Fail if exists | No   | Start         | No    | Yes
```

**A)** Predict the mode for each description:
```
1. Read-only, file must exist, pointer at start:              ?
2. Read+write, no truncate, file must exist, pointer at start: ?
3. Creates/truncates, write-only:                              ?
4. Creates/truncates, read+write:                              ?
5. Appends only, creates if missing:                          ?
6. Read+write appends, creates if missing:                    ?
7. Exclusive create, fails if file exists:                    ?
```

**B)** True or False:
```python
# Assume 'data.txt' already exists with content "hello"
f = open('data.txt', 'r+')
# Which statements are True?
```
- A: `f.read()` works → True/False?
- B: `f.write('x')` works → True/False?
- C: `f.write('x')` truncates the file first → True/False?
- D: The pointer starts at the beginning → True/False?
- E: If file doesn't exist, `FileNotFoundError` is raised → True/False?

**C)** Multiple choice — which mode opens file for both reading and writing without truncating, pointer at start?
- A: `'w+'`
- B: `'a+'`
- C: `'r+'`
- D: `'a'`

Write answers here:
```
A) 7 modes:
# 1. Read-only, file must exist, pointer at start:              r
# 2. Read+write, no truncate, file must exist, pointer at start:  r+
# 3. Creates/truncates, write-only:                              w
# 4. Creates/truncates, read+write:                              w+
# 5. Appends only, creates if missing:                          a
# 6. Read+write appends, creates if missing:                    a+
# 7. Exclusive create, fails if file exists:                    x


B) 5 True/False:
True
True
False
True
True

C) Answer:
B, C
```

---

## Task 6 — PCAP Select-Two: full mixed sim (all recent gaps)

**Q1.** Which TWO are always True?
```python
import sys
```
- A: `type(sys.path) is list`
- B: `type(sys.modules) is tuple`
- C: `type(sys.modules) is dict`
- D: `sys.argv is None`

A, C

**Q2.** Which TWO are True after:
```python
class P:
    speed = 100
    def move(self): pass

class Q(P):
    def stop(self): pass

class R(Q):
    pass

r = R()
```
- A: `hasattr(R, 'move')`
- B: `'move' in R.__dict__`
- C: `hasattr(r, 'speed')`
- D: `'speed' in r.__dict__`

A, C

**Q3.** Which TWO are valid Python lambda expressions?
- A: `lambda x: return x * 2`
- B: `lambda: 0`
- C: `lambda x, y=1: x + y`
- D: `lambda x: if x > 0: x`

B, C, D (all three VALID!)

**Q4.** Which TWO are true about the following code?
```python
class Dog:
    pass

d = Dog()
```
- A: `str(d) == 'd'`
- B: `'Dog' in str(d)`
- C: `type(d) is Dog`
- D: `str(d) == 'Dog'`

B, C

**Q5.** Which TWO are true about `open()` modes?
- A: `'r+'` truncates the file on open
- B: `'r+'` requires the file to already exist
- C: `'w'` creates the file if it doesn't exist
- D: `'a'` starts the write pointer at the beginning

Write answers here:
```
Q1: A, C
Q2: A, C
Q3: B, C, D (all three VALID!)
Q4: B, C
Q5: B, C
```

---

## Task 7 — Project: Fix `exit_reason` display bug + verify output

The `exit_reason` in some trades shows "still open". This was caused by `should_close()` being called after the position was already removed.

**The fix has already been partially applied** — `backtest_engine.py` now uses `position[0]` and `position[1]` tuple unpacking in `process_price`. But we need to verify the end-to-end run produces correct exit reasons.

**Your task:**
1. Run `main.py` and inspect the output
2. Confirm that no trades show `exit_reason = 'still open'`
3. If the bug persists, read `position_manager.py` to check what `close_triggered_positions` returns and trace the tuple
4. Report: how many trades, win rate, total PnL, and 3 sample exit reasons from the output

Write your findings here:
```
Trades:
Win rate:
Total PnL:
Sample exit reasons (3):
Bug fixed? Y/N: N

Dude, nearly ALL trades show still open.
I have no fucking idea why.
I've inspected position_manager.py, backtest_engine.py and main.py

I'm not able to find the flaw - it seems to me that the logic is alright, and that we should technically send the exit reason when creating a Trade, and it should be there, but it's fucking not for whatever reason.

Below is the list of trades:


[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 82720858-2db5-4886-be9a-8464ac150651: [LOSS] BUY 1 FDAX: 22711.0 -> 22708.0 (still open) | P&L: $-3.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 44ca2755-7858-42e8-9928-cf07bf4004b2: [LOSS] BUY 1 FDAX: 22744.0 -> 22744.0 (still open) | P&L: $0.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 74510055-0b4f-4e30-bf39-b962aee2a245: [LOSS] BUY 1 FDAX: 22691.0 -> 22688.0 (still open) | P&L: $-3.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 815d6c7c-89b3-4654-821e-8fd8bebfd005: [WIN] BUY 1 FDAX: 22729.0 -> 22744.0 (still open) | P&L: $15.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 12b9a465-5113-4853-82b2-79f4c4b15d33: [WIN] BUY 1 FDAX: 22780.0 -> 22790.0 (still open) | P&L: $10.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade d7b39f09-cc53-4169-9584-d3785a25d894: [WIN] BUY 1 FDAX: 22819.0 -> 22852.0 (still open) | P&L: $33.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade f76189c8-7489-4502-ad0b-8d777f146453: [WIN] BUY 1 FDAX: 23123.0 -> 23131.0 (still open) | P&L: $8.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 525ec052-5d69-4f64-828b-3557fd113fdf: [LOSS] BUY 1 FDAX: 23155.0 -> 23145.0 (still open) | P&L: $-10.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 0f44830a-be15-4b72-b439-2811f3d90d1d: [LOSS] BUY 1 FDAX: 23477.0 -> 23473.0 (still open) | P&L: $-4.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 53669fb9-6405-4e7c-a8c9-6f118fab633d: [LOSS] BUY 1 FDAX: 23367.0 -> 23358.0 (still open) | P&L: $-9.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 4f4f61ef-a749-45f1-aec6-3bbd615cc168: [WIN] BUY 1 FDAX: 23273.0 -> 23275.0 (still open) | P&L: $2.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade d9c94624-e89d-4b7d-84ce-4b2aa16e8ff0: [LOSS] BUY 1 FDAX: 23306.0 -> 23301.0 (still open) | P&L: $-5.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade d2e5e7e8-132a-421f-a425-074d002176a8: [LOSS] BUY 1 FDAX: 22936.0 -> 22914.0 (still open) | P&L: $-22.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade b5fbbaec-c0e2-4cc9-9b19-6b2fe797cea5: [LOSS] BUY 1 FDAX: 22963.0 -> 22951.0 (still open) | P&L: $-12.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 72a593c5-cf77-4554-91ef-a8b4a25032fa: [LOSS] BUY 1 FDAX: 22654.0 -> 22645.0 (still open) | P&L: $-9.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade a069a871-dcba-4a88-b847-308fb2ca3785: [WIN] BUY 1 FDAX: 22668.0 -> 22673.0 (still open) | P&L: $5.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade d93e33af-c893-459d-9006-949a9e04bc16: [LOSS] BUY 1 FDAX: 19879.0 -> 19823.0 (still open) | P&L: $-56.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 57fadedf-48fd-4e9d-b46f-b968032fc900: [LOSS] BUY 1 FDAX: 19959.0 -> 19946.0 (still open) | P&L: $-13.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade d52b68db-faec-4b63-b782-f55bf0fc8624: [WIN] BUY 1 FDAX: 20439.0 -> 20448.0 (still open) | P&L: $9.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 429dbbe7-2af4-404d-94d1-66cd6b499585: [WIN] BUY 1 FDAX: 20525.0 -> 20539.0 (still open) | P&L: $14.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 56091ed4-e043-4993-b786-c8ad1312d11c: [LOSS] BUY 1 FDAX: 21121.0 -> 21107.0 (still open) | P&L: $-14.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade ba7e367e-5b24-4220-af11-e33f85429a27: [LOSS] BUY 1 FDAX: 21150.0 -> 21147.0 (still open) | P&L: $-3.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 1fae2686-fb68-4759-942a-3876535c8e6b: [LOSS] BUY 1 FDAX: 21329.0 -> 21294.0 (still open) | P&L: $-35.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade f6b0b274-352b-46d6-92e1-2a8ec79b1b02: [WIN] BUY 1 FDAX: 21381.0 -> 21388.0 (still open) | P&L: $7.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 29edd396-4682-4eb5-956d-e6e8bf0f7999: [LOSS] BUY 1 FDAX: 21330.0 -> 21327.0 (still open) | P&L: $-3.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 1b36f50c-75a2-4bb7-85c9-fac1131c8336: [WIN] BUY 1 FDAX: 21369.0 -> 21375.0 (still open) | P&L: $6.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade d0b24adf-9ce7-4713-9de3-ccb732d67028: [WIN] BUY 1 FDAX: 22056.0 -> 22065.0 (still open) | P&L: $9.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 55fd5bb7-88fe-4071-b950-51dea7ee22eb: [WIN] BUY 1 FDAX: 22066.0 -> 22073.0 (still open) | P&L: $7.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 1df16e4b-2c6c-463a-acc1-b4c7cffb92f9: [LOSS] BUY 1 FDAX: 22051.0 -> 22035.0 (still open) | P&L: $-16.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 9027c7e9-b599-4a50-b953-290f9f04499f: [LOSS] BUY 1 FDAX: 22105.0 -> 22102.0 (still open) | P&L: $-3.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 211b5a50-0466-41fd-9b5d-5c77876424a7: [LOSS] BUY 1 FDAX: 22404.0 -> 22396.0 (still open) | P&L: $-8.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 0911955d-2bec-4291-be6a-ee298cf878fd: [LOSS] BUY 1 FDAX: 22435.0 -> 22426.0 (still open) | P&L: $-9.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 6aa1cc86-ca4f-4b09-9887-22cfadb94864: [WIN] BUY 1 FDAX: 22521.0 -> 22532.0 (still open) | P&L: $11.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 0e3f966d-0038-4dc9-8538-214553b14a77: [LOSS] BUY 1 FDAX: 22559.0 -> 22559.0 (still open) | P&L: $0.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 7ffe6ca5-64da-4b2e-abbf-f871ba2af6e0: [LOSS] BUY 1 FDAX: 22606.0 -> 22596.0 (still open) | P&L: $-10.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade b7c0df03-db7d-4d09-83ac-e02f956103d6: [LOSS] BUY 1 FDAX: 23023.0 -> 23015.0 (still open) | P&L: $-8.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade f25799a0-ed4e-493d-9460-d9cfc494f71d: [WIN] BUY 1 FDAX: 23036.0 -> 23042.0 (still open) | P&L: $6.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 2745443e-e5c9-4786-8321-cd0a3396dbda: [WIN] BUY 1 FDAX: 23334.0 -> 23340.0 (still open) | P&L: $6.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade ee879057-efba-4ee5-abfe-8f949ddfece1: [WIN] BUY 1 FDAX: 23354.0 -> 23357.0 (still open) | P&L: $3.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 323ec715-b4d0-44eb-a4ff-dbe532e77d59: [WIN] BUY 1 FDAX: 23440.0 -> 23441.0 (still open) | P&L: $1.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 03adf39b-09e9-4935-a3fd-bb5df730cf4f: [WIN] BUY 1 FDAX: 23457.0 -> 23459.0 (still open) | P&L: $2.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 9f68ef61-aef9-4177-890c-d831fc11bf7f: [WIN] BUY 1 FDAX: 23624.0 -> 23626.0 (still open) | P&L: $2.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade a0ffb419-a529-4b44-8d66-27a901ea3c21: [LOSS] BUY 1 FDAX: 24000.0 -> 23874.0 (buy sl hit) | P&L: $-126.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 549bb3f0-97cb-4a0c-a854-12e04b02d122: [LOSS] BUY 1 FDAX: 23719.0 -> 23698.0 (buy sl hit) | P&L: $-21.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 23940573-d0b5-44a7-949f-e4bfe0139caf: [LOSS] BUY 1 FDAX: 23572.0 -> 23563.0 (still open) | P&L: $-9.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 747d8b3e-40de-4f80-92fa-fef1860f9df0: [LOSS] BUY 1 FDAX: 23594.0 -> 23588.0 (still open) | P&L: $-6.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 5c2f416a-3d74-40b6-8998-9339c1803670: [WIN] BUY 1 FDAX: 23838.0 -> 23839.0 (still open) | P&L: $1.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade e439a48b-69e4-4019-941d-aeb6b9f9895d: [WIN] BUY 1 FDAX: 23859.0 -> 23861.0 (still open) | P&L: $2.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 86f2f58b-8ef7-40a1-85e0-d41ae85ac739: [LOSS] BUY 1 FDAX: 24066.0 -> 24064.0 (still open) | P&L: $-2.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 3910d733-af36-4f24-a4e8-55b246f7f60f: [LOSS] BUY 1 FDAX: 24097.0 -> 24094.0 (still open) | P&L: $-3.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 1115e950-265e-4e4e-8213-f72b3689429c: [LOSS] BUY 1 FDAX: 24166.0 -> 24161.0 (still open) | P&L: $-5.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade af198aad-de93-4d2f-ba1e-04b432955f91: [LOSS] BUY 1 FDAX: 24166.0 -> 24161.0 (still open) | P&L: $-5.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 12ce765d-a158-4119-a01a-31714c550c79: [WIN] BUY 1 FDAX: 24249.0 -> 24256.0 (still open) | P&L: $7.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 6f721df8-29d3-4bd4-8fcd-f5fe1daf9a12: [WIN] BUY 1 FDAX: 24282.0 -> 24283.0 (still open) | P&L: $1.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 31ee09f5-e8e9-4a47-adee-df5f9840056c: [LOSS] BUY 1 FDAX: 24183.0 -> 24174.0 (still open) | P&L: $-9.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade a0a14960-aad0-411e-8d2d-35f1fe445c6c: [WIN] BUY 1 FDAX: 24207.0 -> 24212.0 (still open) | P&L: $5.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 1af36c47-2aad-4e61-ba90-20d0464ae740: [LOSS] BUY 1 FDAX: 24080.0 -> 24077.0 (still open) | P&L: $-3.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 23f4876c-087c-498a-9ed9-39dfa60c54db: [WIN] BUY 1 FDAX: 24369.0 -> 24370.0 (still open) | P&L: $1.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 993f8d06-35ee-49b5-83a5-16600f09456d: [WIN] BUY 1 FDAX: 24404.0 -> 24416.0 (still open) | P&L: $12.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 18f69f5e-19ea-47a7-bcbc-de801993e286: [LOSS] BUY 1 FDAX: 24418.0 -> 24382.0 (still open) | P&L: $-36.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade f4bfef0e-a243-4aa5-b7af-43be92734c0f: [LOSS] BUY 1 FDAX: 24339.0 -> 24337.0 (still open) | P&L: $-2.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade fbfa2db5-29e5-411e-856d-a56af337d6ac: [LOSS] BUY 1 FDAX: 24103.0 -> 24093.0 (still open) | P&L: $-10.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade ad749d83-2265-4fe4-b3d6-93ae1caa3bfe: [LOSS] BUY 1 FDAX: 24123.0 -> 24108.0 (still open) | P&L: $-15.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 37d32593-d39d-436d-b3e9-71ca0f1c3e55: [WIN] BUY 1 FDAX: 23799.0 -> 23800.0 (still open) | P&L: $1.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 5bc9d090-7f73-4b90-80f6-f094d77ca692: [WIN] BUY 1 FDAX: 23856.0 -> 23860.0 (still open) | P&L: $4.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 57b10985-5dc7-49ee-90a4-efbc858e2dea: [LOSS] BUY 1 FDAX: 23649.0 -> 23648.0 (still open) | P&L: $-1.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade c716aca5-2799-4e31-adef-11231ab7a97f: [WIN] BUY 1 FDAX: 23670.0 -> 23676.0 (still open) | P&L: $6.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 8f89edea-b7b0-49ea-8c79-3f7772589d84: [WIN] BUY 1 FDAX: 23554.0 -> 23555.0 (still open) | P&L: $1.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 8b5631a7-2fe6-41ac-9bd6-37983f132d44: [LOSS] BUY 1 FDAX: 23332.0 -> 23330.0 (still open) | P&L: $-2.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 72dd7ec9-6442-46c6-9748-09582b151f24: [LOSS] BUY 1 FDAX: 23362.0 -> 23358.0 (still open) | P&L: $-4.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 320ae171-796d-4724-af15-643927763ff7: [WIN] BUY 1 FDAX: 23503.0 -> 23531.0 (still open) | P&L: $28.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 097a90eb-029e-490d-91b0-87e50fd1fc4d: [WIN] BUY 1 FDAX: 23503.0 -> 23531.0 (still open) | P&L: $28.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade d4e967fc-70c6-4602-ad15-0d1c9a942d05: [LOSS] BUY 1 FDAX: 23899.0 -> 23899.0 (still open) | P&L: $0.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 45aa7d66-4088-4cb0-ae4a-9cb08b098ee6: [LOSS] BUY 1 FDAX: 23931.0 -> 23929.0 (still open) | P&L: $-2.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 4454c577-2840-459a-a2fb-53fa6b159843: [WIN] BUY 1 FDAX: 23791.0 -> 23793.0 (still open) | P&L: $2.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 5f8cdcc2-d893-4a4a-b52f-e79f48e1cc4c: [LOSS] BUY 1 FDAX: 23809.0 -> 23805.0 (still open) | P&L: $-4.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade ffb5bd24-750e-42d8-90e7-182ea8207c5a: [LOSS] BUY 1 FDAX: 24013.0 -> 24011.0 (still open) | P&L: $-2.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 9112047d-c209-4a87-afa7-008fb8f00875: [LOSS] BUY 1 FDAX: 24035.0 -> 24028.0 (still open) | P&L: $-7.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 29771669-aa5e-455d-bfa6-8272e5f859a6: [LOSS] BUY 1 FDAX: 24020.0 -> 24016.0 (still open) | P&L: $-4.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade f460775e-a723-4e3a-9b5d-805908b59026: [LOSS] BUY 1 FDAX: 24036.0 -> 24033.0 (still open) | P&L: $-3.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 441a2555-0d88-4507-a3cf-3489c1d0f223: [WIN] BUY 1 FDAX: 24015.0 -> 24021.0 (still open) | P&L: $6.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade aee000be-03bf-40ab-8ecb-464faa955e58: [WIN] BUY 1 FDAX: 24022.0 -> 24033.0 (still open) | P&L: $11.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade d5d0edbf-69cf-4b10-b2fc-e63ba67966c1: [WIN] BUY 1 FDAX: 24286.0 -> 24287.0 (still open) | P&L: $1.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 82df923a-86b6-4462-bd55-2357571f6b7b: [LOSS] BUY 1 FDAX: 24315.0 -> 24310.0 (still open) | P&L: $-5.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 74cc0303-eedf-4ca4-8ff1-07fed5c17654: [WIN] BUY 1 FDAX: 24500.0 -> 24506.0 (still open) | P&L: $6.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade e259c23d-270d-45a4-8bca-a86043930b88: [WIN] BUY 1 FDAX: 24516.0 -> 24530.0 (still open) | P&L: $14.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade fe2b1710-edf0-450b-b5e4-f23689505f46: [LOSS] BUY 1 FDAX: 24234.0 -> 24231.0 (still open) | P&L: $-3.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade f5ae46eb-5884-4b7e-9bf8-d1fca2f76c43: [WIN] BUY 1 FDAX: 24257.0 -> 24263.0 (still open) | P&L: $6.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 79f38af4-6113-4184-89af-7f8b0f792e7d: [LOSS] BUY 1 FDAX: 24222.0 -> 24215.0 (still open) | P&L: $-7.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 30d1c422-e793-4d1d-8acd-a40967e88a80: [LOSS] BUY 1 FDAX: 24246.0 -> 24243.0 (still open) | P&L: $-3.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade f6e50d4e-ce0e-4c59-a7bb-3c315f9cde78: [LOSS] BUY 1 FDAX: 24414.0 -> 24408.0 (still open) | P&L: $-6.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 38ed82be-75cc-44a5-b6ec-2c29b07dec89: [WIN] BUY 1 FDAX: 24448.0 -> 24453.0 (still open) | P&L: $5.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade d7d6713a-bb84-4666-8a79-133cdffbb34b: [WIN] BUY 1 FDAX: 24258.0 -> 24259.0 (still open) | P&L: $1.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 280cad37-86df-4698-86ce-4ffd3dba1330: [WIN] BUY 1 FDAX: 24280.0 -> 24282.0 (still open) | P&L: $2.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade ce9e71bf-8890-450d-8903-b8b3a67915d8: [LOSS] BUY 1 FDAX: 24350.0 -> 24350.0 (still open) | P&L: $0.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade e4704a9d-bf82-43a2-bd2b-0170f99de0cc: [LOSS] BUY 1 FDAX: 24380.0 -> 24376.0 (still open) | P&L: $-4.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 8e83a1dc-e2d7-4b2c-b078-b95c44ae17ae: [LOSS] BUY 1 FDAX: 24305.0 -> 24296.0 (still open) | P&L: $-9.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 4034b75b-b98d-4bcf-8904-91b86b2952d8: [LOSS] BUY 1 FDAX: 24327.0 -> 24324.0 (still open) | P&L: $-3.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 2d10c079-b116-4755-88e1-b017c25cc373: [LOSS] BUY 1 FDAX: 23827.0 -> 23819.0 (still open) | P&L: $-8.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade c68418a9-e622-43b0-9c9e-67b331d68592: [LOSS] BUY 1 FDAX: 23997.0 -> 23996.0 (still open) | P&L: $-1.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 9f8dbf39-2aaf-47b5-8760-eff5ef4b1499: [LOSS] BUY 1 FDAX: 24034.0 -> 24034.0 (still open) | P&L: $0.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade c210f415-7a7b-4121-a2bd-fa52a98d662b: [WIN] BUY 1 FDAX: 24145.0 -> 24149.0 (still open) | P&L: $4.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade ad72f93d-099a-404b-89f9-9854ea373e11: [LOSS] BUY 1 FDAX: 24155.0 -> 24140.0 (still open) | P&L: $-15.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 71115700-8297-44a9-804d-b7d07d905784: [LOSS] BUY 1 FDAX: 24272.0 -> 24271.0 (still open) | P&L: $-1.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade d7b01716-8020-45fb-9d7f-12a3c0aef728: [WIN] BUY 1 FDAX: 24272.0 -> 24273.0 (still open) | P&L: $1.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 1cb5e086-f609-41aa-8bd9-e4b17938fa72: [WIN] BUY 1 FDAX: 24295.0 -> 24299.0 (still open) | P&L: $4.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 708e09db-3231-4bd5-9143-340b171be133: [LOSS] BUY 1 FDAX: 24379.0 -> 24379.0 (still open) | P&L: $0.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 94fee390-ad24-4597-b1c1-5f4ea1744af9: [WIN] BUY 1 FDAX: 24394.0 -> 24398.0 (still open) | P&L: $4.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 4afb01d2-928f-40f9-9262-fae2ae6ab8ed: [LOSS] BUY 1 FDAX: 24418.0 -> 24418.0 (still open) | P&L: $0.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 641ae1da-f35c-43f9-a027-1097fa8084dc: [LOSS] BUY 1 FDAX: 24448.0 -> 24448.0 (still open) | P&L: $0.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 3914290a-ef11-46f7-8c38-3d500b009618: [LOSS] BUY 1 FDAX: 24418.0 -> 24413.0 (still open) | P&L: $-5.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 5abe6216-598e-46b7-b356-672e8ffdf3ae: [LOSS] BUY 1 FDAX: 24340.0 -> 24337.0 (still open) | P&L: $-3.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade efc802f5-ebad-45b9-8bb2-ffc809b6d341: [LOSS] BUY 1 FDAX: 24358.0 -> 24356.0 (still open) | P&L: $-2.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade cf570260-5303-4df2-a843-25461d7df467: [LOSS] BUY 1 FDAX: 24334.0 -> 24331.0 (still open) | P&L: $-3.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 2b237fa7-db0a-4be4-9569-1b3f3a006c3f: [LOSS] BUY 1 FDAX: 24344.0 -> 24342.0 (still open) | P&L: $-2.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade f5ed2ef2-8edf-4557-ace5-126a1b146949: [LOSS] BUY 1 FDAX: 24243.0 -> 24243.0 (still open) | P&L: $0.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade e979a386-4f3d-4fee-bc7c-fece09f3cea8: [WIN] BUY 1 FDAX: 24263.0 -> 24266.0 (still open) | P&L: $3.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 23ce53b9-710d-48ea-9b44-77f7aad6fe52: [LOSS] BUY 1 FDAX: 24077.0 -> 24073.0 (still open) | P&L: $-4.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 2468c11c-7c44-45d5-96eb-21816eb40f56: [LOSS] BUY 1 FDAX: 23680.0 -> 23679.0 (still open) | P&L: $-1.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 8276f296-adaa-4238-82c4-165e38a6e89f: [WIN] BUY 1 FDAX: 23716.0 -> 23720.0 (still open) | P&L: $4.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 8baa5f61-6526-4548-8737-669339714f8f: [LOSS] BUY 1 FDAX: 23810.0 -> 23804.0 (still open) | P&L: $-6.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 94fe4bd6-1dcb-4cce-bf34-a7869c7ee026: [LOSS] BUY 1 FDAX: 23810.0 -> 23804.0 (still open) | P&L: $-6.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 797311c4-37b9-48dc-b540-9cc45ef823cb: [WIN] BUY 1 FDAX: 23830.0 -> 23835.0 (still open) | P&L: $5.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade bd018be2-0f1e-4ca9-aca2-ed9ed0ef145f: [LOSS] BUY 1 FDAX: 23849.0 -> 23835.0 (still open) | P&L: $-14.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 7f18dc82-ab63-43dd-84d7-d787898d9f5d: [LOSS] BUY 1 FDAX: 23715.0 -> 23712.0 (still open) | P&L: $-3.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 92866a91-5a79-4977-98ad-e6e36a441f0e: [WIN] BUY 1 FDAX: 23742.0 -> 23743.0 (still open) | P&L: $1.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 9be77003-5e7c-48a4-b653-7d363dbcd4bd: [LOSS] BUY 1 FDAX: 23860.0 -> 23859.0 (still open) | P&L: $-1.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade b0aca162-8de4-407d-8359-793f169c98fc: [LOSS] BUY 1 FDAX: 23815.0 -> 23807.0 (still open) | P&L: $-8.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 033cdcf3-8a10-41a2-95f3-7f1e42bf47fc: [LOSS] BUY 1 FDAX: 23819.0 -> 23819.0 (still open) | P&L: $0.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 1642854a-3ae8-436e-b617-94447b57b7f3: [WIN] BUY 1 FDAX: 23840.0 -> 23841.0 (still open) | P&L: $1.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade bfde4af1-0c83-449d-92cb-3423da7f3e62: [WIN] BUY 1 FDAX: 23807.0 -> 23816.0 (still open) | P&L: $9.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade de9eb495-daac-4ca5-8ad5-b3c4ffb37251: [LOSS] BUY 1 FDAX: 23829.0 -> 23829.0 (still open) | P&L: $0.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 7d720acd-cb57-4d2a-935d-6129adf62967: [LOSS] BUY 1 FDAX: 23831.0 -> 23831.0 (still open) | P&L: $0.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 7b196052-fab0-4d85-a97e-1738cd603f90: [WIN] BUY 1 FDAX: 23846.0 -> 23881.0 (still open) | P&L: $35.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 1c0ab294-5ce1-46b5-be7b-fc210d639615: [WIN] BUY 1 FDAX: 23879.0 -> 23881.0 (still open) | P&L: $2.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 7df0514f-06fc-4bf1-afc2-e1448a02f3f0: [WIN] BUY 1 FDAX: 23895.0 -> 23903.0 (still open) | P&L: $8.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade e816d675-8539-4099-aaed-3fda95fad399: [WIN] BUY 1 FDAX: 23972.0 -> 23977.0 (still open) | P&L: $5.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade e1fa709a-6775-4eea-b88d-78fde5b76672: [LOSS] BUY 1 FDAX: 23986.0 -> 23983.0 (still open) | P&L: $-3.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 78140e34-4f0e-46d0-83e6-6f905b05719d: [WIN] BUY 1 FDAX: 24452.0 -> 24462.0 (still open) | P&L: $10.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 8d1079c1-0bb2-436f-bba6-6d2eb57b4c36: [LOSS] BUY 1 FDAX: 24466.0 -> 24463.0 (still open) | P&L: $-3.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 0a0792fd-3bf4-4b90-aa2a-40dbb8edbd2e: [WIN] BUY 1 FDAX: 24542.0 -> 24546.0 (still open) | P&L: $4.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade aba7e7be-db9f-434a-90d3-898073f5cdcd: [LOSS] BUY 1 FDAX: 24580.0 -> 24569.0 (still open) | P&L: $-11.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 76277605-6744-42ec-b3b6-a60ed4ce35d7: [LOSS] BUY 1 FDAX: 24534.0 -> 24533.0 (still open) | P&L: $-1.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 083cd4f3-0aac-4e50-8474-7553e05f5534: [LOSS] BUY 1 FDAX: 24561.0 -> 24557.0 (still open) | P&L: $-4.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 33a8e07b-c49f-4852-bc0a-686fed00da2a: [WIN] BUY 1 FDAX: 24646.0 -> 24652.0 (still open) | P&L: $6.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 0d71d549-139c-4ec6-bcc4-3fe0b45815ed: [WIN] BUY 1 FDAX: 24680.0 -> 24684.0 (still open) | P&L: $4.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 163f0134-951d-43cb-ad6e-eb98b7a9eeb9: [WIN] BUY 1 FDAX: 24816.0 -> 24818.0 (still open) | P&L: $2.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 0b0aeed7-a55a-4179-a3c0-6f5535e3a54b: [LOSS] BUY 1 FDAX: 24853.0 -> 24853.0 (still open) | P&L: $0.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 40eaad96-c8d7-41e0-9e91-983d7b96419a: [LOSS] BUY 1 FDAX: 24351.0 -> 24338.0 (still open) | P&L: $-13.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 95082a86-0e14-44d8-817c-41bf29c08075: [WIN] BUY 1 FDAX: 24362.0 -> 24370.0 (still open) | P&L: $8.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 64280305-7a4f-4845-88dc-a949df96e7be: [LOSS] BUY 1 FDAX: 24011.0 -> 24007.0 (still open) | P&L: $-4.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 8b0cc594-8b53-441a-b2c9-6d3b1bb27302: [LOSS] BUY 1 FDAX: 24067.0 -> 24063.0 (still open) | P&L: $-4.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 404a2b18-779c-4850-8ded-bb63cc89e32a: [LOSS] BUY 1 FDAX: 24260.0 -> 24260.0 (still open) | P&L: $0.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade a5bdb161-f51e-48bd-8fb4-22b57b2f4d61: [WIN] BUY 1 FDAX: 24284.0 -> 24288.0 (still open) | P&L: $4.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade b4f5bc64-98b6-4f77-99d0-61cb6cddbb52: [LOSS] BUY 1 FDAX: 24423.0 -> 24423.0 (still open) | P&L: $0.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade e73c30a2-3082-46b7-aedf-4f1720f6e5a9: [LOSS] BUY 1 FDAX: 24430.0 -> 24425.0 (still open) | P&L: $-5.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade a8af6cb5-6191-4133-bec5-3106d77d06a9: [WIN] BUY 1 FDAX: 24302.0 -> 24310.0 (still open) | P&L: $8.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 951cfe64-697d-44e3-86df-6b9ff38a56f8: [LOSS] BUY 1 FDAX: 24392.0 -> 24392.0 (still open) | P&L: $0.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade dc4cc930-6f23-4920-a315-f66508ce6903: [LOSS] BUY 1 FDAX: 24426.0 -> 24425.0 (still open) | P&L: $-1.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade c9af6722-380e-4bff-a386-24ce67554ab7: [LOSS] BUY 1 FDAX: 24299.0 -> 24291.0 (still open) | P&L: $-8.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 0405d952-3eda-4678-8053-00e5d48875b6: [LOSS] BUY 1 FDAX: 23933.0 -> 23929.0 (still open) | P&L: $-4.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 687d201a-1147-4f77-801c-4e967a762563: [LOSS] BUY 1 FDAX: 23970.0 -> 23970.0 (still open) | P&L: $0.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 5397241a-471b-4b82-9615-e39ca46bf54b: [LOSS] BUY 1 FDAX: 23976.0 -> 23974.0 (still open) | P&L: $-2.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 205c7f1b-b3bd-4864-b869-77794fbe311b: [WIN] BUY 1 FDAX: 24015.0 -> 24018.0 (still open) | P&L: $3.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 6cf787f6-17f0-43b4-8f54-cd713ad5d2d3: [LOSS] BUY 1 FDAX: 24117.0 -> 24117.0 (still open) | P&L: $0.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 6a48de79-f9cb-4c18-a186-42ee7bce2ce5: [LOSS] BUY 1 FDAX: 24056.0 -> 24053.0 (still open) | P&L: $-3.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 42690347-d9f7-478f-9d1e-57f0f10d834c: [LOSS] BUY 1 FDAX: 24076.0 -> 24076.0 (still open) | P&L: $0.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade e829638f-def1-4daa-802b-2b909c76dd36: [LOSS] BUY 1 FDAX: 24106.0 -> 24104.0 (still open) | P&L: $-2.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 73acc8d4-e05e-4afb-8b4c-6d71108f7792: [LOSS] BUY 1 FDAX: 24125.0 -> 24119.0 (still open) | P&L: $-6.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 5059493a-89c8-4495-a1e6-1a00f128bafa: [LOSS] BUY 1 FDAX: 24478.0 -> 24476.0 (still open) | P&L: $-2.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 14cc3082-1e3c-4c97-9e22-152837386d64: [WIN] BUY 1 FDAX: 24505.0 -> 24511.0 (still open) | P&L: $6.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 0451b99e-8ada-480c-b462-823e8ec92791: [WIN] BUY 1 FDAX: 23266.0 -> 23267.0 (still open) | P&L: $1.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade d200dd33-b5e2-44b9-b37b-c609cce57278: [WIN] BUY 1 FDAX: 23300.0 -> 23304.0 (still open) | P&L: $4.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade caaf5c92-7fb5-4fe0-9882-025cfa5c6c1c: [WIN] BUY 1 FDAX: 23526.0 -> 23527.0 (still open) | P&L: $1.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade ce136a6f-248e-4e58-8f8e-ba2ed4cefa8b: [LOSS] BUY 1 FDAX: 23541.0 -> 23539.0 (still open) | P&L: $-2.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 74c82466-3a72-4175-9b4d-ea1a7aab2057: [WIN] BUY 1 FDAX: 23399.0 -> 23480.0 (buy tp hit) | P&L: $81.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 5edccea3-a04b-476b-9871-649912854332: [WIN] BUY 1 FDAX: 23399.0 -> 23480.0 (buy tp hit) | P&L: $81.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 03d4fa6b-f09a-4c7c-bf13-571ff505302f: [WIN] BUY 1 FDAX: 23639.0 -> 23646.0 (still open) | P&L: $7.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 4339e981-906d-4d87-bb29-f54a66a8fbfb: [LOSS] BUY 1 FDAX: 23678.0 -> 23667.0 (still open) | P&L: $-11.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 07658491-064c-4015-8882-51332654585e: [WIN] BUY 1 FDAX: 23818.0 -> 23819.0 (still open) | P&L: $1.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 27e78bba-065a-4b91-9965-7dfdfbeb24eb: [WIN] BUY 1 FDAX: 23834.0 -> 23837.0 (still open) | P&L: $3.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 1de92ef1-2b81-4326-9873-8597112d8b58: [WIN] BUY 1 FDAX: 23800.0 -> 23803.0 (still open) | P&L: $3.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade fe1a38db-8960-4a1e-8392-07e735a23ef1: [WIN] BUY 1 FDAX: 23818.0 -> 23820.0 (still open) | P&L: $2.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 96117d3c-82bb-4c8a-a80e-9504760bbc72: [LOSS] BUY 1 FDAX: 23943.0 -> 23943.0 (still open) | P&L: $0.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade af9d796e-fd2f-4c6b-a65d-a19ef238064c: [LOSS] BUY 1 FDAX: 24072.0 -> 24071.0 (still open) | P&L: $-1.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade ad0baca3-7a25-45ec-8b90-cc528310b68a: [WIN] BUY 1 FDAX: 24092.0 -> 24095.0 (still open) | P&L: $3.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 54b5ec43-550b-4019-ab06-652c634deca9: [WIN] BUY 1 FDAX: 24105.0 -> 24107.0 (still open) | P&L: $2.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 78c9b68b-afd2-47e8-a4dc-c1eac5a966a3: [LOSS] BUY 1 FDAX: 24122.0 -> 24121.0 (still open) | P&L: $-1.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade c392dc07-d3f1-47cb-9f47-ec4cae0fe2e2: [WIN] BUY 1 FDAX: 24180.0 -> 24182.0 (still open) | P&L: $2.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 46286a6e-bc0d-411f-ba7d-f81a4b718564: [LOSS] BUY 1 FDAX: 24204.0 -> 24200.0 (still open) | P&L: $-4.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 4b10fe56-c967-47c7-8992-0e76afafa868: [LOSS] BUY 1 FDAX: 24175.0 -> 24171.0 (still open) | P&L: $-4.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 376ec0ef-a77a-4c74-a4ea-b3c4ba9a3c6c: [LOSS] BUY 1 FDAX: 24185.0 -> 24183.0 (still open) | P&L: $-2.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade bb19630b-e062-43d3-b2b4-956855d53ee9: [LOSS] BUY 1 FDAX: 24419.0 -> 24413.0 (still open) | P&L: $-6.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade bf0008ea-bb9c-48cc-bc40-7a5e6636d4df: [LOSS] BUY 1 FDAX: 24434.0 -> 24429.0 (still open) | P&L: $-5.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 22ced06d-bff4-40d4-9f5e-b8ff21eeb3ca: [WIN] BUY 1 FDAX: 24508.0 -> 24513.0 (still open) | P&L: $5.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 19f7af55-1f91-453a-9c7e-a1309f579a37: [LOSS] BUY 1 FDAX: 24550.0 -> 24549.0 (still open) | P&L: $-1.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 5e45374a-365a-4c54-ab27-dc5a78d7e07a: [WIN] BUY 1 FDAX: 24564.0 -> 24573.0 (still open) | P&L: $9.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 58e9ebfa-efdf-4a24-9d2d-79ac4e715f2a: [LOSS] BUY 1 FDAX: 25068.0 -> 25062.0 (still open) | P&L: $-6.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 58ef3075-902b-4fb6-8ed9-5d1277966b3d: [WIN] BUY 1 FDAX: 25091.0 -> 25101.0 (still open) | P&L: $10.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade f5cf906d-9649-4397-8c43-d0b0c1c53f71: [WIN] BUY 1 FDAX: 25182.0 -> 25185.0 (still open) | P&L: $3.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 7c003d35-524d-4b43-9e76-3b644e0da1dd: [WIN] BUY 1 FDAX: 25198.0 -> 25210.0 (still open) | P&L: $12.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 889f2bc5-47c3-46d5-b6eb-8b880fe43cf7: [LOSS] BUY 1 FDAX: 25298.0 -> 25290.0 (still open) | P&L: $-8.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade d83ab831-2b86-4d82-ad21-426fc367e597: [WIN] BUY 1 FDAX: 25308.0 -> 25310.0 (still open) | P&L: $2.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 9ef1caa8-12fb-43c8-82a7-5499b44ea1f2: [WIN] BUY 1 FDAX: 25437.0 -> 25444.0 (still open) | P&L: $7.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade bf3f557b-fc73-4528-93bd-51fe5c0209f7: [WIN] BUY 1 FDAX: 25451.0 -> 25453.0 (still open) | P&L: $2.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade dbf2b247-500b-4a12-9032-707fadb5932c: [WIN] BUY 1 FDAX: 25605.0 -> 25608.0 (still open) | P&L: $3.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 92ca6fc2-7285-460a-b2c4-ae65bff389f3: [WIN] BUY 1 FDAX: 25605.0 -> 25608.0 (still open) | P&L: $3.00
[@LPP Strategy | d7df9e43-a890-4c33-858d-10c56ede9544] Trade 34df4b1f-c082-4872-8489-36bd4b6e427d: [LOSS] BUY 1 FDAX: 25459.0 -> 25453.0 (still open) | P&L: $-6.00
[@LPP Strategy | b99de049-9dd2-4876-83bf-ba82a66cc9a4] Trade 927fb7ed-8c69-42cd-a251-0638f8185832: [WIN] BUY 1 FDAX: 25480.0 -> 25483.0 (still open) | P&L: $3.00
```

I need you to inspect - position_manager.py, backtest_engine.py, run_backtest() in main.py, and try to help me find the possible flaw of the system, because I'm fucking tired of this shit and I don't have time to waste for this.


---

**When done:** notify me for assessment.
