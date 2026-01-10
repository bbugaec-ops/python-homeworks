from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass

    def info(self):
        return f"{self.__class__.__name__} is a transport."


class Car(Transport):
    def move(self):
        return "Car drives"

class Bicycle(Transport):
    def move(self):
        return "Bicicle pidals along yhe bike lane"

class Train(Transport):
    def move(self):
        return "Train runs on rains"

transport = [Car(), Bicycle(), Train()]

for t in transport:
    print(t.info())
    print(t.move())