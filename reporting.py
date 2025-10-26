from patterns.ObserverPattern import *
# Mock Strategy
class MockStrategy:
    def __init__(self, publisher: SignalPublisher):
        self.publisher = publisher

    def generate_signal(self, price, volume):
        signal = {
            "timestamp": datetime.datetime.now().isoformat(),
            "type": "BUY" if price < 100 else "SELL",
            "price": price,
            "volume": volume
        }
        print(f"\n[Strategy] Generated signal: {signal}")
        self.publisher.notify(signal)

if __name__ == "__main__":
    publisher = SignalPublisher()
    strategy = MockStrategy(publisher)

    logger = LoggerObserver()
    alert = AlertObserver()

    # Attach observers dynamically
    publisher.attach(logger)
    publisher.attach(alert)

    # Generate a few example signals
    strategy.generate_signal(price=98, volume=500)
    strategy.generate_signal(price=105, volume=2000)

    # Detach an observer and continue
    publisher.detach(logger)
    strategy.generate_signal(price=99, volume=1500)