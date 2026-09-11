while True:
    try:
        yas = int(input("Lütfen yaşınızı giriniz: "))
    except ValueError:
        print("Hata: Lütfen sadece sayısal bir değer giriniz.")
    else:
        print(f"Kayıt başarılı, yaşınız: {yas}")
        break