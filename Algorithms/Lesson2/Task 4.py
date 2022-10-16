""" Без аналитики задание считается не принятым
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for j, i in enumerate(nums) if not j % 2]


def func_3(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


numbers = [i for i in range(1, 500)]

print(f'func_1 - {timeit("func_1(numbers)", "from __main__ import func_1, numbers", number=10000)}')
print(f'func_2 - {timeit("func_2(numbers)", "from __main__ import func_2, numbers", number=10000)}')
print(f'func_3 - {timeit("func_3(numbers)", "from __main__ import func_3, numbers", number=10000)}')

"""
    Параметр number выбирал исходя из фактически получаемого времени. Если время получается в сотых долях секунды, то
результаты плавают от запуска к запуску так, что невозможно оценить преимущество скорости какого-либо скрипта.
На десятых долях секунды результаты уже стабильно выделяют более оптимальные алгоритмы.
    Первый вариант выполнился за 0.455 c. - самый медленный, так как на каждом шаге идет выбор элементов, потом 
проверка остатка от деления и добавление в список
    Второй вариант - 0.312 c. - самый быстрый, так как нет необходимости создавать и инициализировать переменную 
счетчика;
    Третий вариант - 0.373c. - cредний по скорости выполнения. Лучше чем первый, т.к. нет излишнего создания
и пошагового добавления элементов на каждой итерации. Список создается одним разом исходя из заданных условий.
"""