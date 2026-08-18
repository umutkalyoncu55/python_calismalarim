def kalori_hesapla(protein, karb, yag):
    return (protein * 4) + (karb * 4) + (yag * 9)

ogunler = [
    {"ad": "Yulaf & Rice Cream", "p": 25, "k": 60, "y": 6},
    {"ad": "Tavuklu Pilav", "p":45, "k":70, "y":10},
    {"ad": "Ton Balıklı Salata", "p":30, "k": 10, "y": 12}
]

gunluk_hedef_kalori = 2500
toplam_kalori = 0
toplam_protein = 0

print("--- GÜNLÜK ÖĞÜN ÖZETİ ---")
for ogun in ogunler:
    ogun_kalorisi = kalori_hesapla(ogun["p"], ogun["k"], ogun["y" ])
    toplam_kalori += ogun_kalorisi
    toplam_protein += ogun["p"]
    print(f"- {ogun['ad']}: {ogun_kalorisi} kcal (Protein: {ogun['p']}g)")

print("--------------------")
print(f"Toplam Alınan Kalori: {toplam_kalori} / {gunluk_hedef_kalori} kcal")
print(f"Toplam Alınan Protein: {toplam_protein}g")

if toplam_kalori > gunluk_hedef_kalori:
    print("Uyarı: Günlük kalori hedefini aştın!")
else:
    kalan = gunluk_hedef_kalori - toplam_kalori
    print(f"Hedefe ulaşmak için kalan kalori: {kalan} kcal")
