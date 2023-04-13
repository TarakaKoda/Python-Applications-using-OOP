class Storge:
    def __init__(self, item, price, quantity):
        self.item = item
        self.item_prise = price
        self.item_quantity = quantity

    @property
    def total_price(self):
        return f"Total Price: ${self.item_prise * self.item_quantity}"


class Manager:
    def __init__(self, first, last, storage_instance, list_of_items=None):
        self.first_name = first
        self.last_name = last
        self.storge = storage_instance
        if list_of_items is None:
            self.list_of_items = []
        else:
            self.list_of_items = list_of_items

    def add_item(self, item):
        if item not in self.list_of_items:
            self.list_of_items.append(item)
            return f"Item: '{item}' Added to the List\nUpdated List: {self.list_of_items}"
        else:
            return f"Item: '{item}' is already exists in the List: {self.list_of_items}"

    def remove_item(self, item):
        if item in self.list_of_items:
            self.list_of_items.remove(item)
            return f"Item: '{item}' has been removed from the List\nUpdated List: {self.list_of_items}"
        else:
            return f"Item: '{item}' does not exists in the list: {self.list_of_items}"

    def total_items_list(self):
        for index, items in enumerate(self.list_of_items,start=1):
            print(f"{index}. {items}, price: {self.storge.item_prise}, Total no.of quantity: {self.storge.item_quantity}")

    @property
    def total_prince(self):
        return self.storge.total_price


item1 = Storge("phone", 15000, 5)
item2 = Storge("charger", 3000,5)
mgr1 = Manager("srinu","koda",item1)
print(mgr1.add_item("charger"))

# print(mgr1.item_prise)
print(mgr1.total_prince)
print(item1.total_price)
print(mgr1.add_item("phone"))
print(mgr1.total_prince)
mgr1.total_items_list()