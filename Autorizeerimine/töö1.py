
from random import *
import smtplib
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
    Генерация случайного пароля
    """
    tähed = ascii_letters + digits + punctuation
    return ''.join(choice(tähed) for i in range(pikkus))

def kuva_kasutajad(kasutajad, paroolid):
    """
    Вывод списка пользователей и их паролей
    """
    if kasutajad:
        print("Registreeritud kasutajad:")
        for i, kasutaja in enumerate(kasutajad):
            print(f"{i+1}. Kasutajanimi: {kasutaja}, Parool: {paroolid[i]}")
    else:
        print("Hetkel pole ühtegi registreeritud kasutajat.")

# Добавляем код, который был предоставлен
import random

str0=".,:;!_*-+()/#¤%&"
str1 = '0123456789'
str2 = 'qwertyuiopasdfghjklzxcvbnm'
str3 = str2.upper()
print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
str4 = str0+str1+str2+str3
print(str4)
ls = list(str4)
print(ls)
random.shuffle(ls)
print(ls)
# Извлекаем из списка 12 произвольных значений
psword = ''.join([random.choice(ls) for x in range(12)])
# Пароль готов
print(psword)

# Список пользователей
users = []

# Генерация 5 пользователей с фиксированными почтами и паролями
for i in range(5):
    email = f"user{i+1}@example.com"
    password = "Password123"  # Простой фиксированный пароль
    users.append({"email": email, "password": password})

# Вывод сгенерированных пользователей
print("Сгенерированные пользователи:")
for i, user in enumerate(users, start=1):
    print(f"Пользователь {i}:")
    print(f"Email: {user['email']}")
    print(f"Пароль: {user['password']}")