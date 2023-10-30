mathematik = [80, 85, 90, 78, 92, 88, 76, 89, 95, 82]
physik = [75, 88, 82, 79, 91, 86, 77, 90, 94, 81]
chemie = [70, 84, 88, 76, 89, 82, 74, 87, 92, 79]
noten = mathematik + physik + chemie

noten_haeufigkeit = {}

for note in noten:
    if note in noten_haeufigkeit:
        noten_haeufigkeit[note] += 1
    else:
        noten_haeufigkeit[note] = 1

print("Die Häufigkeit jeder Note in dem Fach ist:")
for note, haeufigkeit in noten_haeufigkeit.items():
    print("Note:", note, "- Häufigkeit:", haeufigkeit)
