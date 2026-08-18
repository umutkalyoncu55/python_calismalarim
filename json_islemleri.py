import json

with open("kullanici.json", "r", encoding="utf-8") as dosya:
    veri = json.load(dosya)

print("--- JSON DOSYASINDAN OKUNAN VERİLER ---")
print(f"Kullanıcı Adı : {veri['isim']}")
print(f"Yaş           : {veri['yas']}")
print(f"Ana Hedef     : {veri['hedef']}")
print(f"Bitti Dersler : {veri['tamamlanan_dersler']}")
