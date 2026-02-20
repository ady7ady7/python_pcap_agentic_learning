from typing import List
from datetime import datetime
import logging
from algo_backtest.engine.position import Position
from algo_backtest.engine.trade import Trade
from algo_backtest.engine.position_manager import PositionManager


logger = logging.getLogger(__name__)
fmt = logging.Formatter('[%(asctime)s] [%(levelname)s]: %(message)s')


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
        
        
    def __str__(self) -> str:
        """
        Return a summary like:
        BacktestEngine: 2 open | 3 closed | PnL: $1500.00
        """
        
        return f'{__name__}: {(self.position_manager.get_position_count())} open | {len(self.completed_trades)} closed | PnL: ${self.total_pnl}'
        
        
    def open_position(self, ticker, side, entry, quantity, stop_loss, take_profit) -> Position:
        """
        Open a new position and add to manager.

        Returns:
            The created Position object
        """
        
        position = Position(ticker, side, entry, quantity, stop_loss, take_profit)
        self.position_manager.add_position(position)
        logger.info(f'Position {self.position_manager.position.position_id}: {position.side} {position.ticker} @ {position.entry}')
        return position
        
    
    def process_price(self, ticker: str, current_price: float) -> List[Trade]:
        
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
        
        closed_positions = self.position_manager.close_triggered_positions(ticker, current_price)
        logger.debug(f'Processing price for {ticker} at ${current_price}')
        newly_closed_trades = []
        for position in closed_positions:
            exit_reason = position.should_close(current_price)[1]
            trade = Trade(
                          position.position_id,
                          position.ticker, 
                          position.side, 
                          position.entry_price, 
                          current_price, 
                          position.quantity,
                          exit_reason = exit_reason)
            logger.info(f'Position {trade.position_id} @ {trade.ticker} closed with {trade.pnl} as a {exit_reason}')
            newly_closed_trades.append(trade)
            self.completed_trades.append(trade)
            
        return newly_closed_trades
            
 
 
    @property
    def total_pnl(self) -> float:
        """Sum of PnL from all completed trades."""
        self._total_pnl = round(sum([trade.pnl for trade in self.completed_trades]), 2)
        return self._total_pnl

    @property
    def win_rate(self) -> float:
        """Win rate using Trade.calculate_win_rate()."""
        self._win_rate = Trade.calculate_win_rate(self.completed_trades)
        return self._win_rate
    
    

if __name__ == '__main__':
    engine = BacktestEngine()

    # Open positions on different tickers
    engine.open_position('FDAX', 'BUY', 24500, 1, stop_loss=24450, take_profit=24600)
    engine.open_position('EURUSD', 'BUY', 1.0800, 10000, stop_loss=1.0750, take_profit=1.0850)

    # FDAX price moves — should only affect FDAX position
    closed = engine.process_price('FDAX', 24600)
    print(f'FDAX trades closed: {len(closed)}')       # 1 (TP hit)
    print(f'Open positions: {engine.position_manager.get_position_count()}')  # 1 (EURUSD still open)

    # EURUSD price moves — should only affect EURUSD position
    closed = engine.process_price('EURUSD', 1.0850)
    print(f'EURUSD trades closed: {len(closed)}')      # 1 (TP hit)
    print(f'Open positions: {engine.position_manager.get_position_count()}')  # 0

    # Verify unique IDs
    engine2 = BacktestEngine()
    p1 = engine2.open_position('FDAX', 'BUY', 24500, 1, stop_loss=24450, take_profit=24600)
    p2 = engine2.open_position('FDAX', 'SELL', 24500, 1, stop_loss=24550, take_profit=24400)
    print(p1.position_id != p2.position_id)  # True — different IDs