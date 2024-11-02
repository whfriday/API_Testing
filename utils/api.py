import os
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Путь к директории проекта

import sys
sys.path.append(project_dir)
# Путь для импорта файлов проекта

from utils.helper_methods import Http_Methods
from utils.checking import Checking

class Star_Wars_API:
    """Методы для тестирования SWAPI"""

    base_url = "https://swapi.dev/api/"  # базовая url

    @staticmethod
    def get_DV_info():
        """Получение информации о Дарте Вейдере"""

        get_resourse = "people/4/"
        get_url = Star_Wars_API.base_url + get_resourse
        print(get_url)
        result_get = Http_Methods.get_request(url=get_url)
        return result_get

    @staticmethod
    def get_film_with_people_info(url):
        """Получение информации о фильмах с участием 'people/4/' """

        get_url = url
        print(get_url)
        result_get = Http_Methods.get_request(url=get_url)
        return result_get
    
    @staticmethod
    def get_character_info(url):
        """Получение информации о персонаже"""

        get_url = url
        result_get = Http_Methods.get_request(url=get_url)
        return result_get

    @staticmethod
    def get_character_set(films):
        """Получение информации о фильме"""

        #создание пустого множества имён персонажей; необходимо для уникальности имён персонажей в файле
        Star_Wars_API.characters_set = set()
        # пробегаем по всем элементам полученного списка фильмов с участием DV
        for i in films:
            print(f"\nПолучение информации о фильме #{i[-2]}")
            result_get_info_film = Star_Wars_API.get_film_with_people_info(i)
            Checking.check_status_code(result=result_get_info_film, status_code=200)
            Checking.check_json_token(result=result_get_info_film, expected_value=['title', 'episode_id', 'opening_crawl', 'director', 'producer', 'release_date', 'characters', 'planets', 'starships', 'vehicles', 'species', 'created', 'edited', 'url'])
            check_film_info = result_get_info_film.json()
            characters_http_list = check_film_info.get("characters")  # получение списка персонажей в фильме

            print(f"\nПолучение информации о персонажах фильма #{i[-2]}")

            # пробегаем по всем элементам списка "characters_http_list"
            for k in characters_http_list:
                result_get_characters = Star_Wars_API.get_character_info(k)
                Checking.check_status_code(result=result_get_characters, status_code=200)
                Checking.check_json_token(result=result_get_characters, expected_value=['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url'])
                check_characters_info = result_get_characters.json()
                character_name = check_characters_info.get("name")  # получение имени персонажа
                Star_Wars_API.characters_set.add(character_name)  # занесение имени во множество
        return Star_Wars_API.characters_set