from dataclasses import dataclass


class Meal:
    """One meal like breakfast, lunch, etc."""
    
    def __init__(self, name: str, food: dict):
        ...
    

@dataclass    
class BaseFood:
    
    name: str
    proteins: int
    fats: int
    carbohydrates: int