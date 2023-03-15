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
    
autot = list()

for i in range(10):
    huippunopeus = random.randint(100,200)
    autot.append(Auto('ABC-'+str(i+1), huippunopeus))

a=1
while(a==1):
    for auto in autot:
        if auto.kuljettuMatka < 10000:
            muutos = random.randint(-10, 15)
            auto.kiihdyta(muutos)
            auto.kulje(1)
        else:
            a=2

for auto in autot:
    print(f'Rekisterinumero: {auto.rekisterinumero}, kuljettu matka: {auto.kuljettuMatka}')

