from abc import ABC, abstractmethod

# AbstractFactory
class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


#ConcreteFactory
class LightThemeFactory(UIFactory):
    def create_button(self):
        return LightButton()

    def create_checkbox(self):
        return LightChackbox()

    def create_chackbox(self):
        return DarkCheckbox()

class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass
    

class LightButton(Button):
    def click(self):
        print("Light Button clicen")

class DarkButton(Button):
    def click(self):
        print("Dark Button ")

class LightChackbox(Checkbox):
    def check(self):
        print("Light Chackbox")

class DarkChackbox(Checkbox):
    def check(self):
        print("Dark Chackbox")

def client_code(factory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.click()
    checkbox.check()

light_factory = LightThemeFactory()
client_code(light_factory)

dark_factory = DarkThemeFactory()
client_code(dark_factory)
