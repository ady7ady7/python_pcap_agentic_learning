

'''
Data loading module for AlgoBacktest
'''


from typing import Optional
import pandas as pd


class DataLoader:
    '''
    Class used to load and validate data
    
    Attributes:
        file_path: path to the csv file with trading data
    
    '''

    def __init__(self, file_path: str) -> None:
        '''Initialize the DataLoader class with file path'''
        print('DataLoader initialized.')
        self.filepath = file_path
        
    def __repr__(self):
        '''
        Unambiguous representation
        '''
        return f'DataLoader(filepath = {self.filepath})'

    
    
    def load_data(self) -> Optional[pd.DataFrame]:
        '''
        Load CSV data with error handling.

        Returns:
            DataFrame with columns: timestamp, ticker, open, high, low, close, volume (and DF index)
            Returns None if file not found.

        Raises:
            ValueError: If CSV format is invalid or missing required columns.
            FileNotFoundError: If file is missing or file name is wrong.
            Pandas Parser Error: If there are any issues with data parsing.
        '''
        
        try:
            with open(self.filepath, 'r') as f:
                data = pd.read_csv(f)
                data.columns = ['timestamp', 'ticker', 'open', 'high', 'low', 'close', 'volume']
            
        
        except FileNotFoundError as e:
            print(f'File not found: {str(e)}')
            return None
        except ValueError as e:
            print(f'Value Error! {str(e)}')
            return None
        except pd.errors.ParserError as e:
            print(f'Pandas Parser Error: {str(e)}')
            return None
        except Exception as e:
            print(f'Unexpected error: {str(e)}')
            return None
            
        
        else:
            print('Data loading succeeded')
            return data
        
        finally:
            print('Data loading operation ended.')
    
    
    
    def validate_data(self, df: pd.DataFrame) -> bool:
        '''
        Method used to check whether all rows/columns are valid.
        
        checks if:
        - all the columns are in the dataframe
        - there are no missing values
        - High price in every row is higher than Low price
        
        Args:
        - df - Pandas Dataframe with columns: ['timestamp', 'ticker', 'open', 'high', 'low', 'close', 'volume']
        
        Returns:
        - is_valid - True/False, depending on the results of the check
        '''
        
        req_columns = ['timestamp', 'ticker', 'open', 'high', 'low', 'close', 'volume']
        is_valid = True
        
        
        missing_columns = set(req_columns) - set(df.columns)
        if missing_columns:
            print(f'Missing columns: {missing_columns}')
            is_valid = False
                
        nan_values = df[req_columns].isna().sum()
        if nan_values.any() > 0:
            print(f'Missing values found: {len(nan_values)}')
            is_valid = False
            
        invalid_rows = df[df['high'] < df['low']]
        if not invalid_rows.empty:
            print(f'Found {len(invalid_rows)} invalid rows: {invalid_rows}')
            is_valid = False
            
        return is_valid
    
    
    def get_candle_count(self) -> int:
       """
       Return total number of candles in loaded data.

       Returns:
           Number of rows in DataFrame, or 0 if data not loaded.
       """
       
       data = self.load_data()
       
       if data is not None:
           return len(data)
       else:
           return 0
    
    
    def get_bullish_candles(self, data: pd.DataFrame) -> pd.DataFrame:
       """
       Return only bullish candles (close > open).

       Args:
           data: OHLC DataFrame.

       Returns:
           Filtered DataFrame with only bullish candles.
       """
       
       bullish_candles = data[data['close'] > data['open']]
       return bullish_candles
       