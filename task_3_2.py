"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш
Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей
ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""

import hashlib
import sqlite3


def add_data(log, passwd):
    """
    Добавление записей в бд.
    """
    conn = sqlite3.connect('task_3_2_db.sqlite')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO accounts (login, password_hash) VALUES ('{log}', '{passwd}')")
    conn.commit()
    conn.close()


def get_data(user_login):
    """
    Получение записи из бд по логину
    """
    conn = sqlite3.connect('task_3_2_db.sqlite')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM accounts WHERE login='{user_login}'")

    id, login, password_hash = cursor.fetchone()

    conn.close()
    return id, login, password_hash


def remove_data(user_login):
    """
    Удаление записи по логину. В данном случае не используется, просто для тренировки :)
    """
    conn = sqlite3.connect('task_3_2_db.sqlite')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM accounts WHERE login='{user_login}'")
    conn.commit()
    print(f'Запись пользователя {user_login} успешно удалена!')
    conn.close()


def registration():
    entered_login = (input('Введите логин для регистрации: \n'))
    try:
        if get_data(entered_login):
            print('Учетная запись уже существует!')
            return
    except TypeError:
        entered_password = (input('Введите пароль: \n'))
        password_hash = hashlib.sha256(entered_login.encode('utf-8') + entered_password.encode('utf-8')).hexdigest()
        add_data(entered_login, password_hash)
        print(f'В базу данных добавлена запись: {get_data(entered_login)}')


def login_in():
    try:
        entered_login = input('Пожалуйста введите логин для входа: \n')
        entered_password = input('Пожалуйста введите пароль: \n')
        entered_password_hash = hashlib.sha256(entered_login.encode('utf-8') +
                                               entered_password.encode('utf-8')).hexdigest()
        id, login, password = get_data(entered_login)
    except TypeError:
        command = input('Пользователь с данным сочетанием логина и пароля не зарегистрирован! '
                        'Хотите попытаться ввести еще раз? (Да/Нет): \n').lower()
        if command == 'да':
            return login_in()
        else:
            return

    if pass_check(entered_password_hash, password):
        print('Добро пожаловать!')
        return
    else:
        print('Попробуйте в другой раз!')


def pass_check(pass1, pass2):
    print(f'Хэш введенного пароля: {pass1}')
    print(f'Хэш пароля хранящийся в бд: {pass2}')
    if pass1 == pass2:
        return True
    else:
        command = input('Пароль не верен! Хотите попытаться ввести еще раз? (Да/Нет): \n').lower()
        if command == 'да':
            return pass_check(pass1, pass2)
        elif command == 'нет':
            return
        else:
            print('Команда не распознана! Пожалуйста введите "да" или "нет"')
            return pass_check(pass1, pass2)


if __name__ == '__main__':
    registration()
    """
    Введите логин: 
    TestUser
    Введите пароль: 
    123123
    В базу данных добавлена запись: (25, 'TestUser', '7097b9e3d6ed657f5757daf78a08a7a27673dc5aa6482a6e8742fc99766ef8bc')
    """
    login_in()
    """
    Пожалуйста введите логин: 
    TestUser
    Пожалуйста введите пароль: 
    123123
    7097b9e3d6ed657f5757daf78a08a7a27673dc5aa6482a6e8742fc99766ef8bc
    7097b9e3d6ed657f5757daf78a08a7a27673dc5aa6482a6e8742fc99766ef8bc
    Добро пожаловать!
    """

