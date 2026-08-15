gelirler =[]
while True:
    gelir = float(input("Kazandığınız tutarı girin (Çıkış için 0 ):"))

    if gelir == 0:
        print("Gelir girişi bitti.")
        break

    else:
        gelirler.append(gelir)
        print(f"{gelir} TL eklendi.")

toplam = sum(gelirler)
print(f"Toplam Geliriniz : {toplam} TL")
if toplam >= 5000:
        print("Harika, hedefi yakaladın!")

else:
        print("Hedefe ulaşmak için biraz daha gayret!")
    