# HAFTA 4 - İleri Python Kavramları

## İçerik
Bu hafta, Python'da **Fonksiyonlar**, **Veri Yapıları**, **Kontrol Akışı** ve **Nesne Yönelimli Programlama (OOP)** gibi ileri seviye kavramların uygulandığı üç proje yer almaktadır.

---

## 📂 Dosyalar ve Açıklamaları

### 1. **trader.py** - Ticari Simülasyon Programı
**Amaç:** RSI (Relative Strength Index) göstergesi kullanarak otomatik alım-satım simülasyonu yapmak.

**Öğrenilen Konseptler:**
- Global değişkenler
- Fonksiyonlar ve parametreler
- Sonsuz döngüler (`while True`)
- Rastgele sayı üretimi (`random` modülü)
- Gecikme ekleme (`time` modülü)

**Program Akışı:**
```
1. Başlangıç bütçesi: 1000
2. Her turda rastgele bir RSI değeri üretilir
3. RSI < 30: Alım yap (Bütçeden para çıkar)
4. RSI > 70: Satım yap (Bütçeye para ekle)
5. Diğer durumlar: Bekle (Bütçe değişmez)
```

**Örnek Çıktı:**
```
Mevcut RSI: 25
Alım yap
Alım fiyatı: 45
Yeni bakiye: 955
```

---

### 2. **yahoo_finance.py** - Veri Yapıları Çalışması
**Amaç:** Kişi bilgilerini depolamak ve ekrana yazdırmak (Liste ve Sözlük kullanımı).

**Öğrenilen Konseptler:**
- Listeler (Lists)
- Sözlükler (Dictionaries)
- Koleksiyon içinde döngü (`for` loop)
- Sözlüklerden veri erişimi (Dictionary keys)

**Veri Yapısı:**
- 9 kişinin bilgileri (Ad, Yaş, Şehir)
- Sözlük anahtarlarına boşluk ile başlanması (Not: Bu bir yazım hatası olabilir - `"Name "` yerine `"Name"` daha uygun olur)

**Program Çıktısı:**
```
Name: John Doe
Age: 30
City: New York
----------------
Name: Jane Smith
Age: 25
City: Los Angeles
...
```

---

### 3. **ucak.py** - Nesne Yönelimli Programlama (OOP)
**Amaç:** Uçak sınıfı oluşturup kalkış, iniş, hareket ve durum sorgulama işlemlerini gerçekleştirmek.

**Öğrenilen Konseptler:**
- Sınıf tanımlama (`class`)
- Yapıcı metod (`__init__`)
- Instance variables (self.ucak_tip, self.konum)
- Ortak metotlar (methods)
- Nesne oluşturma ve metot çağırma

**Sınıf Yapısı:**

| Metod | Açıklama | Konum Değişimi |
|-------|----------|---|
| `__init__(ucak_tipi)` | Uçağı başlatır, konumu (0, 0, 0) olarak ayarlar | - |
| `kalkis()` | Uçak kalkış yapıyor, konumu (0, 0, 1000) olur | ↑ 1000m |
| `inis()` | Uçak iniş yapıyor, konumu (0, 0, 0) olur | ↓ 0m |
| `hareket_et(yeni_konum)` | Uçak belirtilen konuma hareket eder | Özel |
| `durum()` | Şu anki konumu ekrana yazdırır | - |

**Örnek Çalışma:**
```
Boeing 747 kalkış yapıyor...
[2 saniye bekleme]
Boeing 747 kalkış tamamlandı. Şu anki konum: (0, 0, 1000)

Boeing 747 hareket ediyor...
[1 saniye bekleme]
Boeing 747 hareket tamamlandı. Şu anki konum: (100, 200, 3000)

Boeing 747 şu anki konumu: (100, 200, 3000)

Boeing 747 iniş yapıyor...
[2 saniye bekleme]
Boeing 747 iniş tamamlandı. Şu anki konum: (0, 0, 0)
```

---

## 🎯 Hafta 4 Öğrenme Hedefleri

✅ Fonksiyonlarla kodun yeniden kullanılabilirliğini arttırmak
✅ Global ve lokal değişkenleri kullanmak
✅ Veri yapılarını etkili bir şekilde kullanmak
✅ OOP ilkelerini anlayıp sınıf ve nesne oluşturmak
✅ Modülleri (random, time) ve kütüphaneleri kullanmak
✅ Döngüleri ve kontrol akışını mastering etmek

---

## 💡 Geliştirme Önerileri

### trader.py için:
- Fiyat dinamik olarak değiştirilmeli (her işlemde farklı fiyat)
- Grafik gösterim eklenebilir (matplotlib kullanarak)
- İşlem geçmişi tutulabilir

### yahoo_finance.py için:
- Sözlük anahtarlarındaki boşluklar kaldırılmalı
- Dosyadan veri okuma özelliği eklenebilir

### ucak.py için:
- Yakıt sistemi eklenebilir
- Hız kavramı eklenerek daha realistik simülasyon yapılabilir
- Hata kontrolü (error handling) kullanılabilir

---

## 🚀 Çalıştırma

Her bir Python dosyasını çalıştırmak için terminal'de şu komutları kullanın:

```bash
# Trader simülasyonu başlat
python trader.py

# Yahoo Finance verileri görüntüle
python yahoo_finance.py

# Uçak simülasyonu çalıştır
python ucak.py
```

---

## 📚 Kaynaklar
- Python Fonksiyonlar: Built-in `time`, `random` modülleri
- OOP Konseptleri: Class, Methods, Attributes
- Veri Yapıları: Lists, Dictionaries

