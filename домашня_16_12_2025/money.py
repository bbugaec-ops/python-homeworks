"""4 вправа з уроку 11,12,2025"""


class Money:
    def __init__(self,currency: str, major:int=0, minor:int=0):
        if not currency or not currency.strip():   # чи не пуста валюта
            raise ValueError("currency is required")

        self._currency = currency.strip()
        self._major = int(major)
        self._minor = int(minor)
        self._normalize()

    def set_parts(self,major:int,minor:int) -> None:  #Встановлюються нові числа і знову нормалізується все
        self._major = int(major)
        self._minor = int(minor)
        self._normalize()

    def print(self) -> None:
        print(self)

    @property
    def currency(self) -> str:
        return self._currency

    @property
    def major(self) -> int:
        return self._major

    @property
    def minor(self) -> int:
        return self._minor

    def to_minor_units(self) -> int:
        return self._major * 100 + self._minor   #   Переводить суму в копійки

    def subtract(self,other:'Money') -> None:
        if self._currency != other._currency:    #  Віднімає інші гроші від цих
            raise ValueError(f"Different currencies: {self._currency} vs {other._currency}")
        #     Перевіряє валюту

        total = self.to_minor_units() - other.to_minor_units()
        #   Рахує все в копійках і віднімає

        if total < 0:
            total = 0

        self._major = total // 100   #  Сюди записує гроші і копійки
        self._minor = total % 100


    def _normalize(self) -> None:

        totel = self._major * 100 + self._minor
        if totel < 0:
            totel = 0
        self._major = totel // 100
        self._minor = totel % 100

    def __str__(self) -> str:
        return f"{self._currency} {self._major}.{self._minor:02d}"  # якщо 5 копійок то буде  0,5


class Product:
    def __init__(self,name:str,price:Money):
        if not name or not name.strip():
            raise ValueError("name is required")
        if price is None:
            raise ValueError("price is required")
        self._name = name.strip()
        self._price = price

    def decreasw_price(self,major:int = 0, minor: int = 0) -> None:
        discount = Money(self._price.currency,major,minor)     #   Робить знижку
        self._price.subtract(discount)                      #  і віднімає її

    def print(self) -> None:
        print(f"Product: {self._name}, price:{self._price}")   #  Друкує цей товар


if __name__ == "__main__":
    price = Money("UAN",125,50)
    product = Product("Хліб",price)

    product.print()
    product.decreasw_price(10,75)   #  знижка
    product.print()

    product.decreasw_price(0,150)    #  тоже знижка
    product.print()

