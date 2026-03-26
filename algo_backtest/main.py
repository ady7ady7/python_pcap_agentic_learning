

'''

This is the main.py for my professional backtesting framework for algotrading strategies
I'm working on this project as a part of my daily Python PCAP practice routine, using the small steps methodology

'''

import logging
import sys
from __init__ import __version__
import check_dependencies
import pandas as pd
from datetime import datetime, time

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
    
def run_backtest(df: pd.DataFrame, strategies: list) -> BacktestEngine:
    
    backtest_engine = BacktestEngine()
    
    for strategy in strategies:
        current_positions = {strategy: None}
        
        start = strategy.session_start() #time filtering - this will have to be modularized ``
        end = strategy.session_end()
        
        for idx, row in df.iloc[1:].iterrows():
            t = datetime.fromisoformat(row['candle_open']).time()
            is_rth = (start is None) or (start <= t <= end)
            session_ending = end is not None and t > end
            
            if session_ending and current_positions[strategy]:
                backtest_engine.force_close_all('FDAX', row['open'])
                current_positions[strategy] = None
                continue
            
            if is_rth:
                
                signal = strategy.generate_signal(row['open'], row['vwap_rth'])
                if signal == 'BUY' and current_positions[strategy] is None:
                    backtest_engine.open_position(#data.iloc[idx]['ticker'], 
                                                'FDAX',
                                                'BUY', 
                                                row['open'], 
                                                quantity = 1,
                                                stop_loss = row['open'] - 50,
                                                take_profit = row['open'] + 50,
                                                strategy_id = strategy.strategy_id,
                                                strategy_name = strategy.get_name())
                    current_positions[strategy] = True
                
                elif signal == 'SELL' and current_positions[strategy] is None:
                    backtest_engine.open_position(#data.iloc[idx]['ticker'], 
                                                'FDAX',
                                                'SELL', 
                                                row['open'], 
                                                quantity = 1,
                                                stop_loss = row['open'] + 50,
                                                take_profit = row['open'] - 50,
                                                strategy_id = strategy.strategy_id,
                                                strategy_name = strategy.get_name())
                    current_positions[strategy] = True
                    
                    
                newly_closed = backtest_engine.process_price(#data.iloc[idx]['ticker'],
                                                            'FDAX',
                                                            data.iloc[idx]['close'])
                
                if newly_closed:
                    current_positions[strategy] = None
        
    
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
    
    strategies = [VwapStrategy('FDAX')]
    test_engine = run_backtest(data, strategies)
    print(test_engine)
    test_engine.strategy_report()
    
