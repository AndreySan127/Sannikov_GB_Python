""" Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
# print(f'Количество цифр в числе {number}: четных - {count_even}, нечетных - {count_odd}')

def count_even_odd(u_number, count_even=0, count_odd=0, counter=0):
    """
    Функция определяет количество четных и нечетных цифр во введенном чилсе, в том чилсе и в нуле.
    """
    try:
        u_number = int(u_number)
    except ValueError:
        print('Ошибка ввода. Введите число!')
    if u_number == 0 :
        if counter == 0:
            count_even += 1
            return f'Количество цифр в числе: четных - {count_even}, нечетных - {count_odd}'
        else:
            return f'Количество цифр в числе: четных - {count_even}, нечетных - {count_odd}'
    elif u_number % 2 == 0:
        counter += 1
        count_even += 1
    elif u_number % 2 == 1:
        counter += 1
        count_odd += 1
    return count_even_odd(u_number // 10, count_even, count_odd, counter)


print(count_even_odd(input('Введите натуральное число: ')))