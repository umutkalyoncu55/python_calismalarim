notlar = []

while True :
    not_girdi = int(input("Not girin (Çıkış için -1): "))

    if not_girdi == -1:
        print("Not girişi tamamlandı.")
        break
    else:
        notlar.append(not_girdi)
        print(f"{not_girdi} notu eklendi.")

print("\n--- SINAV ANALİZİ ---")
print(f"Girdiğiniz Notlar: {(notlar)}")
print(f"Notların Toplamı: {sum(notlar)}")

print("\n--- GEÇEN ÖĞRENCİLER (50+) ---")
for n in notlar:
    if n >= 50:
        print(f"Geçti {n}")
        

