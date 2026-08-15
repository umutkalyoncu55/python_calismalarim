setler =[]
while True:
    agirlik = float(input("Bastığınız ağırlığı girin (KG) - ( Çıkış için 0):"))

    if agirlik == 0:
        print("Anternman kaydı tamamlandı.")
        break

    else:
        setler.append(agirlik)
        print(f"{agirlik} KG sete eklendi.")

print(f"Toplam Yaplım Set Sayısı: {len(setler)}")
print(f"Toplam Kaldırılan Ağırlık: {sum(setler)}")
print("\n--- Ağır Setler (50KG ve Üzeri) ---")
for a in setler:
    if a >= 50:
        print(f"Ağır Set: {a} KG")
        