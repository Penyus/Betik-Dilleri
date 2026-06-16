class hesapMakinesi:
    def __init__(self, a,b):
        self.sayi1 = a
        self.sayi2 = b
    def toplama(self):
        sonuc = self.sayi1 + self.sayi2
        print("Toplama Sonucu: ", sonuc)
    def carpma(self):
        sonuc = self.sayi1 * self.sayi2
        print("Çarpma Sonucu: ", sonuc)
    def cikarma(self):
        sonuc = self.sayi1 - self.sayi2
        self.memory.append(sonuc)
        print(sonuc)

B.sa