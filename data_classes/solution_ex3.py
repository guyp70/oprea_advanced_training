import attr


PRODUCTS = [
    ('Desk', 'good', 1000, 24),
    ('Chair', 'good', 100, 75),
    ('Computer', 'bad', 2000, 6),
    ('Mouse', 'bad', 50, 1337),
    ('Keyboard', 'ok', 100, 42),
    ('Monitor', 'bad', 500, 18),
    ('Laptop', 'good', 1500, 40),
]


@attr.s()
class Product(object):
    name = attr.ib()
    quality = attr.ib()
    price = attr.ib()
    code = attr.ib()

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
