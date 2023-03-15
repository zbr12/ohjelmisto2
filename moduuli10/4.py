import random

class Auto:

    maara = 0

    def __init__(self, rekisteri, hnopeus):
        self.rekisterinumero = rekisteri
        self.huippunopeus = hnopeus
        self.tamanHetkinenNopeus = 0
        self.kuljettuMatka = 0

    def kiihdyta(self, muutos):
        self.tamanHetkinenNopeus = self.tamanHetkinenNopeus + muutos
        if self.tamanHetkinenNopeus > self.huippunopeus:
            self.tamanHetkinenNopeus = self.huippunopeus
        elif self.tamanHetkinenNopeus < 0:
            self.tamanHetkinenNopeus = 0
        return
    
    def kulje(self, aika):
        self.kuljettuMatka = self.kuljettuMatka + aika*self.tamanHetkinenNopeus
        return
    


class Kilpailu:
    def __init__(self, nimi, km, autot):
        self.nimi = nimi
        self.pituus = km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)
        return
    
    def tulosta_tilanne(self):
        for auto in self.autot:
            print(f'Rekisterinumero: {auto.rekisterinumero}, tämänhetkinen nopeus: {auto.tamanHetkinenNopeus}, huippunopeus:{auto.huippunopeus}, kuljettu matka: {auto.kuljettuMatka}')
        print('')

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kuljettuMatka >= self.pituus:
                return True
        return False
    
autot = list()

for i in range(10):
    huippunopeus = random.randint(100,200)
    autot.append(Auto('ABC-'+str(i+1), huippunopeus))

    
kilpailu = Kilpailu('Suuri romuralli', 8000, autot)

tunti = 0
while kilpailu.kilpailu_ohi()==False:
    kilpailu.tunti_kuluu()
    tunti = tunti+1
    if tunti%10 == 0:
        kilpailu.tulosta_tilanne()
kilpailu.tulosta_tilanne()