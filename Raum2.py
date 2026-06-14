# --- RAUM 2: DIE DATEN-BIBLIOTHEK ---
print("\n--- RAUM 2: DIE DATEN-BIBLIOTHEK ---")
print("Hier stehen tausende Bücher über Datenstrukturen.")
print("Um den Ausgang zu finden, musst du ein Rätsel lösen.")

antwort3 = input("Wie nennt man eine Liste in Python, die man NICHT mehr verändern kann? (Tipp: fängt mit 'T' an): ")

if antwort3.lower() == "tuple" or antwort3.lower() == "tupel":
    print("\n🔓 Großartig! Die finale Geheimtür öffnet sich!")
    if "Schlüssel" in inventar:
        print("🔑 Du benutzt den Schlüssel aus Raum 1 und schließt das Tor auf!")
        print("🏆 FREIHEIT! Du hast die Python-Prüfung erfolgreich überstanden!")
    else:
        print("🔒 Die Tür ist abgeschlossen und du hast keinen Schlüssel in Raum 1 gefunden... Du bist gefangen!")
else:
    print("\n❌ Falsche Antwort! Die Bibliothek stürzt über dir zusammen. Game Over!")