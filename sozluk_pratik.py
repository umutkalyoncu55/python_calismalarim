oyuncu = {
    "kullanici_adi": "Umut",
    "seviye": 1,
    "can": 100
}

print(f"Oyuncu Adı: {oyuncu['kullanici_adi']}")
print(f"Başlangıç Seviyesi: {oyuncu['seviye']}")

oyuncu["seviye"] = 2
oyuncu["can"] = 120
oyuncu["unvan"] = "Savaşçı"

print("\n--- GÜNCEL OYUNCU PROFİLİ ---")
print(f"Yeni Seviye: {oyuncu['seviye']}")
print(f"Yeni Can: {oyuncu['can']}")
print(f"Unvan: {oyuncu['unvan']}")
