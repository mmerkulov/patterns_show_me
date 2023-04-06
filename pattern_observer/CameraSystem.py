from __future__ import annotations

from abc import ABC, abstractmethod


class CameraSystem(ABC):

    def __init__(self):
        self.__observers: list = []

    def subscribe(self, observer: Observer):
        if observer not in self.__observers:
            self.__observers.append(observer)
            print(f'Подключили {observer}')

    def unsubscribe(self, observer: Observer):
        if observer in self.__observers:
            self.__observers.remove(observer)
            print(f'Отключили {observer}')

    def notify(self):
        for observer in self.__observers:
            observer.make_photo()


class AbstractObserver(ABC):
    @abstractmethod
    def make_photo(self):
        pass


class Observer(AbstractObserver):
    def __init__(self, name):
        self.name = name

    def make_photo(self):
        print(f'Наблюдатель {self.name} сделал фотографию.')


camera1 = Observer(name='camera1')
camera2 = Observer(name='camera2')
camera3 = Observer(name='camera3')

system = CameraSystem()
system.subscribe(camera1)
system.subscribe(camera2)
system.subscribe(camera3)

system.notify()

system.unsubscribe(camera1)

system.notify()
