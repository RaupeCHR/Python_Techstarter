def caesar_entschluesseln(verschluesselter_text, schluessel):
    entschluesselter_text = ""
    for zeichen in verschluesselter_text:
        if zeichen.isalpha():
            ascii_wert = ord(zeichen)
            if zeichen.islower():
                entschluesselter_buchstabe = chr((ascii_wert - schluessel - 97) % 26 + 97)
            else:
                entschluesselter_buchstabe = chr((ascii_wert - schluessel - 65) % 26 + 65)
            entschluesselter_text += entschluesselter_buchstabe
        else:
            entschluesselter_text += zeichen
    return entschluesselter_text

def main():
    while True:
        nachricht = input("Geben Sie die zu verschlüsselnde/entschlüsselnde Nachricht ein: ")
        schluessel = int(input("Geben Sie den Verschlüsselungsschlüssel ein (eine Ganzzahl zwischen -25 und +25): "))
        modus = input("Möchten Sie die Nachricht verschlüsseln (V) oder entschlüsseln (E)? ")

        if schluessel < -25 or schluessel > 25:
            print("Ungültiger Schlüssel. Der Schlüssel muss eine ganze Zahl zwischen -25 und +25 sein.")
            continue

        if modus.upper() == "V":
            verschluesselter_text = caesar_entschluesseln(nachricht, schluessel)
            print("Verschlüsselter Text:", verschluesselter_text)
        elif modus.upper() == "E":
            entschluesselter_text = caesar_entschluesseln(nachricht, -schluessel)
            print("Entschlüsselter Text:", entschluesselter_text)
        else:
            print("Ungültiger Modus. Bitte wählen Sie entweder 'V' für Verschlüsselung oder 'E' für Entschlüsselung.")

        weiter = input("Möchten Sie eine weitere Nachricht verschlüsseln oder entschlüsseln? (J/N): ")
        if weiter.upper() != "J":
            break

if __name__ == "__main__":
    main()
