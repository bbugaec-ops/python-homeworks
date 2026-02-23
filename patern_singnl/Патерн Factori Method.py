class Car:
    pass

class BMW(Car):
    pass

class Audi(Car):
    pass

class Mb(Car):
    pass


def car_factory(brand):
    if brand == "BMW":
        return BMW()
    elif brand == "Audi":
        return Audi()
    elif brand == "Mb":
        return Mb()
    else:
        raise ValueError("unknown brand !")


car1 = car_factory("BMW")
car2 = car_factory("Audi")