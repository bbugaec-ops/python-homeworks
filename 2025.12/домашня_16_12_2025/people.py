"""
2)Використовуючи механізм множинного успадкування, розробіть клас "Людина". Мають бути класи
      "Мозок", "Серце", "Ноги" і т.д. """

class Brain:
    def think(self):
        return "я думаю над вправою "

class Heart:
    def beat(self):
        return "серце б'ється"

class Legs:
    def walk(self):
        return "я хожу"

class Eyes:
    def eye(self):
        return "я дивлюся"

class Ears:
    def ear(self):
        return "я тебе чую"

class Arms:
    def arm(self):
        return "я здороваюсь"


class Human(Brain,Heart,Legs,Eyes,Ears,Arms):
    def live(self):
        print(self.think())
        print(self.beat())
        print(self.walk())
        print(self.eye())
        print(self.ear())
        print(self.arm())


person = Human()
person.live()