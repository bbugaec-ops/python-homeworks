def repart_three_times(func):
    def inner():
        for i in range(3):
            func()

    return inner


@repart_three_times
def say():
    print('hello world :')


say()
