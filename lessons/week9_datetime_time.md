# `time` vs `datetime` — Python Standard Library

## The Core Distinction

| | `time` module | `datetime` module |
|---|---|---|
| What it is | Thin wrapper around C's system clock | Full OOP date/time toolkit |
| Primary unit | Float (Unix timestamp) | Objects: `date`, `time`, `datetime`, `timedelta` |
| Human-readable output | Via `strftime()` on a `struct_time` | Via `.strftime()` on any datetime object |
| Arithmetic | Subtract floats | `timedelta` objects |
| Typical use | Measuring elapsed time, sleeping, Unix timestamps | Working with calendar dates, formatting, parsing |

**One-line rule:** Use `time` when you care about *seconds elapsed*. Use `datetime` when you care about *what day/time it is*.

---

## The `time` Module

```python
import time
```

### Unix timestamp — `time.time()`

Returns seconds since the Unix epoch (1970-01-01 00:00:00 UTC) as a float.

```python
import time

ts = time.time()
print(ts)       # 1741132800.4823
print(type(ts)) # <class 'float'>
```

This is raw machine time — no year, no month, just a big float. Not human-readable on its own.

### Converting to human-readable — `time.ctime()`

Converts a Unix timestamp to a readable string (local time).

```python
import time

ts = time.time()
print(time.ctime(ts))   # 'Thu Mar  5 14:30:00 2026'
print(time.ctime(0))    # 'Thu Jan  1 01:00:00 1970'  (epoch, local TZ)
```

### `struct_time` — `time.localtime()` / `time.gmtime()`

Converts a Unix timestamp to a named tuple (`struct_time`) you can inspect field by field.

```python
import time

ts = time.time()
local = time.localtime(ts)   # local timezone
utc   = time.gmtime(ts)      # UTC

print(local.tm_year)   # 2026
print(local.tm_mon)    # 3
print(local.tm_mday)   # 5
print(local.tm_hour)   # 14
print(local.tm_min)    # 30
print(local.tm_sec)    # 0
print(local.tm_wday)   # 3  (Monday=0, Thursday=3)
print(local.tm_yday)   # 64 (day of year)
```

`gmtime()` with no argument = current UTC time.
`localtime()` with no argument = current local time.

### Formatting `struct_time` → string — `time.strftime()`

```python
import time

local = time.localtime()
print(time.strftime("%Y-%m-%d %H:%M:%S", local))  # '2026-03-05 14:30:00'
print(time.strftime("%A, %B %d %Y", local))        # 'Thursday, March 05 2026'
```

### Parsing string → `struct_time` — `time.strptime()`

```python
import time

t = time.strptime("2026-03-05 14:30:00", "%Y-%m-%d %H:%M:%S")
print(type(t))      # <class 'time.struct_time'>
print(t.tm_year)    # 2026
```

### `struct_time` → Unix timestamp — `time.mktime()`

The inverse of `localtime()`. Converts a `struct_time` back to a float timestamp.

```python
import time

t = time.strptime("2026-03-05", "%Y-%m-%d")
ts = time.mktime(t)
print(ts)   # 1741129200.0  (float, platform-dependent)
```

### Sleeping — `time.sleep()`

Pauses execution for N seconds (float accepted).

```python
import time

time.sleep(1)      # 1 second
time.sleep(0.25)   # 250 milliseconds
```

### Measuring elapsed time — `time.perf_counter()`

High-resolution timer for benchmarking. Value is arbitrary (only differences matter).

```python
import time

start = time.perf_counter()
# ... some work ...
elapsed = time.perf_counter() - start
print(f"Elapsed: {elapsed:.4f}s")
```

Do NOT use `time.time()` for benchmarking — it can jump backwards on clock adjustments.
`perf_counter()` is monotonic and has nanosecond resolution.

### `time` module summary

