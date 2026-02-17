# Week 7, Day 3 - Wednesday
## Topic: `logging` — Closing Gaps + Project Integration

**Date:** 2026-02-18

**Target Difficulty:** 5/10

**Lesson Reference:** `lessons/week3_5_7_stdlib_fileio.md` → Week 7 section

**Remember:** Work in `practice.py`. Paste FINAL answers here for review.

---

## Task 1: Close the Gap — `logging.exception()`

This is the one concept that has been wrong twice. Fix it today.

**Run this in `practice.py` and read the output carefully:**

```python
import logging
import sys

logger = logging.getLogger('exc_test')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

try:
    result = 1 / 0
except ZeroDivisionError:
    logger.error("error() call")
    logger.exception("exception() call")
```

**Q1:** Write down exactly what appeared for `logger.error()` vs `logger.exception()`. What is the difference in output?

**Q2:** Does `logger.exception()` raise anything or stop execution?

**Q3:** At what log level does `logger.exception()` emit its record — DEBUG, INFO, WARNING, ERROR, or CRITICAL?

**Q4 (PCAP-style, no code):** When is `logger.exception()` appropriate to use?
- A) Anywhere you want to log at ERROR level
- B) Only inside `except` blocks, where a traceback exists to capture
- C) Only for CRITICAL errors that stop the program
- D) As a replacement for `raise`

```
Q1 — difference in output:

Q2:

Q3:

Q4:
```

---

## Task 2: PCAP Simulation — logging (Full Set)

No running code. 5 minutes max.

**Q1:** What is printed?
```python
import logging
logging.error("problem")
```
- A) Nothing — no handler configured
- B) `ERROR:root:problem`
- C) `problem`
- D) Raises an error

**Q2:** Logger level = `WARNING`. Handler level = `DEBUG`. A `logger.info("msg")` call is made. What happens?
- A) Message appears — handler is DEBUG so it passes
- B) Message is blocked — logger gate is WARNING, info(20) < warning(30)
- C) Message appears but with a warning prefix
- D) RuntimeError is raised

**Q3:** What is the numeric value of `logging.CRITICAL`?
- A) 40
- B) 45
- C) 50
- D) 60

**Q4:** Which statement is true about `logging.basicConfig()`?
- A) Can be called multiple times to update configuration
- B) Only the first call takes effect; subsequent calls are silently ignored
- C) Raises a RuntimeError if called twice
- D) The last call always wins

**Q5:** What does this produce?
```python
import logging
logging.basicConfig(level=logging.WARNING)
logging.info("a")
logging.warning("b")
logging.error("c")
```
- A) `b` and `c` only (bare text)
- B) `INFO:root:a`, `WARNING:root:b`, `ERROR:root:c`
- C) `WARNING:root:b` and `ERROR:root:c`
- D) Nothing — basicConfig requires a format string

```
Q1:
Q2:
Q3:
Q4:
Q5:
```

---

## Task 3: PROJECT — Read `BacktestEngine` First

Before writing anything, read the existing code.

Open `algo_backtest/engine/backtest.py`. Answer these questions about what's already there:

**Q1:** What methods does `BacktestEngine` currently have? List them.

**Q2:** What does `open_position()` do step by step?

**Q3:** Where does a `Trade` get created? (Which method, at what point?)

```
Q1 — methods:

Q2 — open_position() steps:

Q3 — Trade creation:
```

---

## Task 4: PROJECT — Add Logging to `BacktestEngine`

Now that you've read the code and understand it, add logging.

**Rules:**
1. Add `import logging` at the top of the file
2. Add `logger = logging.getLogger(__name__)` at module level (outside the class)
3. Use `%s` / `%.2f` style — NOT f-strings
4. Do NOT add `basicConfig()` inside the file
5. Type hints must stay intact

**What to log:**
- `open_position()`: log at INFO when a position is opened — include side, ticker, entry price, position_id
- `process_price()`: log at DEBUG each time it's called — include ticker and price
- In `process_price()`, when a Trade closes: log at INFO — include ticker, pnl, exit reason

**Paste the full modified file here** (not just the methods — the whole file so I can review it in context):

```python
# Task 4 — algo_backtest/engine/backtest.py with logging added

```

---

## Task 5: PROJECT — Wire Up Logging in `main.py`

Now configure logging at the application entry point.

**Read `main.py` first.** Then add a `setup_logging()` function at the top that:
1. Gets the root logger
2. Sets level to `logging.DEBUG`
3. Adds a `StreamHandler` to stdout with format: `%(asctime)s [%(levelname)-8s] %(name)s: %(message)s`
4. Is called once before any backtest logic runs

**Paste only the `setup_logging()` function and the call site:**

```python
# Task 5 — setup_logging() function and where it's called in main.py

```

**Then run `main.py` and paste 3-5 lines of actual log output you see:**

```
Actual output:

```

---

## Task 6: PCAP Warm-up — `logging` vs `warnings` + Levels

**Q1:** Which correctly logs a WARNING-level record?
- A) `warnings.warn("msg", logging.WARNING)`
- B) `logging.warn("msg")`  ← note: `warn` not `warning`
- C) `logging.warning("msg")`
- D) `log.warning("msg")`

**Q2:** `logging.warn()` exists in Python but is deprecated. What does it do?
- A) Nothing — it raises DeprecationWarning
- B) Same as `logging.warning()` but prints a deprecation notice
- C) Logs at INFO level
- D) Raises AttributeError

**Q3:** A module calls `logging.getLogger(__name__)`. The module is `algo_backtest.engine.backtest`. Which logger name is created?
- A) `backtest`
- B) `engine.backtest`
- C) `algo_backtest.engine.backtest`
- D) `__name__`

```
Q1:
Q2:
Q3:
```

---

**Today's goal:** One remaining gap closed (Task 1). Two-gate and singleton solid from yesterday. Project integration done on your own terms — you understand the tool now, so adding it to real code should feel natural.
