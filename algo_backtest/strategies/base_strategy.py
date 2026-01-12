
'''Abstract Method Class - base strategy'''

from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    '''A class with abstract method used to generate trading signal'''
    def __init__(self, name: str):
        self.name = name
        
    @abstractmethod
    def generate_signal(self, price: float) -> str:
        pass
    
    def get_name(self) -> str:
        '''inherited method to fetch a given strategy name'''
        return self.name