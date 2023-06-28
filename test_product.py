import pytest
from products import Product, NonStockedProduct, LimitedProduct
import promotions


def test_normal_create_product():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    assert bose.is_active()


def test_create_product_empty_name():
    with pytest.raises(ValueError, match="You have to provide the name of the product"):
        bose = Product("", price=250, quantity=500)


def test_create_product_negative_price():
    with pytest.raises(ValueError, match="Cannot have a negative price"):
        bose = Product("Bose QuietComfort Earbuds", price=-1250, quantity=500)


def test_create_product_quantity_zero():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    bose.buy(500)
    assert not bose.is_active()


def test_product_quantity_changed_correctly():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    bose.buy(200)
    assert bose.get_quantity() == 300


def test_cannot_buy_larger_than_what_exists():
    with pytest.raises(ValueError, match="Quantity larger than what exists"):
        bose = Product("Bose QuietComfort Earbuds", price=1250, quantity=500)
        bose.buy(501)


def test_buy_two_second_half_price():
    macbook = Product("MacBook Air M2", price=1450, quantity=100)
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    macbook.set_promotion(second_half_price)
    assert macbook.buy(2) == 2175


def test_buy_three_third_one_free():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    bose.set_promotion(third_one_free)
    assert bose.buy(3) == 500


def test_buy_thirty_percent_off():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)
    bose.set_promotion(thirty_percent)
    assert bose.buy(3) == 525


def test_buy_one_each():
    # setup initial stock of inventory
    macbook = Product("MacBook Air M2", price=1450, quantity=100)
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    google_pixel = Product("Google Pixel 7", price=500, quantity=250)
    windows_licence = NonStockedProduct("Windows License", price=125)
    shipping = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    macbook.set_promotion(second_half_price)
    bose.set_promotion(third_one_free)
    windows_licence.set_promotion(thirty_percent)

    assert macbook.buy(1) == 1450
    assert bose.buy(1) == 250
    assert google_pixel.buy(1) == 500
    assert windows_licence.buy(1) == 87.50
    assert shipping.buy(1) == 10


def test_buy_more_than_maximum():
    with pytest.raises(ValueError, match="Only 1 is allowed from this product!"):
        shipping = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
        shipping.buy(2)


pytest.main()
