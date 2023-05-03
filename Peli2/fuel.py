from geopy.distance import geodesic
import math

class Fuel:
    def __init__(self, initial_fuel=100):
        self.fuel = initial_fuel

    def calculate_distance(self, curr_coords, dest_coords):
        distance_km = math.floor(geodesic(curr_coords, dest_coords).km)
        #print(distance_km, "kilometrit")
        return distance_km
    def get_fuel_cost(self, distance):
        self.fuel -= math.floor((distance/100))
        #print("SELF FUEL ", self.fuel)

        return self.fuel

    def get_fuel(self):
        return self.fuel

    def use_fuel(self, distance):
        self.fuel -= distance/100

    def refill_fuel(self):
        self.fuel = 100
