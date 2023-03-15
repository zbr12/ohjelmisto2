import random

class Hissi:
    def __init__(self, alin, ylin):
        self.alinKerros = alin
        self.ylinKerros = ylin
        self.nykyinenKerros = alin

    def kerros_ylos(self):
            if self.nykyinenKerros < (self.ylinKerros):
                self.nykyinenKerros +=1
                print(f'Nykyinen kerros: {self.nykyinenKerros}')
            return
        
    def kerros_alas(self):
            if self.nykyinenKerros > (self.alinKerros):
                self.nykyinenKerros -=1
                print(f'Nykyinen kerros: {self.nykyinenKerros}')
            return
        
    def siirry_kerrokseen(self, kerros):
        i=self.nykyinenKerros
        if i>kerros:
            while i>kerros:
                self.kerros_alas()
                i=i-1
        elif i<kerros:
            while i<kerros:
                self.kerros_ylos()
                i=i+1
        else:
            print(f'Olet jo kerroksessa {i}')
        return
    
class Talo:
    def __init__(self, alin, ylin, maara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for i in range(maara):
             self.hissit.append(Hissi(alin, ylin))

    def aja_hissia(self, hissi, kohde):
         print(f'Hissi {hissi}:')
         self.hissit[hissi].siirry_kerrokseen(kohde)
         return
    
    def palohalytys(self):
         print('Palohälytys!')
         for i in range(len(self.hissit)):
              self.aja_hissia(i, self.alin)
         return
    
talo = Talo(1, 5, 4)
for i in range(len(talo.hissit)):
     kerros = random.randint(1,5)
     talo.aja_hissia(i, kerros)

talo.palohalytys()