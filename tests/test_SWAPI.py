import os
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Путь к директории проекта

import sys
sys.path.append(project_dir)
# Путь для импорта файлов проекта

# import json
from utils.api import Star_Wars_API
from utils.helper_methods import File_Working
from utils.checking import Checking
import allure

@allure.epic("Получение списка персонажей в фильмах с участием другого персонажа")
class Test_Get_Сharacters_List:
    """Тест по получению списка персонажей"""

    @allure.description("Получение списка персонажей, присутствующих в фильмах с Дартом Вейдером")
    def test_characters_with_DV(self):
        """Тест по получению списка персонажей, присутствующих в фильмах с Дартом Вейдером"""

        print("\nПолучение информации о DV - метод GET")
        result_get_info_DV = Star_Wars_API.get_DV_info()
        check_DV_info = result_get_info_DV.json()
        films_http_list = check_DV_info.get("films")  #получение списка фильмов с участием DV
        Checking.check_status_code(result=result_get_info_DV, status_code=200)
        Checking.check_json_token(result=result_get_info_DV, expected_value=['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld', 'films', 'species', 'vehicles', 'starships', 'created', 'edited', 'url'])
        
        print("Фильмы с участием DV:")
        print(*films_http_list, sep=", ")

        print("\nПолучение информации о фильмах с участием DV - метод GET")
        #Получение информации о фильме и о каждом персонаже из него с последующим занесением их во множество
        Star_Wars_API.get_character_set(films_http_list) 
                     
        # создание списка из множества персонажей и сортировка их в алфавитном порядке
        characters_name_list = list(Star_Wars_API.characters_set)
        new_chacters_list = sorted(characters_name_list)

        # запись в файл отсортированного списка
        File_Working.append_to_file(massive=new_chacters_list)

        print('Тестирование на персонажей в фильмах с DV выполнен успешно!')
        
