"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 10)

@pytest.fixture
def magazine():
    return Product("magazine", 50, "This is a magazine", 20)


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
        """Тест проверяет ситуацию, когда запрашивается больше продуктов, чем есть на складе"""
        assert not product.check_quantity(11)

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

    def test_cart_remove_product_one_item_less_than_quantity(self, product):
        """Тест проверяет удаление нескольких единиц продукта"""
        pass

    def test_cart_remove_product_one_item_equal_quantity(self, product):
        """Тест проверяет удаление всех единиц продукта"""
        pass

    def test_cart_remove_product_one_item_greater_than_quantity(self, product):
        """Тест проверяет удаление большего количества продукта, чем есть в корзине"""
        pass

    def test_cart_remove_product_one_item_empty_remove_count(self, product):
        """Тест проверяет удаление продукта из корзины, когда не передано количество для удаления"""
        pass

    def test_cart_remove_product_some_items_less_than_quantity(self, product):
        """Тест проверяет удаление нескольких единиц продукта, когда в корзине несколько продуктов"""
        pass

    def test_cart_remove_product_some_items_equal_quantity(self, product):
        """Тест проверяет удаление всех единиц продукта, когда в корзине несколько продуктов"""
        pass

    def test_cart_remove_product_some_items_greater_than_quantity(self, product):
        """Тест проверяет удаление большего количества продукта, чем есть в корзине, когда в корзине несколько продуктов"""
        pass

    def test_cart_remove_product_some_items_empty_remove_count(self, product):
        """Тест проверяет удаление продукта из корзины, когда не передано количество для удаления, когда в корзине несколько продуктов"""
        pass

    def test_cart_add_product_after_removing(self, product):
        """Тест проверяет добавление продукта после его удаления из корзины"""
        pass

    def test_cart_clear_one_item(self, product):
        """Тест проверяет очистку корзины с одним продуктом"""
        pass

    def test_cart_clear_some_items(self, product):
        """Тест проверяет очистку корзины с несколькими продуктами"""
        pass

    def test_cart_clear_empty_cart(self, product):
        """Тест проверяет очистку пустой корзины"""
        pass

    def test_cart_get_total_price_one_item(self, product):
        """Тест проверяет стоимость корзины с одним продуктом"""
        pass

    def test_cart_get_total_price_some_items(self, product):
        """Тест проверяет стоимость корзины с несколькими продуктами"""
        pass

    def test_cart_get_total_price_empty_cart(self, product):
        """Тест проверяет стоимость корзины без продуктов"""
        pass

    def test_cart_get_total_price_after_removing(self, product):
        """Тест проверяет стоимость корзины, когда часть продуктов была удалена"""
        pass

    def test_cart_get_total_price_after_adding(self, product):
        """Тест проверяет стоимость корзины, когда продукты были добавлены к уже добавленным"""
        pass

    def test_cart_buy_one_item(self, product):
        """Тест проверяет покупку одного продукта"""
        # не забыть проверить, что количество на складе уменьшилось
        pass

    def test_cart_buy_some_items(self, product):
        """Тест проверяет покупку нескольких продуктов"""
        pass

    def test_cart_buy_after_adding(self, product):
        """Тест проверяет покупку, когда продукт был добавлен, частично удален и еще раз добавлен"""
        pass

    def test_cart_buy_empty_cart(self, product):
        """Тест проверяет покупку, когда корзина пустая"""
        # ValueError?
        pass

    def test_cart_buy_one_item_excess_quantity(self, product):
        """Тест проверяет покупку одного продукта в большем количестве, чем доступно"""
        # не забыть проверить, что количество на складе уменьшилось
        pass

    def test_cart_buy_some_items_excess_quantity(self, product):
        """Тест проверяет покупку нескольких продуктов в большем количестве, чем доступно"""
        pass

    def test_cart_buy_after_purchase(self, product):
        """Тест проверяет покупку, когда продукт был куплен, и его количество на складе уменьшилось"""
        pass

