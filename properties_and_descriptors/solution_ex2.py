from typing import Optional


class Property:
    def __init__(
        self, getter: Optional[callable] = None,
        setter: Optional[callable] = None,
        deleter: Optional[callable] = None,
    ) -> None:
        self.getter = getter
        self.setter = setter
        self.deleter = deleter

    def __get__(self, instance, owner):
        if self.getter is None:
            raise AttributeError("unreadable attribute")

        if instance is None:
            return self
        return self.getter(instance)

    def __set__(self, instance, value):
        if self.setter is None:
            raise AttributeError("can't set attribute")

        self.setter(instance, value)

    def __del__(self, instance):
        if self.deleter is None:
            raise AttributeError("can't delete attribute")

        self.deleter(instance)


def my_property(
    fget: Optional[callable] = None,
    fset: Optional[callable] = None,
    fdel: Optional[callable] = None,
) -> Property:
    return Property(fget, fset, fdel)


class Human(object):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self._age = None  # type: Optional[int]

        self.age = age

    def __repr__(self) -> str:
        return f"{self.name} is {self.age} years old."

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value


def main():
    h = Human("Adam", 20)
    print(h)
    try:
        h.age = -10
        print(h)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
