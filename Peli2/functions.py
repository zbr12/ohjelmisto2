import mysql.connector

def search_by_icao(icao):
    cnx = mysql.connector.connect(user='root', password='password',
                                  host='127.0.0.1',
                                  database='airports')
    cursor = cnx.cursor(dictionary=True)

    query = ("SELECT * FROM airports WHERE ident = %s")
    cursor.execute(query, (icao,))

    airport = cursor.fetchone()
    cursor.close()
    cnx.close()

    return airport

def get_continents():
    cnx = mysql.connector.connect(user='root', password='password',
                                  host='127.0.0.1',
                                  database='airports')
    cursor = cnx.cursor(dictionary=True)

    query = ("SELECT DISTINCT continent FROM countries")
    cursor.execute(query)

    continents = cursor.fetchall()
    cursor.close()
    cnx.close()

    return continents

def get_countries(continent):
    cnx = mysql.connector.connect(user='root', password='password',
                                  host='127.0.0.1',
                                  database='airports')
    cursor = cnx.cursor(dictionary=True)

    query = ("SELECT iso_country, name FROM countries WHERE continent = %s ORDER BY name")
    cursor.execute(query, (continent,))

    countries = cursor.fetchall()
    cursor.close()
    cnx.close()

    return countries

def get_airports_by_country(country):
    cnx = mysql.connector.connect(user='root', password='password',
                                  host='127.0.0.1',
                                  database='airports')
    cursor = cnx.cursor(dictionary=True)

    query = ("SELECT * FROM airports WHERE iso_country = %s ORDER BY name")
    cursor.execute(query, (country,))

    airports = cursor.fetchall()
    cursor.close()
    cnx.close()

    return airports

def get_airport_info(airport_id):
    cnx = mysql.connector.connect(user='root', password='password',
                                  host='127.0.0.1',
                                  database='airports')
    cursor = cnx.cursor(dictionary=True)

    query = ("SELECT * FROM airports WHERE ident = %s")
    cursor.execute(query, (airport_id,))

    airport = cursor.fetchone()
    cursor.close()
    cnx.close()

    return airport