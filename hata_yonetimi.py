try:
    sayi = int(input("Lütfen bir sayı girin: "))
    print(f"Girdiğiniz sayının 2 kat: {sayi * 2} ")

except ValueError:
    print("HATA: Lütfen harf değil, geçerli bir sayı girin!")

print(" program çökmeyip çalışmaya devam etti!")
