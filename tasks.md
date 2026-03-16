# Week 10, Day 1 — PCAP Review Warm-Up
**Date:** 2026-03-17 | **Mode:** Light session — 3 exercises

---

## Exercise 1 — Predict the output (mutable default + scope)

```python
def f(x, data=[]):
    data.append(x)
    return data

result = f(1)
result = f(2)
print(result)
print(f(3, []))
print(f(4))
```

**Your answer:**


[1, 2]
[3]
[3, 4]



---

## Exercise 2 — Predict the output (MRO + super())

```python
class A:
    def hello(self):
        return "A"

class B(A):
    def hello(self):
        return super().hello() + "B"

class C(A):
    def hello(self):
        return super().hello() + "C"

class D(B, C):
    pass

print(D().hello())
print(D.__mro__)
```

**Your answer:**

ACB, but honestly I'm not sure why (I was expecting ABAC first, but it doesn't make sense to me now.). I need this revisioned and explained. I know this is an edge case, but it's weird. I'd rather focus on more real examples, but definitely I want to undertsand this and cover this gap in the most simple way.

D -> B -> C -> A

---

## Exercise 3 — Find the bug

```python
import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("app")
logger.debug("debug")
logger.warning("warn")
```

The developer expects both `debug` and `warn`. They only see `warn`. Why? Fix it in one line.

**Your answer (explanation + fix):**

We see only WARN, as only the first basicConfig instance works.
It's very easy to fix it.

import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("app")
logger.debug("debug")
logger.warning("warn")


However, logging is not that much PCAP relevant, we don't really need to practice it that much. I didn't even see in during my PCAP learning tbh, so it's an overkill and I don't want to waste time on it now.


---

## Answers

Ex 1:
Ex 2:
Ex 3:
