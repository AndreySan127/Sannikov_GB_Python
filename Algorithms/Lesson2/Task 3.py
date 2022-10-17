""" Введите число, которое требуется перевернуть: 1230
Перевернутое число: 0321
"""


def reverse_num(u_number, reverse_number = ''):
    try:
        u_number = int(u_number)
    except ValueError:
        print('Ошибка ввода. Введите число!')
    reverse_number += str(u_number % 10)
    if u_number < 10:
        return reverse_number
    else:
        return reverse_number + reverse_num(u_number // 10)


print(reverse_num(input('Введите натуральное число: ')))
