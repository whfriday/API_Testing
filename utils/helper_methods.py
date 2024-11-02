import os
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Путь к директории проекта

import sys
sys.path.append(project_dir)
# Путь для импорта файлов проекта

import requests
from utils.logger import Logger
import allure

class Http_Methods():
    """Класс для отправки запросов"""

    headers = {'Content-Type' : 'application/json'}     #заголовки проекта
    cookies = ""        #куки проекта

    @staticmethod
    def get_request(url):
        """Отправка GET запроса"""

        with allure.step("GET"):
            Logger.add_request(url, method='GET')
            result = requests.get(url=url, headers=Http_Methods.headers, cookies=Http_Methods.cookies)
            Logger.add_response(result)
            return result
    
class File_Working():
    """Класс для работы с файлами"""

    @staticmethod
    def append_to_file(massive):
        """Запись в файл массива персонажей построчно"""

        with allure.step("Write to file"):
            with open(f"{project_dir}\\files\\characters.txt", "a", encoding="utf-8") as file:  # Открытие файла в режиме добавления
                print(*massive, file=file, sep="\n")