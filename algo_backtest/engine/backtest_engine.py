from typing import List
from datetime import datetime
from typing import Optional
import logging
from engine.position import Position
from engine.trade import Trade
from engine.position_manager import PositionManager


logger = logging.getLogger(__name__)


class BacktestEngine:
    '''
    This module is used as the main orchestrator for integrating other modules and handling our strategy backtesting in one place.
    As of now it's connected with few other modules:

    - Position - simulates 'open' positions, assigns unique position_id and potentially triggers closing positions
    - PositionManager - similar as above, yet it manages multiple positions and logs them, the rest is the same
    - Trade - manages CLOSED positions, after a given position is triggered as closed, a Trade object is created based on the relevant attributes

    The current structure of the flow is quite clear, and in the end it should allow me to test multiple strategies and their performance if they were launched simultaneously.
    This is and always was the MAIN goal of creating this project, and we're not far from that.

    The current methods of the BacktestEngine:

    - open_position(self, ticker, side, entry, quantity, stop_loss, take_profit) -> returns a Position object + appends it to the position manager
    - process_price(self, ticker: str, current_price: float) -> returns a list of closed trades for a given ticker,
    based on the processed price, automatically creates trade objects for every closed trade and appends them to self.completed_trades list.

    Read-only properties:
    win_rate 
    total_pnl

    These are self-explanatory.

    Updated on 23.02.2026 (added this module-level docstring)
    '''
    
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
        
        
    def open_position(self, 
                      ticker, 
                      side, 
                      entry, 
                      quantity, 
                      stop_loss, 
                      take_profit, 
                      strategy_id: Optional[str] = None, 
                      strategy_name: Optional[str] = None) -> Position:
        """
        Open a new position and add to manager.
        
        Args:
        ticker: str,
        side: str,
        entry_price: float, 
        quantity: float, 
        stop_loss: Optional[float] = None,
        take_profit: Optional[float] = None
        

        Returns:
            The created Position object
        """
        
        position = Position(ticker, side, entry, quantity, stop_loss, take_profit, strategy_id, strategy_name)
        self.position_manager.add_position(position)
        logger.info(f'@Strategy {position.strategy_name}: {position.strategy_id} Position {position.position_id}: {position.side} {position.ticker} @ {entry}')
        return position
        
    
    def process_price(self, ticker: str, current_price: float) -> List[Trade]:
        
        """
        Check all positions for a given ticker and given price.
        Close any that hit SL/TP and convert to Trade objects.
        
        Args:
        - ticker: str
        - current_price: float

        Steps:
        1. Use position_manager.close_triggered_positions(current_price)
        2. For each closed position, create a Trade object
        3. Add Trade to completed_trades
        4. Return list of newly created trades

        Returns:
            List of newly closed trades (empty if none closed)
        
        Appends self.completed_trades with all the newly closed trades.
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
                          stop_loss = position.stop_loss,
                          take_profit = position.take_profit,
                          strategy_id = position.strategy_id,
                          strategy_name = position.strategy_name,
                          exit_reason = exit_reason)
            logger.info(f'@Strategy {position.strategy_id}, {position.strategy_name} || Position {trade.position_id} @ {position.ticker} closed with {trade.pnl} as a {exit_reason}')
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
    pass
###Outdated test, removed for now