# --- ERWEITERUNG: RAUM 2 (INDEX-FRAGE) ---
        print("\n--- RAUM 2: DIE DATEN-BIBLIOTHEK ---")
        print("Du betrittst eine Bibliothek voller Listen.")
        print("Ein Geist erscheint und zeigt auf eine Liste: ['Python', 'Java', 'C++']")
        
        quiz_index = input("An welcher Stelle (Index) steht 'Python' in dieser Liste? (0, 1 oder 2): ")
        
        if quiz_index == "0":
            print("\nDer Geist nickt: 'Korrekt! In Python fängt man bei 0 an zu zählen.'")
            print("Er gibt dir einen 'Daten-Kristall' für dein Inventar.")
            inventar.append("Daten-Kristall")
            print(f"Dein Inventar enthält jetzt: {inventar}")
        else:
            leben -= 1
            print("\nDer Geist schüttelt den Kopf: 'Falsch!'")
            print(f"Ein Leben verloren. Deine Leben: {leben}")
        
        # Prüfung, ob das Spiel weitergeht
        if leben <= 0:
            print("\nGAME OVER")
        else:
            print("\nDu gehst weiter durch den Gang...")

