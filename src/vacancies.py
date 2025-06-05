import f


class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = (
        "name",
        "address",
        "salary_from",
        "salary_to",
        "description",
        "company_id",
        "company_name",
        "vacancy_id"
    )

    def __init__(
        self,
        name: str,
        address: str,
        salary_from: int,
        salary_to: int,
        description: str,
        company_id: str,
        company_name: str,
        vacancy_id: str
    ) -> None:
        """Метод для инициализации экземпляра класса"""
        self.name = Vacancy._validate_name(name)
        self.address = Vacancy._validate_address(address)
        self.salary_from = Vacancy._validate_salary_from(salary_from)
        self.salary_to = Vacancy._validate_salary_to(salary_to)
        self.description = Vacancy._validate_description(description)
        self.company_id = Vacancy._validate_company_id(company_id)
        self.company_name = Vacancy._validate_company_name(company_name)
        self.vacancy_id = Vacancy._validate_vacancy_id(vacancy_id)


    @classmethod
    def cast_to_object_list(cls, dirty_list_vacations: list) -> list:
        """Метод инициализации объектов вакансий"""
        clear_list_vacations = []
        for item in dirty_list_vacations:
            name = f.ichain(item, "name") or "Not name"
            address = f.ichain(item, "apply_alternate_url") or "Not address"
            salary_from = f.ichain(item, "salary_range", "from") or 0
            salary_to = f.ichain(item, "salary_range", "to") or 0
            description = f.ichain(item, "snippet", "requirement") or "Not description"
            company_id = f.ichain(item, "employer", "id") or "Not company id"
            company_name = f.ichain(item, "employer", "name") or "Not company name"
            vacancy_id = f.ichain(item, "id") or "Not vacancy"


            clear_list_vacations.append(
                cls(
                    name,
                    address,
                    salary_from,
                    salary_to,
                    description,
                    company_id,
                    company_name,
                    vacancy_id
                )
            )

        return clear_list_vacations

    def __repr__(self) -> str:
        """Метод переопределения магического метода"""
        return f"{self.__class__.__name__}('{self.salary_from}-{self.salary_to}')"

    def __str__(self) -> str:
        """Метод переопределения магического метода"""
        return f"Вакансия: {self.name}, {self.salary_from}-{self.salary_to}, {self.address}, {self.description}"

    @staticmethod
    def _validate_name(name: str) -> str:
        """Метод валидации по имени"""
        if isinstance(name, str) and len(name) > 0:
            return name

        raise ValueError("Ошибка имени")

    @staticmethod
    def _validate_address(address: str) -> str:
        """Метод валидации по адресу"""
        if isinstance(address, str) and len(address) > 0:
            return address

        raise ValueError("Ошибка адреса")


    @staticmethod
    def _validate_salary_from(salary_from: int) -> int:
        """Метод валидации по начальной зарплате"""
        if isinstance(salary_from, int) and salary_from >= 0:
            return salary_from

        return 0

    @staticmethod
    def _validate_salary_to(salary_to: int) -> int:
        """Метод валидации по предельной зарплате"""
        if isinstance(salary_to, int) and salary_to >= 0:
            return salary_to

        return 0

    @staticmethod
    def _validate_description(description: str) -> str:
        """Метод валидации по описанию"""
        if isinstance(description, str):
            return description
        return "Нет описания"

    def to_dict(self) -> dict:
        """Метод для записи в файл"""
        return {
            "name": self.name,
            "address": self.address,
            "experience": self.experience,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "description": self.description,
        }

    @classmethod
    def _validate_company_name(cls, company_name: str) -> str:
        """Метод валидации по имени организации"""
        if isinstance(company_name, str) and len(company_name) > 0:
            return company_name
        raise ValueError("Не правильное название компании")

    @classmethod
    def _validate_company_id(cls, company_id: str) -> str:
        """Метод валидации по id компании"""
        if isinstance(company_id, str):
            return company_id

        raise ValueError("Не правильный номер id")

    @classmethod
    def _validate_vacancy_id(cls, vacancy_id: str) -> str:
        """Метод валидации по id вакансии"""
        if isinstance(vacancy_id, str):
            return vacancy_id

        raise ValueError("Не правильный номер id")
