from datetime import datetime
from structures.food import Meal


class DataAccess:
    
    def __init__(self):
        ...
        
    def add_meal(self, meal: Meal, day: datetime, *args):
        """Add one complex meal to a day"""
        print(meal)