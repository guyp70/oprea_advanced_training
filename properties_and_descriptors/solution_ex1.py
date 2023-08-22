from typing import Optional


class Human(object):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self._age = None  # type: Optional[int]

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
