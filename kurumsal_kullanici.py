class Kullanici:
    def __init__(self, isim, eposta):
        self.isim = isim
        self.eposta = eposta

    def bilgileri_goster(self):
        print(f"Kullanıcı: {self.isim} | E-posta: {self.eposta}")

class KurumsalKullanici(Kullanici):
    def __init__(self, isim, eposta, sirket_adi):
        super().__init__(isim, eposta)
        self.sirket_adi = sirket_adi

    def fatura_kes(self):
        print(f"{self.sirket_adi} sirketi adına fatura kesildi!")
        print(f"Yetkili: {self.isim} ({self.eposta})")        

sirket_hesabi = KurumsalKullanici("Umut", "umut@sirket.com", "Kalyoncu Medya")
sirket_hesabi.bilgileri_goster()
sirket_hesabi.fatura_kes()


