from typing import List, Tuple
import random
from country import Country
from airport import Airport
from encounter import Encounter
from database import Database

class Game:
    db = Database()
    def __init__(self, db, fuel, inventory):
        self.db = db
        self.fuel = fuel
        self.current_airport = None
        self.airports = Airport.get_all_airports(self.db)
        self.countries = Country.get_all_countries(self.db)
        self.encounters = Encounter.get_all_encounters(self.db)
        self.inventory = []
        self.score = 0
        self.game_over = False

    def get_current_airport(self) -> Airport:
        return self.current_airport

    def get_fuel(self) -> float:
        return self.fuel

    def set_fuel(self, fuel: float) -> None:
        self.fuel = fuel

    def travel(self, destination: Airport) -> Tuple[bool, str]:
        if destination not in self.current_airport.get_neighbors():
            return False, f"{destination.get_name()} is not a neighbor of {self.current_airport.get_name()}."

        fuel_needed = self.current_airport.get_distance(destination)

        if fuel_needed > self.fuel:
            return False, f"Not enough fuel to travel to {destination.get_name()}."

        self.fuel -= fuel_needed
        self.current_airport = destination

        return True, f"Traveled to {destination.get_name()}."

    def check_encounter(self) -> Tuple[bool, str]:
        encounter_chance = random.randint(1, 10)

        if encounter_chance <= 3:
            money_found = random.randint(100, 1000)
            return True, f"Found {money_found} euros."

        elif encounter_chance <= 6:
            money_lost = random.randint(100, 1000)
            return True, f"Lost {money_lost} euros."

        else:
            return False, "Nothing happened."

    def check_win(self) -> bool:
        return self.current_airport.get_name() == self.airports[0].get_name()
