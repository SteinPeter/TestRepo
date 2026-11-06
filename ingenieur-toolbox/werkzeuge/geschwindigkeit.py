from werkzeuge._hilfen import zahl_eingeben

NAME = "Geschwindigkeit umrechnen"
BESCHREIBUNG = "Rechnet km/h in m/s um und umgekehrt"


def ausfuehren():
    print("1) km/h -> m/s    2) m/s -> km/h")
    wahl = input("Auswahl: ").strip()
    if wahl == "1":
        v = zahl_eingeben("Geschwindigkeit in km/h")
        print(f"{v} km/h = {v / 3.6:.3f} m/s")
    elif wahl == "2":
        v = zahl_eingeben("Geschwindigkeit in m/s")
        print(f"{v} m/s = {v * 3.6:.3f} km/h")
    else:
        print("Ungueltige Auswahl.")
