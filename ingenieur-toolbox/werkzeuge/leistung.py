
"""Berechnet die elektrische Leistung aus Spannung und Stromstärke."""

from werkzeuge._hilfen import zahl_eingeben

NAME = "Elektrische Leistung"
BESCHREIBUNG = "Berechnet die Leistung P = U * I aus Spannung und Stromstärke."


def ausfuehren():
    spannung = zahl_eingeben("Spannung U (V)")
    strom = zahl_eingeben("Stromstärke I (A)")

    leistung = spannung * strom

    print(f"Elektrische Leistung: {leistung:.3f} W")

