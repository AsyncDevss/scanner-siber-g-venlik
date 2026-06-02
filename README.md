# AeroScan - Asenkron Port Tarayıcı

AeroScan, ağ güvenliği analizlerinde hedef sistemdeki açık kapıları (portları) hızlı bir şekilde tespit etmek amacıyla geliştirilmiş Python tabanlı bir siber güvenlik aracıdır.

Python'ın `asyncio` kütüphanesini kullanarak **asenkron (eşzamanlı)** mimariyle çalışır. Bu sayede geleneksel tarayıcılar gibi her portu sırayla beklemek yerine, yüzlerce portu saniyeler içinde tarayabilir.

---

## 🚀 Özellikler

* **Yüksek Hız:** Asenkron yapısı sayesinde minimum sürede maksimum port taraması gerçekleştirir.
* **Akıllı Servis Tespiti:** Açık olan portlarda çalışan yaygın servisleri (SSH, FTP, HTTP, HTTPS vb.) otomatik eşleştirir.
* **Güvenli Test Modu:** Varsayılan olarak `127.0.0.1` (Localhost) üzerinde çalışacak şekilde yapılandırılmıştır, test sızmaları için güvenlidir.

---

## 🛠️ Kurulum ve Çalıştırma

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz.

### Gereksinimler
* Bilgisayarınızda **Python 3.7+** sürümünün yüklü olması gerekmektedir. Ekstra bir dış kütüphane (`pip install` vb.) kurmanıza gerek yoktur, standart kütüphaneler kullanılmıştır.

### Çalıştırma Adımları

1. Bu depoyu bilgisayarınıza indirin veya kodu kopyalayın:
   ```bash
   git clone [https://github.com/kullanici-adiniz/proje-isminiz.git](https://github.com/kullanici-adiniz/proje-isminiz.git)
   cd proje-isminiz
