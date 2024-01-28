import unittest

from task6_11 import leap_year, valid_date


class TestTask611(unittest.TestCase):

    def test_leap_year(self):
        # проверка високосного года
        self.assertTrue(leap_year(2024, False))
        self.assertTrue(leap_year(1600, False))

    def test_non_leap_year(self):
        # проверка невисокосного года
        self.assertFalse(leap_year(2023, False))
        self.assertFalse(leap_year(1700, False))

    def test_date_exists(self):
        # Проверка существующих дат
        self.assertTrue(valid_date('27.01.2024'))
        self.assertTrue(valid_date('27.01.2023'))
        self.assertTrue(valid_date('30.11.2023'))

    def test_date_non_exists(self):
        # Проверка несуществующих дат
        self.assertFalse(valid_date('37.01.2024'))
        self.assertFalse(valid_date('00.01.2023'))
        self.assertFalse(valid_date('29.02.2023'))

    def test_date_raises(self):
        # Проверка ошибки ввода
        with self.assertRaises(ValueError):
            valid_date('тридцатое января две тысячи двадцать третьего года')


unittest.main()