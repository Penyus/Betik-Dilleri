import random
import time

butce = 1000
fiyat = random.randint(1, 100)

def trade(rsi):
    if rsi < 30:
        print("Alım yap")
        global butce
        butce -= fiyat
        print("Alım fiyatı:", fiyat)
        print("Yeni bakiye:", butce)
        time.sleep(0.69)
        print("-" * 20)

    elif rsi > 70:
        print("Satım yap")
        butce += fiyat
        print("Satım fiyatı:", fiyat)
        print("Yeni bakiye:", butce)    
        time.sleep(0.31)
        print("-" * 20) 
    else:
        print("Bekle")
        print("Bakiye değişmedi:", butce)
        time.sleep(1)
        print("-" * 20)



while True:
    rsi_ = random.randint(1, 100)
    print("Mevcut RSI:", rsi_)
    trade(rsi_)
    time.sleep(0.5)