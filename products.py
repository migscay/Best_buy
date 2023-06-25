class Product:

    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("You have to provide the name of the product")
        else:
            self.name = name

        if price < 0:
            raise ValueError("Cannot have a negative price")
        else:
            self.price = float(price)

        try:
            self.quantity = int(quantity)
        except (TypeError, ValueError) as error:
            print("You have to provide a valid quantity for the Product")

        self.active = True

    def set_quantity(self, quantity):
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        In case of a problem (when? think about it), raises an Exception.
        :param quantity:
        :return: quantity * self.price
        """
        if quantity > self.quantity:
            raise ValueError("Quantity larger than what exists")

        self.set_quantity(self.quantity - quantity)

        if self.quantity == 0:
            self.deactivate()

        return self.price * quantity


class NonStockedProduct(Product):
    def __init__(self, name, price):
        if not name:
            raise ValueError("You have to provide the name of the product")
        else:
            self.name = name

        if price < 0:
            raise ValueError("Cannot have a negative price")
        else:
            self.price = float(price)

        self.active = True


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = int(maximum)

def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    #error = Product("error product", price="error", quantity="error")
    #error = Product("", price="price", quantity="quantity")

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())


if __name__ == "__main__":
    main()