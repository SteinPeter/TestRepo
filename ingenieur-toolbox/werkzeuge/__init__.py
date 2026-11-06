"""Findet automatisch alle Werkzeuge in diesem Ordner.

Jede .py-Datei, die NICHT mit "_" beginnt, gilt als Werkzeug und muss enthalten:
    NAME          - kurzer Name fuer das Menue
    BESCHREIBUNG  - ein Satz, was das Werkzeug macht
    ausfuehren()  - Funktion, die das Werkzeug startet

Hier muss beim Hinzufuegen eines Werkzeugs NICHTS geaendert werden.
"""

import importlib
import pkgutil


def lade_werkzeuge():
    werkzeuge = []
    for modul_info in pkgutil.iter_modules(__path__):
        if modul_info.name.startswith("_"):
            continue  # Hilfsdateien und Vorlage ueberspringen
        modul = importlib.import_module(f"{__name__}.{modul_info.name}")
        if all(hasattr(modul, attr) for attr in ("NAME", "BESCHREIBUNG", "ausfuehren")):
            werkzeuge.append(modul)
        else:
            print(f"Hinweis: '{modul_info.name}.py' fehlt NAME, BESCHREIBUNG oder ausfuehren().")
    return sorted(werkzeuge, key=lambda m: m.NAME.lower())
