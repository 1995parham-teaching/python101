from typing import Any


# Borg override __dict__ with its class-level dictionary
# so all of its instances has access to the same methods and properties.
class Borg:
    __namespace: dict[str, Any] = {"parameter": 10}

    def __init__(self) -> None:
        self.__dict__ = Borg.__namespace

    def __getattr__(self, name: str) -> Any:
        return self.__dict__[name]

    def __setattr__(self, name: str, value: Any) -> None:
        self.__dict__[name] = value


# set a parameter on b1 (an instance of Borg) and print
# it, it works as expected.
b1 = Borg()
setattr(b1, "hello", "Hi")
print(b1.hello)


# define b2 (a new instance of Borg) and it has access to the
# parameter defined by b1.
b2 = Borg()
print(b2.hello)

# set another value for _hello_ parameter on b2.
setattr(b2, "hello", "Bye")

# _hello_ parameter is changed on b1.
print(b1.hello)

# print _paramater_ on b1.
print(b1.parameter)

# define _name_ parameter on b1.
b1.name = "Elahe"

# print _name_ parameter from b2.
print(b2.name)
