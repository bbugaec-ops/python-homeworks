class Add:
    def __init__(self, value):
        self.value = value


    def __add__(self, other):
        if not isinstance(other,Add):
            return NotImplemented

        return Add(self.value + other.value)

    def __repr__(self):
        return str(self.value)


a = Add(143.5)
b = Add(32.4)
result_numbers = a + b

print("143.5 + 32.4 =",result_numbers)

s1 = Add("ай")
s2 = Add("фон")
result_strings = s1 + s2

print('"ай + фон"=',result_strings)
