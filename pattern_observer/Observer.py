from __future__ import annotations

from abc import ABC, abstractmethod
from random import randrange


class Subject(ABC):

    @abstractmethod
    def subscribe(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class SpecialSubject(Subject):
    _state: int = None

    _observers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        print(f'Подписчик {observer} добавлен.')
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        print(f'Подписчик {observer} удалён.')
        self._observers.remove(observer)

    def notify(self) -> None:
        print('Запускаем процесс оповещения:')
        if self._observers:
            for obs in self._observers:
                obs.update_state(self)
        else:
            print('Нет ни одного подписчика')

    def some_logic_code(self) -> None:
        print("\nПодписка: Делаем какое-то действие.")
        self._state = randrange(0, 10)

        print(f"Подписка: Моё состояние изменено на: {self._state}")
        self.notify()


class Observer(ABC):
    @abstractmethod
    def update_state(self, subject: Subject) -> None:
        pass


class A_Observer(Observer):
    def update_state(self, subject: Subject):
        if subject._state < 3:
            print("A_Observer: Отреагировал на событие")


class B_Observer(Observer):
    def update_state(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("B_Observer: Отреагировал на событие")


subj = SpecialSubject()
obs1 = A_Observer()
subj.subscribe(obs1)

obs2 = B_Observer()
subj.subscribe(obs2)

subj.some_logic_code()
