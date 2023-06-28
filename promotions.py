from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    @abstractmethod
    def apply_promotion(self):
        pass


class SecondHalfPrice(Promotion):
    def apply_promotion(self, price, quantity):
        purchase_price = 0
        if quantity > 1:
            purchase_price += price * .5
            quantity -= 1
        purchase_price += price * quantity

        return purchase_price


class ThirdOneFree(Promotion):
    def apply_promotion(self, price, quantity):
        purchase_price = 0
        quotient, remainder = divmod(quantity, 3)
        purchase_price += quotient * 2 * price
        purchase_price += remainder * price

        return purchase_price


class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, price, quantity):
        discount = price * quantity * (self.percent / 100)
        full_price = price * quantity
        return full_price - discount
