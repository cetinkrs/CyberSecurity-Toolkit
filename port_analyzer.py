hedef_portlar={
    80: "open",
    22: "closed",
    443: "open",
    21: "open"
}
def port_tarama(gelen_portlar: dict) -> list:
    """
    Bu fonkiyon bir port sözlüğünü alır, sadece durumu "open" olanları  ayıklar ve tehkikeli portların listesini geri döndürür.
    """
    acik_portlar=[]
    for port_numarasi, port_durumu in gelen_portlar.items():
        if port_durumu == "open":
            acik_portlar.append(port_numarasi)
    return acik_portlar
tehlikeli_portlar = port_tarama(hedef_portlar)

if tehlikeli_portlar:
    print(f"Sistemde açık portlar tespit edildi ve düzeltilmesi gerek:{tehlikeli_portlar}")
else:
    print("Sistemde herhangi bir açık port yoktur.")
