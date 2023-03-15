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

hissi = Hissi(1, 7)
hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(20)
hissi.siirry_kerrokseen(1)

         