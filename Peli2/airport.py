import mysql.connector
from database import Database

class Airport:
    def __init__(self, icao, db, conn):
        self.icao = icao
        self.db = Database()
        self.conn = self.db.get_conn()

    def get_airport_info(icao):
        db = Database()

        cursor = db.conn.cursor()
        query = """
            SELECT * FROM lentokentat WHERE lentokentta_id = %s
        """
        cursor.execute(query, (icao,))
        airport_info = cursor.fetchone()
        cursor.close()
        #print(airport_info, "AIRPORT INFO")
        if not airport_info:
            return {}

        # create a dictionary with the relevant airport information
        airport_dict = {
            'name': airport_info[5],
            #'city': airport_info[10],
            #'country': airport_info[8],
            'latitude_deg': float(airport_info[6]),
            'longitude_deg': float(airport_info[7]),
            #'elevation_ft': airport_info[6],
            'icao': airport_info[2],
            #'iata': airport_info[13],
        }
        return airport_dict
    def get_all_airports(cls):
        """
        Get all airports from the lentokentat table
        """
        db = Database()
        cur = db.get_conn().cursor(dictionary=True)
        cur.execute("SELECT * FROM lentokentat")
        rows = cur.fetchall()
        airports = []
        #print(rows)
        print(rows[0])

        #for row in rows:
        #    airport = cls(row[0], row[1], row[2], row[3], row[4])
        #    airports.append(airport)
        return airports
