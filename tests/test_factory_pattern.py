import pytest
from patterns.FactoryPattern import InstrumentFactory, Stock, Bond, ETF

def test_create_stock():
    data = {"type": "stock", "symbol": "AAPL", "price": 180.0, "shares": 10}
    inst = InstrumentFactory.create_instrument(data)
    assert isinstance(inst, Stock)
    assert inst.get_value() == pytest.approx(1800.0)
    assert "AAPL" in inst.get_description()

def test_create_bond():
    data = {
        "type": "bond",
        "symbol": "US10Y",
        "face_value": 1000,
        "coupon_rate": 0.03,
        "years_to_maturity": 10
    }
    inst = InstrumentFactory.create_instrument(data)
    assert isinstance(inst, Bond)
    assert inst.get_value() == pytest.approx(1300.0)
    assert "US10Y" in inst.get_description()

def test_create_etf():
    data = {"type": "etf", "symbol": "SPY", "nav": 500.0, "units": 2}
    inst = InstrumentFactory.create_instrument(data)
    assert isinstance(inst, ETF)
    assert inst.get_value() == pytest.approx(1000.0)
    assert "SPY" in inst.get_description()

def test_invalid_type():
    data = {"type": "crypto", "symbol": "BTC", "price": 50000}
    with pytest.raises(ValueError):
        InstrumentFactory.create_instrument(data)