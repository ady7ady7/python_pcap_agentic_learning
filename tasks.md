# Week 7, Day 2 - Tuesday
## Topic: `logging` — Observe, Predict, Build

**Date:** 2026-02-17

**Target Difficulty:** 4/10

**Lesson Reference:** `lessons/week3_5_7_stdlib_fileio.md` → Week 7 section (PART 1–7)

**Today's approach:** Run first, understand what you see. Then predict. Then build from scratch.

**Remember:** Work in `practice.py`. Paste FINAL answers here for review.

---

## Task 1: Observe — Run These, Read the Output

No predictions yet. Just run each snippet in `practice.py` and write what you actually see printed.

**Snippet A:**
```python
import logging
logging.warning("hello")
```
What did you see?
```
A:
```

**Snippet B:**
```python
import logging
logging.debug("hello")
logging.info("hello")
logging.warning("hello")
```
What did you see?
```
B:
```

**Snippet C:**
```python
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("hello")
logging.info("hello")
logging.warning("hello")
```
What did you see?
```
C:
```

**Snippet D — run this, read carefully:**
```python
import logging
logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.WARNING)  # second call
logging.debug("hello")
```
What did you see?
```
D:
```

After running all four — answer these:
1. What is the default output FORMAT (exactly what gets printed before your message)?
2. What changed between B and C?
3. What happened in D on the second `basicConfig()` call?

```
Q1:
Q2:
Q3:
```

---

## Task 2: Observe — The Two Gates

Run this in `practice.py` and record exactly what appears:

```python
import logging
import sys

logger = logging.getLogger('gate_test')
logger.setLevel(logging.DEBUG)          # Gate 1: Logger

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.WARNING)       # Gate 2: Handler
logger.addHandler(handler)

logger.debug("debug")
logger.info("info")
logger.warning("warning")
logger.error("error")
```

What appeared?
```
Output:
```

Now answer:
**Q1:** `debug` and `info` passed Gate 1 (logger is DEBUG). Why didn't they appear?
**Q2:** Change ONE line so that `info` also appears. Which line, and what to?

```
Q1:
Q2: Change line ___ from ___ to ___
```

Now run your change and confirm.

---

## Task 3: Observe — The Singleton

Run this and record the output:

```python
import logging

a = logging.getLogger('my_logger')
b = logging.getLogger('my_logger')
c = logging.getLogger('other_logger')

print(a is b)
print(a is c)
print(id(a) == id(b))
```

Output:
```
a is b:
a is c:
id(a) == id(b):
```

**Q1:** In your own words: what does `getLogger('same_name')` do if that logger was already created?

**Q2:** Why is this useful in a project with 10 modules all using `getLogger('engine')`?

```
Q1:
Q2:
```

---

## Task 4: Predict, Then Verify

Now that you've observed the patterns — predict WITHOUT running first, then run to check.

**Q1:** What appears?
```python
import logging
logging.basicConfig(level=logging.INFO)
logging.debug("a")
logging.info("b")
logging.warning("c")
```
Prediction:
```
Q1 prediction:
```
Run it. Were you right?
```
Q1 actual:
```

**Q2:** What appears?
```python
import logging
import sys

logger = logging.getLogger('predict')
logger.setLevel(logging.ERROR)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

logger.debug("1")
logger.info("2")
logger.warning("3")
logger.error("4")
logger.critical("5")
```
Prediction (which messages appear):
```
Q2 prediction:
```
Run it. Were you right?
```
Q2 actual:
```

**Q3:** What appears?
```python
import logging
import sys

logger = logging.getLogger('predict2')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.ERROR)
logger.addHandler(handler)

logger.debug("1")
logger.warning("3")
logger.error("4")
```
Prediction:
```
Q3 prediction:
```
Actual:
```
Q3 actual:
```

---

## Task 5: Build From Scratch — Step by Step

**Do each step separately. Run after each step to see the change.**

**Step 1:** Create a logger named `'backtest'`. Set its level to `DEBUG`. Do NOT add any handlers yet. Call `logger.warning("test")`. What happens?
```python
# Step 1 code:

# What happened:
```

**Step 2:** Add a `StreamHandler` (stdout). Set its level to `DEBUG`. Add a basic `Formatter` with format `'[%(levelname)s] %(message)s'`. Attach it to the logger. Call `logger.warning("test")` again.
```python
# Step 2 code:

# What changed:
```

**Step 3:** Add a `FileHandler` writing to `'test.log'`. Set it to `DEBUG`. Use the same formatter. Call `logger.debug("debug line")` and `logger.warning("warning line")`. Then open `test.log` and read it.
```python
# Step 3 code:

# What appeared in console:
# What appeared in test.log:
```

**Step 4:** Add the duplicate-handler guard from the lesson. Wrap everything in a function called `build_logger(name: str) -> logging.Logger`. Call it twice with the same name — confirm each call returns the same logger without adding duplicate handlers.
```python
# Step 4 — full build_logger() function:

```

---

## Task 6: PCAP Drill — The Four Gaps from Day 1

These are the exact concepts you got wrong yesterday. No running code.

**Q1:** What is the default output format when you call `logging.warning("price spike")` with no configuration?
- A) `price spike`
- B) `WARNING: price spike`
- C) `WARNING:root:price spike`
- D) `[WARNING] price spike`

**Q2:** Logger level = `DEBUG`. Handler level = `ERROR`. Which messages appear in the output?
- A) All messages (DEBUG and above)
- B) Only ERROR and CRITICAL
- C) Nothing — conflicting levels cancel out
- D) Only DEBUG

**Q3:** `logging.getLogger('engine')` is called in module A, then in module B. Which is true?
- A) Two separate logger objects, each independently configured
- B) The same logger object both times — loggers are singletons by name
- C) Module B gets a copy of module A's logger
- D) An error is raised on the second call

**Q4:** What does `logging.exception("msg")` do that `logging.error("msg")` does NOT?
- A) Raises an exception to stop execution
- B) Logs at CRITICAL level instead of ERROR
- C) Appends the current traceback to the log record
- D) Nothing — they are identical

**Q5:** What is the numeric value of `logging.WARNING`?
- A) 20
- B) 25
- C) 30
- D) 40

```
Q1:
Q2:
Q3:
Q4:
Q5:
```

---

**Today's Goal:**
By the end of Task 5, you should be able to build a working logger from nothing — without looking at the lesson. If you can do that, Tasks 6 and the project integration tomorrow will make complete sense.
