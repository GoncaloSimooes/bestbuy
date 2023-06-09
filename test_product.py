
import pytest
from bestbuy.products import Product


def test_create_normal_product():
    product = Product("iPhone 12", price=999, quantity=10)
    assert product.name == "iPhone 12"
    assert product.price == 999
    assert product.quantity == 10
    assert product.is_active()


def test_create_product_with_invalid_details():
    with pytest.raises(Exception):
        Product("", price=-100, quantity=5)


def test_product_quantity_zero_becomes_inactive():
    product = Product("Headphones", price=50, quantity=0)
    assert product.is_active()


def test_product_purchase_modifies_quantity_and_returns_output():
    product = Product("Camera", price=300, quantity=10)
    quantity_purchased = 3
    total_price = product.buy(quantity_purchased)
    assert product.quantity == 7
    assert total_price == 900


def test_buying_larger_quantity_than_exists_invokes_exception():
    product = Product("Speaker", price=100, quantity=5)
    with pytest.raises(Exception):
        product.buy(10)