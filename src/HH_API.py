from abc import ABC, abstractmethod

import requests


class BaseHeadHunterAPI(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def load_vacancies(self) -> list: ...

    """ Абстрактный метод """


class HeadHunterAPI(BaseHeadHunterAPI):
    """Класс для работы с API HeadHunter"""

    LIST_ID = [
        11669695,
        2066667,
        1911403,
        4685961,
        197566,
        2300703,
        1189354,
        45124,
        9498120,
        2393,
        4437201,
        5125017,
        710,
        167893
    ]


    def __init__(self) -> None:
        """Метод для инициализации экземпляра класса"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params: dict = {"text": "", "page": 0, "per_page": 100, "employer_id": 0, "area": 113}
        self.__vacancies: list = []



    def load_vacancies(self) -> list:
        """Метод для получения списка вакансий"""


        for i in self.LIST_ID:
            self.__params["employer_id"] = i

            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            if response.status_code == 200:
                vacancies = response.json()["items"]
                self.__vacancies.extend(vacancies)



        return self.__vacancies
