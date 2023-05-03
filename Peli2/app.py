from flask import Flask, jsonify, request, render_template
from database import Database
from airport import Airport
from flask_cors import CORS
from flask import url_for
from lentokentat import Lentokentat
from game import Game
import json
from fuel import Fuel
from randomkentat import Randomkentat
import random, string
from palkinto import Palkinto

palkinto = Palkinto()
lentokentat = Lentokentat()

app = Flask(__name__)
CORS(app)
db = Database()

def fly(id, dest, consumption=0):
    if id==0:
        game = Game(0, dest, consumption)
    else:
        game = Game(id, dest, consumption)
    #game.location[0].fetchWeather(game)
    #nearby = game.location[0].find_nearby_airports()
    #for a in nearby:
        #game.location.append(a)
    json_data = json.dumps(game, default=lambda o: o.__dict__, indent=4)
    #print(json_data)
    return json_data

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/continents')
def get_continents():
    cursor = db.get_conn().cursor(dictionary=True)
    cursor.execute('SELECT DISTINCT continent FROM country ORDER BY continent ASC')
    continents = cursor.fetchall()
    cursor.close()
    return jsonify(continents)

@app.route('/countries/<continent>')
def get_countries(continent):
    cursor = db.get_conn().cursor(dictionary=True)
    cursor.execute('SELECT iso_country, avattu FROM country WHERE continent = %s ORDER BY avattu ASC', (continent,))
    countries = cursor.fetchall()
    cursor.close()
    return jsonify(countries)

@app.route('/palkinto', methods=['get'])
def get_palkinto():
    icao = request.args.get('icao', None)
    game_id = request.args.get('game_id', None)
    return jsonify(palkinto.hae_palkinto(icao, game_id))

@app.route('/avattu', methods=['GET'])
def avaa_palkinto():
    icao = request.args.get('icao')
    game_id = request.args.get('game_id')
    result = palkinto.update_avattu(icao, game_id)
    return jsonify(result)

@app.route('/tyyppi/<id>')
def get_tyyppi(id):
    return jsonify(palkinto.hae_tyyppi(id))

@app.route('/encounter')
def get_encounter():
    return jsonify(palkinto.hae_encounter())



@app.route('/airports/<country>')
def get_airports(country):
    cursor = db.get_conn().cursor(dictionary=True)
    cursor.execute('SELECT ident, avattu, latitude_deg, longitude_deg, iso_country, municipality FROM airport WHERE iso_country = %s ORDER BY avattu ASC', (country,))
    airports = cursor.fetchall()
    cursor.close()
    return jsonify(airports)

@app.route('/airport_info/<icao>')
def get_airport_info(icao):
    airport = Airport(icao)
    airport_info = airport.get_airport_info(icao)
    return jsonify(airport_info)


@app.route('/european_airports')
def get_european_airports():
    return jsonify(lentokentat.get_airports())

'''def LuoPeli(pelaajaYksi, pelaajaRange, aloitusRaha, aloituskentta, kaikkiLentokentat):
    conn = db.get_conn()
    if conn.is_connected():
        cursor = conn.cursor(dictionary=True)

        # Insert player data
        insert_query = "INSERT INTO pelaaja(nimi, etäisyys, raha, lokaatio) VALUES (%s, %s, %s, %s);"
        insert_values = (pelaajaYksi, pelaajaRange, aloitusRaha, aloituskentta)
        cursor.execute(insert_query, insert_values)

        global g_id
        g_id = cursor.lastrowid

        # Get rewards
        palkinnot = HaePalkinnot()
        palkinto_list = []
        for palkinto in palkinnot:
            for i in range(0, palkinto["todennäköisyys"], 1):
                palkinto_list.append(palkinto['id'])

        # Shuffle airports and assign rewards
        g_ports = kaikkiLentokentat[0:].copy()
        random.shuffle(g_ports)
        for i, palkinto_id in enumerate(palkinto_list):
            insert_query = "INSERT INTO lentokentat(game_id, lentokentta_id, nimi, palkinto) VALUES (%s, %s, %s, %s);"
            insert_values = (g_id, g_ports[i]['ident'], g_ports[i]['avattu'], palkinto_id)
            cursor.execute(insert_query, insert_values)

        #conn.commit()
        #conn.close()

        return g_id
    else:
        return None'''


