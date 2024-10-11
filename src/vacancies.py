class Vacancy:
    """Класс для работы с вакансиями"""
    __slots__ = ('name', 'salary_from', 'salary_to', 'url', 'requirements')

    def __init__(self, name: str,  url: str, requirements: str, salary_from: int = None, salary_to: int = None):
        """Инициализация экземпляров класса Vacancy"""
        self.name = name
        if salary_from is None:
            self.salary_from = 0
        else:
            self.salary_from = salary_from
        if salary_to:
            self.salary_to = salary_to
        else:
            self.salary_to = 0
        self.url = url
        self.requirements = requirements

    def __str__(self):
        """Метод, который отображает информацию об объекте класса Vacancy для пользователей"""
        return (f"{self.name}, зарплата {self.salary_from} - {self.salary_to} руб. Требования: {self.requirements}. "
                f"Полная информация по ссылке: {self.url}")

    def __eq__(self, other):
        """Метод сравнения на равенство экземпляров класса по зарплате"""
        if type(other) is Vacancy:
            return self.salary_from == other.salary_from
        raise TypeError

    def __ne__(self, other):
        """Метод сравнения на неравенство экземпляров класса по зарплате"""
        if type(other) is Vacancy:
            return self.salary_from != other.salary_from
        raise TypeError

    def __lt__(self, other):
        """Метод сравнения на меньшее из экземпляров класса по зарплате"""
        if type(other) is Vacancy:
            return self.salary_from < other.salary_from
        raise TypeError

    def __gt__(self, other):
        """Метод сравнения на большее из экземпляров класса по зарплате"""
        if type(other) is Vacancy:
            return self.salary_from > other.salary_from
        raise TypeError
