from abc import ABC, abstractmethod


class AbstractSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=AbstractSingleton):
    @staticmethod
    def some_code(a: int, b: int):
        print('Nice code, bro!')
        return a + b


s1 = Singleton() #.some_code(100, 100)
s2 = Singleton() #.some_code(10, 10)

print(s1.some_code(100, 100))
print(s2.some_code(10, 15))
print(id(s1), id(s2), s1, s2)
