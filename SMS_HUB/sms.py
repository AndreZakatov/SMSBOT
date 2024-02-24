import requests

API_KEY = '208493Ub764004feff56815610891d0d5717678'
COUNTRY = ''
OPERATOR = ''
SERVICE = ''
MAXPRICE = int()
STATUS_CODE = int()
ID = ''

# Обязательный параметр API_KEY
get_number_status = f'https://smshub.org/stubs/handler_api.php?api_key={API_KEY}&action=getNumbersStatus&' \
                    f'country={COUNTRY}&operator={OPERATOR}'

# Обязательный параметр API_KEY
url = f'https://smshub.org/stubs/handler_api.php?api_key={API_KEY}&action=getNumbersStatus&' \
      f'country={COUNTRY}&operator={OPERATOR}'

# Обязательный параметр API_KEY
get_balance = f'https://smshub.org/stubs/handler_api.php?api_key={API_KEY}&action=getBalance'

# Обязательный параметр API_KEY, SERVICE,
get_number = f'https://smshub.org/stubs/handler_api.php?api_key={API_KEY}' \
             f'&action=getNumber' \
             f'&service={SERVICE}' \
             f'&operator={OPERATOR}' \
             f'&country={COUNTRY}' \
             f'&maxPrice={MAXPRICE}'

# Изменить статус, все параметры обязательны
set_status = f'https://smshub.org/stubs/handler_api.php?api_key={API_KEY}&' \
                f'action=setStatus&status={STATUS_CODE}&id={ID}'

# Получить статус, все поля обязательные
get_status = f'https://smshub.org/stubs/handler_api.php?api_key={API_KEY}&action=getStatus&id={ID}'

# Получение списка цен
get_price = f'https://smshub.org/stubs/handler_api.php?api_key={API_KEY}' \
            f'&action=getPrices' \
            f'&service={SERVICE}' \
            f'&country={COUNTRY}'

try:
    response = requests.get(url)
    response.raise_for_status()  # Проверка наличия ошибок в ответе
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Ошибка запроса: {e}")
