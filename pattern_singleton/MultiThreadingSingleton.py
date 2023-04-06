from threading import Lock, Thread
from abc import ABC, abstractmethod


class SingletonMeta(type):
    _instances: dict = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(cls, *args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str = None) -> None:
        self.value = value

    @staticmethod
    def some_business_code():
        pass


def test_singleton(value: str = None) -> None:
    singleton = Singleton(value=value)
    print(singleton.value)


# process1 = Thread(target=test_singleton, args=("FOO",))
# process2 = Thread(target=test_singleton, args=("BAR",))
# process1.start()
# process2.start()
test_singleton(value='FOO')
