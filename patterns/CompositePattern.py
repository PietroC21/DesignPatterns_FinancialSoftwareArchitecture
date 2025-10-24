from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Any, Union
from pathlib import Path
import json

class PortfolioComponent(ABC):
    @abstractmethod
    def get_value(self) -> float: ...
    @abstractmethod
    def get_positions(self) -> List["Position"]: ...

@dataclass
class Position(PortfolioComponent):
    symbol: str
    quantity: float
    price: float
    def get_value(self) -> float:
        return self.quantity * self.price
    def get_positions(self) -> List["Position"]:
        return [self]

@dataclass
class PortfolioGroup(PortfolioComponent):
    name: str
    children: List[PortfolioComponent]
    def get_value(self) -> float:
        return sum(ch.get_value() for ch in self.children)
    def get_positions(self) -> List[Position]:
        out: List[Position] = []
        for ch in self.children:
            out.extend(ch.get_positions())
        return out

def load_portfolio(path: Union[str, Path]) -> PortfolioGroup:
    
    data = json.loads(Path(path).read_text())

    def build(node: Dict[str, Any]) -> PortfolioGroup:
        children: List[PortfolioComponent] = []
        for p in node.get("positions", []):
            children.append(Position(
                symbol=p["symbol"],
                quantity=float(p["quantity"]),
                price=float(p["price"])
            ))
        for sp in node.get("sub_portfolios", []):
            children.append(build(sp))
        return PortfolioGroup(name=node.get("name", "Portfolio"), children=children)

    return build(data)

def print_tree(node: PortfolioComponent, indent: int = 0) -> None:
    pad = "  " * indent
    if isinstance(node, PortfolioGroup):
        print(f"{pad}{node.name}: value=${node.get_value():,.2f}")
        for ch in node.children:
            print_tree(ch, indent + 1)
    else:
        n = node  # Position
        print(f"{pad}{n.symbol} qty={n.quantity} px={n.price} "
              f"value=${n.get_value():,.2f}")

if __name__ == "__main__":
    root = load_portfolio("portfolio_structure.json")  
    print_tree(root)
    print("Total value:", root.get_value())

