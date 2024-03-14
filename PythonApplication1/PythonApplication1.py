import random
import smtplib
import string
# Словарь для хранения пользователей и их паролей
kasutajad_paroolidega = {}
# Словарь для хранения сообщений пользователей
saadetud_sonumid = {}
def registreeri_kasutaja():
    """
    Регистрация нового пользователя
    """
    nimi = input("Sisesta kasutajanimi: ")
    if nimi in kasutajad_paroolidega:
        print("Kasutajanimi on juba võetud.")
        return False

    parool = input("Sisesta parool: ")
    kasutajad_paroolidega[nimi] = parool
    saadetud_sonumid[nimi] = []  # Инициализация пустого списка сообщений для нового пользователя
    print("Kasutaja registreeritud.")
    return True
def autoriseeri_kasutaja():
    """
    Авторизация пользователя
    """
    nimi = input("Sisesta kasutajanimi: ")
    if nimi not in kasutajad_paroolidega:
        print("Sellist kasutajat ei ole.")
        return False
    
    parool = input("Sisesta parool: ")
    if parool != kasutajad_paroolidega[nimi]:
        print("Vale parool.")
        return False
    
    print("Autoriseeritud!")
    return True
def saada_sonum():
    """
    Отправка сообщения другому пользователю
    """
    saatja = input("Sisesta oma kasutajanimi: ")
    if saatja not in kasutajad_paroolidega:
        print("Sellist kasutajat ei ole.")
        return False
    
    vastuvoetud = input("Sisesta saaja kasutajanimi: ")
    if vastuvoetud not in kasutajad_paroolidega:
        print("Sellist saajat ei ole.")
        return False
    
    sonum = input("Sisesta oma sõnum: ")
    saadetud_sonumid[vastuvoetud].append((saatja, sonum))
    print("Sõnum saadetud.")
    return True
def kuva_sonumid():
    """
    Отображение сообщений для пользователя
    """
    kasutaja = input("Sisesta oma kasutajanimi: ")
    if kasutaja not in kasutajad_paroolidega:
        print("Sellist kasutajat ei ole.")
        return False

    sonumid = saadetud_sonumid[kasutaja]
    if sonumid:
        print(f"Sulle saadetud sõnumid:")
        for saatja, sonum in sonumid:
            print(f"Saatja: {saatja}, Sõnum: {sonum}")
    else:
        print("Sulle pole saadetud sõnumeid.")
    return True
def kuva_kasutajad_paroolidega():
    """
    Отображение зарегистрированных пользователей и их паролей
    """
    print("Registreeritud kasutajad ja nende paroolid:")
    for kasutaja, parool in kasutajad_paroolidega.items():
        print(f"Kasutajanimi: {kasutaja}, Parool: {parool}")

# Простой цикл, позволяющий пользователю выбирать действия
while True:
    print("\nVali tegevus:")
    print("1. Registreeri kasutaja")
    print("2. Autoriseeri kasutaja")
    print("3. Saada sõnum")
    print("4. Kuva saadetud sõnumid")
    print("5. Kuva kasutajad ja nende paroolid")
    print("6. Välju")

    valik = input("Valik: ")

    if valik == "1":
        registreeri_kasutaja()
    elif valik == "2":
        autoriseeri_kasutaja()
    elif valik == "3":
        saada_sonum()
    elif valik == "4":
        kuva_sonumid()
    elif valik == "5":
        kuva_kasutajad_paroolidega()
    elif valik == "6":
        print("Programm lõpetab töö.")
        break
    else:
        print("Vigane valik. Palun vali uuesti.")

