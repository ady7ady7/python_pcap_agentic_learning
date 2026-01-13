from .base_strategy import BaseStrategy

class LevelCrossStrategy(BaseStrategy):
    '''
    A strategy based on crossing certain levels
    '''
    
    def __init__(self, level: float):
        '''Initializing the class with defined level'''
        super().__init__('Level Cross Strategy')
        self.level = level
        
    
    def generate_signal(self, price: float) -> str:
        '''
        Method used to generate signal based on a price you pass - this is a mock method mainly used to practice.
        
        It's an instance of a method that inherits abstract method from BaseStrategy (so it's mandatory).
        Signals for real strategies most likely will be more robust.
        '''
        if price > self.level:
            return 'BUY'
        elif price < self.level:
            return 'SELL'
        elif price == self.level:
            return 'HOLD'
    
    
    def get_level(self) -> float:
        '''Method used to return the set level'''
        return self.level