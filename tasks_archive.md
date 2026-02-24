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

## Week 4, Day 1 - 2026-01-26 (Monday)

**Topic:** Lambda Functions, map() & filter()
**Score:** 98% (A+)
**Difficulty:** 5/10
**Time Spent:** 70 minutes (including lesson)

**Tasks Completed:**
1. Lambda basics (4 questions - 4/4)
2. Lambda with ternary expression (perfect nested ternary)
3. map() practice (3 questions - 2.5/3)
4. filter() practice (3 questions - 3/3)
5. Sorting with lambda key (3 questions - 3/3)
6. PROJECT: Trade filtering with lambda (perfect)
7. PCAP multiple choice (4 questions - 4/4)
8. Combining map() and filter() (works, bonus correct)

**Key Learnings:**
- Lambda syntax: `lambda params: expression`
- Lambda can only have ONE expression (no statements, no return keyword)
- `map()` applies function to all items, returns map object
- `filter()` selects items where function returns True
- `filter(None, items)` keeps truthy values (NOT searches for None)
- Sorting with `key=lambda x: ...`

**Student Question:**
- "Why does `filter(None, items)` remove falsy values?"
- Answered: `None` as function means "use truthiness", not "find None objects"

**Corrections:**
- Task 3 Q1: First `print(result)` shows `<map object at 0x...>`, not the list

**Project Milestones:**
- Trade filtering with lambda functions
- Combined conditions in filter

---

## Week 4, Day 2 - 2026-01-27 (Tuesday)

**Topic:** Closures & Factory Functions
**Score:** 90% (A-)
**Difficulty:** 4/10
**Time Spent:** 50 minutes

**Tasks Completed:**
1. Closure basics (4 questions - 4/4)
2. make_counter closure (perfect implementation)
3. nonlocal vs global (3 questions - 3/3)
4. Late binding trap (Q1-Q2 correct, Q3 fix missed)
5. PROJECT: make_price_validator (logic works, spec deviation)
6. PCAP multiple choice (4 questions - 3/4)
7. PROJECT: make_trade_logger (perfect implementation)
8. Closure vs class comparison (thoughtful analysis)

**Key Learnings:**
- Closures remember variables from enclosing scope
- `nonlocal` needed only for MODIFYING enclosing variables, not reading
- Late binding trap: lambda captures variable reference, not value
- Fix: `lambda i=i: i` captures value at definition time
- Factory functions create customized functions

**Critical Corrections:**
- Task 4 Q3: Fix is `lambda i=i: i` (default argument captures value)
- Task 6 Q4: Lambda works in loops! Issue is late binding, not lambda functionality
- Reading outer variables doesn't need `nonlocal` - only writing does

**Student Question:**
- "Why does reading outer variable work without `nonlocal`?"
- Answered: Read = LEGB lookup automatic. Write = needs `nonlocal`/`global`

**Project Milestones:**
- make_counter closure working
- make_trade_logger with tuple return
- make_price_validator with validation logic

---

## Week 4, Day 3 - 2026-01-28 (Wednesday)

**Topic:** reduce(), Decorators & Functional Patterns
**Score:** 89% (B+)
**Difficulty:** 5/10
**Time Spent:** 55 minutes

**Tasks Completed:**
1. reduce() basics (4 questions - 4/4)
2. reduce() implementations (product, max, flatten - 3/3)
3. Decorator basics (4 questions - 3/4)
4. announce decorator (works, but calls function twice)
5. PROJECT: Trade stats with reduce (3/3)
6. PCAP multiple choice (4 questions - 3/4)
7. PROJECT: log_call decorator (works)
8. Combining map/filter/reduce (caught mentor error!)

**Key Learnings:**
- reduce() requires initializer when reducing dicts to numbers
- Decorator syntax: `foo = decorator(foo)` not `decorator.foo()`
- Decorators use closures to "remember" the wrapped function
- Don't call wrapped function twice in decorator wrapper

