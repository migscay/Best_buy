class Product:

    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("You have to provide the name of the product")
        else:
            self.name = name

        if price < 0:
            raise ValueError("Cannot have a negative price")
        else:
            self.price = price

        try:
            self.quantity = int(quantity)
        except (TypeError, ValueError) as error:
            print("You have to provide a valid quantity for the Product")

        self.active = True

        self.promotion = ""

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

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def show(self):
        if isinstance(self, LimitedProduct):
            return f"{self.name}, Price: {'${}'.format(self.price)}, " \
                   f"Limited to 1 per order!," \
                   f" Promotion: {self.promotion.get_name() if self.promotion else 'None'} "
        else:
            return f"{self.name}, Price: {'${}'.format(self.price)}, " \
                   f"Quantity: {self.quantity if self.quantity > 0 else 'Unlimited'}," \
                   f" Promotion: {self.promotion.get_name() if self.promotion else 'None'} "

    def buy(self, quantity):
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        :param quantity:
        :return: quantity * self.price
        """
        if quantity > self.quantity:
            raise ValueError("Quantity larger than what exists")

        self.set_quantity(self.quantity - quantity)

        if self.quantity == 0:
            self.deactivate()

        purchase_price = 0.00
        """
        if the product has a promotion, product
        purchase price comes from applying
        the promotion
        """
        if self.promotion:
            purchase_price = self.promotion.apply_promotion(self.price, quantity)
        else:
            purchase_price = self.price * quantity

        return purchase_price


class NonStockedProduct(Product):
    def __init__(self, name, price, quantity=0):
        super().__init__(name, price, quantity)

        self.active = True
        self.quantity = quantity

    def buy(self, quantity):
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        :param quantity:
        :return: quantity * self.price
        """
        purchase_price = 0.00
        """
        if the product has a promotion, product
        purchase price comes from applying
        the promotion
        """
        if self.promotion:
            purchase_price = self.promotion.apply_promotion(self.price, quantity)
        else:
            purchase_price = self.price * quantity

        return purchase_price


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = int(maximum)

    def buy(self, quantity):
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        :param quantity:
        :return: quantity * self.price
        """
        if quantity > self.maximum:
            raise ValueError(f"Only {self.maximum} is allowed from this product!")

        purchase_price = 0.00
        """
        if the product has a promotion, product
        purchase price comes from applying
        the promotion
        """
        if self.promotion:
            purchase_price = self.promotion.apply_promotion(self.price, quantity)
        else:
            purchase_price = self.price * quantity

        return purchase_price

    def get_maximum(self):
        return self.maximum


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())


if __name__ == "__main__":
    main()