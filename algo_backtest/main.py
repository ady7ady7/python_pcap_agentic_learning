

'''

This is the main.py for my professional backtesting framework for algotrading strategies
I'm working on this project as a part of my daily Python PCAP practice routine, using the small steps methodology

'''

import logging
import sys
from __init__ import __version__
import check_dependencies

from engine.trade import Trade
from data.data_loader import DataLoader

def setup_logging():
    logger = logging.getLogger() #root logger, not __main__
    logger.setLevel(logging.DEBUG)
    
    stream_handler = logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter('%(asctime)s [%(levelname)-8s] %(name)s: %(message)s')
    stream_handler.setFormatter(fmt)
    
    logger.addHandler(stream_handler)
    
    logger.debug('Logging in main initialized.')    


def run_simple_backtest() -> None:
    """
    Run a simple backtest:
    1. Load OHLC data
    2. Simulate 3 manual trades (you choose entry/exit points from data)
    3. Print each trade with magic methods
    4. Calculate and display win rate
    """

    print("=== AlgoBacktest Core - Week 1 Demo ===\n")

    # Step 1: Load data
    loader = DataLoader('ohlc_mock_data.csv')
    print(f"Loader: {repr(loader)}")

    data = loader.load_data()
    if data is None:
        print("Failed to load data!")
        return

    print(f"Loaded {len(data)} candles\n")

    # Step 2: Create sample trades (pick 3 trades from your data)
    # Example: BUY at row 5's open, exit at row 10's close
    # You choose the indices based on your ohlc_mock_data.csv

    trades = []
    trade1 = Trade(data.iloc[24]['ticker'], 
                  'BUY', 
                  data.iloc[24]['open'],
                  data.iloc[26]['close'],
                  10000,
                  data.iloc[24]['timestamp'],
                  data.iloc[26]['timestamp'],
                  ''
                  )
    
    trade2 = Trade(data.iloc[28]['ticker'], 
                  'SELL', 
                  data.iloc[28]['open'],
                  data.iloc[29]['close'],
                  10000,
                  data.iloc[28]['timestamp'],
                  data.iloc[30]['timestamp'],
                  ''
                  )
    
    trade3 = Trade(data.iloc[14]['ticker'], 
                  'BUY', 
                  data.iloc[14]['open'],
                  data.iloc[24]['close'],
                  10000,
                  data.iloc[14]['timestamp'],
                  data.iloc[25]['timestamp'],
                  ''
                  )
    
    trades = [trade1, trade2, trade3]
    # Trade 1: Your choice (BUY)
    # Hint: data.iloc[index]['column_name'] to access specific values

    print("=== Trade Results ===")
    for i, trade in enumerate(trades, 1):
        print(f"{i}. {trade}")  # Uses __str__


    # Step 4: Calculate statistics
    win_rate = Trade.calculate_win_rate(trades)
    total_pnl = sum(trade.pnl for trade in trades)
 

    print(f"=== Statistics ===")
    print(f"Total Trades: {len(trades)}")
    print(f"Win Rate: {win_rate:.1f}%")
    print(f"Total P&L: ${total_pnl:.2f}")



if __name__ == '__main__':
    setup_logging()
    check_dependencies.check_deps()
    print(f'Current version: {__version__}')
    print('AlgoBacktest Core - Ready')
    run_simple_backtest()