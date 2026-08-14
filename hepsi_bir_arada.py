urunler = ["Elma", "Muz"]
fiyatlar = [15.0, 25.5]

print("=== MARKET KASASI KONTROL SİSTEMİ ===")

while True:
    islem = input("İşlem seçin (ekle / sil / bitir): ")

    if islem == "ekle":
        yeni_urun = input("Eklenecek ürün adı: ")
        yeni_fiyat = float(input("Ürünün fiyatı (TL): "))
        urunler.append(yeni_urun)
        fiyatlar.append(yeni_fiyat)
        print(f"-> {yeni_urun} sepete eklendi!")

    elif islem == "sil":
        silinecek = input("Silinecek ürün adı: ")
        if silinecek in urunler:
            urunler.remove(silinecek)  
            print(f"-> {silinecek} sepetten çıkarıldı.")
        else:
            print("-> Bu ürün zaten sepette yok!")

    elif islem == "bitir":
        print("\nAlışveriş tamamlandı, özet çıkarılıyor...")
        break

    else:
        print("-> Geçersiz işlem! Lütfen 'ekle', 'sil' veya 'bitir' yazın.")

print("========== ÖZET ==========")
print(f"Son Sepetiniz: {urunler}")


toplam_tutar = sum(fiyatlar)
print(f"Toplam Ödenecek Tutar: {toplam_tutar} TL")

print("\n--- 20 TL Üzerindeki Ürün Fiyatları ---")
for f in fiyatlar:
    if f > 20:
        print(f"Pahalı Ürün Fiyatı: {f} TL")