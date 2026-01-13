from algo_backtest.strategies import MovingAverageStrategy, LevelCrossStrategy

'''Test script used to check if our strategies work properly'''

def test_strategy(strategy, prices: list[float]) -> None:
    """Test a strategy with a list of prices.

    Args:
        strategy: Any strategy that has generate_signal method
        prices: List of prices to test
    """
    print(f"\nTesting: {strategy.get_name()}")
    for price in prices:
        signal = strategy.generate_signal(price)
        print(f"  Price {price}: {signal}")


if __name__ == '__main__':
    print('Test')
    strat1 = MovingAverageStrategy(5)
    strat2 = LevelCrossStrategy(100.5)
    
    strat1.add_price(430)
    strat1.add_price(230)
    strat1.add_price(450)
    strat1.add_price(470)
    strat1.add_price(490)
    strat1.add_price(530)
    test_strategy(strat1, [430, 450, 520, 550, 570, 460, 430, 320])
    test_strategy(strat2, [120, 105, 90, 20])