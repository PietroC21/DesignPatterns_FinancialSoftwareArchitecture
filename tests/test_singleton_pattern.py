import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

import pytest
import json
from io import StringIO
from patterns.SingletonPattern import SingletonConfig

def test_singleton_shared_instance(monkeypatch):
    mock_data = {
        "log_level": "DEBUG",
        "data_path": "mock_data.csv",
        "report_path": "mock_report/",
        "default_strategy": "MeanReversion"
    }

    mock_file = StringIO(json.dumps(mock_data))
    monkeypatch.setattr("builtins.open", lambda *args, **kwargs: mock_file)

    c1 = SingletonConfig()
    c2 = SingletonConfig()

    assert c1 is c2
    assert c1.log_level == "DEBUG"
    assert c1.data_path == "mock_data.csv"
    assert c1.report_path == "mock_report/"
    assert c1.default_strategy == "MeanReversion"