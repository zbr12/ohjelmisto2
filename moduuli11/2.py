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
    
class Sahkoauto(Auto):
    def __init__(self, rekisteri, hnopeus, akkukapasiteetti):
        self.akkukapasiteettiKWh = akkukapasiteetti
        super().__init__(rekisteri, hnopeus)

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, hnopeus, tankki):
        self.tankkiL = tankki
        super().__init__(rekisteri, hnopeus)

sahkoauto = Sahkoauto('ABC-15', 180, 52.5)
polttoauto = Polttomoottoriauto('ACD-123', 165, 32.3)

sahkoauto.kiihdyta(100)
polttoauto.kiihdyta(150)

sahkoauto.kulje(3)
polttoauto.kulje(3)

print(f'Sähköauton kulkema matka: {sahkoauto.kuljettuMatka} km')
print(f'Polttomoottoriauton kulkema matka: {polttoauto.kuljettuMatka}')