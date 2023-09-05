from datetime import datetime
import dataclasses
import sqlite3

from structures.food import Meal, Food
import constants


class DataAccess:
    
    def __init__(self):
        self.con = sqlite3.connect(constants.DB_PATH)
        self.cur = self.con.cursor()
        self._init_diary_table()
        self._init_food_table()

    def _init_diary_table(self):
        q = """
            CREATE TABLE IF NOT EXISTS diary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT)
        """
        self.cur.execute(q)

    def _init_food_table(self):
        q = """
            CREATE TABLE IF NOT EXISTS food (
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            name TEXT,
            proteins INTEGER, 
            fats INTEGER, 
            carbohydrates INTEGER, 
            kcal INTEGER,
            quantity_unit TEXT)
            
        """
        self.cur.execute(q)

    def get_all_food_names(self):

        q = "SELECT name FROM food"
        self.cur.execute(q)
        return self.cur.fetchall()

    def filter_food_names(self, chunk: str) -> list:
        q = """SELECT name from food
                 WHERE name like "%?%" """
        self.cur.execute()
        return self.cur.fetchall()

    def create_table_for_day(self, day: datetime):

        q = """CREATE TABLE IF NOT EXISTS ? (name, quantity, quantity_unit)"""

        self.cur.execute(q, (day,))

    def get_food_quantity_unit(self, name: str):

        q = """FROM ? SELECT quantity_unit"""

        self.cur.execute(q, (name,))
        return self.cur.fetchone()[0]

    def add_food_to_day(self, day: datetime, food: Food, quantity: float):

        self.create_table_for_day(day)
        q = """INSERT INTO ?
                    VALUES(?, ?)
                    """
        self.cur.execute(q, (food.name, quantity))

    def add_day(self, day: datetime):
        q = """INSERT INTO diary (day)
                       VALUES (?)"""
        self.cur.execute(q, (day,))

    def add_new_food(self, food: Food):

        q = """INSERT INTO food (name, proteins, fats, carbohydrates, kcal, quantity_unit)
                         VALUES (?, ?, ?, ?, ?, ?)"""
        self.cur.execute(q, dataclasses.fields(food))

DA = DataAccess()
