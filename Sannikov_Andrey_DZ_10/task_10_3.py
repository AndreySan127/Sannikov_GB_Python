class OrganicCell(object):
    def __init__(self, size: int):
        if size <= 0:
            raise Exception('Клетка не может иметь меньше одной ячейки')
        self.size = size

    def __add__(self, other):
        return OrganicCell(self.size + other.size)

    def __sub__(self, other):
        result = self.size - other.size
        if result > 0:
            return OrganicCell(result)
        else:
            raise Exception(f'Ошибка! Вычитание {self} из {other} невозможно!')

    def __mul__(self, other):
        return OrganicCell(self.size * other.size)

    def __truediv__(self, other):
        return OrganicCell(self.size // other.size)

    def make_order(self, row_size: int) -> str:
        rows = ['*' * row_size for _ in range(self.size // row_size)]
        tail = '*' * (self.size % row_size)
        rows.append(tail)
        return '\n'.join(rows)

    def __str__(self):
        return '*' * self.size


if __name__ == '__main__':
    ameba_1 = OrganicCell(2)
    ameba_2 = OrganicCell(6)
    ameba_add = ameba_1 + ameba_2
    try:
        ameba_sub1 = ameba_1 - ameba_2
    except Exception as e:
        ameba_sub1 = None
        print(e)
    ameba_sub2 = ameba_2 - ameba_1
    ameba_mul = ameba_1 * ameba_2
    ameba_div = ameba_2 / ameba_1

    print('ameba_1\t', ameba_1)
    print('ameba_2\t', ameba_2)
    print('add\t\t', ameba_add)
    print('sub1\t', ameba_sub1)
    print('sub2\t', ameba_sub2)
    print('mul\t\t', ameba_mul)
    print('div\t\t', ameba_div)

    ameba_3 = OrganicCell(18)
    order_18_5 = ameba_3.make_order(5)
    print(f'\norder_18_5\n{order_18_5}')