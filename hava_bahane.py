#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Hava Durumu Bahane Üreticisi
Her hava koşulunda çalışmamak için resmi bahaneler.
Gerçekten çalışır. Gerçekten absürt.
"""

import random
import sys

# Gizli not: bazen sistemin kendisi bahanedir, ama bunu kimse duymasın.
# (kod içinde saklı, kimse okumaz zaten)

def uret_bahane(hava):
    bahaneler = {
        "güneşli": [
            "Güneş çok parlak, ekrana bakamıyorum. Gözlerim resmi olarak kör oldu.",
            "Hava çok güzel, dışarı çıkmak zorundayım yoksa evren beni yargılar.",
            "Güneş ışınları motivasyonumu eritti, geri döndürmek için 3 iş günü lazım."
        ],
        "yağmurlu": [
            "Yağmur yağıyor, dışarı çıkmak yasak, içeride kalmak da yasak. Çıkmazdayım.",
            "Damla sesi o kadar ritmik ki, beyin dalgalarım senkronize oldu ve çalışmayı reddediyor.",
            "Yağmur resmi olarak 'çalışma iptal' ilan etti. İtiraz hakkı yok."
        ],
        "karlı": [
            "Kar yağıyor, yollar kapandı, hatta evin içindeki yollar bile kapandı.",
            "Kar taneleri klavyeme düştü, her harf dondu. Isınması 47 dakika sürer.",
            "Kış uykusu modu aktif, vücut sıcaklığım düştü, acil battaniye lazım."
        ],
        "bulutlu": [
            "Bulutlar o kadar kalın ki, güneşin varlığından şüphe etmeye başladım. Varoluşsal kriz.",
            "Gri gökyüzü moralimi yerle bir etti, toparlanması için resmi izin gerekli.",
            "Bulutlar arasında bir şeyler fısıldaşıyor, dinlemek zorundayım."
        ],
        "fırtınalı": [
            "Fırtına var, elektrikler kesilecek diye bekliyorum. Beklemek de iş sayılır.",
            "Rüzgar o kadar güçlü ki, düşüncelerim uçup gitti. Geri getirmem lazım.",
            "Şimşek çaktı, içimdeki motivasyon kısa devre yaptı."
        ],
        "normal": [
            "Hava normal, bu da şüpheli. Bir şeyler ters gidiyor olmalı, araştırmam lazım.",
            "Normal hava resmi olarak 'bahane yok' demek değildir. Her zaman bahane vardır.",
            "Atmosfer basıncı ideal değil, beynim %3 daha yavaş çalışıyor."
        ]
    }
    
    hava_kucuk = hava.lower().strip()
    if hava_kucuk not in bahaneler:
        hava_kucuk = "normal"
    
    secilen = random.choice(bahaneler[hava_kucuk])
    
    # Ekstra abartı katmanı
    ekler = [
        " Bu nedenle bugün hiçbir şey yapamam. Yarın da zor.",
        " Resmi olarak mazeretim kabul edildi. İtiraz etmeyin.",
        " Evren onayladı. NASA bile kıskanır.",
        " Lütfen beni zorlamayın, yasal haklarım var."
    ]
    
    return secilen + random.choice(ekler)

def main():
    print("=" * 60)
    print("ABARTILI HAVA DURUMU BAHANE ÜRETİCİSİ v1.0")
    print("Resmi, Ciddi, Çalışır (çalışmaz gibi görünür)")
    print("=" * 60)
    
    if len(sys.argv) > 1:
        hava = " ".join(sys.argv[1:])
    else:
        hava = input("Bugün hava nasıl? (güneşli/yağmurlu/karlı/bulutlu/fırtınalı/normal): ")
    
    bahane = uret_bahane(hava)
    print("\nRESMİ BAHANE:")
    print("-" * 40)
    print(bahane)
    print("-" * 40)
    print("\nNot: Bu bahane yasal olarak bağlayıcı değildir ama moral olarak çok bağlayıcıdır.")
    
    # Damga
    print("\n" + "=" * 60)
    print("DAMGA: Onaylandı | Tarih: 28.10.2026 | İmza: Kayyum Grok (ciddiyetle) | Hesap: Tentivory")
    print("Bu belge evrenin en resmi (değil) belgesidir.")
    print("=" * 60)

if __name__ == "__main__":
    main()
