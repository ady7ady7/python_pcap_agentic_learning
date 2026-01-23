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

## Week 2, Day 2 - 2026-01-13

**Topic:** Polymorphism & Multiple Strategies
**Score:** 8/8 tasks completed | 86.25% (bonus task 9 not completed)
**Difficulty:** 5/10

**Tasks Completed:**
1. PCAP warm-up (polymorphism prediction with shapes)
2. PROJECT: LevelCrossStrategy implementation
3. PROJECT: MovingAverageStrategy implementation (self-corrected performance issues)
4. Polymorphism testing script (test_strategies.py)
5. isinstance() patterns (type checking)
6. MRO prediction (incorrect - critical gap identified)
7. PCAP multiple choice (3 polymorphism questions)
8. Code review (fix polymorphism bugs in Vehicle classes)

**Key Learnings:** Polymorphism (using objects through same interface), duck typing in Python, ABCs for polymorphic contracts, isinstance() for type-specific behavior, `__init__.py` and `__all__` for package management (industry standard), self-correction of performance issues (slicing vs `.remove()`)

**Student Question:**
"What does `__all__` mean in `__init__.py` and why do we use it?"
- **Answer:** Controls public API, enables clean imports, standard for Mid/Senior devs, provides explicit namespace control

**Student Corrections:**
- Fixed MovingAverageStrategy to use slicing (`[-self.ma_period:]`) instead of `.remove()` for O(1) performance
- Fixed `generate_signal()` to add price internally and handle all BUY/SELL/HOLD cases
- Caught mentor error on non-existent `get_level()` and `get_name()` methods (used attributes directly)
- Requested bonus tasks not count toward base 100% (correct)

**Critical Gap Identified:**
- **MRO (Method Resolution Order):** Predicted "C" but correct answer is "B" (0/10 on task)
- **Misconception:** Thought last-written method overwrites, but Python uses C3 linearization (left-to-right)
- **Rule:** In `class D(B, C)`, B has priority over C (leftmost parent wins)
- **Action:** Must practice MRO with diamond inheritance patterns

**Project Milestones:**
- Implemented `LevelCrossStrategy` (price level crossing)
- Implemented `MovingAverageStrategy` (MA-based signals with state management)
- Both strategies inherit from `BaseStrategy` ABC
- Configured `algo_backtest/strategies/__init__.py` with `__all__` (professional packaging)
- Demonstrated polymorphism through common interface

---

## Week 2, Day 3 - 2026-01-14

**Topic:** Composition vs Inheritance, Advanced Polymorphism & MRO Practice
**Score:** 5/7 base tasks completed (Tasks 3 & 6 skipped) | 86% (B)
**Difficulty:** 8/10 (too high - overengineered tasks)

