import json

#проверка на количество полученных товаров
with open("results/кофе.json", "r", encoding="utf-8") as f:
    saved = json.loads(f.read())
    print(len(saved['items']))