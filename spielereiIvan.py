"""print("Hello Guy")

my_name = input("Wie heißt du ? ")
print(f"Hi {my_name} ,ich freue mich dich hier zu sehen!")

my_age = int(input("Wie alt bist du ?"))
print(f"Oh wirklich ? Dass heißt du wirst im Jahr 2040 {my_age  +17} Jahre alt.")
"""
import random

def hangman():
    wortliste = [
    "Apfel", "Banane", "Kirsche", "Orange", "Erdbeere", "Himbeere", "Birne", "Pfirsich", "Mango", "Ananas",
    "Tomate", "Gurke", "Karotte", "Kartoffel", "Zwiebel", "Brokkoli", "Blumenkohl", "Spinat", "Salat", "Paprika",
    "Huhn", "Rind", "Schwein", "Lamm", "Fisch", "Garnelen", "Thunfisch", "Forelle", "Lachs", "Schinken",
    "Brot", "Nudeln", "Reis", "Kartoffelchips", "Cracker", "Müsli", "Haferflocken", "Cornflakes", "Toast", "Croissant",
    "Kaffee", "Tee", "Orangensaft", "Apfelsaft", "Cola", "Limonade", "Mineralwasser", "Eistee", "Milch", "Smoothie",
    "Schokolade", "Eis", "Kuchen", "Keks", "Praline", "Donut", "Muffin", "Pudding", "Waffel", "Marshmallow",
    "Hund", "Katze", "Pferd", "Kuh", "Schwein", "Hase", "Huhn", "Fuchs", "Löwe", "Elefant",
    "Auto", "Fahrrad", "Motorrad", "Bus", "Zug", "Flugzeug", "Schiff", "Traktor", "Taxi", "U-Bahn",
    "Buch", "Zeitung", "Zeitschrift", "Roman", "Krimi", "Fantasy", "Biografie", "Kochbuch", "Sachbuch", "Gedicht",
    "Computer", "Handy", "Tablet", "Fernseher", "Kamera", "Lautsprecher", "Drucker", "Smartwatch", "Spielekonsole", "Kopfhörer",
    "Schule", "Universität", "Klassenzimmer", "Lehrer", "Schüler", "Hausaufgaben", "Prüfung", "Studium", "Vorlesung", "Bibliothek",
    "Musik", "Film", "Theater", "Konzert", "Oper", "Tanz", "Kunst", "Ausstellung", "Museum", "Literatur",
    "Sommer", "Herbst", "Winter", "Frühling", "Sonne", "Regen", "Schnee", "Wolken", "Wind", "Blume",
    "Sport", "Fußball", "Basketball", "Tennis", "Schwimmen", "Laufen", "Radfahren", "Fitness", "Yoga", "Golf",
    "Reisen", "Urlaub", "Strand", "Meer", "Berge", "Stadt", "Sehenswürdigkeit", "Abenteuer", "Rucksack", "Koffer",
    "Liebe", "Freundschaft", "Familie", "Hochzeit", "Geburtstag", "Jubiläum", "Valentinstag", "Muttertag", "Vaterstag", "Weihnachten",
    "Haus", "Wohnung", "Garten", "Schlafzimmer", "Küche", "Bad", "Wohnzimmer", "Esszimmer", "Balkon", "Terrasse",
    "Beruf", "Arbeit", "Büro", "Kollege", "Chef", "Meeting", "Projekt", "Präsentation", "Karriere", "Erfolg",
    "Gesundheit", "Ernährung", "Fitness", "Entspannung", "Yoga", "Meditation", "Schlaf", "Stress", "Sport", "Wellness",
    "Wissenschaft", "Forschung", "Experiment", "Entdeckung", "Labor", "Theorie", "Analyse", "Hypothes", "Studie", "Daten",
    "Technologie", "Innovation", "Entwicklung", "Programmierung", "Künstliche Intelligenz", "Robotik", "Virtual Reality", "App", "Software", "Hardware",
    "Natur", "Tiere", "Umwelt", "Wald", "Wiese", "Fluss", "See", "Berg", "Wüste", "Ozean",
    "Mode", "Kleidung", "Schuhe", "Tasche", "Accessoire", "Schmuck", "Schminke", "Parfum", "Brille", "Hut"
]



    wort = random.choice(wortliste)
    buchstaben = list(wort)
    spieler_wort = ["_"] * len(wort)
    versuche = 10
    gewonnen = False
    
    print("Willkommen bei Hangman! Du Hast 10 Versuche!")
    
    while versuche > 0 and not gewonnen:
        print("".join(spieler_wort))
        buchstabe = input("Rate einen Buchstaben: ")
        
        if buchstabe in buchstaben:
            for i in range(len(buchstaben)):
                if buchstaben[i] == buchstabe:
                    spieler_wort[i] = buchstabe
            if "_" not in spieler_wort:
                gewonnen = True
        else:
            versuche -= 1
            print("Falsch geraten! Du hast noch", versuche, "Versuche übrig.")
    
    if gewonnen:
        print("Glückwunsch! Du hast das Wort geraten:", wort)
    else:
        print("Leider verloren! Das Wort war:", wort)

hangman()