| Function | Input | Output | Use |
|---|---|---|---|
| `time.time()` | — | `float` (Unix ts) | Current timestamp |
| `time.ctime(ts)` | `float` | `str` | Quick readable string |
| `time.localtime(ts)` | `float` | `struct_time` | Inspect fields (local TZ) |
| `time.gmtime(ts)` | `float` | `struct_time` | Inspect fields (UTC) |
| `time.mktime(st)` | `struct_time` | `float` | Back to Unix ts |
| `time.strftime(fmt, st)` | `struct_time` | `str` | Format to string |
| `time.strptime(s, fmt)` | `str` | `struct_time` | Parse from string |
| `time.sleep(n)` | `float` | `None` | Pause execution |
| `time.perf_counter()` | — | `float` | Elapsed time benchmarking |

---

## The `datetime` Module

The `datetime` module contains **four classes** you need to know:

| Class | What it represents |
|---|---|
| `date` | A calendar date (year, month, day) — no time |
| `time` | A wall-clock time (hour, minute, second, microsecond) — no date |
| `datetime` | A combined date + time |
| `timedelta` | A duration (difference between two points in time) |

**Warning:** `from datetime import time` shadows the `time` *module*. Keep the import clean.

```python
from datetime import date, time, datetime, timedelta  # import classes
import time as time_module                             # keep module accessible if needed
```

### `date` — calendar date only

```python
from datetime import date

d = date(2026, 3, 5)       # year, month, day
print(d)                    # 2026-03-05
print(d.year)               # 2026
print(d.month)              # 3
print(d.day)                # 5
print(d.weekday())          # 3  (Monday=0, Thursday=3)
print(d.isoweekday())       # 4  (Monday=1, Thursday=4)
print(d.isoformat())        # '2026-03-05'

today = date.today()        # current local date
```

### `time` (from datetime) — wall-clock time only

```python
from datetime import time

t = time(14, 30, 45)        # hour, minute, second
print(t)                    # 14:30:45
print(t.hour)               # 14
print(t.minute)             # 30
print(t.second)             # 45
print(t.isoformat())        # '14:30:45'
```

`datetime.time` has no concept of date and no `.today()` or `.now()`. It is just a container for clock fields.

### `datetime` — date + time combined

```python
from datetime import datetime

dt = datetime(2026, 3, 5, 14, 30, 45)   # year, month, day, hour, minute, second
print(dt)                                 # 2026-03-05 14:30:45
print(dt.year)                            # 2026
print(dt.hour)                            # 14
print(dt.date())                          # 2026-03-05  (returns date object)
print(dt.time())                          # 14:30:45    (returns time object)

now = datetime.now()                      # current local datetime
utc = datetime.utcnow()                   # current UTC datetime (naive)
```

**Unix timestamp ↔ datetime:**

```python
from datetime import datetime

# Unix timestamp → datetime
dt = datetime.fromtimestamp(1741132800.0)   # local timezone
print(dt)                                    # 2026-03-05 00:00:00

# datetime → Unix timestamp
ts = dt.timestamp()
print(ts)                                    # 1741132800.0
print(type(ts))                              # <class 'float'>
```

This is the bridge between the `time` module's world (floats) and `datetime`'s world (objects).

### `strftime` and `strptime` — the critical pair

**strftime** = **f**ormat → datetime object → string
**strptime** = **p**arse → string → datetime object

```python
from datetime import datetime

now = datetime.now()

# datetime → string
s = now.strftime("%Y-%m-%d %H:%M:%S")      # '2026-03-05 14:30:45'
s = now.strftime("%d/%m/%Y")               # '05/03/2026'
s = now.strftime("%A, %B %d %Y")          # 'Thursday, March 05 2026'

# string → datetime
dt = datetime.strptime("2026-03-05", "%Y-%m-%d")
dt = datetime.strptime("05/03/2026 14:30", "%d/%m/%Y %H:%M")
```

**Format codes (memorise these):**

| Code | Meaning | Example |
|---|---|---|
| `%Y` | 4-digit year | `2026` |
| `%m` | 2-digit month | `03` |
| `%d` | 2-digit day | `05` |
| `%H` | 24-hour hour | `14` |
| `%M` | minute | `30` |
| `%S` | second | `45` |
| `%A` | full weekday name | `Thursday` |
| `%B` | full month name | `March` |
| `%f` | microseconds | `000000` |

