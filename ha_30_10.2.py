# Aufgabe1: leeres Wörterbuch
film_bewertungen = {}

#Aufgabe2: fünf Filmtitel und Bewertungen in Wörterbuch 
film_bewertungen["Avengers"] = 8
film_bewertungen["Antman"] = 7
film_bewertungen["Thor"] = 9
film_bewertungen["Spiderman"] = 8
film_bewertungen["Captain Marvel"] = 9

#Aufgabe3: Funktion die die durchschnittliche Bewertung aller Filme berechnet
def durchschnittliche_bewertung(wörterbuch):
    anzahl_filme = len(wörterbuch)
    summe_bewertungen = sum(wörterbuch.values())
    durchschnitt = summe_bewertungen / anzahl_filme
    return durchschnitt

# Aufgabe4: Funktion die den Filmtitel mit der höchsten Bewertung zurückgibt
def höchste_bewertung(wörterbuch):
    höchste_bewertung = max(wörterbuch.values())
    for film, bewertung in wörterbuch.items():
        if bewertung == höchste_bewertung:
            return film

# Aufgabe5: Funktion die eine Liste der Filmtitel zurückgibt mit 6+ Bewertung
def filme_ab_6(wörterbuch):
    filme_ab_6 = [film for film, bewertung in wörterbuch.items() if bewertung >= 6]
    return filme_ab_6

# Aufgabe6: Füge Film hinzu und aktualisiere das Wörterbuch
film_bewertungen["The incredible Hulk"] = 6

# Aufgabe7: Kontroll-Ausgabe Wörterbuch
#print("Aufgabe7: Kontrolle ob Film 6 hinzugefügt wurde:", film_bewertungen)

# Aufgabe8: Funktion durchschnittliche Bewertung, Film mit höchster Bewertung, Liste Filme mit Bewertung von 6+ zu ermitteln für Ausgabe
durchschnitt = durchschnittliche_bewertung(film_bewertungen)
höchste_bewertung_film = höchste_bewertung(film_bewertungen)
filme_ab_6_liste = filme_ab_6(film_bewertungen)

# Ausgabe Aufgabe3
#print("Aufgabe3: Durchschnittliche Bewertung:", durchschnitt)
# Ausgabe Aufgabe4
#print("Aufgabe4: Film mit der höchsten Bewertung:", höchste_bewertung_film)
# Ausgabe Aufgabe5
#print("Aufgabe5: Filme mit einer Bewertung von 6 oder höher:", filme_ab_6_liste)