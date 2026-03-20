

'''

This is the main.py for my professional backtesting framework for algotrading strategies
I'm working on this project as a part of my daily Python PCAP practice routine, using the small steps methodology

'''

import logging
import sys
from __init__ import __version__
import check_dependencies
import pandas as pd

from engine.backtest_engine import BacktestEngine
from data.data_loader import DataLoader
from strategies.vwap_strategy import VwapStrategy

def setup_logging():
    logger = logging.getLogger() #root logger, not __main__
    logger.setLevel(logging.DEBUG)
    
    stream_handler = logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter('%(asctime)s [%(levelname)-8s] %(name)s: %(message)s')
    stream_handler.setFormatter(fmt)
    
    logger.addHandler(stream_handler)
    
    logger.debug('Logging in main initialized.')    
    
def run_backtest(df: pd.DataFrame) -> BacktestEngine:
    backtest_engine = BacktestEngine()
    vwap_strategy = VwapStrategy('FDAX')
    current_positions = {vwap_strategy: None}
    
    for idx, row in df.iloc[1:].iterrows():
        signal = vwap_strategy.generate_signal(row['open'], row['vwap_rth'])
        if signal == 'BUY' and current_positions[vwap_strategy] is None:
            backtest_engine.open_position(#data.iloc[idx]['ticker'], 
                                          'FDAX',
                                          'BUY', 
                                          row['open'], 
                                          quantity = 1,
                                          stop_loss = row['open'] - 50,
                                          take_profit = row['open'] + 50,
                                          strategy_id = '1',
                                          strategy_name = vwap_strategy.get_name())
            current_positions[vwap_strategy] = True
        
        elif signal == 'SELL' and current_positions[vwap_strategy] is None:
            backtest_engine.open_position(#data.iloc[idx]['ticker'], 
                                          'FDAX',
                                          'SELL', 
                                          row['open'], 
                                          quantity = 1,
                                          stop_loss = row['open'] + 50,
                                          take_profit = row['open'] - 50,
                                          strategy_id = '1',
                                          strategy_name = vwap_strategy.get_name())
            current_positions[vwap_strategy] = True
            
            
        newly_closed = backtest_engine.process_price(#data.iloc[idx]['ticker'],
                                                     'FDAX',
                                                     data.iloc[idx]['close'])
        
        if newly_closed:
            current_positions[vwap_strategy] = None
    
    
    return backtest_engine


if __name__ == '__main__':
    
    x = DataLoader('algo_backtest\data\FDAX_M1_OHLC.csv')
    print(x)
    data = x.load_data()
    x.validate_data(data)
    print(len(data))
    print(data.head(3))
    
    setup_logging()
    print('Starting the backtest test procedure in main.py - logging set!')
    
    test_engine = run_backtest(data)
    print(test_engine)
    test_engine.strategy_report()
    
