

'''

This is the main.py for my professional backtesting framework for algotrading strategies
I'm working on this project as a part of my daily Python PCAP practice routine, using the small steps methodology

'''

import logging
import sys
from __init__ import __version__
import check_dependencies

from engine.backtest_engine import BacktestEngine
from data.data_loader import DataLoader

def setup_logging():
    logger = logging.getLogger() #root logger, not __main__
    logger.setLevel(logging.DEBUG)
    
    stream_handler = logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter('%(asctime)s [%(levelname)-8s] %(name)s: %(message)s')
    stream_handler.setFormatter(fmt)
    
    logger.addHandler(stream_handler)
    
    logger.debug('Logging in main initialized.')    


if __name__ == '__main__':
    setup_logging()
    print('Starting the backtest test procedure in main.py - logging set!')
    engine = BacktestEngine()
    engine.open_position('EURUSD', 'BUY', 105.6, 10000, 103.2, 107.7, strategy_id = '432', strategy_name = 'Super XD')
    engine.open_position('EURUSD', 'SELL', 105.6, 10000, 110.2, 102.7, strategy_id = '432', strategy_name = 'Super XD')
    engine.open_position('FDAX', 'BUY', 25554, 10, 25500, 25750, strategy_id = '6546', strategy_name = 'DAXI')
    engine.open_position('FDAX', 'SELL', 25580, 10, 25660, 25350, strategy_id = '2334', strategy_name = 'DAXI')    
    

    engine.process_price('EURUSD', 104.2)
    engine.process_price('EURUSD', 106.2)
    engine.process_price('EURUSD', 108.2)
    engine.process_price('EURUSD', 102.2)
    
    engine.process_price('FDAX', 25654)
    engine.process_price('FDAX', 25760)
    engine.process_price('FDAX', 25620)
    engine.process_price('FDAX', 25440)
    engine.process_price('FDAX', 25240)
    
    print(engine)
    print(engine.total_pnl)
    print(engine.win_rate)
    print([trade.r_multiple for trade in engine.completed_trades])
    #print(engine.trades_by_strategy()) - not needed, we will directly request this in strategy_report
    x = engine.trades_by_strategy()
    print(x)
    engine.strategy_report()