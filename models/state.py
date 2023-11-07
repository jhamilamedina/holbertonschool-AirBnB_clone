#!/usr/bin/python3
"""Definimo una clase llamada State"""
from models.base_model import BaseModel


class State(BaseModel):
    """Define el nombre del estado de la ciudad

    Args:
        name(str): Estado de la ciudad
    """

    name = ""
