#!/usr/bin/python3
"""Definimos una clase"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Representación de la clase"""
    def __init__(self):
        """Inicializa los atributos:
        id, create_at, update_at
        """

        self.id = str(uuid.uuid4())
        """Establece la fecha y hora de la creación al momento actual
        en formato ISO
        """
        self.created_at = datetime.now()
        """Establece la fecha y hora de actualización en formato ISO"""
        self.updated_at = datetime.now()

    def __str__(self):
        """Devuelve una representacion en cadena del objeto
        incluyendo el nombre de la clase, el IDE y los atributos
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Actualiza la fecha y hora al momento actual en formato ISO"""
        self.update_at = datetime.now()

    def to_dict(self):
        """
        Este metodo agrega el nombre de la clase al diccionario y devuelve
        todos los atributos en un diccionario
        """
        my_dict = dict(self.__dict__)
        my_dict['created_at'] = self.__dict__['created_at'].isoformat()
        my_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return (my_dict)
