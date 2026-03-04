"""  Завдання 1
Створіть клас Passport (паспорт), який міститиме паспортну інформацію про громадянина заданої країни.

За допомогою механізму успадкування реалізуйте клас ForeignPassport (закор­дон­ний паспорт), похідний від Passport.

Нагадаємо, що закордонний паспорт містить, крім паспортних даних, дані про візи і номер закордонного паспорта.

Кожен із класів має містити необхідні методи. """

class Passport:
    def __init__(self,name="",first_name="",second_name="",id=0):
        self.name = name
        self.first_name = first_name
        self.second_name = second_name
        self.id = id



    def input_data(self):
        self.name = input("Імя :")
        self.first_name = input("Фамілія :")
        self.second_name = input("Побатькові :")
        self.id = int(input("введіть айді код (цифри):"))

    def show_info(self):
        print("\n-------Інформація-------")
        print(f"Імя :", {self.name})
        print(f"Фамілія :", {self.first_name})
        print(f"Побатькові :", {self.second_name})
        print(f"Аді-код :", {self.id})

class ForeignPassport(Passport):
    def __init__(self,name="",first_name="",second_name="",id=0,visa="",nom_pass=0):
        super().__init__(name="",first_name="",second_name="",id=0)
        self.visa = visa
        self.nom_pass = nom_pass

    def input_foregint_data(self):
        self.visa = input("Віза відкрита ? (так/ні):")
        self.nom_pass = int(input("№ загран паспорта :"))

    def show_info(self):
        super().show_info()
        print(f"Віза відкрита : {self.visa}")
        print(f"№ закордонного паспорта : {self.nom_pass}")


fp = ForeignPassport()
fp.input_data()
fp.input_foregint_data()
fp.show_info()

# passport1 = Passport("Іван","Петренко ","Іванович",34535)
# passport1.show_info()
#
# passport2 = Passport("Василь","Вітюк","Олегович",23223465)
# passport2.show_info()
