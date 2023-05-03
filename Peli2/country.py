from typing import List, Tuple
from database import Database

class Country:
    def __init__(self, name: str, currency: str):
        self.name = name
        self.currency = currency

    def __str__(self) -> str:
        return f'{self.name} ({self.currency})'

    @classmethod
    def get_all_countries(cls, db: Database) -> List['Country']:
        countries = []
        # Query the database and create Country objects based on the results
        # Append each object to the countries list
        return countries