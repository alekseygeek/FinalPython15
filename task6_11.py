# Задача N1 из 6го домаашнего задания:

# 6.1 Вы работаете над разработкой программы для проверки корректности даты,
# введенной пользователем. На вход будет подаваться дата в формате
# "день.месяц.год". Ваша задача - создать программу, которая проверяет,
# является ли введенная дата корректной или нет.

import logging
import sys


logging.basicConfig(
    level = logging.INFO,
    format = "[%(asctime)s] %(levelname)s: %(message)s"
)


def leap_year(year, log=True):
    """Проверка, високосный ли год"""
    # log - отключение логгирования во время тестов
    leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    if log and leap:
        logging.info('Проверяемая дата високосного года')
    return leap


def valid_date(date_str):
    """Проверка существования даты"""
    day, month, year = map(int, date_str.split('.'))
    if month < 1 or month > 12:
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        max_day = 29 if leap_year(year) else 28
    return False if day < 1 or day > max_day else year >= 1 and year <= 9999


if __name__ == "__main__":
    if len(sys.argv) != 2:
        logging.error(
            "Пожалуйста, передайте дату в формате 'dd.mm.yyyy' как аргумент"
            " командной строки, например: (python 6_1.py  31.12.2022)."
        )
    else:
        date_str = sys.argv[1]
        if valid_date(date_str):
            logging.info(f"{date_str} - Дата существует")
        else:
            logging.info(f"{date_str} - Дата не существует")