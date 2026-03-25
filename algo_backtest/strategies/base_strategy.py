
'''Abstract Method Class - base strategy'''

from abc import ABC, abstractmethod
from datetime import time
    

class BaseStrategy(ABC):
    '''A class with abstract method used to generate trading signal'''
    def __init__(self, name: str):
        self.name = name
        
    @abstractmethod
    def generate_signal(self, price: float) -> str:
        pass
    
    @abstractmethod
    def session_start(self) -> time | None: ...

    @abstractmethod  
    def session_end(self) -> time | None: ...
    

    def get_name(self) -> str:
        '''inherited method to fetch a given strategy name'''
        return self.name
