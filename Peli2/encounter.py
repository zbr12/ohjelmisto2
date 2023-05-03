from database import Database

class Encounter:
    def __init__(self, id, tyyppi, teksti, kysymys, vastaus, min_raha, max_raha):
        self.id = id
        self.tyyppi = tyyppi
        self.teksti = teksti
        self.kysymys = kysymys
        self.vastaus = vastaus
        self.min_raha = min_raha
        self.max_raha = max_raha

    @classmethod
    def get_all_encounters(cls, db):
        db = Database()
        cur = db.conn.cursor()
        cur.execute("SELECT * FROM encounter")
        rows = cur.fetchall()
        return [cls(*row) for row in rows]