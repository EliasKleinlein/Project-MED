#Initialisierung der Lebenspunkte am Start
lebenspunkte = 3

def zeige_leben():
    """Zeigt die aktuellen Lebenspunkte als herzen an"""
    print(f"\n❤️ Lebenspunkte: {lebenspunkte} / 3")
    print("-" * 30)

def schaden_nehmen(anzahl):
    """zieht Lebenspunkte ab und prüft, ob das Spiel vorbei ist"""
    global lebenspunkte
    lebenspunkte -= anzahl
    print(f"\n💥 Autsch! Du hast {anzahl} Schaden genommen!")

    if lebenspunkte <= 0:
        lebenspunkte = 0
        print(f"\n💀 Game Over! Professor SynthaxError hat dich erwischt")
        #hier könnte man später das Spiel beenden oder neu starten
    else:
        zeige_leben()

        