class Auto:
    def __init__(self, rekisteri, hnopeus):
        self.rekisterinumero = rekisteri
        self.huippunopeus = hnopeus
        self.tamanHetkinenNopeus = 0
        self.kuljettuMatka = 0

uusiAuto = Auto('ABC-123', '142 km/h')
print(f'Auton rekisteritunnus: {uusiAuto.rekisterinumero}, Auton huippunopeus: {uusiAuto.huippunopeus}, Tämänhetkinen nopeus: {uusiAuto.tamanHetkinenNopeus}, Kuljettu matka: {uusiAuto.kuljettuMatka}')