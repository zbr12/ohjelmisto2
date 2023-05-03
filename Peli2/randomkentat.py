import mysql.connector
from database import Database
import requests
from bs4 import BeautifulSoup
import random, string
class Randomkentat:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_conn()

    def HaePalkinnot(self):
        if self.conn.is_connected():
            cursor = self.conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM palkinto")
            palkinnot = cursor.fetchall()
            return palkinnot
        else:
            return []

    def get_country_name(code):
        # Fetch the country code data from the website
        response = requests.get('https://www.iban.com/country-codes')
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the table rows that contain the country code and name
        rows = soup.select('table tr')[1:]

        for row in rows:
            columns = row.select('td')
            row_code = columns[1].text.strip()
            if row_code == code:
                name = columns[0].text.strip().title()
                return name
        return None


    def get_european_airports(self):
        if self.conn.is_connected():
            letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
            status = {
                "id": ''.join(random.choice(letters) for i in range(20)),
            }
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
            country_dict = {}


            #for airport in airports:
            #    print(airport['longitude_deg'], airport['latitude_deg'])

        # Insert 30 airports into the `lentokentat` table with their corresponding `palkinto_id`
            palkinnot = self.HaePalkinnot()
            palkinto_list = []
            for palkinto in palkinnot:
                for i in range(0, palkinto["todennäköisyys"], 1):
                    palkinto_list.append(palkinto['id'])

            for airport, palkinto_id in zip(airports, palkinto_list):
                query = "INSERT INTO lentokentat(game_id, lentokentta_id, nimi, palkinto, latitude_deg, longitude_deg) VALUES (%s, %s, %s, %s, %s, %s);"
                cursor.execute(query, (status['id'], airport['ident'], airport['name'], palkinto_id, airport['latitude_deg'], airport['longitude_deg']))

            self.conn.commit()  # commit changes to the database
            print("Tiedot lähetetty")
        #cursor.close()
        #conn.close()¨
            return airports, status
        else:
            return "Could not connect to database"
