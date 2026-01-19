""" Завдання 2
Створіть додаток для приготування пасти. Додаток має вміти створювати щонайменше три види пасти.
Класи різної пасти мають містити такі методи:
Тип пасти;
Соус;
Начинка;
Добавки.
Для реалізації використовуйте твірні патерни. """

class Pasta:
    def __init__(self):
        self.pasta_type = None
        self.sauce = None
        self.filling = None
        self.additions = []

    def __str__(self):
        return (
            f"Pasta(\n"
            f"  type = {self.pasta_type},\n"
            f"  sauce = {self.sauce},\n"
            f"  filling = {self.filling},\n"
            f"  additions = {self.additions}\n"
            f")"
        )


class PastaBuilder:
    def __init__(self):
        self.pasta = Pasta()

    def set_type(self, pasta_type):
        self.pasta.pasta_type = pasta_type
        return self

    def set_sauce(self, sauce):
        self.pasta.sauce = sauce
        return self

    def set_filling(self, filling):
        self.pasta.filling = filling
        return self

    def add_addition(self, addition):
        self.pasta.additions.append(addition)
        return self

    def build(self):
        ready_pasta = self.pasta
        self.pasta = Pasta()
        return ready_pasta


class PastaDirector:
    def __init__(self, builder: PastaBuilder):
        self.builder = builder

    def make_carbonara(self):
        return (
            self.builder
            .set_type("Спагеті")
            .set_sauce("вершковий")
            .set_filling("бекон")
            .add_addition("пармезан")
            .add_addition("чорний перець")
            .build()
        )

    def make_bolognese(self):
        return (
            self.builder
            .set_type("Тальятеле")
            .set_sauce("томатний")
            .set_filling("яловичина")
            .add_addition("базилік")
            .add_addition("пармезан")
            .build()
        )

    def make_vegetarian(self):
        return (
            self.builder
            .set_type("Пенне")
            .set_sauce("песто")
            .set_filling("овочі")
            .add_addition("оливки")
            .add_addition("рукола")
            .build()
        )
    def make_risoni(self):
        return (
            self.builder
            .set_type("Резоні")
            .set_sauce("слівки")
            .set_filling("прованські трави")
            .add_addition("пармезан")
            .add_addition("криветки")
            .build()
        )
    def make_capellini(self):
        return (
            self.builder
            .set_type("Капеліні")
            .set_sauce("помідори")
            .set_filling("фарш ")
            .add_addition("яйця, сир,")
            .add_addition("зелена цибуля")
            .build()
        )


builder = PastaBuilder()
director = PastaDirector(builder)

pasta1 = director.make_carbonara()
print(pasta1)

print("--------------")

pasta2 = director.make_bolognese()
print(pasta2)

print("--------------")

pasta3 = director.make_vegetarian()
print(pasta3)

print('-------------------')

pasta4 = director.make_risoni()
print(pasta4)

print('--------------------')

pasta5 = director.make_capellini()
print(pasta5)
