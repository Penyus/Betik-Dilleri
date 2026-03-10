# 🎲 Zar Atma Simülasyonu (Olasılık Hesaplama)

**Ders:** Betik Dilleri  
**Hafta:** 2  
**Tarih:** 10.02.2026  
**Konu:** Olasılıklarla kod yazma, koda dökme

## 📋 Proje Tanımı
Bu proje, basit bir zar atma oyununu Python kullanarak simüle eder. Amaç, belirli olasılık dağılımlarına sadık kalarak rastgelelik (randomness) içeren bir algoritma oluşturmaktır.

Projede **2 adet zar** atılmaktadır ve sonuçlar aşağıdaki olasılık kurallarına göre belirlenmektedir:

* 🟡 **Galatasaray (GS) Kazanır:** %25 İhtimal
* 🔵 **Fenerbahçe (FB) Kazanır:** %25 İhtimal
* ⚪ **Beraberlik:** %50 İhtimal

## 🧮 Matematiksel Mantık
Bu olasılıkları sağlamak için zarların üzerindeki sayıların **Tek (1,3,5)** veya **Çift (2,4,6)** gelme durumları kullanılmıştır.

Standart bir zarda Tek veya Çift gelme olasılığı %50'dir. İki zarın kombinasyonları şu sonucu doğurur:

| Zar 1 | Zar 2 | Sonuç | Olasılık Hesabı | Durum |
| :---: | :---: | :---: | :---: | :--- |
| Çift | Çift | **GS Kazanır** | $\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$ | **%25** |
| Tek | Tek | **FB Kazanır** | $\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$ | **%25** |
| Tek | Çift | **Beraberlik** | $\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$ | \multirow{2}{*}{**%50** (Toplam)} |
| Çift | Tek | **Beraberlik** | $\frac{1}{2} \times \frac{1}{2} = \frac{1}{4}$ | |

## 🚀 Özellikler

Kod içerisinde iki farklı mod bulunmaktadır:

1.  **Tekli Atış Modu:** * Kullanıcıdan maç sonucu tahmini alınır.
    * Zarlar atılır ve anlık sonuç gösterilir.
    * Tahminin doğruluğu kontrol edilir.

2.  **Toplu Atış (Simülasyon) Modu:**
    * Kullanıcıdan "N" adet zar atılması istenir.
    * Binlerce kez zar atılarak "Büyük Sayılar Yasası" gereği oranların %25-%25-%50 dağılımına yaklaştığı gözlemlenir.
    * Serinin genel kazananı ile kullanıcının tahmini karşılaştırılır.

## 🛠️ Kurulum ve Çalıştırma

Proje standart Python kütüphaneleri ile çalışır, ek bir kurulum gerektirmez.

1.  Repoyu klonlayın veya dosyayı indirin.
2.  Terminal veya konsolu açın.
3.  Aşağıdaki komutla çalıştırın:

```bash
python zar_Problemi.py