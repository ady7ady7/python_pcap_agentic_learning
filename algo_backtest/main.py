

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
from strategies.lpp_strategy import LPPStrategy

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
    current_positions = {strategy: None for strategy in strategies}
    traded_today = {strategy: None for strategy in strategies}

    for strategy in strategies:
        strategy.prepare(df)

    for _, row in df.iterrows():
        t = datetime.fromisoformat(row['candle_open']).time()
        current_date = datetime.fromisoformat(row['candle_open']).date()
        #print(strategy.levels_by_date[current_date])
    
        for strategy in strategies:
            start = strategy.session_start()
            end = strategy.session_end()
            is_rth = (start is None) or (start <= t <= end)
            session_ending = end is not None and t > end

            if session_ending and current_positions[strategy] is not None:
                backtest_engine.force_close_all('FDAX', strategy.strategy_id, price = row['open'], candle_time=row['candle_close'])
                current_positions[strategy] = None
                continue

            if is_rth and traded_today[strategy] != current_date:
                signal = strategy.generate_signal(row, current_date)
                
                if signal == 'HOLD':
                    pass
                if signal == 'BUY' and current_positions[strategy] is None:
                    backtest_engine.open_position(
                        'FDAX',
                        'BUY',
                        entry = strategy.get_entry(row, current_date),
                        quantity=1,
                        stop_loss=strategy.get_sl(row, current_date),
                        take_profit=strategy.get_tp(row, current_date),
                        strategy_id=strategy.strategy_id,
                        strategy_name=strategy.get_name(),
                        open_time = row['candle_open']
                    )
                    current_positions[strategy] = True
                    traded_today[strategy] = current_date

                elif signal == 'SELL' and current_positions[strategy] is None:
                    backtest_engine.open_position(
                        'FDAX', 
                        'SELL', 
                        entry = strategy.get_entry(row, current_date),
                        quantity=1,
                        stop_loss=strategy.get_sl(row, current_date),
                        take_profit=strategy.get_tp(row, current_date),
                        strategy_id=strategy.strategy_id,
                        strategy_name=strategy.get_name(),
                        open_time = row['candle_open']
                    )
                    current_positions[strategy] = True
                    traded_today[strategy] = current_date

        newly_closed = backtest_engine.process_price('FDAX', row['close'], row['candle_close'])
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
                    #ticker #entry #sl #tp
    strategies = [
                LPPStrategy('FDAX', 'BUY', 'LR1_LR2_025', 'LPP_LR1_050', 'LR2'), #4
                LPPStrategy('FDAX', 'SELL', 'LS2', 'LS2_LS1_050', 'LS3'), #6
                LPPStrategy('FDAX', 'SELL', 'LR2', 'LR3', 'LPP'), #7
                LPPStrategy('FDAX', 'SELL', 'LR2_LR3_075', 'LR3', 'LR1'), #8
                LPPStrategy('FDAX', 'SELL', 'LS2_LS1_025', 'LS2_LS1_050', 'LS3'), #10 BEZ FILTRA modyfikowany S3
                LPPStrategy('FDAX', 'SELL', 'LS2_LS1_025', 'LS2_LS1_075', 'LS3_LS2_075') #11
                  ]
    test_engine = run_backtest(data, strategies)
    print(test_engine)
    test_engine.strategy_report()
    

    for trade in test_engine.completed_trades[::10]:
        print(trade)
