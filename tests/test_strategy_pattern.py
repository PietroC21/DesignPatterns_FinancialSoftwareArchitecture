import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

import pytest
from patterns.StrategyPattern import MeanReversionStrategy, BreakoutStrategy

class MockTick:
    def __init__(self, price: float):
        self.price = price

@pytest.fixture
def mock_params_json(tmp_path):
    params = {
        "MeanReversionStrategy": {"lookback_window": 3, "threshold": 0.02},
        "BreakoutStrategy": {"lookback_window": 3, "threshold": 0.02}
    }
    path = tmp_path / "strategy_params.json"
    path.write_text(str(params).replace("'", '"'))
    return path

def test_mean_reversion_buy_signal(mock_params_json):
    strat = MeanReversionStrategy(params_path=mock_params_json)
    prices = [100, 102, 99, 90]  # last price well below mean
    signals = []
    for p in prices:
        tick = MockTick(price=p)
        signals = strat.generate_signals(tick)
    assert "BUY" in signals

def test_mean_reversion_sell_signal(mock_params_json):
    strat = MeanReversionStrategy(params_path=mock_params_json)
    prices = [100, 102, 101, 110]  # last price well above mean
    signals = []
    for p in prices:
        tick = MockTick(price=p)
        signals = strat.generate_signals(tick)
    assert "SELL" in signals

def test_breakout_buy_signal(mock_params_json):
    strat = BreakoutStrategy(params_path=mock_params_json)
    prices = [100, 102, 101, 103, 104, 105]  # breaks new high
    signals = []
    for p in prices:
        tick = MockTick(price=p)
        signals = strat.generate_signals(tick)
    assert "BREAKOUT_BUY" in signals

def test_breakout_sell_signal(mock_params_json):
    strat = BreakoutStrategy(params_path=mock_params_json)
    prices = [100, 99, 98, 95, 94, 93]  # breaks new low
    signals = []
    for p in prices:
        tick = MockTick(price=p)
        signals = strat.generate_signals(tick)
    assert "BREAKOUT_SELL" in signals