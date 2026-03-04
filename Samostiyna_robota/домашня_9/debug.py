def dekor(func):

    def inner():
        print('start function :')
        func()
        print('finish function :')

    return inner

@dekor
def say():
    print('hello world :')

say()
