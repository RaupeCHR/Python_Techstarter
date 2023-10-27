# Spedition soll 1000 Kistenausliefern der LKW schafft pro Fahrt nur 75
count_boxes = 1000
boxes_perdrive = 75

# Berechnung der Fahrten
count_drives = count_boxes // boxes_perdrive + 1
boxes_lastdrive = count_boxes % boxes_perdrive

# Ausgabe der Ergebnisse
print("Anzahl der Fahrten:", count_drives)
print("Kisten bei der letzen Fahrt:", boxes_lastdrive)
