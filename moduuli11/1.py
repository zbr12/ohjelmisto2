class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f'Nimi: {super.nimi}, Kirjoittaja: {self.kirjoittaja}, sivumäärä: {self.sivumaara} sivua.')
        return

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f'Nimi: {super.nimi}, päätoimittaja: {self.paatoimittaja}.')
        return

lehti = Lehti('Aku Ankka', 'Aki Hyyppä')
kirja = Kirja('Hytti n:o 6', 'Rosa Likström', '200')

lehti.tulosta_tiedot()
kirja.tulosta_tiedot()