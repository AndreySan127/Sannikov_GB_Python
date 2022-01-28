# 1 минута
one_minute = 60
# 1 час
one_hour = 3600
# 1 день
one_day = 86400
# 1 неделя
one_week = 604800
# 1 месяц (30.44 дней)
one_month = 2629743
# 1 год (365.24 дней)
one_year = 31556926

#Пользователь вводит продолжительность duration в секундах:
duration = int (input('Укажите продолжительность в секундах: '))

#вывод информации до минуты:
if duration<one_minute:
    print ('{} сек'.format(duration))
#вывод информации до часа:
elif one_minute <= duration and one_hour > duration:
    my_minute=duration//one_minute
    my_second=duration%one_minute
    print ('{} мин {} сек'.format(my_minute,my_second));
#вывод информации до суток:
elif duration >= one_hour and duration < one_day:
    my_hour=duration // one_hour
    duration=duration % one_hour
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print ('{} час {} мин {} сек'.format(my_hour,my_minute,my_second));
#вывод информации до недели:
elif duration >= one_day and duration < one_week:
    my_day = duration // one_day
    duration=duration % one_day
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print('{} дн {} час {} мин {} сек'.format(my_day, my_hour, my_minute, my_second));
#вывод информации до месяца:
elif duration >= one_month and duration < one_year:
    my_week = duration//one_week
    duration=duration%one_week
    my_day = duration // one_day
    duration = duration % one_day
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print('{} нед {} дн {} час {} мин {} сек'.format(my_week, my_day, my_hour, my_minute, my_second));
#вывод информации до года:
elif duration >= one_year:
    my_year=duration//one_year
    duration = duration % one_year
    my_week = duration//one_week
    duration=duration%one_week
    my_day = duration // one_day
    duration = duration % one_day
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_minute = duration // one_minute
    my_second = duration % one_minute
    print('{} год {} нед {} дн {} час {} мин {} сек'.format(my_year, my_week, my_day, my_hour, my_minute, my_second));