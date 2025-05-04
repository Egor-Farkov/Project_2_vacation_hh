class Vacancy:
    """Класс для работы с вакансиями"""

    __slots__ = (
        "name",
        "address",
        "experience",
        "salary_from",
        "salary_to",
        "description",
    )

    def __init__(
        self,
        name: str,
        address: str,
        experience: str,
        salary_from: int,
        salary_to: int,
        description: dict,
    ) -> None:
        """Метод для инициализации экземпляра класса"""
        self.name = Vacancy._validate_name(name)
        self.address = Vacancy._validate_address(address)
        self.experience = Vacancy._validate_experience(experience)
        self.salary_from = Vacancy._validate_salary_from(salary_from)
        self.salary_to = Vacancy._validate_salary_to(salary_to)
        self.description = Vacancy._validate_description(description)

    @classmethod
    def cast_to_object_list(cls, dirty_list_vacations: list) -> list:
        """Метод инициализации объектов вакансий"""
        clear_list_vacations = []
        for item in dirty_list_vacations:
            salary_range = item["salary_range"]
            description = item["snippet"]
            if salary_range:
                clear_list_vacations.append(
                    cls(
                        item["name"],
                        item["apply_alternate_url"],
                        item["experience"]["name"],
                        salary_range["from"],
                        salary_range["to"],
                        description,
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
    def _validate_experience(experience: str) -> str:
        """Метод валидации по опыту"""
        if isinstance(experience, str) and len(experience) > 0:
            return experience

        raise ValueError("Ошибка")

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
    def _validate_description(description: dict) -> str:
        """Метод валидации по описанию"""
        if isinstance(description, dict) and len(description) > 0:
            responsibility = description.get("responsibility")

            return responsibility if responsibility else ""
        return "Нет описания"

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "address": self.address,
            "experience": self.experience,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "description": self.description,
        }
