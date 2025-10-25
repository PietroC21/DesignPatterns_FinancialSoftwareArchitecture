from InstrumentFactory import Stock,ETF,Bond

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


if __name__ == '__main__':
    stock = Stock("AAPL", "Equity", 190.3, "Technology", "Apple Inc.")
    decorated = DrawdownDecorator(BetaDecorator(VolatilityDecorator(stock)))
    print(decorated.get_metrics())

