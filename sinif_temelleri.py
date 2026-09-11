class Sporcu:
    def __init__(self, isim, yas, kilo):
        self.isim = isim
        self.yas = yas
        self.kilo = kilo

    def bilgi_ver(self):
        print(f"Sporcu: {self.isim} | Kilo: {self.kilo} kg")

    def kilo_al(self, miktar):
        self.kilo += miktar
        print(f"{self.isim} {miktar} kg aldı! Güncel Kilo: {self.kilo} kg")

    def kilo_ver(self, miktar):
        self.kilo -= miktar
        print(f"{self.isim} {miktar} kg verdi! Güncel Kilo: {self.kilo} kg")

sporcu1 = Sporcu("Umut", 24, 66.9)
sporcu1.bilgi_ver()
sporcu1.kilo_al(2.5)
sporcu1.kilo_ver(1.0)
