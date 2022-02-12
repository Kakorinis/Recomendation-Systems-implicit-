# 2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis).
# Найти среди них любое, требующее авторизацию (любого типа).
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

import requests
import json

# Из приложенного к уроку ресурсу сборника сайтов с api взфл амазон и box.com.
# На амазоне не понятно как искать api, пришлось работь в боксом. С ним тоже непонятно

# 1-ый способ (взят из документации с сайта https://developer.box.com/reference/get-authorize/)
# pip install boxsdk
# модуль установился, но почему-то пайтон его не видит и выдает ошибку
from boxsdk import OAuth2

oauth = OAuth2(
    client_id='18566248728',
    client_secret='42nYNA8puKBUqDQ',
    store_tokens=your_store_tokens_callback_method,
)

auth_url, csrf_token = oauth.get_authorization_url('http://YOUR_REDIRECT_URL')

# Redirect user to auth_url, where they will enter their Box credentials

# 2-ой способ (пример с урока)
service = 'https://developer.box.com/reference/'
token = '42nYNA8puKBUqDQ'

req = requests.get(f'{service} {token}')
data = json.loads(req.text)
print(data)