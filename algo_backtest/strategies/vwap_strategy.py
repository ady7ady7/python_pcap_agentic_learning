from .base_strategy import BaseStrategy

class VwapStrategy(BaseStrategy):
    '''
    Strategy which works based on current VWAP values
    
    
    '''
    
    def __init__(self, ticker: str):
        super().__init__('VWAP Strategy')
        self.ticker = ticker
        
    def generate_signal(self, price: float, vwap: float):
        
        '''
        Currently the strategy follows the simplest possible rule set
        
        We simply buy above VWAP and sell below, that's it.
        '''
        signal = None
        
        if price > vwap:
            signal = 'BUY'
        elif price < vwap:
            signal = 'SELL'
            
        return signal
    
    def get_name(self) -> str:
        '''inherited method to fetch a given strategy name'''
        return self.name