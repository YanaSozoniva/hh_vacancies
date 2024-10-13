import json
import os
from typing import Any

# from src.API_hh import HeadHunterAPI
from src.worked_file import WorkedFile


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

    def read_file(self) -> list[Any]:
        """Метод для чтения данных из json-файла"""
        if self.__is_exists_file():
            full_path = os.path.abspath(self.__file_name)
            with open(full_path, "r", encoding="UTF-8") as json_file:
                try:
                    data = json.load(json_file)
                except Exception as e:
                    print(f"Произошла ошибка {e}")
                    data = []
            return data

    def write_file(self, vacancy: list[dict]) -> None:
        """Метод для добавления данных в файл"""
        if self.__is_exists_file():
            full_path = os.path.abspath(self.__file_name)
            vacan_data = self.read_file()

            for vacancy_add in vacancy:
                if vacancy_add not in vacan_data:
                    vacan_data.append(vacancy_add)

            with open(full_path, "r+", encoding="UTF-8") as json_file:
                json.dump(vacan_data, json_file, indent=2, ensure_ascii=False)

    def delete_info_from_file(self, vacancy_del: dict) -> None:
        """Метод для удаления данных из файла"""
        if self.__is_exists_file():
            full_path = os.path.abspath(self.__file_name)
            vacan_data = self.read_file()
            try:
                vacan_data.remove(vacancy_del)
            except ValueError:
                print("Вакансия не была удалена, т.к. она не была найдена")
            else:
                with open(full_path, "w", encoding="UTF-8") as json_file:
                    json.dump(vacan_data, json_file, indent=2, ensure_ascii=False)
                print("Вакансия удалена из файла")


# if __name__ == '__main__':
#     file = JsonFile("../data/vacancies.json")
#
#     vacancies = HeadHunterAPI()
#     # file.write_file(vacancies.get_vacancies('python'))
#     data_json = file.read_file()
#     vac = {'id': '108424453', 'premium': False, 'name': 'Python Developer (Remote)',
#     'department': None, 'has_test': False, 'response_letter_required': False,
#     'area': {'id': '2759', 'name': 'Ташкент', 'url': 'https://api.hh.ru/areas/2759'},
#     'salary': None, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': None,
#     'response_url': None, 'sort_point_distance': None, 'published_at': '2024-10-09T16:20:22+0300',
#     'created_at': '2024-10-09T16:20:22+0300', 'archived': False,
#     'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=108424453',
#     'show_logo_in_search': None, 'insider_interview': None,
#     'url': 'https://api.hh.ru/vacancies/108424453?host=hh.ru',
#     'alternate_url': 'https://hh.ru/vacancy/108424453', 'relations': [],
#     'employer': {'id': '5674346', 'name': 'УайтСнейк',
#     'url': 'https://api.hh.ru/employers/5674346', 'alternate_url': 'https://hh.ru/employer/5674346',
#     'logo_urls': {'original': 'https://img.hhcdn.ru/employer-logo-original/923495.png',
#     '240': 'https://img.hhcdn.ru/employer-logo/4134541.png',
#     '90': 'https://img.hhcdn.ru/employer-logo/4134540.png'},
#     'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=5674346',
#     'accredited_it_employer': False, 'trusted': True},
#     'snippet': {'requirement': 'Коммерческий опыт создания веб-приложений с использованием
#     <highlighttext>Python</highlighttext>-фреймворков (Django, FastAPI, Flask) от 1 года.
#     Знание <highlighttext>Python</highlighttext> Core и встроенной...', 'responsibility': None},
#     'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [],
#     'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': False,
#     'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}],
#     'accept_incomplete_resumes': False, 'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
#     'employment': {'id': 'full', 'name': 'Полная занятость'},
#     'adv_response_url': None, 'is_adv_vacancy': False, 'adv_context': None}
#
#     print(vac)
#     file.delete_info_from_file(vac)
