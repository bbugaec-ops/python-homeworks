class ValidationMeta(type):
    def __new__(mcls, name, bases, attrs):
        if name != "ValidatedClass":
            if "description" not in attrs:
                raise ValueError(f"{name}: missing 'description' attribute")
            if not isinstance(attrs["description"], str):
                raise ValueError(f"{name}: 'description' must be a string")

            for k, v in attrs.items():
                if callable(v) and not k.startswith("do_"):
                    raise ValueError(f"{name}: method '{k}' must start with 'do_'")

        return super().__new__(mcls, name, bases, attrs)


class ValidatedClass(metaclass=ValidationMeta):
    pass


class GoodClass(ValidatedClass):
    description = "Correct class"

    def do_move(self):
        return "move"

    def do_task(self):
        return "task"


try:
    class BadClass(ValidatedClass):
        description = "Bad class"

        def move(self):
            return "wrong"
except ValueError as e:
    print("BadClass ERROR:", e)


obj = GoodClass()
print("GoodClass OK:", obj.do_move(), obj.do_task())
