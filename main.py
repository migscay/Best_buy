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
            order_error = str(e)

    if order_error:
        print(order_error)
    elif total_order_amount > 0:
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

    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]
    best_buy = store.Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()