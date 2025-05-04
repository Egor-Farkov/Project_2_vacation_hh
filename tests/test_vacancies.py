import pytest

from src.vacancies import Vacancy


def test_vacancy(hh_api_data: dict) -> None:
    """Функция тестирования"""
    vacancy = Vacancy(
        name="Java разработчик (Java+SpringBoot+Kotlin)",
        address="https://hh.ru/applicant/vacancy_response?vacancyId=119867664",
        experience="От 3 до 6 лет",
        salary_from=200000,
        salary_to=200000,
        description={},
    )

    assert isinstance(vacancy, Vacancy)
    vacancy_data = Vacancy.cast_to_object_list(hh_api_data["items"])

    assert vacancy_data[0].name == "Водитель"

    assert vacancy.to_dict()["name"] == vacancy.name
    assert isinstance(vacancy.__str__(), str)
    assert isinstance(vacancy.__repr__(), str)
    with pytest.raises(ValueError):
        Vacancy(
            name="",
            address="https://hh.ru/applicant/vacancy_response?vacancyId=119867664",
            experience="От 3 до 6 лет",
            salary_from=200000,
            salary_to=200000,
            description={},
        )
    with pytest.raises(ValueError):
        Vacancy(
            name="Java разработчик (Java+SpringBoot+Kotlin)",
            address="",
            experience="От 3 до 6 лет",
            salary_from=200000,
            salary_to=200000,
            description={},
        )
    with pytest.raises(ValueError):
        Vacancy(
            name="Java разработчик (Java+SpringBoot+Kotlin)",
            address="https://hh.ru/applicant/vacancy_response?vacancyId=119867664",
            experience="",
            salary_from=200000,
            salary_to=200000,
            description={},
        )

    Vacancy(
        name="Java разработчик (Java+SpringBoot+Kotlin)",
        address="https://hh.ru/applicant/vacancy_response?vacancyId=119867664",
        experience="От 3 до 6 лет",
        salary_from=-1,
        salary_to=-1,
        description={},
    )
