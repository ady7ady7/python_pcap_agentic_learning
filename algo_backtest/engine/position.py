'''Position management for trading strategies.'''

from typing import Optional

class Position:
    '''
    Represents a single trading position
    
    Attributes:
    ticker: e.g. EURUSD, FDAX,
    entry_price: float e.g. 24500.25
    quantity: Number of units
    stop_loss: stop loss price - float e.g. 24470.5 (optional)
    take_profit: take profit price - float e.g. 24530.0 (optional)
    
    '''
    
    def __init__(
        self,
        ticker: str,
        side: str,
        entry_price: float, 
        quantity: float, 
        stop_loss: Optional[float] = None,
        take_profit: Optional[float] = None
    ) -> None:
        
        '''Initialize a new position'''
        
        self.ticker = ticker
        self.side = side.upper() #I decided to include side, as we will usually have this sorted out in this way
        self.entry_price = entry_price
        self.quantity = quantity
        self.stop_loss = stop_loss
        self.take_profit = take_profit
    
        #Therefore is_long or is_short is really redundant + it's also weird.
        
    def calculate_pnl(self, current_price: float) -> float:
        
        '''
        Method used to calculate the current P/L based on the current price.
        Handles incorrect side or current_price below 0.
        
        Returns:
        Unrealized P/L
        '''
        
        if self.side != 'BUY' and self.side != 'SELL':
            print('Incorrect side, it should be either BUY or SELL (case insensitive)')
            return None
        elif current_price < 0:
            print('Incorrect current price, it should be above 0!')
            return None
        
        if self.side == 'BUY':
            pnl = (current_price - self.entry_price) * self.quantity
            return pnl
        elif self.side == 'SELL':
            pnl = (self.entry_price - current_price) * self.quantity
            return pnl
        
    
    def should_close(self, current_price: float) -> bool:
        
        '''
        Method used to check if position should close (hit SL or TP).
        Handles incorrect current_price.
        
        Returns:
        True if SL/TP hit, False otherwise
        '''
        
        if current_price < 0:
            print('Incorrect current price, it should be above 0!')
            return False
        if self.side != 'BUY' and self.side != 'SELL':
            print('Incorrect side, it should be either BUY or SELL (case insensitive)')
            return False
        
        
        if self.side == 'BUY' and current_price < self.stop_loss: #Simple if-checks, starting from SL check
            print('Buy SL hit')
            return True
        elif self.side == 'BUY' and current_price > self.take_profit:
            print('Buy TP hit')
            return True

        
        elif self.side == 'SELL' and current_price > self.stop_loss:
            print('Sell SL hit')
            return True
        elif self.side == 'SELL' and current_price < self.take_profit:
            print('Sell TP hit')
            return True

        
        