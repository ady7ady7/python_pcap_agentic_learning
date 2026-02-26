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
    
    - trades_by_strategy @26.02.26 - method used to group all trades based on their strategy for reporting, so we can see how different strats perform
    - strategy_report  @26.02.26 - self explanatory, reporting method for strategies

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
        
        return f'{__class__.__name__}: {(self.position_manager.get_position_count())} open | {len(self.completed_trades)} closed | PnL: ${self.total_pnl}'
        
        
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
    
    def trades_by_strategy(self) -> dict[str, list[Trade]]:
        '''Method used to filter trades based on their strategy - it can be called explicitly and/or its return may be eventually added to Class attributes, 
        but for now it just returns the dict, and we will use it in strategy_report without adding extra Class attributes
        
        Args:
        None - we use the self.completed_trades from our Class instance
        
        Returns:
        A dict where each strategy_id represents a key, and its trades are represented as a list.
        
        e.g 
        
        {'432': [Trade(position_id='957d8746-f5c1-4c9e-93df-2342e2a316d6', ticker='EURUSD', side='BUY', entry_price=105.6, exit_price=104.2, quantity=10000, pnl=-14000.00, exit_reason='still open', strategy_id='432', strategy_name='Super XD'), 
        Trade(position_id='e14c1475-c77b-4683-90cd-fda6946f42dd', ticker='EURUSD', side='SELL', entry_price=105.6, exit_price=104.2, quantity=10000, pnl=14000.00, exit_reason='still open', strategy_id='432', strategy_name='Super XD')]}
        '''
        
        if not self.completed_trades:
            logger.info(f'There are no completed trades in self.completed_trades, and we cannot proceed with filtering them by the strategy.')
            return None
        else:
            strategies_set = set([(trade.strategy_id, trade.strategy_name) for trade in self.completed_trades])
            completed_trades_by_strategy = {}
            for strategy in strategies_set:
                filtered_trades = [trade for trade in self.completed_trades if trade.strategy_id == strategy[0]]
                completed_trades_by_strategy[strategy] = filtered_trades
            return completed_trades_by_strategy
        
    def strategy_report(self):
        '''Method used to call trades_by_strategy method to get filtered trades and print out a report with stats for every strategy and portfolio total'''
        
        trades_filtered_by_strategy = self.trades_by_strategy()
        for strategy in trades_filtered_by_strategy:
            total_pnl = round(sum([trade.pnl for trade in trades_filtered_by_strategy[strategy]]), 2)
            win_rate = Trade.calculate_win_rate(trades_filtered_by_strategy[strategy])
            avg_r = sum(trade.r_multiple for trade in trades_filtered_by_strategy[strategy]) / len(trades_filtered_by_strategy[strategy])
            print(f'''{3* '-'} {strategy[0]} (ID: {strategy[1]}) {3* '-'}
                  
                  Trades: {len(trades_filtered_by_strategy[strategy])}
                  Win Rate: {win_rate}%
                  Total PnL: ${total_pnl:.2f}
                  Avg R: {avg_r:.2f}R
                  
                  ''')
        print(f'''{3* '-'} PORTFOLIO TOTAL  {3* '-'}
                  
                  Trades: {len(self.completed_trades)}
                  Win Rate: {self.win_rate}%
                  Total PnL: ${self.total_pnl}
                  Avg R: {round(sum(trade.r_multiple for trade in self.completed_trades) / len(self.completed_trades), 2)}R
                  
                  ''')
        

 
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