from abc import ABC, abstractmethod
import time
from numpy import sign
from AdapterPattern import MarketDataPoint
from collections import deque
import json
import pandas as pd


class Strategy(ABC):
    @abstractmethod
    def generate_signals(tick: MarketDataPoint) -> list:
        pass

class MeanReversionStrategy(Strategy):
    def __init__(self, params_path="strategy_params.json"):
        with open(params_path) as f:
            params = json.load(f)["MeanReversionStrategy"]
        self.lookback = params["lookback_window"]
        self.threshold = params["threshold"]
        self.prices = deque(maxlen=self.lookback)

    def generate_signals(self,tick: MarketDataPoint) -> list:
        self.prices.append(tick.price)
        if len(self.prices) < self.lookback:
            return []

        mean_price = sum(self.prices) / len(self.prices)
        deviation = (tick.price - mean_price) / mean_price

        signals = []
        if deviation < -self.threshold:
            signals.append("BUY")
        elif deviation > self.threshold:
            signals.append("SELL")
        return signals

class BreakoutStrategy(Strategy):
    def __init__(self, params_path="strategy_params.json"):
        with open(params_path) as f:
            params = json.load(f)["BreakoutStrategy"]
        self.lookback = params["lookback_window"]
        self.threshold = params['threshold']
        self.prices = deque(maxlen=self.lookback)
        
    def generate_signals(self,tick: MarketDataPoint) -> list:
        self.prices.append(tick.price)
        if len(self.prices) < self.lookback:
            return []

        high = max(self.prices)
        low = min(self.prices)
        signals = []

        if tick.price >= high:
            signals.append("BREAKOUT_BUY")
        elif tick.price <= low:
            signals.append("BREAKOUT_SELL")
        return signals