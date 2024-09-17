import json


def check_for_ID():
    with open('users.json', 'r') as file:
        users = json.load(file)
        print("ALL USERS NAMES ARE:")
        for user in users:
            print(user['name'])

    user_id = input("\nВведите ID пользователя: ")

    user_found = False
    for user in users:
        if str(user['id']) == user_id:
            user_found = True
            print("\nПодробная информация о пользователе:")
            print(f"ID: {user['id']}")
            print(f"Имя: {user['name']}")
            print(f"Имя пользователя: {user['username']}")
            print(f"Email: {user['email']}")
            print("Адрес:")
            print(f"  Улица: {user['address']['street']}")
            print(f"  Квартира: {user['address']['suite']}")
            print(f"  Город: {user['address']['city']}")
            print(f"  Почтовый индекс: {user['address']['zipcode']}")
            print("Компания:")
            print(f"  Название: {user['company']['name']}")
            print(f"  Слоган: {user['company']['catchPhrase']}")
            print(f"  Бизнес: {user['company']['bs']}")
            break

    if not user_found:
        print(f"The user with ID {user_id} is not found!")
    return
