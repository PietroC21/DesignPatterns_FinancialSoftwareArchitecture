from typing import List, Dict, Optional

class Stock:
    def __init__(self,symbol,typeS,price,sector,issuer):
        self.symbol = symbol
        self.type = typeS
        self.price = price
        self.sector = sector
        self.issuer = issuer

    def get_metrics(self):
        return {
            "symbol": self.symbol,
            "type": self.type,
            "price": self.price,
            "sector": self.sector,
            "issuer": self.issuer
        }

class ETF:
    def __init__(self,symbol,typeS,price,sector,issuer):
        self.symbol = symbol
        self.type = typeS
        self.price = price
        self.sector = sector
        self.issuer = issuer

    def get_metrics(self):
        return {
            "symbol": self.symbol,
            "type": self.type,
            "price": self.price,
            "sector": self.sector,
            "issuer": self.issuer
        }

class Bond:
    def __init__(self,symbol,typeS,price,sector,issuer, maturity):
        self.symbol = symbol
        self.type = typeS
        self.price = price
        self.sector = sector
        self.issuer = issuer
        self.maturity = maturity
    
    def get_metrics(self):
        return {
            "symbol": self.symbol,
            "type": self.type,
            "price": self.price,
            "sector": self.sector,
            "issuer": self.issuer,
            "maturity":self.maturity
        }



class StockDecorator:
    def __init__(self,stock):
        self._stock = stock
    def get_metrics(self):
        return self._stock.get_metrics()
        
class VolatilityDecorator(StockDecorator):
    def get_metrics(self):
        metrics = super().get_metrics()
        metrics["volatility"] = 0.25
        return metrics

class BetaDecorator(StockDecorator):
    def get_metrics(self):
        metrics = super().get_metrics()
        metrics["beta"] = 1.1
        return metrics

class DrawdownDecorator(StockDecorator):
    def get_metrics(self):
        metrics = super().get_metrics()
        metrics["max_drawdown"] = -1.1
        return metrics


class Position:
    def __init__(self,symbol,qty,price):
        self.symbol = symbol
        self.quantity = qty
        self.price = price

class Portfolio:
    def __init__(self,name,owner):
        self.name = name
        self.owner = owner
        self.positions:List[Position] = []
        self.sub_portfolios: List['Portfolio'] = []
        