import datetime

suan = datetime.datetime.now()

print(f"Şu anki tam zaman: {suan}")
print(f"Bugünün Tarihi: {suan.strftime('%d/%m/%Y')}")
print(f"Saat: {suan.strftime('%H:%M')}")

