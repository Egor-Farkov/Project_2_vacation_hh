from src.vacancies import Vacancy


def filter_vacancies(vacancies_list: list[Vacancy], filter_words: list[str]) -> list[Vacancy]:
    """Метод фильтрации вакансий"""
    return [vacancies for vacancies in vacancies_list for word in filter_words if word in vacancies.description]


def get_vacancies_by_salary(filtered_vacancies: list[Vacancy], salary_range: str) -> list[Vacancy]:
    """Метод получения вакансий по зарплате"""
    salary_from, salary_to = salary_range.split("-")

    return [
        vacancy
        for vacancy in filtered_vacancies
        if vacancy.salary_from >= int(salary_from) and vacancy.salary_to <= int(salary_to)
    ]


def sort_vacancies(ranged_vacancies: list[Vacancy]) -> list[Vacancy]:
    """Метод сортировки вакансий"""
    return sorted(ranged_vacancies, key=lambda x: x.salary_to, reverse=True)


def get_top_vacancies(sorted_vacancies: list[Vacancy], top_n: int) -> list[Vacancy]:
    """Метод получения запрашиваемых вакансий"""
    return sorted_vacancies[:top_n]


def print_vacancies(top_vacancies: list[Vacancy]) -> None:
    """Метод вывода в консоль"""
    for vacancy in top_vacancies:
        print(vacancy.__str__())
