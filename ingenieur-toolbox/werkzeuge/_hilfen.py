"""Hilfsfunktionen, die alle Werkzeuge benutzen koennen."""


def zahl_eingeben(text):
    """Fragt so lange nach, bis eine gueltige Zahl eingegeben wurde.
    Komma und Punkt sind beide erlaubt (3,5 oder 3.5)."""
    while True:
        eingabe = input(f"{text}: ").strip().replace(",", ".")
        try:
            return float(eingabe)
        except ValueError:
            print("  Bitte eine Zahl eingeben.")
