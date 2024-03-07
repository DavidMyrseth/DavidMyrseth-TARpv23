from random import *
from string import *

def registreeri_kasutaja(kasutajad, paroolid):
    """
    """
    nimi = input("Sisesta kasutajanimi: ")
    if nimi in kasutajad:
        print("Kasutajanimi on juba võetud.")
        return False

    valik = input("Kas soovid luua parooli (L) või lasta luua automaatselt (A)? ").upper()
    if valik == "L":
        parool = input("Sisesta parool: ")
    elif valik == "A":
        parool = genereeri_parool()
    else:
        print("Vigane valik.")
        return False
    kasutajad.append(nimi)
    paroolid.append(parool)
    print("Kasutaja registreeritud.")
    return True

def autoriseeri_kasutaja(kasutajad, paroolid):
    """
    """
    nimi = input("Sisesta kasutajanimi: ")
    if nimi not in kasutajad:
        print("Sellist kasutajat ei ole.")
        return False
    parool = input("Sisesta parool: ")
    if parool != paroolid[kasutajad.index(nimi)]:
        print("Vale parool.")
        return False
    print("Autoriseeritud!")
    return True

def muuda_kasutajanimi(kasutajad):
    """
    """
    vana_nimi = input("Sisesta vana kasutajanimi: ")
    if vana_nimi not in kasutajad:
        print("Sellist kasutajat ei ole.")
        return False
    uus_nimi = input("Sisesta uus kasutajanimi: ")
    if uus_nimi in kasutajad:
        print("Uus kasutajanimi on juba võetud.")
        return False
    indeks = kasutajad.index(vana_nimi)
    kasutajad[indeks] = uus_nimi
    print("Kasutajanimi edukalt muudetud.")
    return True

def muuda_parool(kasutajad, paroolid):
    """
    """
    nimi = input("Sisesta kasutajanimi: ")
    if nimi not in kasutajad:
        print("Sellist kasutajat ei ole.")
        return False

    uus_parool = input("Sisesta uus parool: ")
    paroolid[kasutajad.index(nimi)] = uus_parool
    print("Parool edukalt muudetud.")
    return True

def genereeri_parool(pikkus=12):
    """
    """
    tähed = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(tähed) for i in range(pikkus))

def kuva_kasutajad(kasutajad, paroolid):
    """
    """
    if kasutajad:
        print("Registreeritud kasutajad:")
        for i, kasutaja in enumerate(kasutajad):
            print(f"{i+1}. Kasutajanimi: {kasutaja}, Parool: {paroolid[i]}")
    else:
        print("Hetkel pole ühtegi registreeritud kasutajat.")