**Critical Corrections:**
- Task 3 Q2: `@decorator` = `foo = decorator(foo)` not dot notation
- Task 4: Call wrapped function ONCE, not twice
- Task 6 Q4: Decorators CAN access arguments (that's their purpose!)

**Student Caught Mentor Error:**
Task 8 expected values were wrong. Correct: 4 winners, $1050 total PnL.

**Project Milestones:**
- reduce() for trade statistics
- Decorator logging pattern demonstrated
- map/filter/reduce pipeline for trade processing

---

## Week 4, Day 4 - 2026-01-29 (Thursday)

**Topic:** Week 4 Review & PCAP Drills (Pre-Exam)
**Score:** 89% (B+)
**Difficulty:** 5/10
**Time Spent:** 80 minutes

**Tasks Completed:**
1. Quick fire review (10 questions - 8/10)
2. Output predictions (6 snippets - 6/6)
3. Debug decorator (fixed correctly)
4. Closure stats tracker (works with minor elif bug)
5. PCAP multiple choice (8 questions - 8/8)
6. PROJECT: Functional trade processor (complete)
7. functools.wraps (understood)
8. Integration concepts (good answers)

**Key Learnings:**
- Lambda returns a FUNCTION, not the result directly
- Late binding fix: `lambda i=i: i` captures value at definition
- `filter(None, items)` uses truthiness, NOT searches for None
- `@wraps(func)` preserves function metadata in decorators
- List comprehensions preferred over map/filter in most cases

**Critical Corrections:**
- Q1: `lambda x: x > 5` returns a function (C), not True/False (D)
- Q10: Fix with `lambda i=i: i`, not "use list comprehension"
- Task 4: Use `if` not `elif` when both conditions can be true

**Student Questions Answered:**
- filter(None, ...) explained: None = "use truthiness"
- map/filter in industry: List comprehensions preferred 90% of time

---

## Week 4, Day 5 - 2026-01-30

**Topic:** Final Functional Programming Review & Exam Prep
**Score:** 8/8 tasks completed | 85% (B+)
**Difficulty:** 5-7/10
**Time Spent:** 90 minutes

**Tasks Completed:**
1. Lambda Expression Mastery (6 questions - 6/6)
2. Closure Deep Dive (4 questions - 4/4)
3. map/filter/reduce Pipeline (working implementation)
4. Decorator with Arguments (repeat(n) pattern)
5. PCAP Multiple Choice (6/8)
6. PROJECT: Strategy Signal Generator (caught mentor error!)
7. Decorator Stacking Order (0/3 - weak spot)
8. Week 4 Self-Assessment

**Key Learnings:**
- Lambda fundamentals solid (100% on Task 1)
- Closure tracing mastered (100% on Task 2)
- Decorator stacking: `@a @b def f()` = `f = a(b(f))`
- Application order: bottom-up, Execution order: top-down
- filter(lambda x: x % 2, nums) keeps ODD numbers (truthy)

**Critical Corrections:**
- Stacked decorators: `@deco @deco def five(): return 5` → 5*2*2 = 20 (not error)
- filter(x % 2) keeps truthy (1 for odd), not even numbers
- Decorator stacking output: `<b><i>Hello</i></b>` not `<i><b>Hello</b></i>`

**Student Caught Mentor Error:**
- Task 6 expected output was wrong
- Price 108→106 stays above 105 = HOLD (not SELL)
- Student's signal logic was CORRECT

**Week 4 Summary:**
| Day | Score | Topic |
|-----|-------|-------|
| 1 | 98% | Lambda, map(), filter() |
| 2 | 90% | Closures & Factory Functions |
| 3 | 89% | reduce(), Decorators |
| 4 | 89% | Week Review |
| 5 | 85% | Final Review & Exam Prep |

**Week 4 Average: 90.2% (A-)**

**Weekend Tasks:**
- PCAP Mock Exam A (30 questions) - 93.3%
- PCAP Mock Exam B (30 questions) - 86.7%
- Average: 90%

---

## Week 5, Day 1 - 2026-02-02 (Monday)

**Topic:** datetime Module & File I/O Basics
**Score:** 89% (B+)
**Difficulty:** 5/10
**Time Spent:** 70 minutes

**Tasks Completed:**
1. datetime basics (6 questions - 6/6)
2. File reading methods (4 questions - 2.5/4)
3. File writing practice (3 parts - 3/3)
4. File mode PCAP traps (4 questions - 4/4)
5. PROJECT: TradeLogger class (functional, minor deviations)
6. PCAP multiple choice (8 questions - 8/8)
7. Context manager understanding (3 questions - 2/3)
8. datetime edge cases (3 questions - 3/3)

**Key Learnings:**
- weekday() (0-6) vs isoweekday() (1-7)
- strftime (datetime→string) vs strptime (string→datetime)
- timedelta arithmetic
- File modes: 'w' overwrites, 'a' appends, 'x' creates (fails if exists)
- read() vs readline() vs readlines() - different return types
- Context managers ensure cleanup even on exception

**Areas Needing Practice:**
- readline() includes `\n` character
- readlines() returns LIST of strings
- Context manager exception behavior (file closes, exception propagates)
- strftime timestamp formatting (avoid microseconds)

**Student Feedback:**
- Wants more practice-based tasks (less theory)
- datetime module needs reinforcement through coding
- Requested past concept integration (1-2 tasks)

---

## Week 5, Day 2 - 2026-02-03 (Tuesday)

**Topic:** datetime Practice & File I/O Applications
**Score:** 78% (C+)
**Difficulty:** 6-7/10
**Time Spent:** Long session (practice-heavy)

**Tasks Completed:**
1. datetime coding practice (3 parts - 3/3)
2. File I/O coding practice (3 parts - 2/3, missing read_non_empty_lines)
3. Closure + datetime integration (2 parts - functional)
4. PROJECT: TradeLogger enhancement (type confusion bug)
5. PCAP multiple choice (6 questions - 6/6)
6. ConfigManager with properties (incomplete implementation)
7. Decorator + File I/O (identified bugs, needs help)
8. timedelta deep practice (3 questions - mostly correct)

**Key Issues:**
- File mode 'w' vs 'a' confusion in decorator (overwrites vs appends)
- Calling function twice in decorator wrapper
- Type hint confusion: datetime parameter treated as string
- _load_config printed but didn't actually parse/load values
- December edge case in mondays_in_month

**Strengths:**
- datetime fundamentals solid
- PCAP theory 100%
- Closure concepts understood
- Good debugging instincts (correctly identified decorator issues)

**Areas for Day 3:**
- Decorator patterns (append mode, single function call)
- Property setters with validation and side effects
- Edge cases in date calculations

---

## Week 5, Day 3 - 2026-02-04 (Wednesday)

**Topic:** Decorator Mastery & File Modes Deep Dive
**Score:** 91% (A-)
**Difficulty:** 5-6/10
**Time Spent:** 2 hours

**Tasks Completed:**
1. File mode drill (4 questions - 4/4)
2. Decorator bug fixes (2 parts - 2/2)
3. log_to_file decorator (correct implementation)
4. Type hint contracts (3 questions - Q3 correct, Q1/Q2 task poorly designed)
5. PROJECT: BacktestEngine (uses existing Position/Trade/PositionManager)
6. PCAP multiple choice (6 questions - 5/6)
7. read_non_empty_lines makeup (functional)
8. rate_limiter decorator (correct with nonlocal)

**Key Wins:**
- File mode 'w' vs 'a' mastered
- Decorator pattern: store result once, use append mode
- nonlocal keyword used correctly
- BacktestEngine integrates with existing codebase

**Minor Issues:**
- open_position missing return statement
- Q4 PCAP: confused regular decorator with decorator-with-arguments
- return inside with block (works but suboptimal style)

**Student Feedback:**
- Decorators need more practice to feel comfortable
- rate_limiter pattern is useful real-world example
- 2-hour session was long for one sitting

---

## Week 5, Day 4 - 2026-02-05 (Thursday)

**Topic:** Review & Consolidation (Lighter Day)
**Score:** 93% (A)
**Difficulty:** 4/10
**Time Spent:** 45 minutes

**Tasks Completed:**
1. Decorator with arguments pattern (correct - A)
2. @timer decorator (working implementation)
3. PCAP quick fire (7/8 - Q3 strftime returns string)
4. BacktestEngine bug fix (return statement added)
5. BacktestEngine test (working, correct PnL calculations)
6. Mutable default arguments trap (correct fix, minor output format)

**Key Wins:**
- Decorator with arguments pattern now solid
- BacktestEngine fully functional
- @timer decorator another useful pattern learned
- Mutable default trap understood

**Minor Issue:**
- Q3: strftime ALWAYS returns string, even "%Y" → "2026" not 2026

**Student Feedback:**
- Appreciated lighter session on busy day
- ~45 minutes was manageable

---

## Week 5, Day 5 - 2026-02-06 (Friday)

**Topic:** Week Review & Exam Prep
**Score:** 88% (B+)
**Difficulty:** 5/10 (Task 2 retry: 7-8/10)
**Time Spent:** 70 minutes

**Tasks Completed:**
1. PCAP warm-up - shallow copy + nonlocal (2/2)
2. @retry decorator (correct code, needed AI help)
3. filter_log_by_date (functional, boundary/strip issues)
4. PCAP simulation 10 questions (7/10)
5. BacktestEngine __str__ method (clean)
6. Week 5 self-assessment (honest ratings)
7. Decorator stacking (correct order, wrong details)
8. Exception handling + File I/O (set instead of string bug)

**Key Issues:**
- Q5: @wraps does NOT preserve __code__
- Q6: IOError catches FileNotFoundError (parent catches child)
- Q7: %y = 2-digit year, %Y = 4-digit year
- {text} creates set, not string

**Student Feedback:**
- Decorators still difficult, especially complex patterns
- Wants scaffolded daily decorator practice with explanations
- Doesn't want to rely on AI help
- Other topics comfortable (4-5/5)

**Weekend Tasks:**
- PCAP Mock Exam A (30 questions)
- PCAP Mock Exam B (30 questions)
- Target: 70%+ (21/30) on each

---

## Week 5 Weekend Exams - 2026-02-07

**Topic:** PCAP Mock Exams (Weeks 1-5 Comprehensive)

**Exam A:** 29/30 (96.7%) - Grade: A+ | Time: 15 minutes
**Exam B:** 25/30 (83.3%) - Grade: B+ | Time: 17 minutes
**Average:** 27/30 (90.0%) - Grade: A-

**Exam A Highlights:**
- Only miss: Q30 (f-string :.1f vs :.2f)
- 100% on Decorators, File I/O, datetime, OOP, Closures

**Exam B Mistakes:**
1. Q2: readline() consumed all of 'abc' (no newline), read() returns empty
2. Q8: MRO with super() — DBCA not DBA (recurring gap)
3. Q9: f.read().strip() preserves internal newlines
4. Q23: __new__/Singleton — not yet taught (valid complaint)
5. Q30: Decorator stacking without @wraps — wrapper.__name__ behavior

**Student Feedback:**
- Complaints about arithmetic-based questions (day counting, leap year)
- Valid point about testing __new__ before teaching it
- Decorators (simple) now solid, stacking still needs work
- MRO with super() in diamond inheritance remains a gap

**Week 5 Final Statistics:**
- Daily Average: 87.8%
- Exam Average: 90.0%
- Overall: 88.4% (B+)

---

## Week 6, Day 1 - 2026-02-09

**Topic:** The Iterator Protocol & Advanced Generators
**Score:** 81% (revised) | **Time:** 60 minutes | **Difficulty:** 6-7/10

**Tasks:**
1. PCAP warm-up: iter/generator identity (100%)
2. Decorator trace — scaffolded read-only (70%)
3. FibonacciIterator class (55%)
4. __new__ vs __init__ predictions (90%)
5. yield from + generator pipeline (75%)
6. MRO trace — diamond inheritance (100%)
7. PROJECT: Position IDs + ticker-aware processing (75%)
8. PCAP simulation 5 questions (80%)

**Key Issues:**
- Hardcoded Fibonacci list instead of computing with state
- PositionManager removal line doesn't filter by ticker (critical bug)
- Decorator param_name vs actual value confusion
- :.2f format specifier still recurring
- __init__ receives original args, not __new__-transformed values

**Strengths:**
- MRO gap officially closed (100% across 3 sessions)
- __new__/Singleton understood
- uuid integration in Position clean
- Pipeline concept works

---

## Week 6, Day 2 - 2026-02-10

**Topic:** Iterator Mastery, Bug Fixes & Trade ID Propagation
**Score:** 95% (A) | **Time:** 60 minutes | **Difficulty:** 5-6/10

**Tasks:**
1. PCAP warm-up: iterator reset + partial consumption (92%)
2. Decorator fill-in-the-blanks — 5/5 correct (100%)
3. FibonacciIterator rewrite with dynamic state (100%)
4. __new__ vs __init__ argument flow predictions (100%)
5. PROJECT: Fix PositionManager ticker bug — ID-based removal (90%)
6. PROJECT: Propagate position_id to Trade class (100%)
7. CountdownIterator class (100%)
8. PCAP simulation 5 questions — 4/5 (80%)

**Key Wins:**
- Day 1 gaps all closed (Fibonacci, __init__ args, ticker bug)
- Decorator scaffolding Day 2 complete (all blanks correct)
- Self-caught PositionManager bug in first attempt
- Project: full Position→Trade ID chain working

**Remaining Gap:**
- Iterable vs Iterator pattern (yield in __iter__ = new generator per call)

---

## Week 6, Day 3 - 2026-02-11

**Topic:** Iterable vs Iterator, Decorator Writing & Price Stream Generator
**Score:** 93% (A) | **Time:** 80 minutes | **Difficulty:** 6/10

**Tasks:**
1. PCAP warm-up: iterable vs iterator side-by-side (95%)
2. Decorator written from scratch — @log_call perfect (100%)
3. NumberRange iterable class with yield (100%)
4. Generator edge cases: return value, yield from, partial (95%)
5. PROJECT: PriceTick namedtuple + create_price_stream() (95%)
6. PROJECT: Tick-by-tick backtest with generator (90%)
7. Generator expressions: lazy eval + T/F questions (88%)
8. PCAP simulation 5 questions — 4/5 (80%)

**Key Wins:**
- Decorator scaffolding complete (trace → blanks → write from scratch)
- First generator-powered backtest working
- Generator lazy evaluation understood (mutated source list trick)

**Remaining Gaps:**
- Iterable recognition in exam context (Q8 Q1 — same pattern as Tasks 1-3 but missed)
- "Generators always faster" misconception

---

## Week 6, Day 4 - 2026-02-12

**Topic:** Advanced Generators & Parameterized Decorators
**Score:** 85% (B+) | **Difficulty:** 7/10 | (External session)

**Tasks:**
1. Generator expressions deep dive
2. yield from chaining
3. namedtuple operations (_replace, _fields, _asdict)
4. __new__ and __init__ interaction
5. PROJECT: @repeat(n) decorator factory
6. PROJECT: sma_indicator() generator pipeline
7. PROJECT: filtered price stream with filter_func predicate
8. PCAP simulation — 55% (exposed 6 key gaps)

**Key Wins:**
- Parameterized decorator (@repeat(n)) implemented correctly
- Generator pipeline (sma_indicator consuming price_stream) working
- namedtuple _replace() and _asdict() demonstrated

**Gaps Identified (targeted in Day 5):**
- `in` on generators: sequential consumption not grasped
- `iter(generator) is generator` → True (first occurrence)
- Resettable iterator reset pattern missed
- @wraps stacking `__name__` propagation
- Closure `__name__` reflects def-statement name, not variable
- Independent generator instances

---

## Week 6, Day 5 - 2026-02-13

**Topic:** Exam Gap Closure — Iterator Identity, `in` on Generators, @wraps Stacking, Closure Names
**Score:** 95% (A) | **Time:** 40 minutes | **Difficulty:** 7/10

**Tasks:**
1. `in` operator on generators — sequential consumption (100%)
2. `iter(obj) is obj` identity — iterator vs iterable (100%)
3. Resettable iterators — `__iter__` reset pattern (100%)
4. `__name__` and @wraps stacking (100%)
5. Independent generator instances (80% — Q2 wrong: iter(generator) True not False)
6. PCAP simulation — 6/6 (100%)
7. Concept map — fill-in-the-blanks (95% — Item 2 swapped __iter__/__next__)

**Key Wins:**
- All 6 Day 4 gaps addressed and closed
- Simulation score jumped: Day 4 40-55% → Day 5 100%
- @wraps stacking propagation mastered

**Persistent Gap:**
- `iter(generator) is generator` still wrong in Task 5 Q2 (3rd occurrence across Days 4-5 + exam)

---

## Week 6 Weekend Exams - 2026-02-14/15

**Exam A:** 25/30 (83%) — Time: 18 minutes
**Exam B:** 24/30 (80%) — Time: reported
**Average:** 49/60 (81.7%)

**Exam A Misses (5):**
- Q7: type() after __new__ returning non-instance → reflects actual returned type (int not Weird)
- Q24: Iterator vs iterable direction — every iterator IS an iterable (B), not every iterable is iterator (A)
- Q25: %y vs %Y — 2-digit vs 4-digit year PCAP trap
- Q27: iter(generator) is generator → True not False (4th occurrence of this gap!)
- Q28: del var removes binding only; sys.modules retains cache → B (True, True)

**Exam B Misses (6):**
- Q2: yield from on string IS valid (C was wrong — answer is A)
- Q5: Singleton via __new__ is NOT an error (D was wrong — answer is A)
- Q7: namedtuple _replace() returns new object, not error (D was wrong — answer is B)
- Q9: Resettable iterator after break — second loop resets via __iter__ → B (0 1 2)
- Q23: gen1 is gen2 → False; iter(gen3) is gen3 → True (answered B, correct is A)
- Q30: next() on map object IS valid — map returns an iterator (answered D, correct is A)

**Summary:** "Error" false-positives recur (Q5, Q7, Q30). Critical gap: `iter(generator) is generator` still failing.

---

## Week 6 Summary

| Day | Score | Topic |
|-----|-------|-------|
| 1 | 81% | Iterator Protocol & Advanced Generators |
| 2 | 95% | Iterator Mastery & Trade ID Propagation |
| 3 | 93% | Iterable vs Iterator & Price Stream Generator |
| 4 | 85% | Advanced Generators & Parameterized Decorators |
| 5 | 95% | Exam Gap Closure |
| Exam A | 83% | PCAP Mock (Weeks 1-6) |
| Exam B | 80% | PCAP Mock (Weeks 1-6) |

**Week 6 Daily Average: 89.8% (B+)**

**Strengths:**
- Iterator protocol mastered (custom __iter__/__next__ classes)
- Generator pipelines working (price_stream → sma_indicator)
- Project: full Position→Trade→ID chain, PositionManager ticker bug fixed
- @wraps stacking now solid

**Persistent Gaps entering Week 7:**
- `iter(generator) is generator` → True (failed 4 times across week)
- "Error" false-positives under exam pressure (Singleton, _replace, map iterator)
- %y vs %Y (PCAP trap — failed twice)

**Project Progress:**
- BacktestEngine tick-by-tick simulation via generator pipeline ✅
- @repeat(n) decorator factory ✅
- sma_indicator() generator chaining ✅
- Filtered price stream with predicate ✅

---

## Week 7, Day 1 - 2026-02-16

**Topic:** The `logging` Module — Fundamentals to Project Integration
**Score:** 62% on answered tasks (Tasks 6/7 excused) | **Time:** 60 minutes | **Difficulty:** Felt harder than 5/10

**Tasks:**
1. PCAP warm-up — level threshold predictions (2/3)
2. Theory — named logger vs root logger (2/3)
3. Two-stage filtering prediction (1/3)
4. setup_logger() implementation (8/10 — missing duplicate-handler guard)
5. logging vs warnings distinction (2.5/3)
6. PROJECT: Add logging to BacktestEngine — excused
7. PROJECT: setup_logging() in main.py — excused
8. PCAP simulation 5 questions (2/5)

**Key Wins:**
- basicConfig() one-shot rule understood
- logging.warning() vs warnings.warn() distinction correct
- setup_logger() function structure correct

**Gaps to Close:**
- Two-stage filtering (Logger gate then Handler gate — failed Tasks 3 and 8 Q3)
- Logger singleton by name (same name = same object — failed Task 2 Q3 and 8 Q5)
- logging.exception() vs logging.error() (Task 8 Q4)
- Default output format: WARNING:root:message not bare text

**Action:** Lesson rewritten with scaffolded WHAT/WHY/HOW structure. Day 2 follows observe → predict → build → test approach.

---

## Week 7, Day 4 - 2026-02-19

**Topic:** PCAP Crunch — Exceptions, Strings, Closures + logging.exception() Final Fix
**Score:** 95% (A) [revised after disputes] | **Time:** 70 minutes | **Difficulty:** 6/10

**Tasks:**
1. logging.exception() observe + answer — gap finally closed (3/3 revised)
2. safe_divide() with logging — ValueError not caught in caller; f-strings accepted (9/10)
3. Exception order predictions — all 3 correct after review (3/3 revised)
4. parse_trade_log() string processing — perfect implementation (10/10)
5. Closure/nonlocal predictions — all 4 correct including late-binding lambda (4/4)
6. @log_calls decorator — working; missing `raise` after exception(); f-strings accepted (9/10)
7. PCAP simulation 8 questions — 6/8; wrong on raise "error" (TypeError not SyntaxError) and reading closure vars (B not D)

**Key Wins:**
- logging.exception() gap closed: logs at ERROR + appends traceback, does NOT raise/stop
- parse_trade_log() clean and professional
- All closure/late-binding predictions correct
- Teaching gap acknowledged: %s in log calls never taught explicitly — lesson updated

**Remaining PCAP gaps:**
- `raise "string"` → TypeError at runtime, not SyntaxError (T7 Q2)
- Reading outer vars in closures doesn't need nonlocal (T7 Q5) — knows in practice, missed in theory
- Missing `raise` after `logger.exception()` in decorator (T6)

**Lesson Updated:** `%s` in log calls vs `%(name)s` in Formatters — new PART 8 added to lesson file.

---

## Week 7, Day 3 - 2026-02-18

**Topic:** logging — Closing Gaps + Introspection Touch + Project Integration
**Score:** 90% (A-) [revised after disputes] | **Time:** 50 minutes | **Difficulty:** 5/10

**Tasks:**
1. logging.exception() — observe vs error(), gap targeted (2/4 — Q2/Q3 still wrong)
2. PCAP simulation — full logging set, 5 questions (5/5 — all correct)
3. Introspection — __dict__, hasattr, getattr, setattr, isinstance vs type() (6.5/7)
4. PROJECT: Add logging to BacktestEngine (9.5/10 — f-strings accepted, formatter design fault)
5. PROJECT: setup_logging() in main.py, verified with actual output (7/10 — __main__ not root)
6. PCAP warm-up — logging.warn deprecated, __name__ dotted path (2/3)

**Key Wins:**
- PCAP simulation 100% — all logging concepts solid under pressure
- BacktestEngine logging integrated — INFO on open/close, DEBUG on tick
- Introspection tools all correct — __dict__, hasattr, getattr, setattr, isinstance/type() distinction
- Valid disputes upheld: print() wrappers, f-strings (untaught context), orphan formatter (task fault)

**Remaining Gaps:**
- logging.exception() still wrong on Q2/Q3 (doesn't raise, logs at ERROR level)
- __name__ = full dotted path, not just filename (Q6 Q3)
- Root logger vs named logger in setup_logging() (self-corrected)

**Student Preference Noted:** 10-20% more coding — Day 4 adjusted.

---

## Week 7, Day 2 - 2026-02-17

**Topic:** `logging` — Observe, Predict, Build (Scaffolded)
**Score:** 88% (B+) | **Time:** 50 minutes | **Difficulty:** 5/10

**Tasks:**
1. Observe 4 snippets — default format, basicConfig threshold, one-shot rule (3/3)
2. Two-gate filtering — observe and fix (2.5/3)
3. Singleton confirmed empirically with `is` and `id()` (3/3)
4. Predict then verify — all three two-gate scenarios correct (3/3)
5. Build from scratch step by step — Steps 1-3 correct; Step 4 had 3 bugs, self-corrected (8/10)
6. PCAP drill on Day 1 gaps — 4/5 (logging.exception() still wrong)

**Key Wins:**
- Two-gate mental model formed and applied correctly under prediction pressure
- Built working logger (StreamHandler + FileHandler + Formatter) without lesson reference
- Three Day 1 gaps closed: default format, two-gate rule, logger singleton

**Remaining Gap:**
- `logging.exception()` — does NOT raise; logs at ERROR + appends traceback (2nd occurrence)

---


## Week 7, Day 5 - 2026-02-20

**Topic:** Week 7 Review + PCAP Full Simulation
**Score:** 83% (B) | **Time:** 45 minutes | **Difficulty:** 6/10

**Tasks Completed:**
1. Quick-fire gap closers (no code) — 2/4 (raise "string" and nonlocal-for-reading still wrong)
2. safe_divide() corrected — both bugs fixed, all three call paths demonstrated
3. audit_object() introspection utility — correct logic, but printed instead of returning dict
4. Predict + Fix two PCAP traps — exception order correct; decorator bug misdiagnosed
5. make_validator() closure factory — 10/10, clean implementation
6. PCAP Full Simulation (10 questions) — 7/10 (Q2 iter(generator), Q9 __name__ wrong)

**Persistent Gaps Entering Weekend:**
- iter(generator) is generator → True (5th+ occurrence)
- __name__ = full dotted path when imported (3rd occurrence)
- raise "string" → TypeError at runtime (2nd occurrence)
- Reading outer variable in closure needs no nonlocal (3rd+ occurrence)

---

## Week 7 Weekend Exams - 2026-02-22/23

**Exam A:** 25/30 = 83% | Time: 14 min
**Exam B:** 24/30 = 80% | Time: 9 min
**Combined:** 49/60 = **82%**

**Closed gaps (correct in both exams):**
- iter(generator) is same object — CLOSED
- __name__ = full dotted path when imported — CLOSED
- nonlocal only for assignment not reading — CLOSED

**New gaps identified:**
- Named logger default level = NOTSET (not WARNING) — root is WARNING
- del instance attr reveals class attr (no AttributeError)
- @property calling self.val inside val getter → RecursionError
- basicConfig no-op after last-resort handler fires
- 0.1 + 0.2 == 0.3 → False (IEEE 754)
- a = new_list is rebinding not mutation
- __getitem__ enables for loop via legacy sequence protocol

---

## Week 8, Day 1 - 2026-02-23

**Topic:** Exam Crunch + Documentation
**Score:** ~82% (B) | **Time:** 2 hours | **Difficulty:** 5/10

**Tasks:**
1. PCAP Trap Gauntlet — 6/8 (Q1 wrong: print(x) prints once [1,2] not twice; Q3 wrong: 10+i not [i])
2. Scope drills — 3/3 (nonlocal, closure read, LEGB all correct)
3. Exception hierarchy — 5.5/7 (hierarchy + KeyboardInterrupt correct; __str__ hardcoded 99.0; catch printed manually instead of using e)
4. Docstrings — 7/10 (dead fmt removed; prose style accepted; steps still in process_price; no Raises added — architectural pushback upheld)
5. PCAP sim — 6/8 scored (Q1 __slots__ excused — not PCAP; Q3 context managers excused — not taught; Q6 *args is tuple not list; Q7 __repr__ default is <Class...> not __str__ fallback)
6. Decorator debug — 8/10 (return/return func fixed; wrapper(*args) missing **kwargs missed)
7. Full backtest — 10/10 (4 positions, 2 tickers, logging working, __str__ correct, PnL 60260, win_rate 75%)

**Disputes upheld:**
- __slots__ excused — not on PCAP syllabus
- Context managers excused — not taught
- Validation in BacktestEngine — architectural SRP argument accepted

**New content added:**
- Context managers section added to week8_exam_crunch.md (one PCAP question possible)

---

## Week 8, Day 2 - 2026-02-24

**Topic:** OOP Deep Drills + PCAP Simulation
**Score:** ~88% (B+) | **Time:** 2 hours | **Difficulty:** 6/10

**Tasks:**
1. Predict 8 outputs — 6.5/8 (Q6 wrong: circular linked list, a.next.next.val = 1 not None)
2. OOP bug hunt (Animal→Dog→GuideDog) — 7/10 (core bug identified; fix introduced positional arg order error in GuideDog)
3. PCAP simulation 12 questions — 12/12 (perfect, including untaught metaclass Q7 by reasoning)
4. Custom Countdown iterator — 9/10 (protocol correct; reset() has unnecessary print side-effect)
5. Exception handling refactor — 8/10 (with + specific exceptions correct; missed: print() is code smell in utility, should log or re-raise)
6. Class vs instance attribute trap — 10/10 (fully resolved)
7. Docstrings task — excused (files already documented)

**Project goals noted for Days 3-5:**
- R-multiple profit calculation (risk-normalised PnL, Sharpe, profit factor)
- Strategy-aware positions (strategy_id, strategy_name on Position)
- Per-strategy reporting grouped by strategy_id

---
