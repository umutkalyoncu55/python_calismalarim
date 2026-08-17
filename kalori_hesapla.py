def kalori_hesapla(protein, karbonhidrat, yag):
    toplam = (protein * 4) + (karbonhidrat * 4) + (yag * 9)
    return toplam

ogun_kalori = kalori_hesapla(30, 50 ,10)
print(f"Öğünün Toplam Kalorisi: {ogun_kalori} kcal")

