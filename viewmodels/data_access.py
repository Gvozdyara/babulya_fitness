from datetime import datetime
import dataclasses
import sqlite3

from structures.food import Meal, Food
import constants


class DataAccess:
    
    def __init__(self):
        self.con = sqlite3.connect(constants.DB_PATH)
        self.cur = self.con.cursor()
        self._init_meal_table()


    def _init_meal_table(self):
        q = """
            CREATE TABLE IF NOT EXISTS meals (
            id INTEGER AUTOINCREMENT,
            name TEXT)
        """
        self.cur.execute(q)

    def add_meal(self, meal: Meal, day: datetime, *args):
        """Add one complex meal to a day"""
        q = """
            CREATE TABLE IF NOT EXISTS ? (meal, quant)
        """



    def get_all_meals(self):

        q = "SELECT name FROM meals"
        self.cur.execute(q)
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

    def add_new_food(self, food: Food):

        q = """INSERT INTO food (name, proteins, fats, carbohydrates, kcal, quantity_unit)
                         VALUES (?, ?, ?, ?, ?, ?)"""
        self.cur.execute(q, dataclasses.fields(food))



    def add_new_meal(self, name: str, meal: dict):

        q = """
            CREATE TABLE ? (ingredient, quantity, quantity_unit)
        """

        self.cur.execute(q)
        self.con.commit()

        q = """
        INSERT INTO ? VALUES(?, ?, ?)
        """
        self.cur.executemany(
            q,
            [(name, ingredient, quant, quant_unit)
             for ingredient, (quant, quant_unit) in meal.items()])
        self.con.commit()