def dekor(func):

    def inner():
        for i in range(3):
            func()
       
    return inner

@dekor
def say():
    print('hello world :')

say()


