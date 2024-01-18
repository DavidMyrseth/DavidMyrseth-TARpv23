print("Tere! Olen sinu uus sõber - Python!")
nimi = input("Mis on sinu nimi on?")
print(nimi, ", oi kui ilus nimi!")
vastus=int(input(nimi + "! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
print("index")
if vastus==1:
    height = float(input("Write your height>"))
    mass = int(input("Write your mass>"))
    index = mass/(0.01*height)**2
    print("! Sinu keha indeks on:", round(index))
else:
    print("okay bye")
    print()





