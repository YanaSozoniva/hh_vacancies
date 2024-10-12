from unittest.mock import patch
from src.json_file import JsonFile
import pytest


def test_json_file_init(json_file):
    """Тестирование инициации экземпляра класса JsonFile"""
    assert json_file.file_name == r"C:\Users\user\Desktop\skyPro\hh_vacancies\data\vacancies.json"


@patch("src.json_file.json.load")
def test_read_file(mock_reader, json_file, json_data):
    """Тестирование чтения данных из json - файла"""
    mock_reader.return_value = json_data
    result = json_file.read_file()
    assert result == json_data
    mock_reader.assert_called_once()


def test_read_json_not_found_file():
    """Тестирует, если файл не найден"""
    file = JsonFile("vac.json")
    with pytest.raises(FileNotFoundError):
        file.read_file()


def test_write_file(vacan_list):
    """Тестирование добавления новых вакансий в json - файла"""
    file = JsonFile("../hh_vacancies/tests/test_vacancies.json")
    file.write_file(vacan_list)
    with open(r"C:\Users\user\Desktop\skyPro\hh_vacancies\tests\test_vacancies.json", "r+", encoding="UTF-8") as f:
        line = f.readlines()
        assert line[0:16] == ['[\n', '  {\n', '    "id": "108453823",\n', '    "premium": false,\n',
                              '    "name": "Python Backend Developer",\n', '    "department": null,\n',
                              '    "salary": {\n', '      "from": 200000,\n', '      "to": 250000,\n',
                              '      "currency": "KZT",\n', '      "gross": false\n', '    },\n',
                              '    "response_url": null,\n', '    "archived": false,\n',
                              '    "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108453823",\n',
                              '    "url": "https://api.hh.ru/vacancies/108453823?host=hh.ru",\n']

        f.truncate(0)


def test_write_file_not_found_file():
    """Тестирует, если файл не найден"""
    file = JsonFile("vac.json")
    with pytest.raises(FileNotFoundError):
        file.write_file([])
