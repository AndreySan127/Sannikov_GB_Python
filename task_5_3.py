""" task 3 """

from sys import getsizeof

tutors = [

    'Иван', 'Анастасия', 'Петр', 'Сергей',

    'Дмитрий', 'Борис', 'Елена'

]
klasses = [

    '9А', '7В', '9Б', '9В', '8Б',  # '10А', '10Б', '9А'

]


def my_zip_gen():

    len_klasses = len(klasses)

    return ((tut, klasses[i]) if i < len_klasses else (tut, None)
            for i, tut in enumerate(tutors))


if __name__ == '__main__':

    gen = my_zip_gen()
    print(type(gen))
    print(getsizeof(gen))
    print(*gen)
    # next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration