# Betik Dilleri Uygulamaları

Bu proje, temel döngü işlemleri, çok boyutlu diziler, hata yönetimi (`try-except`) ve rastgele veri simülasyonu içeren Python betiklerinden oluşmaktadır. 

## Dosyalar ve İşlevleri

### 1. `hafta_3.py`
* **İşlev:** Yerleşik `len()` komutu kullanılmadan bir dizinin toplam eleman (indeks) sayısını hesaplar.
* **Yöntem:** Dizi elemanlarına `while True` döngüsü ile erişilir. İndeks sınırı aşıldığında ortaya çıkan `IndexError` hatası yakalanarak sayım işlemi sonlandırılır ve sonuç döndürülür.

### 2. `trader.py`
* **İşlev:** Göreceli Güç Endeksi (RSI) simülasyonu için karar mekanizması içerir.
* **Kurallar:** * RSI < 30 ise: `Alım yap`
    * RSI > 70 ise: `Satım yap`
    * 30 <= RSI <= 70 ise: `Bekle`

### 3. `main.py`
* **İşlev:** Projenin ana çalıştırma dosyasıdır. Diğer modülleri içe aktarır ve aşağıdaki işlemleri yürütür:
    * **Hata Yönetimi (Matematik):** Bir sayının sıfıra bölünmesi durumunu `ZeroDivisionError` ile yakalar.
    * **Tek ve Çok Boyutlu Diziler:** `A = ['Aslı', 'Sude', 'Ece', 'Sena']` gibi tek boyutlu listeler ile iç içe geçmiş listelerin (matrislerin) eleman sayılarını `hafta_3.dizi()` fonksiyonu ile yazdırır.
    * **Sayaç:** Zamanlayıcı (`time.sleep`) kullanarak 1'den 100'e kadar sayar.
    * **Trade Simülasyonu:** Rastgele (1-100 arası) üretilen RSI değerlerini sonsuz bir döngü içerisinde `trader.trade()` fonksiyonuna gönderir.

## Çalıştırma

Kodların doğru çalışması için tüm dosyaların (`hafta_3.py`, `trader.py`, `main.py`) aynı dizin içinde bulunması zorunludur. 

Terminal veya komut satırına aşağıdaki komutu girerek ana dosyayı çalıştırın:
```bash
python main.py