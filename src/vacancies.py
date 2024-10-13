class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = ("id", "name", "salary_from", "salary_to", "currency", "url", "requirements")

    def __init__(self, id: str, name: str, url: str, requirements: str,
                 salary_from=None, salary_to=None, currency: str = 'RUB') -> None:
        """Инициализация экземпляров класса Vacancy"""
        self.id = id
        self.name = name
        if salary_from is None:
            self.salary_from = 0
        else:
            self.salary_from = salary_from
        if salary_to:
            self.salary_to = salary_to
        else:
            self.salary_to = 0
        self.currency = currency
        self.url = url
        self.requirements = requirements

    def __str__(self) -> str:
        """Метод, который отображает информацию об объекте класса Vacancy для пользователей"""
        return (
            f"{self.name}, зарплата {self.salary_from} - {self.salary_to} {self.currency}. "
            f"Требования: {self.requirements}. Полная информация по ссылке: {self.url}"
        )

    @classmethod
    def cast_to_object_list(cls, vacancies_dict: list[dict]) -> list:
        """Метод преобразования списка словарей с вакансиями в список с объектами класса Vacancy"""
        vacancies_list = []
        for vacancy in vacancies_dict:
            id = vacancy["id"]
            name = vacancy["name"]
            url = vacancy["alternate_url"]
            requirements = vacancy["snippet"]["requirement"]
            if vacancy["salary"] is None:
                salary_from, salary_to, currency = None, None, "RUB"
            else:
                salary_from = vacancy["salary"]["from"]
                salary_to = vacancy.get("salary", {}).get("to")
                currency = vacancy["salary"]["currency"]
            vacancies_list.append(cls(id, name, url, requirements, salary_from, salary_to, currency))
        return vacancies_list

    def __eq__(self, other) -> bool:
        """Метод сравнения на равенство экземпляров класса по зарплате"""
        if type(other) is Vacancy:
            return self.salary_from == other.salary_from
        raise TypeError

    def __ne__(self, other) -> bool:
        """Метод сравнения на неравенство экземпляров класса по зарплате"""
        if type(other) is Vacancy:
            return self.salary_from != other.salary_from
        raise TypeError

    def __lt__(self, other) -> bool:
        """Метод сравнения на меньшее из экземпляров класса по зарплате"""
        if type(other) is Vacancy:
            return self.salary_from < other.salary_from
        raise TypeError

    def __gt__(self, other) -> object:
        """Метод сравнения на большее из экземпляров класса по зарплате"""
        if type(other) is Vacancy:
            return self.salary_from > other.salary_from
        raise TypeError

    def convert_to_json(self) -> dict:
        """Метод преобразования объекта класса Vacancy в словарь"""
        vacancy_dict = {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "requirements": self.requirements,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "currency": self.currency
        }
        return vacancy_dict

