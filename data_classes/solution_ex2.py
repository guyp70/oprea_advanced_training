PRODUCTS = [
    ('Desk', 'good', 1000, 24),
    ('Chair', 'good', 100, 75),
    ('Computer', 'bad', 2000, 6),
    ('Mouse', 'bad', 50, 1337),
    ('Keyboard', 'ok', 100, 42),
    ('Monitor', 'bad', 500, 18),
    ('Laptop', 'good', 1500, 40),
]


class Product(object):
    def __init__(self, name: str, quality: str, price: int, code: int) -> None:
        self.name = name
        self.quality = quality
        self.price = price
        self.code = quality

    def __repr__(self) -> str:
        return f"Product({self.name}, {self.quality}, {self.price}, {self.code})"

    def __str__(self) -> str:
        return f"Name: {self.name} Quality: {self.quality} Price: {self.price} Code: {self.code}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return (self.name, self.quality, self.price, self.code) == (other.name, other.quality, other.price, self.code)

    def is_pricey(self) -> bool:
        return self.price > 1000

    def is_popular(self) -> bool:
        return self.price > 1000


def main():
    products = [
        Product(name, quality, price, code)
        for (name, quality, price, code) in PRODUCTS
    ]
    for p in products:
        print(f"Product Description: {p}")
        print(f"{p.name} is {'' if p.is_pricey() else 'not '}pricey!")


if __name__ == '__main__':
    main()
