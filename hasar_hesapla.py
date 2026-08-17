def hasar_hesapla(sdiran_guc, savunma_puanı):
    net_hasar = sdiran_guc - savunma_puanı
    if net_hasar <  0:
        net_hasar = 0
    return net_hasar

vurus1_hasar = hasar_hesapla(85, 30)
print(f"1. Vuruşta Verilen Net Hasar: {vurus1_hasar}")
vurus2_hasar = hasar_hesapla(40, 50)
print(f"2. Vuruşta Verilen Net Hasar: {vurus2_hasar}")
