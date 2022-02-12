# 1. Посмотреть документацию к API GitHub, разобраться как вывести список
# репозиториев для конкретного пользователя, # сохранить JSON-вывод в файле *.json.

import requests
import json

url = 'https://api.github.com'
user = 'Kakorinis'

data_rep = requests.get(f'{url}/users/{user}/repos')

with open('data.json', 'w') as f:
    json.dump(data_rep.json(), f)

for i in data_rep.json():
    print(i['name'])