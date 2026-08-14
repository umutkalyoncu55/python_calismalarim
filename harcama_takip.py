harcamalar = []
while True:
    tutar = float(input("Harcama tutarı girin (Çıkış için 0):"))
    if tutar == 0:
        print("Harcama girişi bitti.")
        break
    else:
        harcamalar.append(tutar)
        print(f"{tutar} TL eklendi")

print("\n--- HARCAMA ÖZETİ ---")
print(f"Girdiğiniz Harcamalar : {harcamalar}")
print(f"Toplam Harcama: {sum(harcamalar)} TL")

print("\n--- BÜYÜK HARCAMALAR (100TL) ---")
for h in harcamalar:
    if h >= 100:
        print(f"Büyük Harcama: {h} TL")



