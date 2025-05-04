import json
import os.path
from abc import ABC, abstractmethod

from config import ROOT_DIR
from src.vacancies import Vacancy


class BaseJson(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def _made_file(self) -> None: ...

    """Метод создания файла"""

    @abstractmethod
    def _save_file(self, data: list[dict]) -> None: ...

    """Метод сохранегия файла"""

    @abstractmethod
    def add_vacancy(self, vacancies: list[Vacancy]) -> None: ...

    """Метод добавления файла"""

    @abstractmethod
    def compare_data(self, vacancies: list[Vacancy]) -> list[Vacancy]: ...

    """Метод сравнения файла"""

    @abstractmethod
    def delete_vacancy(self, vacancy: Vacancy) -> None: ...

    """Метод удаления файла"""


class JSONSaver(BaseJson):
    """Класс для сохранения информации о вакансиях в JSON-файл"""

    def __init__(self, file_name: str = "list_vacancy.json") -> None:
        """Метод инициализации класса"""

        self.__file_name = f"{ROOT_DIR}/data/{file_name}.json"
        self.data_file: list = []
        self._made_file()

    def _made_file(self) -> None:
        """Метод создания класса"""
        if not os.path.exists(self.__file_name):
            with open(self.__file_name, "a", encoding="UTF-8"):
                pass
        else:
            with open(self.__file_name, "r", encoding="UTF-8") as f:
                self.data_file = json.load(f)

    def _save_file(self, data: list[dict]) -> None:
        """Метод сохранения класса"""
        with open(self.__file_name, "w", encoding="UTF-8") as f:
            f.write(json.dumps(data, ensure_ascii=False, indent=4))

    def add_vacancy(self, vacancies: list[Vacancy]) -> None:
        """Метод сохранения вакансий"""

        list_dict: list[Vacancy] = self.compare_data(vacancies)
        list_: list[dict] = [list_d.to_dict() for list_d in list_dict]
        self.data_file.extend(list_)
        self._save_file(self.data_file)

    def compare_data(self, vacancies: list[Vacancy]) -> list[Vacancy]:
        """Метод сравнения вакансий"""
        data = [data.get("address") for data in self.data_file]
        vacancy_list = []
        for vacancy in vacancies:
            if vacancy.address not in data:
                vacancy_list.append(vacancy)
        return vacancy_list

    def delete_vacancy(self, vacancy: Vacancy) -> None:
        """Метод удаления вакансий"""
        for index, item in enumerate(self.data_file):
            if item["address"] == vacancy.address:
                del self.data_file[index]

        self._save_file(self.data_file)
