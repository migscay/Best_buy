class Product:

    def __init__(self, name, price, quantity):
        if not name:
            print("You have to provide the name of the product.")
        else:
            try:
                self.name = name
            except TypeError:
                print("You have to provide the name of the product.")

        try:
            self.price = float(price)
        except (TypeError, ValueError) as error:
            print("You have to provide a valid price for the Product")

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
            raise Exception("Error while making order! Quantity larger than what exists")

        self.set_quantity(self.quantity - quantity)

        if self.quantity == 0:
            self.deactivate()

        return self.price * quantity


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