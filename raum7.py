#so könnte so ein Raum aussehen.

def raum_7():
    global leben
    print("\n=== Raum 3: Die Python-Höhle ===")
    
    # 1. Die Story/Beschreibung
    print("Eine riesige Python versperrt dir den Weg.")
    
    # 2. Die Eingabe
    antwort = input("Wie nennt man eine Liste von Werten in Python? ")[[1, 2], [3, 4]]
    
    # 3. Die Konsequenzen (Spiel-Logik!)
    if antwort.lower() == "liste" or antwort.lower() == "list":
        print("Die Schlange lässt dich passieren!")
        return True # Der Spieler darf weiter
    else:
        leben -= 1 # Das ist Logik: Schaden abziehen
        print(f"Die Schlange zischt! Du verlierst 1 Leben. Leben: {leben}")
        return leben > 0 # Das ist Logik: Wenn Leben 0, ist das Spiel vorbei

