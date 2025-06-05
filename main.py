# Создание экземпляра класса для работы с API сайтов с вакансиями
import os

from src.Manager import DBManager
from src.filter_and_sort import (
    filter_vacancies,
    get_top_vacancies,
    get_vacancies_by_salary,
    print_vacancies,
    sort_vacancies,
)
from src.HH_API import HeadHunterAPI
from src.vacancies import Vacancy
from dotenv import load_dotenv

class_for_key_word = HeadHunterAPI()

load_dotenv()
con = DBManager(
    database=os.getenv("DTBASE_NAME"),
    password=os.getenv("DTBASE_PASSWORD"),
    user=os.getenv("DTBASE_USER"),
    host=os.getenv("DTBASE_HOST"),
    port=os.getenv("DTBASE_PORT")
)


# Функция для взаимодействия с пользователем
def user_interaction() -> None:
    """Функция взаимодействия с пользователем"""

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000
    keyword = class_for_key_word.load_vacancies()
    vacancies_list = Vacancy.cast_to_object_list(keyword)
    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    keyword = class_for_key_word.load_vacancies()
    vacancies_list = Vacancy.cast_to_object_list(keyword)
    print(vacancies_list)
    con.create_db()
    con.connect_db()
    con.create_table()
    con.insert(vacancies_list)
    print(con.get_companies_and_vacancies_count())
    print(con.get_all_vacancies())
    print(con.get_avg_salary())
    print(con.get_vacancies_with_higher_salary())
    print(con.get_vacancies_with_keyword(""))
