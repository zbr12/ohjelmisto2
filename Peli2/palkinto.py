from database import Database

class Palkinto: 
    def __init__(self):
        self.db = Database()

    def hae_palkinto(self, icao, game_id):
        cursor = self.db.get_conn().cursor(dictionary=True)
        cursor.execute('SELECT palkinto, avattu FROM lentokentat WHERE lentokentta_id = %s && game_id = %s', (icao, game_id))
        palkinto = cursor.fetchall()
        cursor.close()
        return (palkinto)
    
    def hae_tyyppi(self, id):
        cursor = self.db.get_conn().cursor(dictionary=True)
        cursor.execute('SELECT tyyppi FROM palkinnot WHERE palkinto_id = %s', (id,))
        tyyppi = cursor.fetchall()
        cursor.close()
        return (tyyppi)
    
    def hae_encounter(self):
        cursor = self.db.get_conn().cursor(dictionary=True)
        cursor.execute('SELECT teksti, kysymys, min_raha, max_raha FROM encounter ORDER BY RAND() LIMIT 1',)
        encounter = cursor.fetchall()
        cursor.close()
        return (encounter)
    
    def avattu(self, icao, game_id):
        cursor = self.db.get_conn().cursor(dictionary=True)
        cursor.execute('UPDATE lentokentat SET avattu = 1 WHERE lentokentta_id = %s && game_id = %s', (icao, game_id))
        tulos = cursor.fetchall()
        print(tulos)
        cursor.close()
        return (tulos)
    
    def update_avattu(self, icao, game_id):
        cursor = self.db.get_conn().cursor()
        icao = icao.upper()
        print (icao)
        query = 'UPDATE lentokentat SET avattu = 1 WHERE lentokentta_id = %s AND game_id = %s'
        print(query)
        cursor.execute(query, (icao, game_id))
        self.db.get_conn().commit()
        cursor.close()