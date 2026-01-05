

'''

This is the main.py for my professional backtesting framework for algotrading strategies
I'm working on this project as a part of my daily Python PCAP practice routine, using the small steps methodology

'''


import sys
from __init__ import __version__
import check_dependencies



if __name__ == '__main__':
    check_dependencies.check_deps()
    print(f'Current version: {__version__}')
    print('AlgoBacktest Core - Ready')