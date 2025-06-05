import psycopg2

from src.vacancies import Vacancy


class DBManager:
    """Класс для подключения к БД PostgreSQL"""

    def __init__(self, user, password, host, database, port):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.port = port
        self.conn = None
        self.cur = None


    def connect_db(self):
        """Метод подключения к БД"""

        self.conn = psycopg2.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password,
            port=self.port
        )

    def create_db(self):
        """Метод создания БД"""
        tmp_data_base = psycopg2.connect(
            dbname="template1", user=self.user, password=self.password, host=self.host, port=self.port
        )

        tmp_data_base.set_session(autocommit=True)
        cursor = tmp_data_base.cursor()
        cursor.execute(
            f"""
        SELECT
        COUNT(*)
        WHERE NOT EXISTS
        (
        SELECT FROM
        pg_database
        WHERE
        datname = '{self.database}'
        );
        """
        )

        check_data_base = cursor.fetchone()
        if check_data_base:
            if check_data_base[0] == 1:
                cursor.execute(f"CREATE DATABASE {self.database};")
        cursor.close()


    def create_table(self):
        """Метод создания таблиц"""
        cursor = self.conn.cursor()
        cursor.execute(
            f"""
        CREATE TABLE if not exists company
        (
        id int PRIMARY KEY,
        name text
        )
        """
        )

        cursor.execute(
            f"""
                CREATE TABLE if not exists vacancy
                (
                id int PRIMARY KEY,
                id_company int references company(id),
                name text,
                address text,
                salary_from int,
                salary_to int,
                description text
                )
                """
        )
        self.conn.commit()
        cursor.close()

    def insert(self, data: list[Vacancy]) -> None:
        """Метод вставки"""
        cursor = self.conn.cursor()
        for vacancy in data:
            cursor.execute(
                f"""
                    INSERT INTO company
                        (id, name) 
                    VALUES
                        (%s, %s)
                    ON CONFLICT (id)
                    DO NOTHING
                    """, (vacancy.company_id, vacancy.company_name)
            )
            cursor.execute(
                f"""
                    INSERT INTO vacancy
                        (id, id_company, name, address, salary_from, salary_to, description) 
                   VALUES
                        (%s, %s, %s, %s, %s, %s, %s)
                        ON CONFLICT (id)
                        DO NOTHING
                   """, (vacancy.vacancy_id, vacancy.company_id, vacancy.name,
                         vacancy.address, vacancy.salary_from, vacancy.salary_to,
                         vacancy.description)
            )
            self.conn.commit()

    def get_companies_and_vacancies_count(self):
        """Метод получения списка всех компаний и количество вакансий у каждой компании."""

        cur = self.conn.cursor()
        cur.execute(
            """
            SELECT company.name, COUNT(*)
             FROM company
             JOIN vacancy on company.id = vacancy.id_company
             GROUP BY company.name
             """
        )
        result = cur.fetchall()
        cur.close()
        return result

    def get_all_vacancies(self):
        """Метод получения списка всех вакансий
        с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию."""

        cur = self.conn.cursor()
        cur.execute(
            """
            SELECT 
            company.name, vacancy.name, salary_from || '-' || salary_to, address
            FROM
            company
            JOIN
            vacancy on company.id = vacancy.id_company
        """
        )
        result = cur.fetchall()
        cur.close()
        return result

    def get_avg_salary(self):
        """Метод получения средней зарплаты по вакансиям."""

        cur = self.conn.cursor()
        cur.execute(
            """
            SELECT 
            (AVG(vacancy.salary_from + vacancy.salary_to)) / 2 as average_salary
            FROM 
            vacancy
            WHERE 
            salary_from > 0
            AND 
            salary_to > 0
            """
        )
        result = cur.fetchone()
        cur.close()
        return result

    def get_vacancies_with_higher_salary(self):
        """Метод получения списка всех вакансий,
        у которых зарплата выше средней по всем вакансиям."""

        cur = self.conn.cursor()
        cur.execute(
            """
            SELECT *
            FROM
            vacancy
            WHERE
            salary_to > (SELECT 
            (AVG(vacancy.salary_from + vacancy.salary_to)) / 2 as average_salary
            FROM 
            vacancy
            WHERE 
            salary_from > 0
            AND 
            salary_to > 0)
            """
        )
        result = cur.fetchall()
        cur.close()
        return result

    def get_vacancies_with_keyword(self, search_word=None):
        """Метод получения списка всех вакансий,
        в названии которых содержатся переданные
        в метод слова."""

        cur = self.conn.cursor()

        if not search_word:
            cur.execute(
                """
                      SELECT *
                      FROM
                      vacancy                      
                      """
            )
            result = cur.fetchall()
            cur.close()
            return result

        cur.execute(
            f"""
            SELECT *
            FROM
            vacancy
            WHERE
            name iLIKE '%{search_word}%'
            """
        )

        result = cur.fetchall()
        cur.close()
        return result


