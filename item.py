import csv


class Item:
    broken_phone = 0
    pay_rate = 0.80  # Pay Rate of 20%
    all = []

    def __init__(self, name: str, price: float, quantity=1):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater then zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater then zero!"

        # Assign to self object
        self.item_name = name
        self.item_price = price
        self.item_quantity = quantity

        # Action to execute
        Item.all.append(self)

    @property
    def calculate_total_price(self):
        return f"Total price of {self.item_name}: {self.item_price} x {self.item_quantity} = " \
               f"{self.item_price * self.item_quantity}"

    def apply_discount(self):
        self.item_price = self.item_price * self.pay_rate
        return f"{self.item_name} price: ${self.item_price}item_name"

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity"))
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            # count out the float that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.item_name}", {self.item_price}, {self.item_quantity})'