#1
#print("Tere maailm!")
#nimi=input("Mis on sinu nimi?") #comment
#vanus=int(input("Kui vana sa oled?")) #float()->2.5
#print("Tere tulemas! "+nimi+". Sa oled"+str(vanus)+" aastat vana")
#print("Tere tulemast! ",nimi,". Sa oled",vanus,"aastat vana")
#print("Tere tulemast! {0}.Sa oled {1} aastat vana".format(nimi,vanus))
#print("Muutuja vanus",vanus,"tüüp on",type(vanus))
#2
#vanus= 18
#eesnimi = "Jaak"
#pikkus = 16.5
#Kas käib kollis = True
#print("Muutuja vanus",eesnimi,"tüüp on",type(eesnimi))
#print("Muutuja vanus",pikkus,"tüüp on",type(pikkus))
#print("Muutuja vanus",kas_käib_koolis,"tüüp on",type(kas_käib_koolis))
#print("Muutuja vanus",pikkus,"tüüp on",type(pikkus))
#3
#from random import *
#konfeti=randint(10,100)
#print("konfeti",konfeti)
#ukral=int(input("skolko ukral"))
#konfeti-=ukral
#print("na stole teper,konfeti","konfet")
#print()
#4
#c = int(input("длинна окружности дерева"))
#summa = c/3.14
#print("диаметр окружности равен:", summa)
#5
#N = int(input("напишите первое число"))
#M = int(input("напишите первое второе число"))
#summa = N*M
#print("диагонали прямоугольного участка земли равен", summa)
#6
#try:
#    aeg = float(input("Mitu tundi kulus sõiduks?")) #aeg ei saa olla 0
#    teepikkus = float((input)"Mitu tundi kilomeetrit sõitsid?" ))
#    kiirus = teepikkus/aeg
#    print("Sinu kiirus oli " + str(kiirus) + " km/h")
#except:
#    print("Viga andmetüübiga")
#
#print()


#time = float (input ("Сколько часов ушло на поездку?") )
#Road = float (input ("Сколько километров ты проехал?") )
#speed = time/Road
#print(speed)
#7
#numbers = (1,2,3,4,5)
#summa = sum(numbers)/len(numbers)
#print(summa)
#8
#frog ="""
#    @..@
#   (----)
#  ( \__/ )
#^^ "" ^^  
#"""
#9
#a = int(input("переменная 1"))
#b = int(input("переменная 2"))
#c = int(input("переменная 3"))
#summa = a+b+c
#print("периметр треугольника:", summa)
#10
#P=randint(1,5)
#hind=12.90
#ind=1.1 #hind koos jätatega
#osa=round(hind/P,2
#print("Iga sõber maksab: ", osa)

#Pitsa = 12.90
#summa = Pitsa/10
#money = (Pitsa+summa)/2
#print(money)


#1)
#print("Kui eesnimi on Juku siis lähme kinno")
#hilimine=input("Kas teile nimi on Juku?")  
#if hilimine.lower()=="juku":
#    print("Me lähme kinno")
#from random import *
#1 Juku läheb kinno
#age=randint(-100,500) #<6 6-14 15-65 >65 <0 ja >100
#print(age, "age on tulemust")
#if age<0 or age>100:

#elif 0<age<6:
#    tulemus="tasuta pilet"
#elif 7<age<15:
#    tulemus="laste pilet"
#elif 15<=age<65:
#    tulemus="täispilet"
#elif 65<=age<100:
#    tulemus="sooduspilet"
#print(tulemus)
#print()

#print("Tere minu naabrid!")
#str(input("Naaber 1 mis sinu nimi on?"))
#str(input("Naaber 2 mis sinu nimi on?"))

#print("")
#str(input("Mis on ristkülikukujulise ruumi seinte mõõtmed?"))
#x=a*b

from datetime import *
from random import *
#14
maht=int(input("Bussi maht: "))
i=int(input("Inimesi arv: "))
ba=round(i/maht) #2;3->2
ba=1/maht
if i%maht==0:
    ba+=1
vb=i%maht
print("Kokku on vaja (0) bussi ja viimasel sõidavadm (1) inimest".format(ba,vb))












#11
#ta=date.today().year
#sp=date(int(input("Sünniaasta: ")),int(input("Sünnikuu: ")),int(input("Sünnipäev: "))).year
#if (ta-sp)%5==0:
#    print("Juubell")
#else:
#    print("Tavaline sünnipäev")


