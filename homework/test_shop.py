"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity_is_less_than(self, product):
        # TODO напишите проверки на метод check_quantity
        """Тест проверяет ситуацию, когда запрашивается меньше продуктов, чем есть на складе"""
        pass

    def test_product_check_quantity_is_equal(self, product):
        # TODO напишите проверки на метод check_quantity
        """Тест проверяет ситуацию, когда запрашивается столько же продуктов, сколько есть на складе"""
        pass

    def test_product_check_quantity_is_greater_than(self, product):
        # TODO напишите проверки на метод check_quantity
        """Тест проверяет ситуацию, когда запрашивается больше продуктов, чем есть на складе"""
        pass

    def test_product_buy_part_of_products(self, product):
        # TODO напишите проверки на метод buy
        """Тест проверяет покупку части продуктов, которые есть на складе"""
        pass

    def test_product_buy_all_products(self, product):
        # TODO напишите проверки на метод buy
        """Тест проверяет покупку всех продуктов, которые есть на складе"""
        pass

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        pass


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_add_product_first_item(self, product):
        """Тест проверяет добавление первого продукта в пустую корзину"""
        pass

    def test_cart_add_product_first_item_greater_than_limit(self, product):
        """Тест проверяет добавление первого продукта в пустую корзину, количество продукта превышает его количество на складе"""
        pass

    def test_cart_add_product_second_item(self, product):
        """Тест проверяет добавление нового продукта в непустую корзину"""
        pass

    def test_cart_add_product_additional_item_less_than_limit(self, product):
        """Тест проверяет добавление продукта в корзину, где уже есть продукт, общее количество меньше, чем на складе"""
        pass

    def test_cart_add_product_additional_item_equal_limit(self, product):
        """Тест проверяет добавление продукта в корзину, где уже есть продукт, общее количество равно количеству на складе"""
        pass

    def test_cart_add_product_additional_item_greater_than_limit(self, product):
        """Тест проверяет добавление продукта в корзину, где уже есть продукт, общее количество превышает количество на складе"""
        # добавить обработку, в которой не будет ошибки, а будет добавлено то количество, которое есть на складе. И выведено сообщение
        pass

    def test_cart_add_product_second_item_greater_than_limit(self, product):
        """Тест проверяет добавление продукта в непустую корзину, количество продукта превышает его количество на складе"""
        pass
