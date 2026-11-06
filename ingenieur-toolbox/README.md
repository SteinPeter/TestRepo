# Ingenieur-Toolbox

Kleines Python-Konsolenprogramm zum Ueben mit Git und GitHub.
Es braucht nur Python 3 - keine weiteren Pakete.

## Starten

```bash
python main.py      # Windows ggf.: py main.py
```

## Aufbau

```
main.py                 Menue, startet die Werkzeuge
werkzeuge/
    __init__.py         findet alle Werkzeuge automatisch (nicht aendern)
    _hilfen.py          Hilfsfunktionen, z. B. zahl_eingeben()
    _vorlage.py         Vorlage fuer ein neues Werkzeug
    ohmsches_gesetz.py  Beispiel-Werkzeug
    kreisflaeche.py     Beispiel-Werkzeug
    geschwindigkeit.py  Beispiel-Werkzeug
```

## Neues Werkzeug hinzufuegen

1. `werkzeuge/_vorlage.py` kopieren und umbenennen (z. B. `biegemoment.py`).
2. `NAME`, `BESCHREIBUNG` und `ausfuehren()` anpassen.
3. `python main.py` - das Werkzeug erscheint automatisch im Menue.

Jede Person arbeitet in ihrer **eigenen Datei** - so gibt es keine Konflikte.

## Ideen fuer Erweiterungen

- Biegemoment / Durchbiegung eines Balkens
- Leistung P = U * I, Reihen- und Parallelschaltung von Widerstaenden
- Drehmoment aus Leistung und Drehzahl
- Temperatur umrechnen (°C, K, °F)
- Dichte / Masse / Volumen
- Zinseszins oder Abschreibung
- Druck (bar, Pa, psi) umrechnen

## Arbeitsweise

Nie direkt auf `main` arbeiten: eigenen Branch anlegen, pushen, Pull Request stellen.
Details stehen in der PDF-Anleitung.
