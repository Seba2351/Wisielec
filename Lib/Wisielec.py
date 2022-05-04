import random

print(" Podaj swoje Imię: ")
imie = input()
lista = ["python", "studia", "gdynia", "nauka", "zaliczenie"]

haslo = str(lista[random.randint(0, len(lista) - 1)])
tablica = list(haslo)
proby = 5
print("Witaj", imie, "zagrajmy w grę odgadnij hasło masz", proby, "prób zanim zginiesz", )

for i in range(len(haslo)):
    tablica[i] = "*"

while proby > 0:
    print("")
    print(imie, " pozostalo ci ", proby, " prób")
    print("")
    print(" ".join(tablica))
    print(" ")

    print("Podaj litere: ")
    litera = input()

    if litera in haslo:

        for i in range(len(haslo)):
            if haslo[i] == litera:
                tablica[i] = litera

        if "".join(map(str, tablica)) == haslo:
            print("")
            print(imie, " pozostalo ci ", proby, " prób")
            print("")
            print(" ".join(tablica))
            print(" ")
            print(imie, " Brawo wygrales!")
            break

    else:
        proby -= 1
        print("")
        print("Pudło, litery", litera, "nie ma w haśle")

        if proby == 0:
            print("")
            print("Pozostalo ci", proby, "prób, koniec gry przegrałeś! Ukrytym hasłem bylo:", haslo)
            break