import sys, pathlib
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

import pytest
import json
from io import StringIO
from patterns.SingletonPattern import SingletonConfig

def test_singleton_shared_instance(monkeypatch):
    c1 = SingletonConfig()
    c2 = SingletonConfig()
    assert c1 == c2