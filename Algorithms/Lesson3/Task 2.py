"""
Допускаются любые усложения задания - валидация, подключение к БД, передача данных в файл
"""
# sqlite, postgres, db_api, orm

import hashlib


class Users:

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.password_hash = hashlib.sha256(self.login.encode() + self.password.encode()).hexdigest()
        # Users.check_user(self)

    def check_user(self):
        try:
            with open('users.txt') as users_file:
                for line in users_file:
                    user_dict = eval(line)
                    if self.login == user_dict['login']:
                        if self.password_hash == user_dict['password_hash']:
                            return print('Доступ предоставлен')
                        else:
                            return print('Неверный пароль')
                else:
                    return print(f'Пользователь {self.login} не зарегистрирован')
                # Users.add_user_to_file(self)
        except FileNotFoundError:
            with open('users.txt', 'x'):
                print(f'База данных не найдена или не создана')

    def add_user(self):
        data = {'login': self.login, 'password_hash': self.password_hash}
        try:
            with open('users.txt') as users_file:
                for line in users_file:
                    user_dict = eval(line)
                    if self.login == user_dict['login']:
                        return print(f'Пользователь {self.login} уже зарегистрирован')
                else:
                    with open('users.txt', 'a'):
                        users_file.write(f'{data}\n')
                    print(f'Пользователь {self.login} добавлен в базу')
        except FileNotFoundError:
            with open('users.txt', 'x'):
                print(f'База данных не найдена или не создана')


user_1 = Users('11111', '11111')
user_2 = Users('11111', '22222')

user_1.add_user()
user_1.check_user()
user_2.check_user()
