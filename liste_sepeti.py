sepet = []

while True:
    print("---Sepet Uygulaması---")
    secim = input("1-Ekle, 2-Çıkar, 3-Göster, 4-Çıkış: ")

    if secim == "1":
        urun = input("Eklenecek ürün: ")
        sepet.append(urun)
        print(f"{urun} sepete eklendi.")

    elif secim == "2":
        urun = input("Çıkarılacak ürün: ")
        if urun in sepet:
            sepet.remove(urun)
            print(f"{urun} sepetten çıkarıldı.")
        else:
            print(f"{urun} zaten sepetinizde yok!")

    elif secim == "3":
        print(f"Sepetinizdeki ürünler: {sepet}")  # {sepet} eklendi!
        print(f"Toplam ürün sayısı: {len(sepet)}")

    elif secim == "4":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz seçim!")
