#hiding internal details and showing only essential features

from abc import ABC

class Animal(ABC):
    def sound():
        pass

class Lion(Animal):
    def sound(self):
        print("Roarrr")

class Cat(Animal):
    def sound(self):
        print("Meowww")

lion = Lion()
lion.sound()
cat = Cat()
cat.sound()