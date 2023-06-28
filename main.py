def store_list_products(store):
    """
    prints the products of the store
    :param store:
    :return:
    """
    store_products = store.get_all_products()

    print("------")
    for product_number in range(len(store_products)):
        product = store_products[product_number]
        print(f"{product_number + 1}. {product.show()}")
    print("------")


def store_total_quantity(store):
    print(f"Total of {store.get_total_quantity()} items in store")


def store_order(store):
    store_list_products(store)
    store_products = store.get_all_products()

    print("When you want to finish order, enter empty text.")
    total_order_amount = 0
    order_error = ""

    while True:
        order_product = input("Which product # do you want? ")
        order_amount = input("What amount do you want? ")

        if not order_product or not order_amount:
            break

        try:
            total_order_amount += store_products[int(order_product) - 1].buy(int(order_amount))
            print("Product added to list!\n")
        except Exception as e:
            print(str(e))

    if total_order_amount > 0:
        print(f"********\nOrder made! Total payment: ${total_order_amount}")


def quit_app(store):
    exit()


def start(store):
    menu_items = ["1. List all products in store", "2. Show total amount in store",
                  "3. Make an order", "4. Quit"]

    menu_functions = {
        1: store_list_products,
        2: store_total_quantity,
        3: store_order,
        4: quit_app
    }

    while True:
        print("\n    Store Menu\n    ----------")
        for choice in menu_items:
            print(choice)

        user_choice = int(input("Please choose a number: "))

        if 0 < user_choice < 5:
            menu_functions[user_choice](store)


def main():
    import store
    import products
    import promotions

    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    best_buy = store.Store(product_list)

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    start(best_buy)


if __name__ == "__main__":
    main()