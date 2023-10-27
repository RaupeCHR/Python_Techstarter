# aufgabe 1

"""name = input("gib deinen Namen ein: ")

print(f"Hi, {name}  schön das du da bist!")

#Aufgabe 2

länge = int(input("Länge eingeben in cm: "))
breite = int(input("Breite eingeben in cm: "))

print("der Flächeinhalt beträgt: ", länge * breite, " cm²")"""

# Aufgabe 3

import random

range = random.randint(1, 20)
geratene_zahl = 0
versuche = 0

while geratene_zahl != range:
    geratene_zahl = int(input("Rate eine Zahl zwischen 1 und 20: "))
    versuche += 1

    if geratene_zahl < range:
        print("Deine Zahl ist zu klein.")
    elif geratene_zahl > range:
        print("Deine Zahl ist zu Groß.")
    else:
        print(f"Glückwunsch! Du hast die Zahl {range} in {versuche} Versuchen erraten.")
        break

#Aufgabe 4
numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
duplicate_list = reversed_list * 2

print("Ursprüngliche Liste: ", numbers)
print("Umgekehrte Liste: ", reversed_list)
print("Duplizierte Liste: ", duplicate_list)


"""
#Aufgabe Tüfftler

studenten = [("Andreas", 92), ("Pablo", 88), ("Dennis", 95), ("Abi", 78), ("Evelyn", 97)]

sortierte_studenten = sorted(studenten, key=lambda x: x[1], reverse=True)

for i in range(3):
    print(f"Platz {i+1}: {sortierte_studenten[i][0]} - Note: {sortierte_studenten[i][1]}")
"""