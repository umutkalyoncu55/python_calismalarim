hedef = 7
hak = 3

while hak > 0:
    tahmin = int(input("1-10 arasında bir sayı tahmin edin:"))

    if tahmin ==hedef:
        print("Tebrikler! Doğru tahmin ettiniz.")
        break

    else:
        hak -= 1
        print(f"Yanlış tahmin. Kalan hakkınız: {hak}")

if hak == 0:
    print(f"Üzgünüz, hakkınız kalmadı. Doğru sayı {hedef} idi.")
    
                       