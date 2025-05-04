from _pytest.capture import CaptureFixture

from src.filter_and_sort import (
    filter_vacancies,
    get_top_vacancies,
    get_vacancies_by_salary,
    print_vacancies,
    sort_vacancies,
)
from src.vacancies import Vacancy


def test_filter(capsys: CaptureFixture, hh_api_data: dict) -> None:
    """Функция тестирования"""
    data_filter = Vacancy.cast_to_object_list(hh_api_data["items"])
    filt_vac = filter_vacancies(data_filter, ["Перевозка"])
    assert filt_vac[0].name == "Водитель"
    vac_salary = get_vacancies_by_salary(filt_vac, "0 - 100000000")
    assert vac_salary[0].name == "Водитель"
    sort_vac = sort_vacancies(vac_salary)
    assert sort_vac[0].name == "Водитель"
    top_vac = get_top_vacancies(sort_vac, 5)
    assert top_vac[0].name == "Водитель"
    print_vacancies(top_vac)
    read_out = capsys.readouterr()
    assert read_out.out == (
        "Вакансия: Водитель, 5000000-8000000, "
        "https://hh.ru/applicant/vacancy_response?vacancyId=120004725, Перевозка "
        "грузов по указанным маршрутам. Поддержание автомобиля в исправном состоянии. "
        "Соблюдение правил дорожного движения и техники безопасности. Ведение "
        "отчетности по...\n"
    )
