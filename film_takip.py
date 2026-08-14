filmler = []
while True:
    sure = int(input("Film süresini dakika olarak girin (Çıkış için 0):"))

    if sure == 0:
        print("Film girişi tamamlandı.")
        break

    else:
        filmler.append(sure)
        print(f"{sure} dakikalık film eklendi.")

print(f"Toplam izlenen film sayısı: {len(filmler)}")
print(f"Toplam ilzeme süresi: {sum(filmler)} dakika")
