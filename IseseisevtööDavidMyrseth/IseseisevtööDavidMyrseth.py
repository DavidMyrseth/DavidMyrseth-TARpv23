from töö1 import *

kasutajad = []
paroolid = []

while True:
    print("Valikud:")
    print("Registreerimine")
    print("Autoriseerimine")
    print("Kasutajanime muutmine")
    print("Parooli muutmine")
    print("Kõikide kasutajate kuvamine")
    print("Lõpetamine")
    valik = input("Vali tegevus: ")
    if valik == "1":
        registreeri_kasutaja(kasutajad, paroolid)
    elif valik == "2":
        autoriseeri_kasutaja(kasutajad, paroolid)
    elif valik == "3":
        muuda_kasutajanimi(kasutajad)
    elif valik == "4":
        muuda_parool(kasutajad, paroolid)
    elif valik == "5":
        kuva_kasutajad(kasutajad, paroolid)
    elif valik == "6":
        print("Programm lõpetab.")
        break
    else:
        print("Vigane valik.")
