# Funtion zur Bestimmung der Ranges
def do_something(x, y):
    if x in range(1, 101) and y in range(10, 21):
        return "VALID RANGE"  # wenn in Bereich das ausgabe VALID
    return "INVALID RANGE"    # wenn nicht im Bereich dann ausgabe INVALID

# Ausgabe der Ergebnisse
result = do_something(90, 12)
print(result)