def upper_text(func):
    def inner():
        result = func()
        return result.upper()
    return inner

@upper_text
def uperr():
    return 'Helo friend !'

print(uperr())