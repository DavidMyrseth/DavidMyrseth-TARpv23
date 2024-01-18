print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Mis on sinu nimi on?")
print(nimi, ", oi kui ilus nimi!")
vastus=int(input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
if vastus==1:
    try:
        height = float(input("Write your height>"))
    except:
        ValueError
    try:
        mass = int(input("Write your mass>"))
    except:
        ValueError
    index = mass/(0.01*height)**2
    print("! Sinu keha indeks on:", round(index))
    if index <16:
        print("Tervisele ohtlik alakaal")
    elif index <=19:
        print("Alakaal")
    elif index <=25:
        print("Normaalkaal")
    elif index <=30:
        print("Ülekaal")
    elif index <=35:
        print("Rasvumine")
    elif index <=40:
        print("Tugev rasvumine")
    elif index >40:
        print("Tervisele ohtlik rasvumine")
    else:
        print("Kahju! See on väga kasulik info!")
        print()
print("Kohtumiseni, " + nimi + "! Igavesti Sinu, Python!")