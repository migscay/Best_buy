class Store:

    def __init__(self, store_products):
        self.products = store_products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def order(self, shopping_list):

        total_price = 0.00

        for product, quantity in shopping_list:
            total_price += product.buy(quantity)

        return total_price

    def get_total_quantity(self):
        total_products = 0

        for product in self.products:
            total_products += product.get_quantity()

        return total_products

    def get_all_products(self):
        for product in self.products:
            if not product.active:
                self.remove_product(product)

        return self.products


def main():
    import products
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]
    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(products)
    """
    #store = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))
    """

if __name__ == "__main__":
    main()
