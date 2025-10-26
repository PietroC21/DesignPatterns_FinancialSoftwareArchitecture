from models import *

if __name__ == '__main__':
    stock = Stock("AAPL", "Equity", 190.3, "Technology", "Apple Inc.")
    decorated = DrawdownDecorator(BetaDecorator(VolatilityDecorator(stock)))
    print(decorated.get_metrics())

