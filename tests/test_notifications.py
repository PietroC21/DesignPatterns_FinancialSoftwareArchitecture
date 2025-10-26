import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

import pytest
from patterns.ObserverPattern import SignalPublisher, LoggerObserver, AlertObserver
from patterns.CommandPattern import CommandInvoker, ExecuteOrderCommand, Trade

'''
def test_observer_notifications(monkeypatch):
    publisher = SignalPublisher()
    logger = LoggerObserver()
    alert = AlertObserver()

    publisher.attach(logger)
    publisher.attach(alert)

    logged_signals = []
    alerted_signals = []

    # monkeypatch logger and alert observers to track updates
    monkeypatch.setattr(logger, "update", lambda signal: logged_signals.append(signal))
    monkeypatch.setattr(alert, "update", lambda signal: alerted_signals.append(signal))

    signal = {"symbol": "AAPL", "type": "BUY", "volume": 1500}
    publisher.notify(signal)

    assert len(logged_signals) == 1
    assert len(alerted_signals) == 1
    assert logged_signals[0]["symbol"] == "AAPL"
    assert alerted_signals[0]["notional"] == 1500'''


def test_command_execute_undo_redo(capsys):
    invoker = CommandInvoker()
    trade = Trade(symbol="AAPL", quantity=100)
    cmd = ExecuteOrderCommand(trade)

    invoker.execute_command(cmd)
    out1 = capsys.readouterr().out
    assert "Executed trade" in out1

    invoker.undo()
    out2 = capsys.readouterr().out
    assert "Undone trade" in out2

    invoker.redo()
    out3 = capsys.readouterr().out
    assert "Executed trade" in out3