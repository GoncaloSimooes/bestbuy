class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise Exception("Invalid name")
        if price < 0:
            raise Exception("Invalid price")
        if quantity < 0:
            raise Exception("Invalid quantity")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> float:
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        if not self.active:
            raise Exception("Product is not active")
        if quantity > self.quantity:
            raise Exception("Insufficient quantity")

        self.quantity -= quantity
        return self.price * quantity


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def show(self) -> str:
        return f"{self.name} - Non Stocked Product"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.quantity_limit = maximum

    def set_quantity(self, quantity):
        if quantity > self.quantity_limit:
            raise Exception("Quantity exceeds the limit for this product.")
        super().set_quantity(quantity)

    def show(self) -> str:
        return f"{self.name} - Limited Product (Max quantity: {self.quantity_limit})"