#8.2
#from datetime import *
#from random import *

#arve_nr= date.today()#datetime.now()
#print(arve_nr)
#tsekk="Arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
#summa=0
#for toode in ["Piim","Leib","Komm"]:
#    hind=randint(50,150)/100
#    v=input("Toode:"+toode+" Hind:"+str(hind)+"\nKas tahad osta?").lower()
#    if v=="jah":
#      mitu=int(input("Mitu?"))
#      tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu+hind)+"\n"
#      summa+=mitu+hind
#tsekk+="Kokku maksta: "+str(summa)
#print(tsekk)
#while True:
#    raha=float(input("Maksa "+str(summa)))
#    if raha==summa:
#        print("Tänan ostu eest!")
#        break
#    elif raha>summa:
#        print("Tänan ostu eest! Tagasi "+str(raha-summa))
#        break
#    else:
#        summa-=raha
#        print("Maksa veel"+str(summa))

#arve_nr= date.today()
#print(arve_nr)
#tsekk="arve: "+str(arve_nr)+"\nToode Hind Kogus Summa\n"
#summa=0

#for tode in ("piim","leib","kommid"):
#    hind=randint(50,100)/100
#    v=input("Toode: "+toode+" Hind: "+str(hind)+"\nKas tahad osta?").lower
#    if v=="jah":
#        mitu=int(input("Mitu? "))
#        tsekk+=toode+" "+str(hind)+" "+str(mitu)+" "+str(mitu*hind)+"\n"
#        summa+=mitu*hind
#tsekk+="Kokku maksta: "+str(summa)
#print(tsekk)
#raha=float(input("Maksa "+str(summa)))
#if raha==summa:
#    print("Tänan ostu eest!")
#elif raha>summa:
#    print("Tänan ostu eest! Tagasi "+str(raha-summa))
#else:
#    print("Maksa veel "+str(summa-raha))

#8.1
#arve_nr= date.today()
#print(arve_nr)
#tsekk="arve: "+str(arve_nr)+/"nToode Hind Kogus Summa/n"
#summa=0

#toode=Piim

#print("tsekk")
#raha=float(input("Maksa "+str(summa)))
#if raha==summa:
#    print("Tänan ostu eest!")
#elif raha>summa:
#    print("Tänan ostu eest! Tagasi "+str(raha-summa))
#else:
#    print("Maksa veel "+str(summa-raha))




#from random import *
##1 Juku läheb kinno
#nimi=input("Mis on sinu nimi?").capitalize() #anna"->"Anna"
#print("Tere", nimi) #Tere Anna
#if nimi=="Juku":
#    print("Lähme kinno")
#    vanus=int(input("Kui vanasa oled?"))
#    if vanus<0 or vanus>100:
#        pilet="vale vanus"
#    elif vanus<6:
#        pilet="tasuta pilet"
#    elif vanus<=14: #15
#        pilet="lastepilet"
#    elif vanus<=65:
#        pilet="täispilet"
#    elif vanus<=100:
#        pilet="sooduspilet"
#    print(pilet) #Ilus ja õige vastus!"Vale vanus" või "On vaja osta ...."
#else:
#    print("Ma ootan Jukut")











#from random import *
#protsent=randint(-100,500) #0-100 0-60 "2" 61-75 "3" 76-89 "4" 90-100 "5"
#print(protsent,"% on testi tulemus")
#if protsent<0 or protsent>100:
#   tulemus="valed andmed"
#elif 0<protsent<60: #protsent<0 and prosent<60 protsent<60
#   tulemus="hinne 2"
#elif 60<protsent<75:
#    tulemus="hinne 3"
#elif 75<protsent<90:
#    tulemust="hiine 4"
#elif 90<protsent<100:
#    tulemust="hiine 5"
#print(tulemust)
#print()

#arv=randint(0,100) #juhuslik täisärv vah


#from random import *
#arv=randint(0,100) #juhuslik täisarv vahemikust 0....100
#print(arv)
#if arv%2==0:
#    print(arv,"on paaris arv")
#else:
#    print(arv,"on paaris arv")
#print()


#print("Tund on alanud")
#hilimine=input("Kas on õpilane on hilinenud?") 
# "JAH"-a upper(), "jah"-a.lower(), "Jah"-.capitalize(), jaH, jAH 
#if hilimine.upper()=="JAH":
#    print("Õpilane ootab 30 min")
#print("Õpilane astub klassi")
