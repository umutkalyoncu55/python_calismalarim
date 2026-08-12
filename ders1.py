dogru_sifre = "1234"

hak = 3

while hak > 0:
    girilen_sifre = input(f"Şifrenizi giriniz (Kalan hakkınız: {hak}):")
    if girilen_sifre == dogru_sifre:
        print("Giriş başarılı! Hoş geliniz.")
        break

    hak = hak - 1

    if hak > 0:
        print("Hatalı şifre!")

    if hak ==0:
        print("3 defa hatalı şifre girdiniz. Kartınız bloke oldu!")
