import pytest

from src.vacancies import Vacancy


@pytest.fixture
def vacancy_1():
    return Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "опыт работы от 3 лет",
                   10000, 60000)


@pytest.fixture
def vacancy_2():
    return Vacancy("Python backend", "<https://hh.ru/vacancy/123489>", "Опыт от 1 года",
                   10000, 30000)

