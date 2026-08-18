import random

gizli_sayi = random.randint(1,20)
tahmin_hakki =5

print("1 ile 20 arasında bir sayı tuttum! Bulabilir misin ?")
while tahmin_hakki > 0:
    tahmin = int(input(f"\nTahmininizi girin (Kalan Hak: {tahmin_hakki}):"))
    if tahmin == gizli_sayi:
        print("TEBRİKLER! Doğru tahmin ettin!")
        break
    elif tahmin < gizli_sayi:
        print("Daha BÜYÜK bir sayı söyle!")
    else:
        print("Daha KÜÇÜK bir sayı söyle!")

    tahmin_hakki -= 1

if tahmin_hakki == 0:
    print(f"\n Maalesef hakkın bitti! Tuttuğum sayı: {gizli_sayi} idi.")
