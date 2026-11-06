import math

from werkzeuge._hilfen import zahl_eingeben

NAME = "Kreisflaeche"
BESCHREIBUNG = "Flaeche und Umfang eines Kreises aus dem Durchmesser"


def ausfuehren():
    d = zahl_eingeben("Durchmesser d in mm")
    flaeche = math.pi * d**2 / 4
    umfang = math.pi * d
    print(f"Flaeche A = {flaeche:.3f} mm^2")
    print(f"Umfang  U = {umfang:.3f} mm")
