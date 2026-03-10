import time 

class ucan: 
    def __init__(self, ucak_tipi):
        self.ucak_tip = ucak_tipi
        self.konum = (0, 0, 0) 

    def kalkis(self):
        print(f"{self.ucak_tip} kalkış yapıyor...")
        time.sleep(2)  
        self.konum = (0, 0, 1000)  
        print(f"{self.ucak_tip} kalkış tamamlandı. Şu anki konum: {self.konum}")
    
    def inis(self):
        print(f"{self.ucak_tip} iniş yapıyor...")
        time.sleep(2) 
        self.konum = (0, 0, 0)  
        print(f"{self.ucak_tip} iniş tamamlandı. Şu anki konum: {self.konum}")
    
    def hareket_et(self, yeni_konum):
        print(f"{self.ucak_tip} hareket ediyor...")
        time.sleep(1)  
        self.konum = yeni_konum  
        print(f"{self.ucak_tip} hareket tamamlandı. Şu anki konum: {self.konum}")
    
    def durum(self):
        print(f"{self.ucak_tip} şu anki konumu: {self.konum}")
ucak= ucan("Boeing 747")
ucak.kalkis()
ucak.hareket_et((100, 200, 3000))
ucak.durum()
ucak.inis()