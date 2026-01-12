# Tasks Archive

This file contains historical summaries of completed daily tasks.
Format: Date | Topic | Score | Difficulty | Notes

---

## Week 1, Day 1 - 2026-01-05

**Topic:** Modules, Packages & Import Mechanisms
**Score:** 8/8 tasks completed | 86.25%
**Difficulty:** Medium-Hard (mixed)

**Tasks Completed:**
1. Import variants (absolute, selective, alias, wildcard)
2. sys.path investigation and manipulation
3. Circular import debugging
4. AlgoBacktest project structure setup
5. Dependency checker with exception handling
6. Name shadowing edge cases
7. PCAP multiple choice (module imports)
8. Lazy import pattern implementation

**Key Learnings:** Import execution order, package structure patterns, exception handling, PEP 8 compliance

---

## Week 1, Day 2 - 2026-01-06

**Topic:** Strings, Exceptions & File I/O
**Score:** 8/8 tasks completed | 78.75%
**Difficulty:** Too Hard (8/10)

**Tasks Completed:**
1. String slicing edge cases (all correct predictions)
2. String methods comparison (find/index, strip variations, split)
3. safe_divide function with exception handling
4. Exception catching order debug
5. DataLoader class with CSV loading and error handling
6. validate_data method for DataFrame validation
7. read_config function with file I/O edge cases
8. PCAP multiple choice (try/except/else/finally execution order)

**Key Learnings:** String immutability, slicing never raises IndexError, `.find()` returns -1, exception hierarchy order matters, context managers for file I/O

**Issues Identified:** Curriculum sequencing error - OOP and advanced Pandas expected without prior instruction

---

## Week 1, Day 3 - 2026-01-07

**Topic:** OOP Fundamentals - Classes, Objects & Methods
**Score:** 9/9 tasks completed | 97.5%
**Difficulty:** Manageable (6/10)

**Tasks Completed:**
1. Understanding `self` (predict Counter output)
2. Instance vs class attributes (predict Dog species behavior)
3. BankAccount class implementation
4. Mutable class attributes trap hunt (TodoList bug)
5. Position class for trading positions (with explicit `side` parameter)
6. DataLoader bug fixes from Day 2 feedback
7. PCAP multiple choice (class/instance attributes, `__init__` returns)
8. OHLCCandle enhancement (doji detection, wick calculations)
9. Bonus: Employee class with auto-incrementing IDs

**Key Learnings:** Classes vs objects (blueprint analogy), `self` as object reference, instance attributes vs class attributes, mutable class attribute traps, connection to mutable default parameters, `__init__` constructor, methods vs functions

**Student Insights:**
- Challenged mentor's signed quantity spec (crypto-only, not industry standard)
- Implemented explicit `side` parameter (correct for futures/CFDs/stocks)
- Self-debugged `or` vs `and` logic error
- Lesson structure worked - material was sufficient for task completion

---

## Week 1, Day 4 - 2026-01-08

**Topic:** Magic Methods & Pandas Essentials
**Score:** 9/9 tasks completed | 93.5%
**Difficulty:** Easy-Medium (5/10)

**Tasks Completed:**
1. `__str__` vs `__repr__` output predictions
2. Magic method trap hunt (missing return statement)
3. Add `__str__` and `__repr__` to Position class
4. Pandas `.any()` drill (three approaches to NaN checking)
5. Boolean indexing practice (filtering OHLC data)
6. Trade class with P&L calculation and magic methods
7. PCAP multiple choice (magic methods, Pandas and/or operators)
8. DataLoader enhancements (`__repr__`, candle counting, filtering)
9. Bonus: Trade class method for win rate calculation

**Key Learnings:** `__str__` vs `__repr__` distinction, magic method fallback behavior, Pandas `.any()` semantics, boolean indexing with `&` operator, class methods, PEP 8 line length compliance

**Student Contributions:**
- Corrected mentor on Task 2 (TypeError IS raised)
- Defended PEP 8 formatting in multi-line f-strings
- Validated P&L calculations ($50 correct, not $500)
- Pandas teaching gap officially closed

---

## Week 1, Day 5 - 2026-01-09

**Topic:** Week 1 Review & Integration (Friday Wrap-up)
**Score:** 8/8 tasks completed | 93.75%
**Difficulty:** Medium (5-6/10)

**Tasks Completed:**
1. Quick fire review (6 questions covering Week 1 concepts)
2. Integration challenge (main.py with DataLoader → Trade → PositionManager workflow)
3. PCAP traps (predict output for 3 tricky code snippets)
4. Exception handling (safe_backtest_runner with try/except/else/finally)
5. Pandas advanced filtering (bullish candles, multi-condition, top-N, conditional columns)
6. PositionManager class (multi-position management with SL/TP checking)
7. PCAP multiple choice (class attributes, exceptions, Pandas operators)
8. Code review challenge (find 8 issues in broken PositionManager, rewrite cleanly)

**Key Learnings:** Week 1 integration (modules + strings + exceptions + OOP + magic methods + Pandas), end-to-end backtest workflow, Pandas optimization patterns (vectorized operations vs `.apply()` vs `.iterrows()`), list comprehension for safe filtering, exception handling complete structure

**Student Contributions:**
- Corrected mentor on Task 2 import paths (relative imports correct when main.py inside package)
- Requested Pandas optimization patterns be added to lessons/pandas.md (completed)
- Fixed PositionManager return type and list modification issues
- Demonstrated professional code review by catching mentor error

**Project Milestones:**
- AlgoBacktest Core functional (DataLoader, Trade, Position, PositionManager)
- End-to-end backtest execution in main.py
- Position management system with SL/TP triggers

**Week 1 Summary:**
40 tasks completed across 5 days. Average score: **89.95% (B+)**. All foundational Python and OOP concepts covered. Project framework established and functional.

---

## Week 2, Day 1 - 2026-01-13

**Topic:** Inheritance Fundamentals
**Score:** 8/8 tasks completed | 94%
**Difficulty:** Medium (5/10)

**Tasks Completed:**
1. PCAP warm-up (predict output with inheritance)
2. SavingsAccount class (inheriting from BankAccount)
3. Strategy pattern (parent Strategy, child LevelCrossStrategy)
4. PCAP trap hunt (missing `super().__init__()`)
5. isinstance/issubclass practice (8 predictions)
6. PROJECT: BaseStrategy ABC (abstract base class for strategies)
7. PCAP multiple choice (3 inheritance questions)
8. Code review (identify 8 issues, fix broken strategy)

**Key Learnings:** Basic inheritance syntax, `super()` function for calling parent methods, method overriding, Abstract Base Classes (ABC) with `@abstractmethod`, `isinstance()`/`issubclass()` for type checking, understanding when parent `__init__` runs and sets attributes

**Student Question:**
"Are these attributes or parameters? What is the difference?"
- **Answer:** Parameters are variables in function definitions (`def __init__(self, owner, balance)`). Attributes are variables attached to objects (`self.owner`, `self.balance`).

**Student Insights:**
- Understood all concepts but noted they need regular practice for refinement
- Correctly used `super()` in all inheritance tasks
- Perfect ABC implementation with abstract methods

**Project Milestones:**
- Created `algo_backtest/strategies/` package
- Implemented BaseStrategy ABC with abstract `generate_signal()` method
- Foundation ready for concrete strategy classes

---

