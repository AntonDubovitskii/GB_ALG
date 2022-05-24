"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""

import hashlib
from uuid import uuid4

web_cash = {}


def cash_check(cash, web_url, salt='some_salt'):
    if cash.get(web_url, None):
        return cash[web_url]
    else:
        cash[web_url] = hashlib.sha512(salt.encode('utf-8') + web_url.encode('utf-8')).hexdigest()
        return f'Кэш страницы {web_url} добавлен, её хэш: {cash[web_url]}'


if __name__ == '__main__':
    print(cash_check(web_cash, 'yandex.ru', salt=uuid4().hex))
    print(cash_check(web_cash, 'mail.ru', salt=uuid4().hex))

    print()
    print(cash_check(web_cash, 'mail.ru'))

