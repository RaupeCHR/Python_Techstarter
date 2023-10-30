mathematik = [80, 85, 90, 78, 92, 88, 76, 89, 95, 82]
physik = [75, 88, 82, 79, 91, 86, 77, 90, 94, 81]
chemie = [70, 84, 88, 76, 89, 82, 74, 87, 92, 79]

def durchschnittsnote(noten):
    summe = sum(noten)
    anzahl = len(noten)
    durchschnitt = summe / anzahl
    return durchschnitt


durchschnitt_mathematik = durchschnittsnote(mathematik)
durchschnitt_physik = durchschnittsnote(physik)
durchschnitt_chemie = durchschnittsnote(chemie)

print("Durchschnittsnote Mathematik:", durchschnitt_mathematik)
print("Durchschnittsnote Physik:", durchschnitt_physik)
print("Durchschnittsnote Chemie:", durchschnitt_chemie)