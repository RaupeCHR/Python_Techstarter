mathematik = [80, 85, 90, 78, 92, 88, 76, 89, 95, 82]
physik = [75, 88, 82, 79, 91, 86, 77, 90, 94, 81]
chemie = [70, 84, 88, 76, 89, 82, 74, 87, 92, 79]

anzahl_schueler = []

fach_noten = [mathematik, physik, chemie]

for fach in fach_noten:
    anzahl = sum(1 for note in fach if note >= 90)
    anzahl_schueler.append(anzahl)

print("Die Anzahl der Schüler, die in jedem Fach eine Note von mindestens 90 erreicht haben, ist:", anzahl_schueler)
