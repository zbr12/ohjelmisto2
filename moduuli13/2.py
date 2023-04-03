from flask import Flask, request
import mysql.connector
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)
app = Flask(__name__)
@app.route('/kenttä/<icao>')
def kenttä(icao):
    sql = "SELECT name, municipality FROM airport WHERE ident = '"+icao+"'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount>0:
        for rivi in tulos:
            name = rivi[0]
            municipality = rivi[1]
        vastaus = {"ICAO" : icao, 
                   "name" : name, 
                   "municipality" : municipality}
    else:
        vastaus = "Ei löydetty kenttää"

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)