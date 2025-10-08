"""
Протестируйте классы из модуля homework/models.py
"""

import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 10)


@pytest.fixture
def magazine():
    return Product("magazine", 50, "This is a magazine", 20)


@pytest.fixture
def empty_cart():
    return Cart()


@pytest.fixture
def cart_with_one_product(product):
    cart = Cart()
    cart.add_product(product, 3)
    return cart


@pytest.fixture
def cart_with_two_products(product, magazine):
    cart = Cart()
    cart.add_product(product, 3)
    cart.add_product(magazine, 5)
    return cart


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity_is_less_than(self, product):
        # TODO напишите проверки на метод check_quantity
        """Тест проверяет ситуацию, когда запрашивается меньше продуктов, чем есть на складе"""
        assert product.check_quantity(5)

    def test_product_check_quantity_is_equal(self, product):
        """Тест проверяет ситуацию, когда запрашивается столько же продуктов, сколько есть на складе"""
        assert product.check_quantity(10)

    def test_product_check_quantity_is_greater_than(self, product):
        """Тест проверяет ситуацию, когда запрашивается больше продуктов, чем есть на складе."""
        assert not product.check_quantity(11)

    def test_product_buy_part_of_products(self, product):
        # TODO напишите проверки на метод buy
        """Тест проверяет покупку части продуктов, которые есть на складе"""
        product.buy(5)
        assert product.quantity == 5

    def test_product_buy_all_products(self, product):
        # TODO напишите проверки на метод buy
        """Тест проверяет покупку всех продуктов, которые есть на складе"""
        product.buy(10)
        assert product.quantity == 0

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(
            ValueError, match=f"Недостаточно {product.name} для покупки."
        ):
            product.buy(15)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product_first_item(self, empty_cart, product):
        """Тест проверяет добавление первого продукта в пустую корзину"""
        empty_cart.add_product(product)
        assert empty_cart.products[product] == 1

    def test_cart_add_product_first_item_less_than_limit(self, empty_cart, product):
        """Тест проверяет добавление первого продукта в пустую корзину, количество продукта не превышает его количество на складе"""
        empty_cart.add_product(product, 4)
        assert empty_cart.products[product] == 4

    def test_cart_add_product_first_item_greater_than_limit(self, empty_cart, product):
        """
        Тест проверяет добавление первого продукта в пустую корзину, количество продукта превышает его количество на складе.
        По требованиям должен быть ValueError на этапе покупки, поэтому здесь добавление не ограничено.
        """
        empty_cart.add_product(product, 14)
        assert empty_cart.products[product] == 14

    def test_cart_add_product_second_item(
        self, cart_with_one_product, magazine, product
    ):
        """Тест проверяет добавление нового продукта в непустую корзину"""
        cart_with_one_product.add_product(magazine, 5)
        assert cart_with_one_product.products[magazine] == 5
        assert cart_with_one_product.products[product] == 3

    def test_cart_add_product_additional_item_less_than_limit(
        self, cart_with_one_product, product
    ):
        """Тест проверяет добавление продукта в корзину, где уже есть продукт, общее количество меньше, чем на складе"""
        cart_with_one_product.add_product(product, 5)
        assert cart_with_one_product.products[product] == 8

    def test_cart_add_product_additional_item_equal_limit(
        self, cart_with_one_product, product
    ):
        """Тест проверяет добавление продукта в корзину, где уже есть продукт, общее количество равно количеству на складе"""
        cart_with_one_product.add_product(product, 7)
        assert cart_with_one_product.products[product] == 10

    def test_cart_add_product_additional_item_greater_than_limit(
        self, cart_with_one_product, product
    ):
        """
        Тест проверяет добавление продукта в корзину, где уже есть продукт,
        общее количество превышает количество на складе.
        По требованиям должен быть ValueError на этапе покупки, поэтому здесь добавление не ограничено
        """
        cart_with_one_product.add_product(product, 11)
        assert cart_with_one_product.products[product] == 14

    def test_cart_add_product_second_item_greater_than_limit(
        self, cart_with_one_product, magazine
    ):
        """
        Тест проверяет добавление продукта в непустую корзину,
        количество продукта превышает его количество на складе.
        По требованиям должен быть ValueError на этапе покупки, поэтому здесь добавление не ограничено
        """
        cart_with_one_product.add_product(magazine, 21)
        assert cart_with_one_product.products[magazine] == 21

    def test_cart_remove_product_one_item_less_than_quantity(self, product):
        """Тест проверяет удаление нескольких единиц продукта"""
        pass

    def test_cart_remove_product_one_item_equal_quantity(
        self, product, cart_with_one_product
    ):
        """Тест проверяет удаление всех единиц продукта"""
        cart_with_one_product.remove_product(product, 1)
        assert cart_with_one_product.products[product] == 2

    def test_cart_remove_product_one_item_greater_than_quantity(
        self, product, cart_with_one_product
    ):
        """Тест проверяет удаление большего количества продукта, чем есть в корзине"""
        cart_with_one_product.remove_product(product, 5)
        assert product not in cart_with_one_product.products

    def test_cart_remove_product_one_item_empty_remove_count(
        self, product, cart_with_one_product
    ):
        """Тест проверяет удаление продукта из корзины, когда не передано количество для удаления"""
        cart_with_one_product.remove_product(product)
        assert product not in cart_with_one_product.products

    def test_cart_remove_product_some_items_less_than_quantity(
        self, product, magazine, cart_with_two_products
    ):
        """Тест проверяет удаление нескольких единиц продукта, когда в корзине несколько продуктов"""
        cart_with_two_products.remove_product(magazine, 3)
        assert cart_with_two_products.products[magazine] == 2
        assert cart_with_two_products.products[product] == 3

    def test_cart_remove_product_some_items_equal_quantity(
        self, product, magazine, cart_with_two_products
    ):
        """Тест проверяет удаление всех единиц продукта, когда в корзине несколько продуктов"""
        cart_with_two_products.remove_product(magazine, 5)
        assert magazine not in cart_with_two_products.products
        assert cart_with_two_products.products[product] == 3

    def test_cart_remove_product_some_items_greater_than_quantity(
        self, product, magazine, cart_with_two_products
    ):
        """Тест проверяет удаление большего количества продукта, чем есть в корзине, когда в корзине несколько продуктов"""
        cart_with_two_products.remove_product(magazine, 20)
        assert magazine not in cart_with_two_products.products
        assert cart_with_two_products.products[product] == 3

    def test_cart_remove_product_some_items_empty_remove_count(
        self, product, magazine, cart_with_two_products
    ):
        """Тест проверяет удаление продукта из корзины, когда не передано количество для удаления, когда в корзине несколько продуктов"""
        cart_with_two_products.remove_product(magazine)
        assert magazine not in cart_with_two_products.products
        assert cart_with_two_products.products[product] == 3

    def test_cart_add_product_after_removing(self, product, cart_with_one_product):
        """Тест проверяет добавление продукта после его удаления из корзины"""
        cart_with_one_product.remove_product(product, 2)
        cart_with_one_product.add_product(product, 3)
        assert cart_with_one_product.products[product] == 4

    def test_cart_clear_one_item(self, cart_with_one_product):
        """Тест проверяет очистку корзины с одним продуктом"""
        cart_with_one_product.clear()
        assert not cart_with_one_product.products

    def test_cart_clear_some_items(self, cart_with_two_products):
        """Тест проверяет очистку корзины с несколькими продуктами"""
        cart_with_two_products.clear()
        assert not cart_with_two_products.products

    def test_cart_clear_empty_cart(self, empty_cart):
        """Тест проверяет очистку пустой корзины"""
        empty_cart.clear()
        assert not empty_cart.products

    def test_cart_get_total_price_one_item(self, cart_with_one_product, product):
        """Тест проверяет стоимость корзины с одним продуктом"""
        expected_price = product.price * cart_with_one_product.products[product]
        assert cart_with_one_product.get_total_price() == expected_price

    def test_cart_get_total_price_some_items(
        self, cart_with_two_products, product, magazine
    ):
        """Тест проверяет стоимость корзины с несколькими продуктами"""
        expected_price = (
            product.price * cart_with_two_products.products[product]
            + magazine.price * cart_with_two_products.products[magazine]
        )
        assert cart_with_two_products.get_total_price() == expected_price

    def test_cart_get_total_price_empty_cart(self, empty_cart):
        """Тест проверяет стоимость корзины без продуктов"""
        assert empty_cart.get_total_price() == 0

    def test_cart_get_total_price_after_removing(self, cart_with_one_product, product):
        """Тест проверяет стоимость корзины, когда часть продуктов была удалена"""
        cart_with_one_product.remove_product(product, 1)
        expected_price = product.price * cart_with_one_product.products[product]
        assert cart_with_one_product.get_total_price() == expected_price

    def test_cart_get_total_price_after_adding(self, cart_with_one_product, product):
        """Тест проверяет стоимость корзины, когда продукты были добавлены к уже добавленным"""
        cart_with_one_product.add_product(product, 2)
        expected_price = product.price * cart_with_one_product.products[product]
        assert cart_with_one_product.get_total_price() == expected_price

    def test_cart_buy_one_item(self, product, cart_with_one_product):
        """Тест проверяет покупку одного продукта"""

        expected_quantity = product.quantity - cart_with_one_product.products[product]
        cart_with_one_product.buy()

        assert not cart_with_one_product.products
        assert product.quantity == expected_quantity

    def test_cart_buy_some_items(self, product, magazine, cart_with_two_products):
        """Тест проверяет покупку нескольких продуктов"""
        product_expected_quantity = (
            product.quantity - cart_with_two_products.products[product]
        )
        magazine_expected_quantity = (
            magazine.quantity - cart_with_two_products.products[magazine]
        )
        cart_with_two_products.buy()

        assert not cart_with_two_products.products
        assert magazine.quantity == magazine_expected_quantity
        assert product.quantity == product_expected_quantity

    def test_cart_buy_empty_cart(self, empty_cart):
        """Тест проверяет покупку, когда корзина пустая"""
        empty_cart.clear()
        assert not empty_cart.products

    def test_cart_buy_one_item_excess_quantity(self, product, cart_with_one_product):
        """Тест проверяет покупку одного продукта в большем количестве, чем доступно"""

        cart_with_one_product.add_product(product, 10)
        expected_product_quantity = product.quantity
        expected_cart_quantity = cart_with_one_product.products[product]

        with pytest.raises(
            ValueError, match=f"Недостаточно {product.name} для покупки."
        ):
            cart_with_one_product.buy()

        assert cart_with_one_product.products[product] == expected_cart_quantity
        assert product.quantity == expected_product_quantity

    def test_cart_buy_some_items_excess_quantity(
        self, product, magazine, cart_with_two_products
    ):
        """Тест проверяет покупку нескольких продуктов в большем количестве, чем доступно"""
        cart_with_two_products.add_product(product, 10)
        expected_product_quantity = product.quantity
        expected_magazine_quantity = magazine.quantity
        expected_cart_len = len(cart_with_two_products.products)

        with pytest.raises(
            ValueError, match=f"Недостаточно {product.name} для покупки."
        ):
            cart_with_two_products.buy()

        assert product.quantity == expected_product_quantity
        assert magazine.quantity == expected_magazine_quantity
        assert len(cart_with_two_products.products) == expected_cart_len
