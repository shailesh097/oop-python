import csv

class Item:
    pay_rate = 0.8 #Rate after 20% discount.
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
        # Run validations to the recieved argument
        assert price >= 0, f"Passed price: {price} should be greater than or equal to 0."
        assert quantity >= 0, f"Passed quantity: {quantity} should be greater than or equal to 0."

        # Assign self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instanciate_from_csv(cls):
        with open('data.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
                )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # E.g: 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    # __repr__ magic method is used for the representation of each instance
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item('Mouse', 50, 5)
item5 = Item('Keyboard', 75, 5)