**PCAP trap:** `strftime` is a method on a `datetime` *instance*. `strptime` is a *classmethod* on `datetime`.

```python
dt.strftime("%Y-%m-%d")              # instance method — formats dt
datetime.strptime("2026-03-05", "%Y-%m-%d")  # classmethod — creates new datetime
```

### `timedelta` — duration and arithmetic

```python
from datetime import datetime, timedelta

now = datetime.now()

delta = timedelta(days=7, hours=3, minutes=30, seconds=15)

future = now + delta
past   = now - delta

# Difference between two datetimes → timedelta
dt1 = datetime(2026, 3, 10)
dt2 = datetime(2026, 3,  1)
diff = dt1 - dt2
print(diff)                  # 9 days, 0:00:00
print(diff.days)             # 9
print(diff.seconds)          # 0  (seconds WITHIN the day portion only)
print(diff.total_seconds())  # 777600.0  (total, always use this)
```

**PCAP trap:** `.seconds` is the seconds component of the day portion only (0–86399). `.total_seconds()` is the full duration as a float — always prefer it for calculations.

### `datetime` module summary

| | `date` | `time` | `datetime` | `timedelta` |
|---|---|---|---|---|
| Constructor | `date(y, m, d)` | `time(h, m, s)` | `datetime(y,m,d,h,m,s)` | `timedelta(days=, seconds=, ...)` |
| Current | `date.today()` | — | `datetime.now()` | — |
| From Unix ts | `date.fromtimestamp(ts)` | — | `datetime.fromtimestamp(ts)` | — |
| To Unix ts | — | — | `dt.timestamp()` | — |
| Format → str | `d.strftime(fmt)` | `t.strftime(fmt)` | `dt.strftime(fmt)` | — |
| Parse str → | `date.fromisoformat(s)` | — | `datetime.strptime(s, fmt)` | — |
| Arithmetic | `d + timedelta` | — | `dt + timedelta` | `td1 + td2` |

---

## Side-by-side: same task in both modules

**Get current time as Unix timestamp:**
```python
import time
ts = time.time()                       # float, always works

from datetime import datetime
ts = datetime.now().timestamp()        # float, same result
```

**Convert Unix timestamp to readable string:**
```python
import time
s = time.ctime(1741132800)             # 'Thu Mar  5 00:00:00 2026'
s = time.strftime("%Y-%m-%d", time.localtime(1741132800))  # '2026-03-05'

from datetime import datetime
s = datetime.fromtimestamp(1741132800).strftime("%Y-%m-%d")  # '2026-03-05'
```

**Measure elapsed time:**
```python
import time
start = time.perf_counter()
# ... work ...
elapsed = time.perf_counter() - start   # use time module — no datetime equivalent
```

**Date arithmetic (add 30 days):**
```python
from datetime import datetime, timedelta
result = datetime.now() + timedelta(days=30)  # use datetime — time module can't do this
```

---

## PCAP Traps

1. **`from datetime import time`** — the class `time` from the `datetime` module shadows the `time` *module*. After this import, `time.sleep()` will raise `AttributeError`.

2. **`strftime` vs `strptime`:** `strftime` = **f**ormat (object → string). `strptime` = **p**arse (string → object). `strptime` is only on `datetime`, not on `date` or `time`.

3. **`timedelta.seconds` vs `timedelta.total_seconds()`:** `timedelta(days=1, seconds=30).seconds` → `30` (not 86430). Always use `.total_seconds()` for full duration.

4. **`time.time()`** returns a float, not a `datetime`. You cannot call `.strftime()` on it directly.

5. **`datetime.time` class has no `.now()`** — only `datetime.datetime` has `.now()`. `datetime.time` is just a static container for clock fields.

6. **`date.isoweekday()` vs `date.weekday()`:** `weekday()` → Monday=0, Sunday=6. `isoweekday()` → Monday=1, Sunday=7.
