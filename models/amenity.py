#!/usr/bin/python3
"""Define la clase Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Muestras las comodidades de la habitacion

    Atributos:
        name (str) = nombres de las comodidades
    """

    name = ""
