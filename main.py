from mitmproxy import http
import json
from functions import *

TARGET_PATH = "/v2/goods/search"

def response(flow: http.HTTPFlow):
    if TARGET_PATH in flow.request.path:
        print(f"Найден ответ на запрос к {TARGET_PATH}")
        term = f'results/{json.loads(flow.request.text).get('term', 'no_term')}.json'
        file_creator(term) #Определяем файл для сохранения ответа

        try:
            text = flow.response.text  # Получаем тело ответа как строку
            data = json.loads(text)    # Парсим JSON в dict
        except Exception as e:
            print(f"Ошибка парсинга JSON: {e}")
            data = None

        if data is not None:
            add_info(term, data) #Заносим данные в файлы
            print(f"Ответ сохранён в {term}")


