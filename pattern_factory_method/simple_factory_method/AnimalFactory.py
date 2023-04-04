import json


class Animal:
    is_alive = True

    def speak(self):
        pass


class Mammals(Animal):
    def speak(self):
        pass


class Lion(Mammals):
    def speak(self):
        return 'Roar'


class Wolf(Mammals):
    def __init(self, name):
        self.name = name

    def speak(self):
        return 'Auf'


class Insect(Animal):
    pass


class Bird(Animal):
    def speak(self):
        return 'Chirik'


class AnimalFactory:
    def __init__(self):
        self.animals = {}

    def register_animal(self, animal_type, animal_class) -> None:
        self.animals[animal_type] = animal_class

    def get_animal(self, animal_type):
        animal_class = self.animals[animal_type]
        if animal_class:
            return animal_class
        else:
            raise 'Cant find any animal'


factory = AnimalFactory()
factory.register_animal('wolf', Wolf)
factory.register_animal('bird', Bird)
factory.register_animal('lion', Lion)

wolf1 = factory.get_animal('wolf')
wolf2 = factory.get_animal('wolf')
print(wolf1, wolf2, id(wolf1), id(wolf2))
