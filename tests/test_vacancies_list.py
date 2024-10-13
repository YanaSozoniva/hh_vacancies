import pytest

from src.vacancies_list import VacanciesList


def test_vacancies_list_init(vacan_list):
    """Тестирование инициализации объекта класса VacanciesList"""
    list_vac = VacanciesList(vacan_list)
    assert len(list_vac) == 2
    assert list_vac.vacancies[1] == {
            "id": "108424453",
            "premium": False,
            "name": "Python Developer (Remote)",
            "department": None,
            "salary": None,
            "alternate_url": "https://hh.ru/vacancy/108424453",
            "relations": [],
            "snippet": {
                "requirement": "Коммерческий опыт создания веб-приложений с использованием "
                               "<highlighttext>Python</highlighttext>-фреймворков (Django, FastAPI, Flask) "
                               "от 1 года. Знание <highlighttext>Python</highlighttext> Core и встроенной...",
                "responsibility": None,
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }


def test_vacancies_list_iterator(vacan_list):
    """Тестирование работы итератора"""
    list_vac = VacanciesList(vacan_list)
    iter(list_vac)

    assert list_vac.index == 0
    assert next(list_vac)["name"] == "Python Backend Developer"
    assert next(list_vac)["name"] == "Python Developer (Remote)"
    assert list_vac.index == 2

    with pytest.raises(StopIteration):
        next(list_vac)


def test_add_vacancy(capsys, vacancy_1, vacancy_2):
    """Тестирование добавления новой вакансии в список"""
    list_vac = VacanciesList()
    list_vac.add_vacancy(vacancy_1)
    assert len(list_vac) == 1
    list_vac.add_vacancy(vacancy_2)
    assert len(list_vac) == 2
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == "Вакансия добавлена"
    assert str(list_vac[0]) == str(vacancy_1)

    list_vac.add_vacancy(vacancy_2)
    assert len(list_vac) == 2
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == "Такая вакансия уже есть"


def test_add_vacancy_other_type():
    """Тестирование попытки добавления не объекта класса Вакансия"""
    list_vac = VacanciesList()
    with pytest.raises(TypeError):
        list_vac.add_vacancy("dfgfgf")
