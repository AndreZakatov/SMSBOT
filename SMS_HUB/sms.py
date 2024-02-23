import requests

API_KEY = "208493U8da1100128d7f6fc6df5caa19c375224"
SERVICE = input('Сервис: ')
OPERATOR = input('Оператор: ')
COUNTRY = input('Страна: ')
MAXPRICE = input('Цена: ')

url = f'https://smshub.org/stubs/handler_api.php?api_key={API_KEY}&action=getNumbersStatus&country={COUNTRY}&operator={OPERATOR}'


response = requests.get(url)

# Обработка ответа
if response.status_code == 200:
    result = response.text
    if result == "NO_NUMBERS":
        print("Нет доступных номеров. Попробуйте позже или измените параметры.")
    elif result == "NO_BALANCE":
        print("Закончились деньги на API-ключе.")
    elif result == "API_KEY_NOT_VALID":
        print("Невалидный статус API-ключа.")
    elif result == "WRONG_SERVICE":
        print("Неверный идентификатор сервиса.")
    elif result.startswith("ACCESS_NUMBER"):
        # Разбор ответа в случае успешной покупки номера
        activation_info = result.split(":")
        activation_id = activation_info[1]
        phone_number = activation_info[2]
        print(f"Получен номер {phone_number} с ID активации {activation_id}.")
else:
    print(f"Ошибка при выполнении запроса. Код ответа: {response.status_code}")
    print(response.text)
