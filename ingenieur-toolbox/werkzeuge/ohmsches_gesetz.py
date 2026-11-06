from werkzeuge._hilfen import zahl_eingeben

NAME = "Ohmsches Gesetz"
BESCHREIBUNG = "Berechnet U, R oder I aus den beiden anderen Groessen"


def ausfuehren():
    print("Was soll berechnet werden?  1) Spannung U   2) Widerstand R   3) Strom I")
    wahl = input("Auswahl: ").strip()
    if wahl == "1":
        r = zahl_eingeben("Widerstand R in Ohm")
        i = zahl_eingeben("Strom I in A")
        print(f"U = R * I = {r * i:.3f} V")
    elif wahl == "2":
        u = zahl_eingeben("Spannung U in V")
        i = zahl_eingeben("Strom I in A")
        if i == 0:
            print("Strom darf nicht 0 sein.")
            return
        print(f"R = U / I = {u / i:.3f} Ohm")
    elif wahl == "3":
        u = zahl_eingeben("Spannung U in V")
        r = zahl_eingeben("Widerstand R in Ohm")
        if r == 0:
            print("Widerstand darf nicht 0 sein.")
            return
        print(f"I = U / R = {u / r:.3f} A")
    else:
        print("Ungueltige Auswahl.")
