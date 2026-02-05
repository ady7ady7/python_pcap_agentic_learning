'''Position management for trading strategies.'''

from typing import Optional, Tuple

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
        
    def __str__(self) -> str:
        '''A Python magic method used to return information about class instead of memory object'''
        return f'{self.side} {self.quantity} {self.ticker} @ {self.entry_price} [SL = {self.stop_loss}, TP = {self.take_profit}]'
    
    
    def __repr__(self) -> str:
        '''A Python magic method used to provide devs with useful information to recreate the object '''
        return f'Position(ticker = {self.ticker}, side = {self.side}, entry_price = {self.entry_price}, quantity = {self.quantity}, stop_loss = {self.stop_loss}, take_profit = {self.take_profit})'
    
    def __hash__(self):
        '''A dunder method that allows us to hash a given position to later be used in a dictionary'''
        return hash((self.ticker, self.side, self.entry_price, self.quantity))
    
    def __eq__(self, other) -> bool:
        '''Checks whether two positions are equal to each other
        
        '''
        return self.ticker == other.ticker and self.side == other.side and self.entry_price == other.entry_price and self.quantity == other.quantity
        
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
            pnl = float((current_price - self.entry_price) * self.quantity)
            return pnl
        elif self.side == 'SELL':
            pnl = float((self.entry_price - current_price) * self.quantity)
            return pnl
        
    
    def should_close(self, current_price: float) -> Tuple[bool, str]:
        
        '''
        Method used to check if position should close (if it hit SL or TP).
        Handles incorrect current_price.
        
        Returns:
        True if SL/TP hit, False otherwise
        '''
        
        if current_price < 0:
            print('Incorrect current price, it should be above 0!')
            return (False, 'Still open')
        if self.side != 'BUY' and self.side != 'SELL':
            print('Incorrect side, it should be either BUY or SELL (case insensitive)')
            return (False, 'Still open')
        
        
        if self.side == 'BUY' and current_price <= self.stop_loss: #Simple if-checks, starting from SL check
            print('Buy SL hit')
            return (True, 'Buy SL hit')
        elif self.side == 'BUY' and current_price >= self.take_profit:
            return (True, 'Buy TP hit')

        
        elif self.side == 'SELL' and current_price >= self.stop_loss:
            return (True, 'Sell SL hit')
        elif self.side == 'SELL' and current_price <= self.take_profit:
            return (True, 'Sell TP hit')

        
        
    @classmethod
    def calculate_position_size(cls,
                                account_balance: float,
                                risk_percent: float, 
                                entry_price: float, 
                                stop_loss_price: float) -> float:
        '''
        A class method used to calculate the position size based on a set risk %,
        entry + stop loss
        
        For now it uses a stop loss price - at some point I might decide to use distance instead - depends on our needs
        '''
        try:
            usd_risk = account_balance * (risk_percent / 100)
            distance = abs(entry_price - stop_loss_price)
            
            if distance != 0:
                position_size = usd_risk / distance
                return position_size
            else:
                print('The stop loss is set at the entry price, returning 0')
                return 0
            
        except Exception as e:
            print(f'Unexpected error: {str(e)}')