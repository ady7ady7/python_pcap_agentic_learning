# PCAP Mock Exam Feedback

This file tracks your performance on Weekend Mock Exams.

---

## Week 1 Exam A - 2026-01-10

**Time Taken:** 12 minutes (Start: 9:10, Finish: 9:22)
**Score:** 24/30 (80%)
**Result:** ✅ PASS (70% required)
**Grade:** B

---

### Section-by-Section Breakdown

| Section | Score | Percentage |
|---------|-------|------------|
| Modules & Packages (1-6) | 4/6 | 66.7% |
| Strings (7-12) | 5/6 | 83.3% |
| Exceptions (13-18) | 6/6 | 100% |
| OOP Fundamentals (19-24) | 5/6 | 83.3% |
| Magic Methods & Pandas (25-30) | 4/6 | 66.7% |

---

### Detailed Question Analysis

#### ✅ Correct Answers (24/30)

**Section 1: Modules & Packages**
- Q1: ✅ A - Correct (`<class 'module'>`)
- Q2: ✅ D - Correct (`import math.sqrt` causes SyntaxError)
- Q3: ✅ A - Correct (`True` - sys.path never empty)
- Q6: ✅ A - Correct (both reference same value)

**Section 2: Strings**
- Q7: ✅ A - Correct (slicing out of range returns empty string)
- Q8: ✅ B - Correct (`"pcap"`)
- Q9: ✅ A - Correct (`.find()` returns -1 when not found)
- Q11: ✅ A - Correct (`.replace()` with count=1)
- Q12: ✅ C - Correct (`.index()` raises ValueError)

**Section 3: Exceptions**
- Q13: ✅ A - Correct (`A C`)
- Q14: ✅ B - Correct (most specific first)
- Q15: ✅ B - Correct (`A B D` - excellent reasoning!)
- Q16: ✅ A - Correct (else executes when no exception)
- Q17: ✅ A - Correct (`Error Done`)
- Q18: ✅ B - Correct (KeyError)

**Section 4: OOP Fundamentals**
- Q20: ✅ B - Correct (self is the instance)
- Q21: ✅ C - Correct (count = 2)
- Q22: ✅ A - Correct (`__init__` returns None implicitly)
- Q23: ✅ B - Correct (mutable class attribute trap)
- Q24: ✅ A - Correct (methods defined inside classes)

**Section 5: Magic Methods & Pandas**
- Q27: ✅ B - Correct (True=1, False=0, sum=2)
- Q28: ✅ A - Correct (boolean indexing syntax)
- Q29: ✅ C - Correct (returns Series)
- Q30: ✅ C - Correct (`&` for AND in Pandas)

---

#### ❌ Incorrect Answers (6/30)

