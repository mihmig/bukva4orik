# Модуль взаимодействия с базой данных MySql (MariaDB)
import os
from typing import List, Dict
from pymysql.cursors import DictCursor
import pymysqlpool
from contextlib import contextmanager

class Db:
    def __init__(self):
        self.pool = pymysqlpool.ConnectionPool(
            database=os.environ['DB_NAME'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            host=os.environ['DB_HOST'],
            port=int(os.environ['DB_PORT']),
            autocommit=True,
            size=1,
            maxsize=2,
            pre_create_num=1,
            charset='utf8mb4'
        )

    @contextmanager
    def connection(self):
        conn = self.pool.get_connection(pre_ping=True)
        try:
            yield conn
        finally:
            conn.close()

    def get_value(self, query: str, params: list = None) -> str | None:
        with self.connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                row = cursor.fetchone()
                return row[0] if row is not None else None

    def get_line(self, query: str, params: list = None) -> Dict | None:
        with self.connection() as conn:
            with conn.cursor(cursor=DictCursor) as cursor:
                cursor.execute(query, params)
                return cursor.fetchone()

    def get_row(self, query: str, params: list = None) -> List:
        with self.connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                rows = cursor.fetchall()
                return [row[0] for row in rows]

    def get_dict(self, query: str, params: list = None) -> dict:
        with self.connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, params)
                records = cursor.fetchall()
                return {r[0]: r[1] for r in records}

    def get_data(self, query: str, params: list = None) -> list[dict]:
        with self.connection() as conn:
            with conn.cursor(cursor=DictCursor) as cursor:
                cursor.execute(query, params)
                return list(cursor.fetchall())

    def execute(self, query: str, params: list = None):
        with self.connection() as conn:
            with conn.cursor(cursor=DictCursor) as cursor:
                return cursor.execute(query, params)

    def insert(self, query: str, params: list = None) -> int:
        with self.connection() as conn:
            with conn.cursor(cursor=DictCursor) as cursor:
                cursor.execute(query, params)
                return conn.insert_id()

    def insert_dict(self, table: str, data: dict) -> int:
        """
        Универсальная вставка словаря в таблицу.
        Ключи словаря должны совпадать с именами столбцов.
        """
        # Формируем список имен столбцов и заглушек %s
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["%s"] * len(data))

        # Собираем итоговый SQL
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

        with self.connection() as conn:
            with conn.cursor(cursor=DictCursor) as cursor:
                # Передаем значения словаря в правильном порядке
                cursor.execute(query, list(data.values()))
                return conn.insert_id()