**Tasks Completed:**
1. MRO Practice (Bat/Platypus diamond inheritance) - **10/10** ✅
2. Composition vs Inheritance Theory (Car/Engine) - **10/10** ✅
3. Position with Composition - SKIPPED (overengineered PositionMetadata)
4. Mixin Pattern (LoggerMixin) - **9/10** ✅
5. PCAP MRO Edge Cases - **10/10** ✅ (challenged mentor's wrong assessment)
6. Strategy Factory - SKIPPED (overengineered factory pattern)
7. Multiple Choice (3 questions) - **10/10** ✅
8. Code Review (Database composition refactoring) - **10/10** ✅

**Key Learnings:**
- **MRO MASTERED:** 0/10 on Day 2 → 10/10 on Day 3 (leftmost-parent-wins rule)
- Composition vs Inheritance (HAS-A vs IS-A) - when to use each
- Mixin pattern for adding functionality via multiple inheritance
- YAGNI principle (You Aren't Gonna Need It) - Option 1 in Task 8 showed senior-level judgment
- **Critical thinking:** Correctly challenged overengineered tasks instead of blindly implementing

**Student Corrections:**
- **Task 5 Case C:** Challenged mentor's wrong scoring - tested code and proved `S(R, Q)` where `R(Q)` does NOT raise error
- **Tasks 3 & 6:** Correctly identified as overengineered ("What the actual fuck is that StrategyFactory bullshit?")
- **Score corrected:** 82.86% → 86% after proving mentor wrong on Case C

**Student Feedback:**
- "Difficulty 8/10 - some really weird tasks + unclear bonus task"
- "Mixins, HAS-A vs IS-A - we need to practice this definitely"
- **"Yet the main objective is PCAP, do not forget"** ← CRITICAL reminder

**Mentor Errors Acknowledged:**
1. Task 5 Case C scoring was wrong (student proved with code)
2. Tasks 3 & 6 were overengineered for the sake of teaching patterns
3. Task 9 had unclear requirements
4. Difficulty too high (8/10 instead of target 5-6/10)

**Project Milestones:**
- No new code (Tasks 3 & 6 skipped)
- MRO understanding solidified (major gap closed)
- Professional engineering judgment demonstrated

**Action Items for Day 4:**
- Focus on **actually useful** implementations (position sizing, strategy comparison)
- More PCAP drills, less abstract OOP patterns
- Target difficulty 5-6/10

---

## Week 2, Day 4 - 2026-01-15

**Topic:** Position Sizing, Exception Handling & PCAP Drills
**Score:** 6/7 base tasks completed (Task 4 skipped) | 84% (B)
**Difficulty:** 5-9/10 (mixed - Task 4 was a brick wall)

**Tasks Completed:**
1. Exception Handling Order (try/except/else/finally) - **8/10** ✅
2. Position Sizing from Risk (@classmethod) - **9/10** ✅
3. List Comprehensions with Conditionals - **10/10** ✅
4. Strategy Backtesting Comparison - SKIPPED (mentor's fault - too big a leap)
5. Mutable Default Arguments trap - **10/10** ✅
6. @classmethod vs @staticmethod - **6/10** (mentor's fault - never taught @staticmethod)
7. Multiple Choice (3 questions) - **6.7/10** (missed super().__init__ behavior)
8. Code Review - Risk Calculator - **10/10** ✅

**Key Learnings:**
- Position sizing formula: `risk_dollars / distance`
- List comprehension: filter-if (at end) vs ternary-if (at beginning)
- Mutable default arguments trap - use `None` pattern
- try/except/else/finally flow - finally ALWAYS runs

**Student Feedback:**
- "Task 4 is definitely a LEAP too big for today"
- "I NEED TO UNDERSTAND THEM, and the road to that is through a step-by-step understanding process"
- "the main goal for me is to understand everything I do"
- Requested lesson file for @classmethod vs @staticmethod

**Critical Gap Identified:**
- **super().__init__() behavior:** Thought Python auto-calls parent's __init__ (it doesn't!)
- Must explicitly call `super().__init__()` or parent attributes won't be initialized

**Mentor Failures:**
1. Task 4 required List[BaseStrategy], Dict types, backtesting engine - none taught
2. Task 6 asked about @staticmethod - never taught
3. Task 9 depended on Task 4 - cascading failure
4. Difficulty mixed (5-9/10) instead of consistent 5-6/10

**Project Milestones:**
- ✅ Position sizing from risk implemented (`calculate_position_size` classmethod)
- ⚠️ Strategy comparison postponed (building blocks needed first)

**Action Items:**
- Create @classmethod/@staticmethod lesson file
- Break strategy comparison into smaller building blocks
- Keep difficulty at 5-6/10

---

## Week 2, Day 5 - 2026-01-16

**Topic:** Week 2 Review & Integration (Friday Wrap-up)
**Score:** 8/8 tasks completed | 92% (A-)
**Difficulty:** 4/10

**Tasks Completed:**
1. Quick Fire Review (6 Questions) - **90%** ✅
2. Inheritance Output Prediction - **100%** ✅
3. Exception Handling Output - **95%** ✅
4. @classmethod/@staticmethod Output - **90%** ✅
5. Position Integration Script - **100%** ✅
6. Multiple Choice (5 Questions) - **90%** ✅
7. Code Review (Find 4 Bugs) - **100%** ✅
8. Week 2 Self-Assessment - Complete ✅

**Key Achievements:**
- Fixed super().__init__() misconception from Day 4
- All 3 inheritance output predictions correct
- Perfect Position integration with calculate_position_size
- Found all 4 bugs in Strategy class code review
- Difficulty was appropriate (4/10 vs previous 8-9/10)

**Student Self-Ratings (5-point scale):**
- Inheritance basics: 5/5
- super().__init__(): 5/5
- MRO: 5/5
- @classmethod: 4/5
- @staticmethod: 4/5
- Composition vs Inheritance: 4/5

**Week 2 Summary:**
| Day | Score | Topic |
|-----|-------|-------|
| 1 | 94% | Inheritance Fundamentals |
| 2 | 86.25% | Polymorphism & Strategies |
| 3 | 86% | Composition & MRO |
| 4 | 84% | Position Sizing |
| 5 | 92% | Week Review |

**Week 2 Average: 88.5% (B+)**

**Weekend Tasks:**
- PCAP Mock Exam A (30 questions)
- PCAP Mock Exam B (30 questions)
- Target: 70%+ (21/30) on each

---

## Week 3, Day 1 - 2026-01-19

**Topic:** Encapsulation & Properties
**Score:** 8/8 tasks completed | 92% (A-)
**Difficulty:** Medium
**Time Spent:** 120 minutes

**Tasks Completed:**
1. PCAP warm-up (access control conventions - 4 questions)
2. Name mangling output prediction
3. @property basics (Temperature class)
4. Price class implementation with validation
5. PROJECT: Trade class with encapsulated PnL
6. Property edge cases (side effects trap)
7. PCAP multiple choice (4 questions - 3/4 correct)
8. Integration: Position and Trade together (PositionTrade class)

**Key Learnings:**
- Access control conventions (`public`, `_protected`, `__private`)
- Name mangling transforms `__attr` to `_ClassName__attr`
- `@property` creates getters, `@name.setter` creates setters
- Properties are accessed without parentheses (not methods!)
- Name mangling purpose: prevent subclass collisions (NOT encryption)

**Critical Corrections:**
- Q7.1: Name mangling prevents accidental name collisions in subclasses, not "encrypting" values
- Task 5 bug: `trade.pnl()` should be `trade.pnl` (property, not method)
- Task 3: `AttributeError: can't set attribute` (no setter), not "no such attribute"

**Project Milestones:**
- Created Trade class with encapsulated PnL using @property
- Extended Position.should_close() to return Tuple[bool, str] for exit reason
- Built PositionTrade integration class (exceeded requirements)

---

## Week 3, Day 2 - 2026-01-20

**Topic:** Advanced Properties, Validation & `random` Module
**Score:** 8/8 + Bonus | 91% (A-)
**Difficulty:** 5/10
**Time Spent:** 120 minutes

**Tasks Completed:**
1. PCAP warm-up - random module basics (4 questions - 2/4)
2. Predict output - seed() behavior
3. Percentage class with validation
4. Property infinite recursion trap (PCAP trap)
5. PROJECT: Trade class enhancements (return_percent, risk_reward_ratio)
6. choice() vs sample() practice
7. PCAP multiple choice (4 questions - 4/4)
8. RiskValidator class with property validation
9. BONUS: Random trade generator function

**Key Learnings:**
- Property validation patterns (setter with constraints)
- Property recursion trap (use `self._value` not `self.value`)
- `random.seed()` makes results reproducible
- `choice()` can repeat, `sample()` returns unique elements

**Critical Corrections:**
- `random.random()` returns [0.0, 1.0) - excludes 1, not 0
- `randint` and `randrange` both return integers (difference is endpoint inclusion)

**Student Feedback:**
- Wants more coding, fewer prediction tasks
- `random` module is low priority - PCAP exam is the focus
- Requested scaffolded explanation for property recursion

**Project Milestones:**
- Trade class enhanced with `return_percent` and `risk_reward_ratio` properties
- RiskValidator class created with property-based validation
- Random trade generator function working

---

## Week 3, Day 3 - 2026-01-21

**Topic:** Decorators, Special Methods & PCAP Drills
**Score:** 8/8 | 89% (B+)
**Difficulty:** 5-6/10
**Time Spent:** 70 minutes

**Tasks Completed:**
1. Exception hierarchy (4 questions - 3.5/4)
2. BankAccount class with full encapsulation
3. `__str__` vs `__repr__` implementation
4. PROJECT: TradeManager class (`__len__`, `__iter__`, properties)
5. PCAP multiple choice (4 questions - 4/4)
6. Debug broken Product class (4 bugs found)
7. PROJECT: Position `__eq__` and `__hash__`
8. Mutable default arguments trap (review)

**Key Learnings:**
- `__len__` and `__iter__` make objects work with `len()` and `for` loops
- `__eq__` and `__hash__` enable set/dict usage
- Bare `except:` catches EVERYTHING (including SystemExit, KeyboardInterrupt)
- Validation should be in `__init__`, not in getter

**Critical Corrections:**
- Bare `except:` issues - catches more than expected
- `__repr__` formatting - don't use `!r` on class name
- Validation placement - validate in `__init__`, not getter

**Student Feedback:**
- Dunder methods weren't taught before being tested
- Requested dunder methods lesson file (created)
- Needs scaffolded inheritance/super() examples

**Project Milestones:**
- TradeManager class created with full functionality
- Position enhanced with `__eq__` and `__hash__`
- week3_dunder_methods.md lesson file created

---

## Week 3, Day 4 - 2026-01-22

**Topic:** Inheritance Patterns, Generators & PCAP Drills
**Score:** 91% (A-) - **Fair tasks only**
**Difficulty:** N/A (mentor error invalidated most tasks)
**Time Spent:** N/A

**MENTOR ERROR:** Majority of tasks tested generators/yield WITHOUT providing lesson material first.

**Fair Tasks Completed:**
1. Inheritance output prediction (3 snippets - 3/3 correct)
2. MarginAccount class with inheritance (excellent implementation)
3. Q1 only: Generator type/StopIteration (ran code to learn)
5. Q2: Class variable inheritance (0/1 - answered B, correct is C)
5. Q3: StopIteration exception (1/1 correct)
6. Debug inheritance bug - missing super().__init__() (perfect)

**Unfair Tasks (NOT SCORED):**
- Task 3 Q2, Q3: Generator expressions, memory differences
- Task 4: PriceGenerator with yield
- Task 5 Q1, Q4: yield questions
- Task 7: TradeManager generator methods
- Task 8: Generator vs list memory

**Key Learnings:**
- Inheritance patterns with/without super() solidified
- Class variable assignment creates new attribute on subclass (doesn't modify parent)
- StopIteration raised when generator exhausted

**Critical Correction:**
- Task 5 Q2: `Child.class_var = "child"` creates NEW attribute on Child, doesn't modify Parent's
- Output is `parent child`, not `child child`

**Student Feedback (Valid):**
- "MAJORITY of tasks revolved around generators and yield, WHERE WE DIDN'T HAVE THEM"
- "What kind of teaching approach is that?"
- Requested: 1. knowledge with examples, 2. scaffolded approach

**Corrective Action:**
- Created `lessons/week3_generators.md` with full scaffolded teaching
- Day 5 will properly introduce generator practice WITH lesson material

**Project Milestones:**
- MarginAccount class implemented correctly
- week3_generators.md lesson file created
- week3_useful_modules.md expanded with sys, os modules

---

## Week 3, Day 5 - 2026-01-23 (Friday)

**Topic:** Generators Practice, Week Review & Exam Prep
**Score:** 91% (A-)
**Difficulty:** 5/10 (appropriate)
**Time Spent:** Not reported

**Tasks Completed:**
1. Generator basics (4 questions - 3.5/4)
2. countdown generator (perfect)
3. Generator expressions (3/3 correct)
4. price_ticks generator (minor bug - didn't track price between ticks)
5. Portfolio class - Week 3 review (excellent)
6. PCAP multiple choice (3/4 - missed Q2 on read-only properties)
7. Debug generator bug (perfect - return → yield)
8. profitable_trades generator method (perfect)

**Key Learnings:**
- Generator syntax with `yield`
- Generator expressions `(x for x in items)`
- Exhausted generators return empty (not StopIteration in for loop)
- `return` in generator causes StopIteration

**Corrections:**
- Task 1 Q2: `list(exhausted_gen)` returns `[]`, not StopIteration
- Task 4: Price should accumulate changes, not always use start_price
- Task 6 Q2: Only Option A is a valid read-only property (B causes recursion, C is a method)

**Student Feedback:**
- "I still kind of don't understand the concept of using these generators. Lists seem to make more sense to me."
- Asked if generators are PCAP relevant (YES)

**Project Milestones:**
- PriceTickGenerator created
- Portfolio class with properties + dunder methods
- SimpleTradeManager with generator method

---

## Week 3 Summary

| Day | Score | Topic |
|-----|-------|-------|
| 1 | 92% | Encapsulation & Properties |
| 2 | 91% | Advanced Properties & Validation |
| 3 | 89% | Dunder Methods & TradeManager |
| 4 | 91% | Inheritance (fair tasks only) |
| 5 | 91% | Generators & Week Review |

**Week 3 Average: 90.8% (A-)**

**Strengths:**
- Excellent class-building skills (Portfolio, TradeManager, MarginAccount)
- Strong debugging abilities
- Good understanding of inheritance/super()
- Quick learner on new concepts (generators picked up in one session)

**Areas for Continued Practice:**
- Read-only property patterns (Option A vs B vs C)
- Generator use cases (when to use vs lists)
- Class variable inheritance behavior

**Weekend Tasks:**
- PCAP Mock Exam A (30 questions)
- PCAP Mock Exam B (30 questions)
- Target: 70%+ (21/30) on each

---

