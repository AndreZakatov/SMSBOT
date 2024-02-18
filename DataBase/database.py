import sqlite3
from datetime import datetime


class Database:
    def __init__(self, db_name='telegram_bot.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        # Создание таблицы "Users"
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                ID INTEGER PRIMARY KEY,
                Username TEXT,
                Balance REAL,
                ReferralCode TEXT
            )
        ''')

        # Создание таблицы "Countries"
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Countries (
                ID INTEGER PRIMARY KEY,
                Name TEXT,
                Flag TEXT
            )
        ''')

        # Создание таблицы "Services"
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Services (
                ID INTEGER PRIMARY KEY,
                Name TEXT
            )
        ''')

        # Создание таблицы "Numbers"
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Numbers (
                ID INTEGER PRIMARY KEY,
                ServiceID INTEGER,
                CountryID INTEGER,
                Number TEXT,
                Price REAL,
                FOREIGN KEY (ServiceID) REFERENCES Services(ID),
                FOREIGN KEY (CountryID) REFERENCES Countries(ID)
            )
        ''')

        # Добавление других таблиц в вашем проекте

        self.connection.commit()



    def close_connection(self):
        self.connection.close()



