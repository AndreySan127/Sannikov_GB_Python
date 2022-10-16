""" Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def start_calc():
    """
    В качестве значения функция start_calc() принимает первый операнд дабы последовательность работы была более удобной
    и понятной для пользователя. Затем она передает полученное значение в функцию calc(num_1), а та, в свою очередь,
    проводит расчет и отвечсет за рекурсивный вызов самой себя. При этом результат предыдущей операции становится
    первым числом для следующей операции.
    """
    num_1 = input('Введите первое число:')
    try:
        num_1 = int(num_1)
        return calc(num_1)
    except ValueError:
        print('Ошибка ввода. Введите число!')
        return start_calc()


def calc(num_1):
    symbol = input('Введите символ операции (+, -, *, / ) или 0 для выхода: ')
    if symbol == '0':
        return print('Работа программы завершена')
    elif symbol not in ['+', '-', '*', '/']:
        print('Введен некорректный символ оператора. Повторите попытку.')
        return calc(num_1)
    try:
        num_2 = int(input('Введите следующее число: '))
        if symbol == "+":
            num_1 = num_1 + num_2
            print(f'Результат равен: {num_1}')
            return calc(num_1)
        elif symbol == '-':
            num_1 = num_1 - num_2
            print(f'Результат равен: {num_1}')
            return calc(num_1)
        elif symbol == '*':
            num_1 = num_1 * num_2
            print(f'Результат равен: {num_1}')
            return calc(num_1)
        elif symbol == '/':
            num_1 = num_1 / num_2
            print(f'Результат равен: {num_1}')
            return calc(num_1)
    except ZeroDivisionError:
        print('Делить на нуль нельзя!')
        return calc(num_1)
    except ValueError:
        print('Ошибка ввода. Введите число!')
        return calc(num_1)


start_calc()