urun = {
    "ad":  "Laptop",
    "fiyat": "15000",
  "stok": 5
}

print(f"Ürün: {urun['ad']} - Fiyatı: {urun['fiyat']} TL - Stok: {urun['stok']}")

urun["fiyat"] = 16500
urun["stok"] = 4
urun["kategori"] = "Teknoloji"

print(f"Güncel Fiyat: {urun['fiyat']} TL | Yeni Stok: {urun['stok']} | Kategori: {urun['kategori']}")

