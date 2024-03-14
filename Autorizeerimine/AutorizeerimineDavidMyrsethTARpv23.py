from töö1 import *

kasutajad = []
paroolid = []

while True:
    print("Valikud:")
    print("1.Registreerimine")
    print("2.Autoriseerimine")
    print("3.Kasutajanime muutmine")
    print("4.Parooli muutmine")
    print("5.Kõikide kasutajate kuvamine")
    print("6.Lõpetamine")
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
