from typing import List, Dict, Optional
from models import Position, Portfolio
import json


class PortfolioBuilder:
    def __init__(self, name):
        self._name = name
        self._owner:Optional[str] = None
        self._positions: List[Position] = []
        self._sub_portfolio:List[Portfolio] = []
    
    def set_owner(self,name):
        self._owner = name
        
    def add_position(self, symbol, quantity, price):
        self._positions.append(Position(symbol,quantity,price))
        return self
        
    def add_subportfolio(self, name, builder):
        sub_portfolio =  builder.build()
        sub_portfolio.name = name
        self._sub_portfolio.append(sub_portfolio)
        return self

    def build(self):
        portfolio = Portfolio(self._name,self._owner)
        portfolio.positions = self._positions
        portfolio.sub_portfolios = self._sub_portfolio
        return portfolio

