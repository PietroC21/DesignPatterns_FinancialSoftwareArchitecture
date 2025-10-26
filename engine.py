from patterns.StrategyPatern import MeanReversionStrategy,BreakoutStrategy
from AdapterPattern import MarketDataPoint
import pandas as pd

def run_strategy(strategy, prices):
    print(f"\nRunning {strategy.__class__.__name__}")
    for i, price in enumerate(prices.iterrows()):
        
        timestamp,symbol,pr = price[1].values
        tick = MarketDataPoint( symbol, pr, timestamp,'Yahoo')
        signals = strategy.generate_signals(tick)
        if signals:
            print(f"Tick {i} | Price: {pr:.2f} | Signals: {signals[0]}")

if __name__ == "__main__":
    prices = pd.read_csv('market_data.csv')

    mean_rev = MeanReversionStrategy()
    breakout = BreakoutStrategy()

    # Demonstrate strategy interchangeability
    for strat in [mean_rev, breakout]:
        run_strategy(strat, prices)