import json
import os
from typing import Any

from src.worked_file import WorkedFile
from src.API_hh import HeadHunterAPI


class JsonFile(WorkedFile):
    """Класс для работы с JSON-файлами"""

    __file_name: str

    def __init__(self, file_name: str = "vacancies.json") -> None:
        """Инициация экземпляров класса JsonFile"""
        self.__file_name = file_name

    @property
    def file_name(self) -> str:
        """Геттер для просмотра пути файла"""
        return self.__file_name

    def __is_exists_file(self) -> bool:
        if os.path.exists(self.__file_name):
            return True
        raise FileNotFoundError("Файл не найден")

    def read_file(self) -> dict[Any, Any] | str:
        """Метод для чтения данных из json-файла"""
        if self.__is_exists_file():
            full_path = os.path.abspath(self.__file_name)
            with open(full_path, "r", encoding="UTF-8") as json_file:

                data = json.load(json_file)

            return data

    def write_file(self, vacancy: list[dict]) -> None:
        """Метод для добавления данных в файл"""
        if self.__is_exists_file():
            full_path = os.path.abspath(self.__file_name)

            with open(full_path, "r+", encoding="UTF-8") as json_file:

                json_file.seek(0, 2)
                json.dump(vacancy, json_file, indent=2, ensure_ascii=False)
                json_file.seek(0)
                lines = json_file.readlines()
                json_file.seek(0)
                for line in lines[0:-1]:
                    if line == '][\n':
                        line = ',\n'
                    json_file.write(line)
                json_file.seek(0)

    def delete_info_from_file(self, vacancy: dict) -> None:
        """Метод для удаления данных из файла"""

        pass


if __name__ == '__main__':
    file = JsonFile("../data/vacancies.json")

    vacancies = HeadHunterAPI()
    file.write_file(vacancies.get_vacancies('python'))
    data_json = file.read_file()
    # print(data_json)
