bakiye = 500
while True:
    print(f"--- Mağaza (Bakiyeniz: {bakiye} TL) ---")
    secim = input("1-Kulaklık (150TL), 2-Klavye (200TL), 3-Çıkış:")

    if secim == "1":
        if bakiye >= 150:
            bakiye -= 150
            print(f"Kulaklık alındı! Kalan bakiye: {bakiye} TL")
        else:
            print("Yetersiz bakiye!")

    elif secim == "2":
        if bakiye >= 200:
            bakiye -= 200
            print(f"Klavye alındı! Kalan bakiye: {bakiye} TL")

        else:
            print("Yetersiz bakiye")

    elif secim == "3":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz Seçim!")
        
