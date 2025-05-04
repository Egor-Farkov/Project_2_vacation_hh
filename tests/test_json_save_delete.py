import os.path

from config import ROOT_DIR
from src.json_save_delete import JSONSaver
from src.vacancies import Vacancy


def test_json_file(hh_api_data: dict) -> None:
    """Тест"""
    if os.path.exists(f"{ROOT_DIR}/data/test_data.json"):
        os.remove(f"{ROOT_DIR}/data/test_data.json")
    vacancies = Vacancy.cast_to_object_list(hh_api_data["items"])
    data_file = JSONSaver("test_data")
    assert isinstance(data_file, JSONSaver)
    data_file.add_vacancy(vacancies)
    data_file.add_vacancy(vacancies)


def test_delete_file(hh_api_data: dict) -> None:
    """Тест"""
    vacancies = Vacancy.cast_to_object_list(hh_api_data["items"])
    data_file = JSONSaver("test_data")
    data_file.delete_vacancy(vacancies[0])
