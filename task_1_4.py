"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.
"""

users_data = {'Anton': {'password': '123123', 'activation': True},
              'Artem': {'password': '200089', 'activation': True},
              'Maria': {'password': 'Gke23re', 'activation': False}}


def activation(users, user_name):
    aus_decision = input(f'Учетная запись пользователя {user_name} не активна!'
                         f' Хотите активировать вашу учетную запись прямо сейчас? (да/нет)\n')
    if aus_decision.lower() == 'да':
        users[user_name]['activation'] = True
        print('Учетная запись активирована, спасибо что присоединились к нам!')
    elif aus_decision.lower() == 'нет':
        print('Не забудьте активировать учётную запись позднее!')
    else:
        print('Команда не распознана, пожалуйста введите "да" или "нет"!')
        activation(users, user_name)


"""
Функция проверяет состояние запрашиваемой учетной записи и корректность введеного пароля, после чего выводит 
приветственное обращение, либо указывает на возникшую проблему.

Алгоритм 1:
Функция принимающая вложенный словарь (nested dictionary), содержащий данные об учетных записях пользователей,
имя пользователя в качестве ключа, а также пароль и данные об активации, в виде вложенное значений. 
Кроме того проверяется значение, содержащее данные о активации. Принадлежность к заданному ключу проверяется с помощью
функции get()
Cложность: O(1).
"""


def platform_auth1(users, user_name, user_password):
    if users.get(user_name):                                                                          # O(1)
        if users[user_name]['password'] == user_password and users[user_name]['activation']:          # O(1)
            return 'Добро пожаловать!'                                                                # O(1)
        elif users[user_name]['password'] != user_password:                                           # O(1)
            return 'Пароль не верный'                                                                 # O(1)
        elif users[user_name]['password'] == user_password and not users[user_name]['activation']:    # O(1)
            activation(users, user_name)                                                              # O(1)
    return 'Данного пользователя не существует'                                                       # O(1)


"""
Функция проверяет состояние запрашиваемой учетной записи и корректность введеного пароля, после чего выводит 
приветственное обращение, либо указывает на возникшую проблему.

Алгоритм 2: 
Алгоритм аналогичен первому, но для выявления нужно пары ключ-значение используется цикл for. В отличие от функции
get(), имеющей сложность O(1), подобный перебор имеет сложность O(N), поэтому в данном случае предпочтительнее 
использовать первый алгоритм.

Сложность: O(N).
"""


def platform_auth2(users, user_name, user_password):
    for key, value in users.items():                                                # O(N)
        if key == user_name:                                                        # O(1)
            if value['password'] == user_password and value['activation']:          # O(1)
                return 'Добро пожаловать!'                                          # O(1)
            elif value['password'] != user_password:                                # O(1)
                return 'Пароль не верный'                                           # O(1)
            elif value['password'] == user_password and not value['activation']:    # O(1)
                activation()                                                        # O(1)
    return 'Данного пользователя не существует'                                     # O(1)


print(platform_auth1(users_data, 'Maria', 'Gke23re'))
print(platform_auth1(users_data, 'Maria', 'Gke2311'))

print(platform_auth2(users_data, 'Anton', '123123'))
print(platform_auth2(users_data, 'Anton', '123155'))
