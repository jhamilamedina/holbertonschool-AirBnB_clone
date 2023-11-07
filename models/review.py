#!/usr/bin/python3
"""Define la clase Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Muestra la reseña de la habitacion

    Atributos:
        place_id(str): el id del lugar
        user_id(str): el id del usuario
        text(str): el texto de la review
    """

    place_id = ""
    user_id = ""
    text = ""
