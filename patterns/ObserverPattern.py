from abc import ABC, abstractmethod
import datetime

# ============= Publisher =============
class SignalPublisher:
    def __init__(self):
        self.observersList = []
    def attach(self, observer):
        self.observersList.append(observer)
    def notify(self, signal):
        for observer in self.observersList:
            observer.update(signal)


# ============ Observers ==============

class Observer(ABC):
    @abstractmethod
    def update(self, signal: dict):
        """Receive signal notification."""
        pass

class LoggerObserver(Observer):
    def update(self, signal: dict):
        print(f"[Logger] {datetime.datetime.now()} - Signal logged: {signal}")

class AlertObserver(Observer):
    def update(self, signal: dict):
        # Suppose large trades are volume > 1000
        if signal.get("volume", 0) > 1000:
            print(f"[ALERT] Large trade detected! {signal}")
        else:
            print(f"[Alert] No alert triggered for signal: {signal['type']}")
