"""VORLAGE fuer ein neues Werkzeug.

So geht's:
1. Diese Datei kopieren und umbenennen, z. B. in "biegemoment.py"
   (Name OHNE Unterstrich am Anfang, nur Kleinbuchstaben und _ ).
2. NAME, BESCHREIBUNG und ausfuehren() anpassen.
3. python main.py starten - das Werkzeug erscheint automatisch im Menue.
"""

from werkzeuge._hilfen import zahl_eingeben

NAME = "Mein Werkzeug"
BESCHREIBUNG = "Beschreibt in einem Satz, was berechnet wird"


def ausfuehren():
    a = zahl_eingeben("Wert a")
    b = zahl_eingeben("Wert b")
    ergebnis = a + b
    print(f"Ergebnis: {ergebnis:.3f}")
