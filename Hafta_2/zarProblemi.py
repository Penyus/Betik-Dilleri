import random 
def zar_at1():
    zar1 = random.randint(1,6)
    return zar1
def zar_at2():
    zar2 = random.randint(1,6)
    return zar2



def tahmin_al():
    while True:
        tahmin = input("Hangi takım kazanır? (GS - Beraberlik - FB): ").strip().lower()
        
        if tahmin in ["gs", "beraberlik", "fb"]:
            return tahmin
        else:
            print("Hata: Geçerli bir takım gir (GS, Beraberlik, FB)!")


def tekli_atis():
    print("\n--- Tekli Atış Modu ---")
    kullanici_tahmini = tahmin_al()

    zar1 = zar_at1()
    zar2 = zar_at2()
    print(f"Zar 1: {zar1}, Zar 2: {zar2}")
    if zar1%2==0 and zar2%2==0:
        print("2 zarda çift geldi Cimbom kazandı")
        gercek_sonuc = "gs"
    elif zar1%2==1 and zar2%2==1:
        print("2 zarda tek geldi Fenerbahçe kazandı")
        gercek_sonuc = "fb"
    else:    
        print("1 zarda tek 1 zarda çift geldi Berabere")
        gercek_sonuc = "beraberlik"
#sakamakamadafaka
    print("-"*20)
    if kullanici_tahmini == gercek_sonuc:
        print("Tahminin doğru. Tebrikler!")
    else:
        print(f"Tahminin yanlış. Maç Sonucu: {gercek_sonuc}")

def toplu_atis():

    print("\n--- Toplu Atış Modu ---")
    print("Serinin sonucu ne olur ?")
    kullanici_tahmini = tahmin_al()
    try:
        tane = int(input("Kaç tane Zar atılsın: "))
    except ValueError:
        print("Sayısal bir değer giriniz!")
        return
    cimbom_sayisi = 0
    fb_sayisi = 0
    berabere_sayisi = 0
    for _ in range(tane):
        zar1 = zar_at1()
        zar2 = zar_at2()
        if zar1%2==0 and zar2%2==0:
            cimbom_sayisi += 1
        elif zar1%2==1 and zar2%2==1:
            fb_sayisi += 1
        else:
            berabere_sayisi += 1
    print(f"\nSonuçlar:")
    print(f"{cimbom_sayisi} kere Cimbom kazandı. ({cimbom_sayisi/tane*100:.2f}%)")
    print(f"{fb_sayisi} kere Fenerbahçe kazandı. ({fb_sayisi/tane*100:.2f}%)")
    print(f"{berabere_sayisi} kere Berabere bitti. ({berabere_sayisi/tane*100:.2f}%)")

    if cimbom_sayisi > fb_sayisi and cimbom_sayisi > berabere_sayisi:
        genel_kazanan = "gs"
    elif fb_sayisi > cimbom_sayisi and fb_sayisi > berabere_sayisi:
        genel_kazanan = "fb"
    elif berabere_sayisi > cimbom_sayisi and berabere_sayisi > fb_sayisi:
        genel_kazanan = "beraberlik"
    else:
        genel_kazanan = "belirsiz" 

    
    print("-" * 20)
    if genel_kazanan == "belirsiz":
        print("⚠️ Sonuçlarda eşitlik var, net kazanan yok.")
    elif kullanici_tahmini == genel_kazanan:
        print(f"Tahminin doğru. Seri '{genel_kazanan.upper()}' ile sonuçlandı.")
    else:
        print(f"Tahminin yanlış. Seri '{genel_kazanan.upper()}' ile sonuçlandı.")
    
while True:
    try:
        secim = int(input("""
────────────────────
   Zar Problemi
    GS x FB                          
────────────────────
1 → Tekli atış
2 → Çoklu atış

Seçimin: """))
        
        if secim == 1 or secim == 2:
            break  
        else:
            print("\n Hata: Sadece 1 veya 2 gir!\n")
            
    except ValueError:
        print("\n Hata: Geçerli bir sayı gir (1 veya 2)!\n")

match secim:
    case 1:
        tekli_atis()
    case 2:
        toplu_atis()
