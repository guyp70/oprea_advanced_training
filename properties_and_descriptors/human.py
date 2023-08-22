class Human(object):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"{self.name} is {self.age} years old."


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
