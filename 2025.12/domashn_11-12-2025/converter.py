"""   Створіть клас для конвертування з метричної системи в англійську, та навпаки. Реалізуйте функціональність у вигляді статичних методів.
Обов'язково реалізуйте конвертування заходів довжини"""


class UnitConverter:
    _count = 0

    @staticmethod
    def meter_to_fuut(m):
        UnitConverter._count += 1
        return m * 3.28083

    @staticmethod
    def fuut_to_meter(ft):
        UnitConverter._count += 1
        return ft / 3.28083

    @staticmethod
    def kilometr_to_miles(km):
        UnitConverter._count += 1
        return km * 0.62137

    @staticmethod
    def miles_to_kilometr(mil):
        UnitConverter._count += 1
        return mil / 0.621337

    @staticmethod
    def cantim_to_inches(cm):
        UnitConverter._count += 1
        return cm / 2.54

    @staticmethod
    def inches_to_cantim(inch):
        UnitConverter._count += 1
        return inch * 2.54

    @staticmethod
    def gruv_to_dollar(gruv):
        UnitConverter._count += 1
        return gruv * 40

    @staticmethod
    def dollar_to_gruv(doll):
        UnitConverter._count += 1
        return doll / 40



    @staticmethod
    def get_count():
        return UnitConverter._count


print(UnitConverter.meter_to_fuut(10))
print(UnitConverter.fuut_to_meter(32.8))
print(UnitConverter.kilometr_to_miles(5))
print(UnitConverter.miles_to_kilometr(3))
print(UnitConverter.cantim_to_inches(30))
print(UnitConverter.inches_to_cantim(12))
print(UnitConverter.dollar_to_gruv(10))
print(UnitConverter.gruv_to_dollar(1))
print("Конвертація:",UnitConverter.get_count())