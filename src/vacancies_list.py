from src.vacancies import Vacancy


class VacanciesList:
    """Класс для работы со списком вакансий"""
    __slots__ = ("__vacancies", "index")

    def __init__(self, vacancies: list = None) -> None:
        """Конструктор для инициализации экземпляра класса."""
        if vacancies is None:
            self.__vacancies = []
        else:
            self.__vacancies = vacancies
        self.index = 0

    @property
    def vacancies(self):
        """Геттер для корректного вывода списка вакансий"""
        return self.__vacancies

    def __len__(self):
        """Метод для подсчета количества вакансий в списке"""
        return len(self.__vacancies)

    def __iter__(self):
        """Возвращает итератор."""
        self.index = 0
        return self

    def __next__(self):
        """Возвращает следующую вакансию из списка вакансий"""
        if self.index < len(self.__vacancies):
            vacancy = self.__vacancies[self.index]
            self.index += 1
            return vacancy
        else:
            raise StopIteration

    def __getitem__(self, item):
        """Возвращает вакансию из списка по указанному индексу"""
        return self.__vacancies[item]

    def add_vacancy(self, vacancy: Vacancy):
        """Метод для добавления вакансии в список"""
        if isinstance(vacancy, Vacancy):
            try:
                if vacancy.id in (vac.id for vac in self.__vacancies):
                    raise ValueError("Такая вакансия уже есть")
            except ValueError:
                print("Такая вакансия уже есть")
            else:
                self.__vacancies.append(vacancy)
                print("Вакансия добавлена")
        else:
            raise TypeError
