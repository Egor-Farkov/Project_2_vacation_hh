# Создание экземпляра класса для работы с API сайтов с вакансиями
from src.filter_and_sort import (
    filter_vacancies,
    get_top_vacancies,
    get_vacancies_by_salary,
    print_vacancies,
    sort_vacancies,
)
from src.HH_API import HeadHunterAPI
from src.vacancies import Vacancy


# Функция для взаимодействия с пользователем
def user_interaction() -> None:
    """Функция взаимодействия с пользователем"""

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000
    class_for_key_word = HeadHunterAPI()
    keyword = class_for_key_word.load_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(keyword)
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
