input_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
"""Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
length_of_list:int = len(input_list)
store_id = id(input_list)
print(f"id before {store_id}")
for _ in range(length_of_list):
    elem = input_list.pop(0)
    if elem.isdigit() and elem.isalnum():
        input_list.append(f'"{int(elem):02d}"')
    elif elem[0] == "+" and elem[1].isdigit():
        input_list.append(f'"+{int(elem):02d}"')
    else:
        input_list.append(elem)
print(' '.join(input_list))

print(f"id after {id(input_list)}")