import attr
from attr import validators
from enum import IntEnum

PRODUCTS = [
    ('Desk', 'good', 1000, 24),
    ('Chair', 'good', 100, 75),
    ('Computer', 'bad', 2000, 6),
    ('Mouse', 'bad', 50, 1337),
    ('Keyboard', 'ok', 100, 42),
    ('Monitor', 'bad', 500, 18),
    ('Laptop', 'good', 1500, 40),
]


class Quality(IntEnum):
    bad = -1
    ok = 0
    good = 1


def code_validator(instance, attribute, value):
    if not isinstance(value, int):
        raise TypeError('code must be an integer')
    digits_sum = sum(int(digit) for digit in str(value))
    return digits_sum % 2 == 0


@attr.s(frozen=True)
class Product(object):
    name = attr.ib(validator=validators.instance_of(str))
    quality = attr.ib(
        validator=validators.instance_of(int),
        converter=lambda q: Quality[q] if isinstance(q, str) else q,
    )
    price = attr.ib(validator=[validators.instance_of(int), validators.ge(0)])
    code = attr.ib(validator=code_validator)

    def is_pricey(self) -> bool:
        return self.price > 1000

    def is_popular(self) -> bool:
        return self.price > 1000


def main():
    products = {
        Product(name, quality, price, code)
        for (name, quality, price, code) in PRODUCTS
    }
    for p in products:
        print(f"Product Description: {p}")
        print(f"{p.name} is {'' if p.is_pricey() else 'not '}pricey!")
    print(attr.evolve(products.pop(), price=999999))


if __name__ == '__main__':
    main()
