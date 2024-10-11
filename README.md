# hh_vacancies

## Описание:

hh_vacancies - это приложение на Python, позволяющее получать информацию о вакансиях с платформы hh.ru в России, 
сохранять ее в файл и позволяет удобно работать с ней: добавлять, фильтровать, удалять

## Установка:

Клонируйте репозиторий:

Для SSH:
```
git@github.com:YanaSozoniva/hh_vacancies.git

```

## Запуск приложения:

Введите команду: python main.py

## Реализованные модули
### Модуль API_hh
Реализован класс, наследующийся от абстрактного класса, для работы с платформой hh.ru.
Класс умеет подключаться к API и получать вакансии.

## Тестирование
Проект покрыт unit-тестами. Для тестирования использовался фреймворк pytest. 
Для их запуска выполните команду:
```
pytest
```