@app.route('/routes')
def routes():
    output = []
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)
        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        output.append((url, methods))
    return '<br>'.join(str(x) for x in output)

@app.route('/random', methods=['POST'])
def random_airport():
    return jsonify(lentokentat.random_airport())

@app.route('/removekentat', methods=['POST'])
def TyhjennaKentat():
    kursori = db.conn.cursor(dictionary=True)
    kursori.execute("DELETE FROM lentokentat")
    return jsonify({})

@app.route('/removepelaajat')
def TyhjennaPelaajat(): #Tyhjentää aikaisemmat pelaajat tietokannasta
    kursori = db.conn.cursor(dictionary=True)
    kursori.execute("DELETE FROM pelaaja")
    return jsonify({})

@app.route('/haehinta', methods=['POST'])
def haehinta():
    lat1 = float(request.args.get('lat1'))
    lng1 = float(request.args.get('lng1'))
    lat2 = float(request.args.get('lat2'))
    lng2 = float(request.args.get('lng2'))
    iso_country = request.args.get('iso')
    curr_coords = {lat1, lng1}
    dest_coords = {lat2, lng2}

    # Calculate the distance between the airports using the Fuel class
    countryName = Randomkentat.get_country_name(iso_country)
    fuel = Fuel()
    distance_km = fuel.calculate_distance(curr_coords, dest_coords)
    fuel_cost = fuel.get_fuel_cost(distance_km)
    #print(fuel_cost)

    # Return the necessary data as a JSON response
    response_data = {
        'distance_km': distance_km,
        'fuel': fuel.fuel,
        'country': countryName,
        # Other data to return
    }
    #print(response_data)
    return jsonify(response_data)

@app.route('/lennakohteeseen', methods=['POST'])
def lennakohteeseen():
    data = request.args
    info = request.get_json()
    print(data, "info")
    distance = info['distance']
    fuelCost = info['fuelCost']
    #print(data, distance, fuelCost)
    kursori = db.conn.cursor(dictionary=True)
    query = "UPDATE pelaaja SET lokaatio = %s, etäisyys = etäisyys - %s, raha = raha - %s"
    kursori.execute(query, (data['icao'], distance, fuelCost))
    # Get the player avattu from the request data
    playerName = "Jari"

    # Query the database for the player information
    query = "SELECT * FROM pelaaja WHERE nimi = %s;"
    kursori.execute(query, (playerName,))
    playerInfo = kursori.fetchone()
    print(playerInfo, "PLAYERINFO")

    # Return the player information in the response
    return jsonify({
        'etäisyys': playerInfo['etäisyys'],
        'raha': playerInfo['raha'],
        'lokaatio': playerInfo['lokaatio'],
        'pisteet': playerInfo['pisteet'],
        'longitude_deg': info['longitude_deg'],
        'latitude_deg': info['latitude_deg'],
        'ident': info['ident']
    })

@app.route('/get_player_name', methods=['POST'])
def get_player_name():
    avattu = request.get_json()
    kursori = db.conn.cursor(dictionary=True)
    query = "INSERT INTO pelaaja SET id = %s, pisteet = 0, nimi = %s, etäisyys = %s, raha = %s, lokaatio = %s, peli_id = %s;"
    kursori.execute(query, (0, avattu['playerName'], 1000, 1000, "EFHK", avattu['gameId']))
    query = "SELECT * FROM pelaaja WHERE nimi = %s AND peli_id = %s;"
    kursori.execute(query, (avattu['playerName'], avattu['gameId']))
    playerInfo = kursori.fetchall()
    print(playerInfo, "player info")
    return jsonify({'etääisyys': playerInfo[0]['etäisyys'], 'raha': playerInfo[0]['raha'], 'lokaatio': playerInfo[0]['lokaatio'], 'pisteet': playerInfo[0]['pisteet']})

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port='3000')