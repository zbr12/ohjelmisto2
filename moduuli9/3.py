class Auto:
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
    


uusiAuto = Auto('ABC-123', 142)
print(f'Auton rekisteritunnus: {uusiAuto.rekisterinumero}, Auton huippunopeus: {uusiAuto.huippunopeus} km/h, Tämänhetkinen nopeus: {uusiAuto.tamanHetkinenNopeus}, Kuljettu matka: {uusiAuto.kuljettuMatka}')
uusiAuto.kiihdyta(30)
uusiAuto.kiihdyta(70)
uusiAuto.kiihdyta(50)
print(f'Auton tämänhetkinen nopeus: {uusiAuto.tamanHetkinenNopeus} km/h')
uusiAuto.kiihdyta(-200)
print(f'Auton tämänhetkinen nopeus: {uusiAuto.tamanHetkinenNopeus} km/h')
