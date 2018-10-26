#!/usr/bin/env python
from abc import abstractmethod, ABCMeta

class Vocalizer(metaclass=ABCMeta):

    @abstractmethod
    def speak(self):
        pass

    def move(self):
        print("Moving....")

class Animal(Vocalizer):
    pass

a1 = Animal()
a1.move()
