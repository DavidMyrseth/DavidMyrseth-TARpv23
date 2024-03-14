from os import system
from gtts import *
def loe_failist(fail:str):
    """Loeme Failist read ja salvestame järjendisse. Funktsioon
    tagastab järjend
    parem str fail:
    rtype: list
    """

    f=open(fail,'r',endcoding="utf-8")
    järjend=[]
    for rida in f:
        järjend.append(rida.strip())
    f.close()
    return järjend

def kirjuta_failist(fail:str,jarjend=[]):
    """
    """
    n=int(input("Sissesta mitu elemendi: "))
    for i in range(n):
        jarjend.append(input(f"{i+1}, element: "))
        f=open(fail,'w',endcording="utf-8")
        for el in jarjend:
            f.write(el+"\n")
        f.close()

def heli(text:str, keel:str):
    obj=gTTS(text=tekst, lang=keel,slow=False).save("heli.mp3")
    system("heli.mp3")

    tekst=input("Sissesta tekst: ")
    heli(tekst,'et')

kirjuta_failist("Text.tekst")

paevad=loe_failist("Paevad.txt")
print(paevad)
