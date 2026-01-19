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
                 ticker: str,
                 side: str,
                 entry_price: float,
                 exit_price: float,
                 quantity: float,
                 entry_time: Optional[str] = None,
                 exit_time: Optional[str] = None,
                 exit_reason: Optional[str] = None
                 ):
        
        """Initialize a completed trade and calculate P&L."""
        
        self._ticker = ticker
        self._side = side.upper()
        self._entry_price = entry_price
        self._exit_price = exit_price
        self._quantity = quantity
        self._entry_time = entry_time
        self._exit_time = exit_time
        
        if exit_reason is not None:
            self._exit_reason = exit_reason.upper()
        else:
            self._exit_reason = ''

        #Properties - is_winner + pnl
        self.__pnl: Optional[float] = None
        self.__is_winner: Optional[bool] = None
        
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
        
        return (f'''{result} {self._side} {self._quantity} {self._ticker}: 
                {self._entry_price} -> {self._exit_price} {self._exit_reason}
                | P&L: ${self.pnl:.2f}''')
    
    def __repr__(self):
        
        
        return (f'Trade(ticker = {self._ticker!r}, side = {self._side!r},'
                f'entry_price = {self._entry_price}, exit_price = {self._exit_price}'
                f'quantity = {self._quantity}, pnl = {self.pnl:.2f}, exit_reason = {self._exit_reason!r}'
        )
    
    
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
        """A property created to check if trade was profitable."""
        if self.pnl > 0:
            self.__is_winner = True
        else:
            self.__is_winner = False
            
        return self.__is_winner
        
    
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
            trades_profits = [trade.pnl() for trade in trades]
            winners = [profit for profit in trades_profits if profit > 0]
            print(trades_profits)
            return (len(winners) / len(trades_profits)) * 100
            
        else:
            return 0