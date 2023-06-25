"""
Test code for the Product class

Test that creating a normal product works.
Test that creating a product with invalid details (empty name, negative price) invokes an exception.
Test that when a product reaches 0 quantity, it becomes inactive.
Test that product purchase modifies the quantity and returns the right output.
Test that buying a larger quantity than exists invokes exception.
"""

import pytest
from products import Product


def test_normal_create_product():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    assert bose.is_active()


"""
If name is empty, ValueError is raised
"""
def test_create_product_empty_name():
    with pytest.raises(ValueError, match="You have to provide the name of the product"):
        bose = Product("", price=250, quantity=500)


"""
If price is negative, ValueError is raised
"""
def test_create_product_negative_price():
    with pytest.raises(ValueError, match="Cannot have a negative price"):
        bose = Product("Bose QuietComfort Earbuds", price=-1250, quantity=500)


"""
If quantity reaches zero, should be deactivated
"""
def test_create_product_quantity_zero():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    bose.buy(500)
    assert not bose.is_active()


"""
quantity bought changes product quantity correctly
"""
def test_product_quantity_changed_correctly():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    bose.buy(200)
    assert bose.get_quantity() == 300


"""
Buying quantity larger than what exists raises exception
"""
def test_cannot_buy_larger_than_what_exists():
    with pytest.raises(ValueError, match="Quantity larger than what exists"):
        bose = Product("Bose QuietComfort Earbuds", price=1250, quantity=500)
        bose.buy(501)

pytest.main()