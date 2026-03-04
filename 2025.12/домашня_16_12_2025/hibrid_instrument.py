"""  5 Реалізуйте множинне спадкування, щоб створити новий клас HybridInstrument, який успадковує від
         кількох класів,
   які представляють різні види музичних інструментів. У цьому класі визначте свій метод play, що комбінує """


class StringInstrument:
    def play(self):
        print("струнний звук ")


class WindInstrument:
    def play(self):
        print("духовий звук ")


class PercussionInstrument:
    def play(self):
        print("ударний звук ")


class HybridInstrument(StringInstrument, WindInstrument, PercussionInstrument):

    def __init__(self,name="Гібридний інструмент"):
        self.name = name

    """Гібридний інструмент, який успадковує від кількох класів
    та комбінує їх властивості та методи"""


    def play(self):
        """Комбінує звуки від усіх успадкованих класів"""
        print(" Гібридний інструмент грає:")
        print("  - ", end="")
        StringInstrument.play(self)  # Звук струнного інструменту
        print("  - ", end="")
        WindInstrument.play(self)  # Звук духового інструменту
        print("  - ", end="")
        PercussionInstrument.play(self)  # Звук ударного інструменту
        print("  → Унікальний комбінований звук! ")




print("\n" + "=" * 60)
print("Завдання 5-6: Гібридний інструмент з множинним успадкуванням")
print("=" * 60)

# Створюємо екземпляр HybridInstrument
hybrid = HybridInstrument()

print("\nВикликаємо метод play() гібридного інструменту:")
hybrid.play()

print("\n" + "-" * 60)
print("Демонстрація множинного успадкування:")
print("-" * 60)

# Показуємо, що HybridInstrument має доступ до методів всіх батьківських класів
print("\n1. Виклик методу play() через StringInstrument:")
StringInstrument.play(hybrid)

print("\n2. Виклик методу play() через WindInstrument:")
WindInstrument.play(hybrid)

print("\n3. Виклик методу play() через PercussionInstrument:")
PercussionInstrument.play(hybrid)

print("\n4. Власний метод play() HybridInstrument (комбінований):")
hybrid.play()

# Показуємо MRO (Method Resolution Order)
print("\n" + "-" * 60)
print("Порядок пошуку методів (MRO):")
print("-" * 60)
print(HybridInstrument.__mro__)

print("\U0001F928")

print()
# Завдання 6. Створення екземпляра класу та його виклик

print("="*50)
print("Завдання 6: Гібридний інструмент")
print("="*50)

hybrid = HybridInstrument("Оркестровий гібрид")

print("\nВиклик методу play():")
hybrid.play()

print("\U0001F600")