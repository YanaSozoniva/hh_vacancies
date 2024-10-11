from src.vacancies import Vacancy
import pytest


def test_vacancies_init(vacancy_1):
    """Тестирование корректности инициализации объектов класса Vacancies"""
    assert vacancy_1.name == "Python Developer"
    assert vacancy_1.url == "<https://hh.ru/vacancy/123456>"
    assert vacancy_1.requirements == "опыт работы от 3 лет"
    assert vacancy_1.salary_from == 10000
    assert vacancy_1.salary_to == 60000


def test_vacancies_init_salary_zero():
    """Тестирование корректности инициализации объектов класса Vacancies c неуказанной зарплатой"""
    vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "опыт работы от 3 лет")
    assert vacancy.name == "Python Developer"
    assert vacancy.url == "<https://hh.ru/vacancy/123456>"
    assert vacancy.requirements == "опыт работы от 3 лет"
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0


def test_vacancies_str(vacancy_1):
    """Тестирование магического метода str"""
    assert str(vacancy_1) == ("Python Developer, зарплата 10000 - 60000 руб. Требования: опыт работы от 3 лет. "
                              "Полная информация по ссылке: <https://hh.ru/vacancy/123456>")


def test_equality_vacancies_other_type(vacancy_1):
    """Тестирование сравнения экземпляра класса Вакансия с другим типом"""
    with pytest.raises(TypeError):
        vacancy_1 == 10000


def test_equality_vacancies(vacancy_1, vacancy_2):
    """Тестирование сравнения на равенство по зарплате"""
    assert vacancy_1 == vacancy_2


def test_not_equality_vacancies(vacancy_1):
    """Тестирование сравнения на неравенство по зарплате"""
    vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "опыт работы от 3 лет")
    assert vacancy_1 != vacancy


def test_less_vacancies(vacancy_1):
    """Тестирование сравнения на меньшее"""
    vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "опыт работы от 3 лет")
    assert vacancy < vacancy_1


def test_more_vacancies(vacancy_1):
    """Тестирование сравнения на большее"""
    vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "опыт работы от 3 лет")
    assert vacancy_1 > vacancy
