"""Ingenieur-Toolbox - kleines Konsolenprogramm zum Ueben mit Git.

Starten mit:  python main.py
(Windows ggf.: py main.py)

Jedes Werkzeug liegt als eigene Datei im Ordner "werkzeuge/".
Neue Dateien dort werden automatisch im Menue angezeigt.

Probiert euch einfach mal aus, das richtige Repo kommt spaeter noch.
"""

from werkzeuge import lade_werkzeuge


def zeige_menue(werkzeuge):
    print("\n=== Ingenieur-Toolbox ===")
    for nummer, werkzeug in enumerate(werkzeuge, start=1):
        print(f"  {nummer}) {werkzeug.NAME}  -  {werkzeug.BESCHREIBUNG}")
    print("  0) Beenden")


def main():
    werkzeuge = lade_werkzeuge()
    while True:
        zeige_menue(werkzeuge)
        auswahl = input("Auswahl: ").strip()
        if auswahl == "0":
            print("Tschuess!")
            break
        if not auswahl.isdigit() or not 1 <= int(auswahl) <= len(werkzeuge):
            print("Ungueltige Auswahl, bitte nochmal.")
            continue
        werkzeug = werkzeuge[int(auswahl) - 1]
        print(f"\n--- {werkzeug.NAME} ---")
        try:
            werkzeug.ausfuehren()
        except KeyboardInterrupt:
            print("\nAbgebrochen.")


if __name__ == "__main__":
    main()
