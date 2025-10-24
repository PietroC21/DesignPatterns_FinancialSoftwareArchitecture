from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Union
import json, xml.etree.ElementTree as ET
from pathlib import Path

@dataclass
class MarketDataPoint:
    symbol: str
    price: float
    timestamp: datetime
    source: str

def parse_iso_utc(ts: str) -> datetime:
    return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone(timezone.utc)

class YahooFinanceAdapter:
    def __init__(self, json_path: Union[str, Path]):
        self.path = Path(json_path)

    def get_data(self) -> MarketDataPoint:
        data = json.loads(self.path.read_text())
        return MarketDataPoint(
            symbol=data["ticker"],
            price=float(data["last_price"]),
            timestamp=parse_iso_utc(data["timestamp"]),
            source="YahooFinance"
        )

class BloombergXMLAdapter:
    def __init__(self, xml_path: Union[str, Path]):
        self.path = Path(xml_path)

    def get_data(self) -> MarketDataPoint:
        tree = ET.parse(self.path)
        root = tree.getroot()
        symbol = root.find("symbol").text
        price = float(root.find("price").text)
        timestamp = parse_iso_utc(root.find("timestamp").text)
        return MarketDataPoint(symbol, price, timestamp, source="BloombergXML")

# ---- Demonstration ----
if __name__ == "__main__":
    yahoo_adapter = YahooFinanceAdapter("external_data_yahoo.json")
    bloom_adapter = BloombergXMLAdapter("external_data_bloomberg.xml")

    yahoo_data = yahoo_adapter.get_data()
    bloom_data = bloom_adapter.get_data()

    print(yahoo_data)
    print(bloom_data)
