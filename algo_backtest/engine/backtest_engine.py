from typing import List
from datetime import datetime
from position import Position
from trade import Trade
from position_manager import PositionManager


class BacktestEngine:
    """
    Orchestrates backtesting using existing Position and Trade classes.

    Lifecycle: Position (open) -> Trade (closed)

    Attributes:
        position_manager: Manages open positions
        completed_trades: List of closed Trade objects
    """
    
    def __init__(self):
        self.position_manager = PositionManager()
        self.completed_trades: List[Trade] = []
        self._win_rate = 0
        self._total_pnl = 0
        
    def open_position(self, ticker, side, entry, quantity, stop_loss, take_profit) -> Position:
        """
        Open a new position and add to manager.

        Returns:
            The created Position object
        """
        
        position = Position(ticker, side, entry, quantity, stop_loss, take_profit)
        self.position_manager.add_position(position)
        
    
    def process_price(self, current_price: float) -> List[Trade]:
        
        """
        Check all positions against current price.
        Close any that hit SL/TP and convert to Trade objects.

        Steps:
        1. Use position_manager.close_triggered_positions(current_price)
        2. For each closed position, create a Trade object
        3. Add Trade to completed_trades
        4. Return list of newly created trades

        Returns:
            List of newly closed trades (empty if none closed)
        """
        closed_positions = self.position_manager.close_triggered_positions(current_price)
        newly_closed_trades = []
        for position in closed_positions:
            exit_reason = position.should_close(current_price)[1]
            trade = Trade(position.ticker, 
                          position.side, 
                          position.entry_price, 
                          current_price, 
                          position.quantity,
                          exit_reason = exit_reason)
            newly_closed_trades.append(trade)
            self.completed_trades.append(trade)
            
        return newly_closed_trades
            
 
 
    @property
    def total_pnl(self) -> float:
        """Sum of PnL from all completed trades."""
        self._total_pnl = sum([trade.pnl for trade in self.completed_trades])
        return self._total_pnl

    @property
    def win_rate(self) -> float:
        """Win rate using Trade.calculate_win_rate()."""
        self._win_rate = Trade.calculate_win_rate(self.completed_trades)
        return self._win_rate
    
    

if __name__ == '__main__':
    engine = BacktestEngine()

    # Open a BUY position: entry 1.0800, SL 1.0750, TP 1.0850
    pos = engine.open_position('EURUSD', 'BUY', 1.0800, 10000,
                               stop_loss=1.0750, take_profit=1.0850)

    print(f'Open positions: {engine.position_manager.get_position_count()}')  # 1

    # Price moves to 1.0820 - no trigger
    closed = engine.process_price(1.0820)
    print(f'Trades closed: {len(closed)}')  # 0

    # Price hits TP at 1.0850
    closed = engine.process_price(1.0850)
    print(f'Trades closed: {len(closed)}')  # 1
    print(f'Total PnL: ${engine.total_pnl:.2f}')  # $500.00