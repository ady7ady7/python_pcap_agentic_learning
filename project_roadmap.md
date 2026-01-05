# AlgoBacktest Core - Project Roadmap

**Goal:** Build a professional backtesting engine for scenario-based trading strategies using Python, Pandas, and NumPy.

**Stack:** Python 3.10+, Pandas, NumPy, OOP Architecture

---

## Phase 1: Foundations & Data (Weeks 1-3)

### Week 1: Project Setup ✓
- [ ] Create package structure (`algo_backtest/`, `data/`, `engine/`, `strategies/`)
- [ ] Setup `requirements.txt` (Pandas, NumPy)
- [ ] Create `main.py` entry point
- [ ] Version tracking in `__init__.py`

### Week 2: Data Infrastructure
- [ ] Build `DataLoader` class (loads CSV using Pandas)
- [ ] Handle missing data / dirty CSVs
- [ ] Implement `get_price_at_time(timestamp)` method
- [ ] Create `data/mock_trades.csv` with sample OHLC data

### Week 3: Core Domain Models
- [ ] `Position` class (attributes: entry_price, sl, tp, size)
- [ ] `Trade` class (attributes: open_time, close_time, pnl)
- [ ] Unit tests for SL/TP calculation logic

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

**Current Status:** Week 1, Day 1 - Initialization Phase
**Last Updated:** 2026-01-05
