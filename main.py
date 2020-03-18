"""
Ich möchte Python lernen! Dafür soll das Tick Tack Tou erstellt werden
"""
class Spieler():
    """
    Klasse Spieler hat alle Eigenschaften des Spielers
    """
    def __init__(self):
        self.zugfreigabe = False # oder True
        self.symbol = "Kreis" # oder "Kreuz"
        self.alias = "empty"

    def Alias_abfragen(self):
        self.alias = input("Wie ist dein Name?\n")
        print("Hallo " + self.alias + "! Schön das Du hier bist.")

    def Zug(self, brett, platznummer):
        # Symbolsyntax: Kreis = 1, Kreuz = 2, Frei = 0
        pass

def Spiel_starten():
    """
    Initialisiert das Spiel.
    :return: Leeres Spielbrett
    """
    brett = [] # Leeres Spielbrett erzeugen
    pass
    return brett

def Brett_auswerten(brett):
    sieger = "niemand" # niemand, kreuz, kreis, unentschieden

    return sieger

def Brett_darstellen(brett):
    print(brett)
    pass

def Spielzug_abfragen():
    pass

# Initialisieren der Variablen
Spieler1 = Spieler()

if __name__ == "__main__":
    Spieler1.Alias_abfragen()



