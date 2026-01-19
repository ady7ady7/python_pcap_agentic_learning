# AlgoBacktest Core - Project Roadmap

**Goal:** Build a professional backtesting engine for scenario-based trading strategies using Python, Pandas, and NumPy.

**Stack:** Python 3.10+, Pandas, NumPy, OOP Architecture

---

## Phase 1: Foundations & Data (Weeks 1-3)

### Week 1: Project Setup ✅ COMPLETE
- [x] Create package structure (`algo_backtest/`, `data/`, `engine/`, `strategies/`)
- [x] Setup `requirements.txt` (Pandas, NumPy)
- [x] Create `main.py` entry point
- [x] Version tracking in `__init__.py`

### Week 2: OOP Foundations ✅ COMPLETE
- [x] Inheritance & Polymorphism (BaseStrategy ABC)
- [x] LevelCrossStrategy & MovingAverageStrategy
- [x] @classmethod for position sizing
- [x] `Position` class with SL/TP, PnL calculation, `should_close()`
- [x] `calculate_position_size` classmethod

### Week 3: Encapsulation & Trade Class (CURRENT)
- [ ] `Trade` class with encapsulated PnL (using @property)
- [ ] Protected/private attributes (`_protected`, `__private`)
- [ ] Property decorators for controlled access
- [ ] Position-to-Trade conversion workflow
- [ ] Unit tests for Trade class

---

## Phase 2: The Engine (Weeks 4-6)

### Week 4: Strategy Architecture
- [ ] `Strategy` Abstract Base Class (ABC)
- [ ] Define `entry_condition(price)` abstract method
- [ ] Define `exit_condition(price, sl, tp)` abstract method
- [ ] Implement `LevelCrossStrategy` (inherits from Strategy)

### Week 5: Backtesting Engine
- [ ] `BacktestEngine` class
- [ ] Private attribute `__pnl` (encapsulation)
- [ ] Method: `simulate_trades(data, strategy)`
- [ ] Event loop: check triggers row-by-row

### Week 6: Event-Driven Architecture
- [ ] Convert DataFrame to generator (yield row as namedtuple)
- [ ] Implement tick-by-tick simulation
- [ ] Log trade execution events

---

## Phase 3: Polish & Documentation (Weeks 7-8)

### Week 7: Logging & Debugging
- [ ] Add Python `logging` module
- [ ] Log: Trade opened, SL hit, TP hit, Trade closed
- [ ] Error handling for edge cases

### Week 8: Finalization
- [ ] Add docstrings to all classes/methods
- [ ] Generate performance charts (optional: matplotlib)
- [ ] Final project demo script

---

## Strategies to Implement (Priority Order)

1. **LevelCrossStrategy:** Enter when price crosses X, exit at SL/TP
2. **TouchAndRetraceStrategy:** Enter on level touch + pullback confirmation
3. **RangeBreakoutStrategy:** Enter on breakout above/below defined range

---

**Current Status:** Week 3, Day 1 - Encapsulation & Trade Class
**Last Updated:** 2026-01-19
