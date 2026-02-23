"""
дання 4
Реалізуйте клас «Автомобіль». Збережіть у класі: назву моделі, рік випуску, виробника, об'єм двигуна, колір машини, ціну.
Реалізуйте методи класу для введення-виведення даних та інших операцій.
"""
class Book:
    def __init__(self, name_book="", year="", autor_book="",price=0.0,publisher="",genre=""):
        self.name_book = name_book
        self.year = year
        self.autor_book = autor_book
        self.price = price
        self.publisher = publisher
        self.genre = genre

    def input_data(self):
        self.name_book = input("Вкажіть назву книги :")
        self.year = input("Якого року ця книга :")
        self.autor_book = input("Назвіть автора :")
        self.price = float(input("Вкажіть ціну :"))
        self.publisher = input("Хто видавець :")
        self.genre = input("Який жанр цеї книги ")


    def print_data(self):
        print("----------Інформація про книгу----------")
        print(f"Назва книги     : {self.name_book}")
        print(f"Якого року ця книга : {self.year}")
        print(f"Автор книги     :  {self.autor_book}")
        print(f"Ціна            :  {self.price} ")
        print(f"Хто випустив    : {self.publisher}")
        print(f"Який жанр книги : {self.genre}")

    def change_name(self,new_name):
        self.name_book = new_name

    def change_avtor_book(self,new_autor):
        self.autor_book = new_autor

    def apply_discount(self,procent):
        if procent < 0 or procent > 100:
            print("Неправельна знижка")
            return
        discount = self.price * (procent / 100)
        self.price -= discount


book = Book()
book.input_data()
book.print_data()

book.change_name("Жито і мир")

book.change_avtor_book("Vasul")

print("\nЗнижка 14% :")
book.apply_discount(14)
book.print_data()