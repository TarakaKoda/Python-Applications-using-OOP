from item import Item


class Phone(Item):
    all = []

    def __init__(self, name: str, price: float, quantity: int, broken_phone: int):
        super().__init__(name, price, quantity)
        # Run validations for received arguments
        assert broken_phone >= 0, "Broken Phone is not greater than zero"

        # Assigning arguments
        self.broken_phone = broken_phone

        Phone.all.append(self)

    def condition_of_phone(self):
        return f"{self.item_name}\nBroken Phones: {self.broken_phone}\nWorking Condition: {self.item_quantity - self.broken_phone}\n"

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.item_name}", {self.item_price}, {self.item_quantity}, {self.broken_phone})'
