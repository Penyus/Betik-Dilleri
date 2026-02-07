import random 


def tekli_atis():
    print("\n--- Tekli Atış Modu ---")
    secim = input("\nYazı mı Tura mı? ").strip().capitalize()

    if secim not in ["Yazı", "Tura"]:
        print("Sadece 'Yazı' veya 'Tura' gir.")
        return
    print(f"{secim} seçtin.")
    atis = random.randint(0,1)
    gelen = "Yazı" if atis == 1 else "Tura"
    if secim == gelen:
        print(f"{gelen} geldi, Kazandın!")
    else:
        print(f"{gelen} geldi, Kaybettin")



def toplu_atis():
    print("\n--- Toplu Atış Modu ---")
    try:
        tane = int(input("Kaç tane Yazı-Tura atılsın: "))
    except ValueError:
        print("Sayısal bir değer giriniz!")
        return
    
    yazi_sayisi = 0
    tura_sayisi = 0

    for _ in range(tane):
        x = random.randint(0,1)
        if x == 1:
            yazi_sayisi +=1
        else:
            tura_sayisi +=1
    print(f"\nSonuçlar:")
    print(f"{yazi_sayisi} tane Yazı geldi.")
    print(f"{tura_sayisi} tane Tura geldi.")   
    if yazi_sayisi > tura_sayisi:
        print(f"Yazı {yazi_sayisi-tura_sayisi} farkla kazandı.")   
    elif tura_sayisi > yazi_sayisi:
        print(f"Tura {tura_sayisi-yazi_sayisi} farkla kazandı") 
    else:
        print("Sonuçlar eşit.")


while True:
    try:
        secim = int(input("""
────────────────────
   Yazı Tura
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
