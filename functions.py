import json
import os

def file_creator(name: str) -> None:
    '''Если файла по такому запросу не существует, мы его создадим'''
    if not os.path.isfile(name):
        with open(name, 'w', encoding='utf-8') as f:
            json.dump({'items': []}, f)

def add_info(name: str, data: dict) -> None:
    '''Заносим данные в файл запроса'''
    with open(name, 'r', encoding='utf-8') as f:
        saved = json.loads(f.read()) #достаем dict объект из файла запроса
        data = data['items']
        for item in data: #фильтруем полученные данные и закидываем их в dict
            str_price = str(item['price'])
            str_r_price = str(item['promotion']['oldPrice'])
            saved['items'].append({'id': item['id'],
                                   'name': item['name'],
                                   'price': str_price[:-2] + '.' + str_price[-2:],
                                   'regular_price': str_r_price[:-2] + '.' + str_r_price[-2:],
                                   'seoCode': item['seoCode']})

    with open(name, 'w', encoding='utf-8') as f: #записываем обновленный dict обратно в файл
        json.dump(saved, f, ensure_ascii=False, indent=2)
