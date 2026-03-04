def repart(n):
    def dekorat(func):
        def inner():
            for i in range(n):
                func()
        return inner
    return dekorat


@repart(3)                        #    цю неміг трохи зробити , і ті тоже на половину
def even():
    print('hello')

even()