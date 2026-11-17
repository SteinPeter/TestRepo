"""Berechnung des Drehmoments."""

from werkzeuge._hilfen import zahl_eingeben

NAME = "Drehmoment berechnen"
BESCHREIBUNG = "Berechnet das Drehmoment aus Kraft und Hebelarm"


def ausfuehren():
    kraft = zahl_eingeben("Kraft F in N")
    hebelarm = zahl_eingeben("Senkrechter Hebelarm r in m")

    drehmoment = kraft * hebelarm

    print(f"Drehmoment: {drehmoment:.3f} N·m")