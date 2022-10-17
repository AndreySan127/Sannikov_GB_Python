 #hash?


def count_substrings(u_str):
    rez_set = set()
    for i in range(len(u_str)):
        for j in range(i + 1, len(u_str) + 1):
            rez_set.add(hash(u_str[i:j]))
            print(f'{u_str[i:j]}, ', end='')
    rez_set.remove(hash(u_str[:len(u_str)]))
    return len(rez_set)


user_str = 'zxxxx'
print(f'\nВ строке "{user_str}" содержится {count_substrings(user_str)} уникальных подстрок')