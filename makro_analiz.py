def besin_kalori_hesapla(besin):
    p = besin["protein"]
    k = besin["karbonhidrat"]
    y = besin["yag"]
    return (p * 4) + (k * 4) + (y * 9)

pilav_tavuk = {
    "ad": "Tavuklu Pilav",
    "protein": 40,
    "karbonhidrat": 60,
    "yag": 8
}

toplam = besin_kalori_hesapla(pilav_tavuk)
print(f"{pilav_tavuk['ad']} Öğünün Kalorisi: {toplam} kcal")
