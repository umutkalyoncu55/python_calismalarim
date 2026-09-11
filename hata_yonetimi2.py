class YasSiniriHatasi(Exception):
    """Kullanıcı 18 yasşından küçük olduğunda fırlatılacak özel hata sınıfı."""
    pass

while True:
    try:
        yas = int(input("Lütfen yaşınızı giriniz: "))
        if yas < 18:
            raise YasSiniriHatasi("Sistemimize 18 yaşından küçükler kayıt olamaz!")
        
    except ValueError:
        print("Hata: Lütfen sadece sayısal bir değer giriniz!\n")

    except YasSiniriHatasi as hata_mesaji:
        print(f"Özel Hata Yakalandı: {hata_mesaji}\n")

    else:
        print(f"Kayıt başarılı! Yaşınız: {yas}")
        break

                  