bakiye = 100
while True:
    secim = input("1-Yatır, 2-Çek, 3-Bakiye Sorgula, 4-Çıkış: ")

    if secim == "1":
        tutar = int(input("Yatırılacak tutar:"))
        bakiye += tutar
        print(f"Yeni bakiye: {bakiye}")

    elif secim == "2":
        tutar = int(input("Çekilecek tutar :"))
        if tutar > bakiye:
            print("Yetersiz bakiye!")
        else:
            bakiye -= tutar
            print(f"Yeni bakiye: {bakiye}")

    elif secim == "3":
        print(f"Mevcut bakiye: {bakiye}")

    elif secim =="4":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim! Lütfen 1-4 arasında bir sayı girin.")