**Q4: `__init__.py` purpose**
- **Your answer:** "Honestly, I don't know."
- **Correct answer:** B - It marks a directory as a Python package
- **Explanation:** In Python 3.3+, `__init__.py` is optional for namespace packages, but it still serves to mark a directory as a regular package. If present, it can contain initialization code (but doesn't have to). You worked with this in Week 1 Day 1 when creating the algo_backtest package structure.
- **Topic:** Modules & Packages

**Q5: Module caching behavior**
- **Your answer:** D - Python creates a new copy of the module
- **Correct answer:** C - Python uses the cached version from `sys.modules`
- **Explanation:** Python caches imported modules in `sys.modules` dictionary. When you import the same module twice, Python doesn't re-execute the code - it retrieves the cached module object. This is why circular imports can work in certain cases.
- **Review:** Week 1 Day 1 tasks on `sys.path` and import mechanisms
- **Topic:** Modules & Packages

**Q10: String mutability**
- **Your answer:** A - `"zbc"`
- **Correct answer:** C - `TypeError`
- **Explanation:** Strings are **immutable** in Python. You cannot modify individual characters using index assignment (`s[0] = "z"`). This raises `TypeError: 'str' object does not support item assignment`. To change a string, you must create a new one (e.g., `s = "z" + s[1:]`).
- **Review:** Week 1 Day 2 - String immutability is a core PCAP concept
- **Topic:** Strings
- **Critical Concept:** This is a fundamental Python principle - know it cold for the exam

**Q19: Instance vs Class Attributes**
- **Your answer:** B - `"Lupus"`
- **Correct answer:** A - `"Canis"`
- **Explanation:** When you assign `d1.species = "Lupus"`, you're creating a **new instance attribute** on `d1` that shadows the class attribute. The class attribute `Dog.species` remains `"Canis"`. Since `d2.species` was never assigned at the instance level, it still references the class attribute. This is a classic PCAP trap!
- **Key Distinction:**
  - `d1.species = "Lupus"` → Creates instance attribute on d1
  - `Dog.species = "Lupus"` → Modifies class attribute (affects all instances without their own instance attribute)
- **Review:** Week 1 Day 3 - OOP Fundamentals, class vs instance attributes
- **Topic:** OOP Fundamentals
- **Critical Concept:** You got Q23 correct (mutable class attribute trap), so you understand shared state. This question tests whether assigning to an instance attribute modifies the class or creates a shadow.

**Q25: `__str__` return type**
- **Your answer:** A - `None`
- **Correct answer:** C - `TypeError`
- **Explanation:** Magic method `__str__` **must return a string**. If it returns `None` (or any non-string), Python raises `TypeError: __str__ returned non-string (type NoneType)`. This is enforced by Python's internals.
- **Review:** Week 1 Day 4 - Magic Methods, `__str__` must return str
- **Topic:** Magic Methods
- **Critical Concept:** `__repr__` has the same requirement - must return a string

**Q26: When `__repr__` is called**
- **Your answer:** A - When you print an object and `__str__` is not defined
- **Correct answer:** A is technically correct, but the full answer includes "also when `repr()` is called explicitly"
- **Partial Credit:** ✅ Your understanding is correct! The answer key says "A - When you print and __str__ is not defined (also when repr() called explicitly)"
- **Actually:** This should be marked CORRECT. You answered A, which is the right choice.
- **Topic:** Magic Methods

**CORRECTION:** Q26 is actually CORRECT! Let me recalculate.

---

### Corrected Score: 25/30 (83.3%) - B

After reviewing Q26, your answer was correct. Updated breakdown:

**Incorrect Answers: 5 total**
- Q4: `__init__.py` purpose (didn't know)
- Q5: Module caching (thought new copy created)
- Q10: String immutability (thought strings are mutable)
- Q19: Instance vs class attributes (thought assignment modifies class attribute)
- Q25: `__str__` return type (thought None is allowed)

---

### Strengths Observed

1. **Exception Handling Mastery:** 6/6 (100%) - Perfect score! You fully understand try/except/else/finally flow, exception hierarchy, and error types.

2. **Pandas Fundamentals:** 4/4 correct Pandas questions - boolean indexing, `.sum()` on booleans, `.isna()` behavior, operators.

3. **String Methods:** Strong understanding of `.find()`, `.index()`, `.replace()`, `.strip()`, `.lower()` - only missed immutability concept.

4. **OOP Basics:** Solid grasp of `self`, `__init__`, methods vs functions, mutable class attribute trap.

5. **Speed:** 12 minutes for 30 questions is extremely fast (24 seconds per question average). You're confident and decisive.

---

### Critical Gaps to Address

#### 🔴 HIGH PRIORITY - Study Immediately

**1. String Immutability (Q10)**
- **What you need to know:**
  - Strings are **immutable** - you cannot change them in place
  - `s[0] = "x"` raises `TypeError`
  - To "modify" a string, create a new one: `s = "x" + s[1:]`
- **PCAP Trap:** Exam loves to test this with index assignment
- **Practice:**
  ```python
  s = "hello"
  # s[0] = "H"  # TypeError!
  s = "H" + s[1:]  # Correct: "Hello"
  ```

**2. Instance vs Class Attributes (Q19)**
- **What you need to know:**
  - `instance.attr = value` → Creates/modifies **instance attribute**
  - `ClassName.attr = value` → Modifies **class attribute**
  - Instance attribute **shadows** class attribute (doesn't modify it)
- **PCAP Trap:** Assigning to instance doesn't affect other instances
- **Review:** Week 1 Day 3 OOP lesson - you got the mutable class attribute trap (Q23) but missed this one

**3. Magic Method Return Types (Q25)**
- **What you need to know:**
  - `__str__` must return `str` (TypeError if not)
  - `__repr__` must return `str` (TypeError if not)
  - `__init__` must return `None` (TypeError if not)
- **PCAP Trap:** Returning wrong type from magic methods

#### 🟡 MEDIUM PRIORITY - Review This Weekend

**4. Module Caching (Q5)**
- **What you need to know:**
  - Python caches imports in `sys.modules` dictionary
  - Second import of same module uses cached version (doesn't re-execute)
  - To force reload, use `importlib.reload(module)`
- **Practice:**
  ```python
  import sys
  import math
  print(id(math))
  import math  # Uses cached version
  print(id(math))  # Same ID!
  ```

**5. `__init__.py` Purpose (Q4)**
- **What you need to know:**
  - Marks directory as Python package (main purpose)
  - Optional in Python 3.3+ for namespace packages
  - Can contain package initialization code (but doesn't have to)
- **You worked with this:** Week 1 Day 1 - algo_backtest package setup

---

### Study Recommendations for Exam B

**Before taking Exam B tomorrow:**

1. **Read these lesson sections:**
   - [lessons/week1_modules_packages.md](../lessons/week1_modules_packages.md) - Module caching, `__init__.py`
   - [lessons/week1_strings_exceptions.md](../lessons/week1_strings_exceptions.md) - String immutability
   - [lessons/week1_oop_fundamentals.md](../lessons/week1_oop_fundamentals.md) - Instance vs class attributes
   - [lessons/week1_class_magic_methods.md](../lessons/week1_class_magic_methods.md) - `__str__`/`__repr__` return types

2. **Practice in REPL:**
   ```python
   # String immutability
   s = "test"
   s[0] = "T"  # What happens?

   # Instance vs class attributes
   class Dog:
       species = "Canis"

   d1 = Dog()
   d2 = Dog()
   d1.species = "Lupus"
   print(d2.species)  # What prints?

   # Magic method return types
   class Test:
       def __str__(self):
           return None  # What happens?

   print(Test())
   ```

3. **Focus areas for Exam B:**
   - Module & package mechanics (you got 4/6 = 66.7%)
   - String immutability edge cases
   - Class attribute shadowing patterns

---

### Performance Comparison

**Time Efficiency:** ⚡ Excellent (12 min / 65 min budget = 18% time used)
- You finished in under 1/5 of the allotted time
- **Pro:** Shows confidence and strong foundational knowledge
- **Con:** May want to slow down and double-check tricky questions (Q10, Q19, Q25 were conceptual, not time-pressure errors)

**Section Performance:**
- **Strongest:** Exceptions (100%) - rock solid
- **Weakest:** Modules & Packages (66.7%), Magic Methods & Pandas (66.7%)

**Exam Strategy Recommendation:**
- For Exam B, allocate 20-25 minutes
- Flag questions you're unsure about, review them before submitting
- Watch for "trap" questions testing immutability and class/instance attributes

---

### Verdict

**Result:** ✅ **PASS** (80% → Corrected to 83.3%)

You demonstrated strong fundamentals across Week 1 topics. Your exception handling is perfect, and your Pandas knowledge is solid. The 5 incorrect answers are fixable with targeted review of:
1. String immutability (critical concept)
2. Instance vs class attributes (PCAP trap)
3. Magic method return types (exam favorite)
4. Module caching behavior
5. `__init__.py` purpose

**Prediction for Exam B:** With focused review of the 5 gaps above, you should score 26-28/30 (87-93%).

**Ready for Week 2?** Yes! An 83% on the first mock exam shows you've absorbed Week 1 material. The gaps are specific and addressable.

---

### Next Steps

- [ ] Review the 5 incorrect questions above
- [ ] Practice string immutability in Python REPL
- [ ] Re-read instance vs class attributes section in OOP lesson
- [ ] Take Exam B tomorrow (Sunday)
- [ ] Compare Exam A vs Exam B performance

**Good work on your first PCAP mock exam!**
