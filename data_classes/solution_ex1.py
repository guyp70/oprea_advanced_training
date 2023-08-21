PRODUCTS = [
    ('Desk', 'good', 1000),
    ('Chair', 'good', 100),
    ('Computer', 'bad', 2000),
    ('Mouse', 'bad', 50),
    ('Keyboard', 'ok', 100),
    ('Monitor', 'bad', 500),
    ('Laptop', 'good', 1500),
]


class Product(object):
    def __init__(self, name: str, quality: str, price: int) -> None:
        self.name = name
        self.quality = quality
        self.price = price

    def __repr__(self) -> str:
        return f"Product({self.name}, {self.quality}, {self.price})"

    def __str__(self) -> str:
        return f"Name: {self.name} Quality: {self.quality} Price: {self.price}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return (self.name, self.quality, self.price) == (other.name, other.quality, other.price)

    def is_pricey(self) -> bool:
        return self.price > 1000


def main():
    for (name, quality, price) in PRODUCTS:
        p = Product(name, quality, price)
        print(f"Product Description: {p}")
        print(f"{p.name} is {'' if p.is_pricey() else 'not '}pricey!")


if __name__ == '__main__':
    main()
