import mysql.connector
from database import Database
from randomkentat import Randomkentat
import random
randomkentat = Randomkentat()
class Lentokentat:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_conn()
        self.airports, self.status = randomkentat.get_european_airports()


    def get_airports(self):

        return self.airports, self.status

    def random_airport(self):
        '''if self.conn.is_connected():
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("""
            SELECT ident, name, latitude_deg, longitude_deg, iso_country, municipality 
            FROM airport 
            WHERE continent LIKE 'EU%' 
                AND type = 'large_airport'
                AND latitude_deg IS NOT NULL 
                AND longitude_deg IS NOT NULL 
                AND municipality NOT IN ('Ponta Delgada', 'Las Palmas', 'Tenerife', 'Lanzarote Island', 'Gran Canaria Island', 'Fuerteventura Island') 
                AND iso_country NOT IN ('RU', 'IS')
            ORDER BY RAND() 
            LIMIT 30
            """)
            airports = cursor.fetchall()

            # Assign a random airport from the list of airports'''
        random_airport = random.choice(self.airports)
        '''
        # Insert 30 airports into the `lentokentat` table with their corresponding `palkinto_id`
            palkinnot = HaePalkinnot()
            palkinto_list = []
            for palkinto in palkinnot:
                for i in range(0, palkinto["todennäköisyys"], 1):
                    palkinto_list.append(palkinto['id'])

            for airport, palkinto_id in zip(airports, palkinto_list):
                query = "INSERT INTO lentokentat(game_id, lentokentta_id, nimi, palkinto) VALUES (%s, %s, %s, %s);"
                cursor.execute(query, (g_id, airport['ident'], airport['name'], palkinto_id))

            self.conn.commit()  # commit changes to the database
        #cursor.close()
        #conn.close()'''
        return random_airport
        '''else:
            return "Could not connect to database"'''

