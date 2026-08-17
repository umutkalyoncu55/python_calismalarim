def hesap_ozeti(kullanici, toplam_harcama):
    print(f"--- Sayın {kullanici.upper()} ---")
    print(f"Bu ayki toplam harcamanız: {toplam_harcama} TL")
    if toplam_harcama > 1000:
        print("Uyarı: Harcamanız yüksek, bütçeyi kontrol edin!\n")
    else:
        print("Tebrikler: Bütçeniz gayet iyi durumda.\n")

hesap_ozeti("Umut", 1500)
hesap_ozeti("Ahmet", 750)