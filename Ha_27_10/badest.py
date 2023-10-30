mathematik = [80, 85, 90, 78, 92, 88, 76, 89, 95, 82]
physik = [75, 88, 82, 79, 91, 86, 77, 90, 94, 81]
chemie = [70, 84, 88, 76, 89, 82, 74, 87, 92, 79]

def beste_schlechteste_noten(lst):
    beste_note = max(lst)
    schlechteste_note = min(lst)
    return [beste_note, schlechteste_note]

mathematik_noten = beste_schlechteste_noten(mathematik)
physik_noten = beste_schlechteste_noten(physik)
chemie_noten = beste_schlechteste_noten(chemie)

print("Die besten und schlechtesten Noten in Mathematik sind:", mathematik_noten)
print("Die besten und schlechtesten Noten in Physik sind:", physik_noten)
print("Die besten und schlechtesten Noten in Chemie sind:", chemie_noten)