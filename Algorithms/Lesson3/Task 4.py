""" ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации
"""

import hashlib

hash_history = set()


def hash_create(url):
    salt = str(url)[::-1]
    url_hash = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
    if url_hash in hash_history:
        return 'Данная страница была захеширована ранее'
    else:
        hash_history.add(url_hash)
        return 'Данная страница захеширована'


print(hash_create("https://gb.ru/education"))
print(hash_create("https://gb.ru/education"))
