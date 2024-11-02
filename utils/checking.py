


class Checking:
    """Методы для проверки ответов запросов"""

    @staticmethod
    def check_status_code(result, status_code):
        """Метод для проверки статус кода"""

        assert status_code == result.status_code, "ОШИБКА, Статус-код не совпадает"
        print(f"Успешно! Статус код = {result.status_code}")

    @staticmethod
    def check_json_token(result, expected_value):
        """Метод для проверки наличия полей в ответе запроса"""

        fields = result.json()     #преобразование ответа в json формат
        assert list(fields) == expected_value, "ОШИБКА, Такого поля в ответе нет"
        print("Все обязательные поля присутствуют!")

    @staticmethod
    def check_json_value(result, field_name, expected_value):
        """Метод для проверки значений обязательных полей в ответе запроса"""

        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, "ОШИБКА, Поле не содержит ожидаемое значение"
        print(f"Поле {field_name} содержит {expected_value}!")

    @staticmethod
    def check_json_search_word_value(result, field_name, search_word):
        """Метод для проверки значений обязательных полей в ответе запроса по заданному слову"""

        check = result.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print(f"Слово {search_word} присутствует в поле {field_name}!")
        else:
            print(f"Слово {search_word} отсутствует в поле {field_name}(")