""" допускается комб-е - цикл и рекурсия
"""



def ascii_table(chr_num=32, symbol_str="", i=0):
    """
    Так как в условии задачи не сказано, диапазон выводимых символов может меняться, то значения начального и конечного
    символов заданы в самой функции.
    """
    if chr_num == 128:
        return print(symbol_str)
    symbol_str += f"{chr_num} - {chr(chr_num)}\t "
    i += 1
    if i // 10 == 1:
        symbol_str += "\n"
        i = 0
    chr_num += 1
    ascii_table(chr_num, symbol_str, i)


ascii_table()