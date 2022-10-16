""" Подсказка:
Базовый случай здесь - угадали число или закончились попытки
"""

from random import randint

attempts = 10


def guess_number(number, i=0):
    user_answer = int(input('Введите Ваш вариант: '))
    if i == attempts - 1:
        return 'Вы проиграли!'
    elif user_answer == number:
        return f'Вы угадали с {i + 1}й попытки'
    else:
        if user_answer > number:
            print(f'Вы ввели слишком большое число. Осталось попыток: {attempts - i - 1}')
            return guess_number(number, i + 1)
        else:
            print(f'Вы ввели слишком маленькое число. Осталось попыток: {attempts - i - 1}')
            return guess_number(number, i + 1)


print(guess_number(randint(0, 100)))