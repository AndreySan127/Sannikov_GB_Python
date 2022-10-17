import time


def timing(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func_output = func(*args, **kwargs)
        end = time.time()
        total = end - start
        print(f'Функция {func.__name__} - {total} секунд.')
        return func_output
    return wrapper


@timing
def get_lst():
    return [i for i in range(10**7)]


@timing
def get_dct():
    return {j: j for j in range(10**7)}


@timing
def lst_pop():
    global lst
    for i in range(1, 10**2):
        lst.pop(i)


@timing
def dct_pop():
    global dct
    for i in range(1, 10**7):
        dct.pop(i)


lst = get_lst()
dct = get_dct()

lst_pop()
dct_pop()

"""
1. Словарь заполняется медленнее, чем список, так как для каждого элемента словаря генерируется хеш.
2. При поиске/удалении элемента операции со словарем производятся быстрее, так как поиск ведется по хешу, без перебора
элементов. Разница в данном примере достигает 10^5 раз.
"""