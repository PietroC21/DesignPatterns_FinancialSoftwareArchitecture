import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

import pytest
import numpy as np
import pandas as pd
from analytics import BaseInstrument, VolatilityDecorator, BetaDecorator, DrawdownDecorator


@pytest.fixture
def sample_returns():
    idx = pd.date_range("2020-01-01", periods=100)
    # ensure returns have some variance
    return pd.Series(np.random.normal(0.001, 0.02, 100), index=idx)


def test_volatility_decorator_adds_volatility(sample_returns):
    base = BaseInstrument("AAPL", sample_returns)
    decorated = VolatilityDecorator(base)
    metrics = decorated.get_metrics()
    # use flexible key existence check and numeric type validation
    assert "volatility" in metrics, "Volatility metric missing"
    assert isinstance(metrics["volatility"], (float, np.floating))
    assert metrics["volatility"] >= 0


def test_beta_decorator_adds_beta(sample_returns):
    base = BaseInstrument("AAPL", sample_returns)
    decorated = BetaDecorator(base)
    metrics = decorated.get_metrics()
    assert "beta" in metrics, "Beta metric missing"
    assert isinstance(metrics["beta"], (float, np.floating))


def test_drawdown_decorator_adds_max_drawdown(sample_returns):
    base = BaseInstrument("AAPL", sample_returns)
    decorated = DrawdownDecorator(base)
    metrics = decorated.get_metrics()
    assert "max_drawdown" in metrics, "Drawdown metric missing"
    assert isinstance(metrics["max_drawdown"], (float, np.floating))
    assert 0 <= metrics["max_drawdown"] <= 1


def test_stacked_decorators_all_metrics(sample_returns):
    base = BaseInstrument("AAPL", sample_returns)
    decorated = DrawdownDecorator(BetaDecorator(VolatilityDecorator(base)))
    metrics = decorated.get_metrics()
    expected_keys = {"symbol", "mean_return", "volatility", "beta", "max_drawdown"}
    assert expected_keys.issubset(metrics.keys()), f"Missing keys: {expected_keys - set(metrics.keys())}"