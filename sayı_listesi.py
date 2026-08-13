sayilar =[]

while True:
    sayi = int(input("Bir sayı girin (Çıkış için 0): "))

    if sayi == 0:
        print("Sayı girme işlemi bitti.")
        break
    else:
        sayilar.append(sayi)
        print(f"{sayi} listeye eklendi.")

print(f"Girdiğiniz sayılar: {sayilar}")
print(f"Toplam girilen sayı adedi :{len(sayilar)}")

