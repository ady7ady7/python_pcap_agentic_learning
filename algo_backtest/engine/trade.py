"""Trade management for completed positions."""
from typing import Optional

class Trade:
    '''
    Represents a completed trade
    
    Attributes:
        ticker: Trading symbol.
        side: 'BUY' or 'SELL'.
        entry_price: Entry price.
        exit_price: Exit price.
        quantity: Number of units.
        entry_time: Entry timestamp (string or datetime).
        exit_time: Exit timestamp (string or datetime).
        pnl: Profit/Loss (calculated automatically).
        exit_reason: 'SL', 'TP', or 'MANUAL'.
    '''
    
    def __init__(self,
                 position_id: str,
                 ticker: str,
                 side: str,
                 entry_price: float,
                 exit_price: float,
                 quantity: float,
                 entry_time: Optional[str] = None,
                 exit_time: Optional[str] = None,
                 stop_loss: Optional[float] = None,
                 take_profit: Optional[float] = None,
                 exit_reason: Optional[str] = None
                 ):
        
        """Initialize a completed trade and calculate P&L."""
        
        self._position_id = position_id
        self._ticker = ticker
        self._side = side.upper()
        self._entry_price = entry_price
        self._exit_price = exit_price
        self._quantity = quantity
        self._entry_time = entry_time
        self._exit_time = exit_time
        self._stop_loss = stop_loss
        self._take_profit = take_profit
        
        if exit_reason is not None:
            self._exit_reason = exit_reason.upper()
        else:
            self._exit_reason = ''

        #Properties - is_winner + pnl + return_percent
        self.__pnl: Optional[float] = None
        self.__is_winner: Optional[bool] = None
        self.__return_percent: Optional[float] = None
        self.__risk_reward_ratio: Optional[float] = None
        
    def __str__(self):
        """
        User-friendly representation.

        Format: [WIN/LOSS] SIDE QUANTITY TICKER: ENTRY -> EXIT (REASON) | P&L: $X.XX
        Example: [WIN] BUY 10000 EURUSD: 1.0800 -> 1.0850 (TP) | P&L: $500.00
        """
        
        if self.is_winner == True:
            result = '[WIN]'
        else:
            result = '[LOSS]'
        
        return (f'''Trade {self._position_id}: {result} {self._side} {self._quantity} {self._ticker}: 
                {self._entry_price} -> {self._exit_price} {self._exit_reason}
                | P&L: ${self.pnl:.2f}''')
    
    def __repr__(self):
        
        
        return (f'Trade {self._position_id}: (ticker = {self._ticker!r}, side = {self._side!r}, '
                f'entry_price = {self._entry_price}, exit_price = {self._exit_price}, '
                f'quantity = {self._quantity}, pnl = {self.pnl:.2f}, exit_reason = {self._exit_reason!r}'
        )
    
    @property
    def position_id(self) -> str:
        '''Read-only property of position id - generated in Position'''
        return self._position_id
    
    @property
    def pnl(self) -> float:
        '''
        Calculate profit/loss based on side.

        Returns:
            P&L in currency units.
        '''
        if self._side != 'BUY' and self._side != 'SELL':
            print('Incorrect side, it should be either BUY or SELL (case insensitive)')
            return None
        elif self._exit_price < 0 or self._entry_price < 0:
            print('Incorrect exit price or entry price, it should be above 0!')
            return None
        
        if self._side == 'BUY':
            self.__pnl = (self._exit_price - self._entry_price) * self._quantity
            return self.__pnl
        elif self._side == 'SELL':
            self.__pnl = (self._entry_price - self._exit_price) * self._quantity
            return self.__pnl
        
    @property 
    def is_winner(self) -> bool:
        '''A property created to check if trade was profitable.'''
        if self.pnl > 0:
            self.__is_winner = True
        else:
            self.__is_winner = False
            
        return self.__is_winner
    
    @property
    def return_percent(self) -> float:
        '''A property used to calculate the %P/L'''
        if self._side == 'BUY':
            self.__return_percent = ((self._exit_price - self._entry_price) / self._entry_price) * 100
        else:
            self.__return_percent = ((self._entry_price - self._exit_price) / self._entry_price) * 100
            
        return self.__return_percent
    
    @property
    def risk_reward_ratio(self) -> float:
        '''A property used to calc R:R ratio'''
        if self._stop_loss == self._entry_price:
            return 0
        else:
            self.__risk_reward_ratio = abs(self._take_profit - self._entry_price) / abs(self._entry_price - self._stop_loss)
        return self.__risk_reward_ratio
    
    @classmethod
    def calculate_win_rate(cls, trades: list['Trade']) -> float:
        """
        Calculate win rate from list of trades.

        Args:
            trades: List of Trade objects.

        Returns:
            Win rate as percentage (0-100).
            Returns 0 if no trades.
        """

        if trades is not None:
            trades_profits = [trade.pnl for trade in trades]
            winners = [profit for profit in trades_profits if profit > 0]
            print(trades_profits)
            return (len(winners) / len(trades_profits)) * 100
            
        else:
            return 0