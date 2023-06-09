from abc import ABC, abstractmethod


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
        self.promotion = None

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

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def show(self) -> str:
        promotion_info = f"Promotion: {self.promotion.get_name()}" if self.promotion else "No promotion"
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, {promotion_info}"

    def buy(self, quantity) -> float:
        if not self.active:
            raise Exception("Product is not active")
        if quantity > self.quantity:
            raise Exception("Insufficient quantity")

        if self.promotion is not None:
            return self.promotion.apply_promotion(self, quantity)

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


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        discount = (self.percent / 100) * product.price * quantity
        return product.price * quantity - discount


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        if quantity % 2 == 0:
            return (product.price * quantity) - ((quantity // 2) * (product.price / 2))
        else:
            return (product.price * quantity) - (((quantity - 1) // 2) * (product.price / 2))


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        free_items = quantity // 3
        return (product.price * quantity) - (free_items * product.price)
