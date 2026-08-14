siparisler = []
while True:
    siparis = input("Sipariş girin (Çıkış için 'tamam'):")
    if siparis == "tamam":
        print("Sipariş alma bitti.")
        break

    else:
        siparisler.append(siparis)
        print(f"{siparis} siparişe eklendi.")

print(f"Toplam Sipariş Sayısı: {len(siparisler)}")
print(f"Sipariş Listeniz: {siparisler}")