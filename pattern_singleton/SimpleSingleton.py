from abc import ABC, abstractmethod


class AbstractSingleton(ABC):
    _instances = None

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]


class Singleton(AbstractSingleton):
    @staticmethod
    def some_code(a: int, b: int):
        print('Nice code, bro!')
        return a + b


s1 = Singleton()
s2 = Singleton()

print(s1.some_code(100, 100))
print(s2.some_code(10, 15))
print(id(s1), id(s2))
