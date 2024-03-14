def failide_kustutamine():
    """
    """
    failinimi=input("Mis fail tahad eemaldada?") #path.isdir("Kaust")
    if path.isfile(failinimi):
        remove(failinimi)
        print(f"Fail {failinimi} oli kustutatud")
    else:
        print(f"Fail {failinimi} puudub")
