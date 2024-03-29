#!/usr/bin/python3
"""Definimos una clase"""

from sqlalchemy.ext.declarative import declarative_base
import uuid
from datetime import datetime
import models
from sqlalchemy import Column, Integer, String, DateTime


Base = declarative_base()

class BaseModel:
    """Representación de la clase"""
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    def __init__(self, *args, **kwargs):
        """Inicializa los atributos:
        id, create_at, update_at
        **kwargs: recibe un diccionario
        """
        if kwargs:  # Si no esta vacion inicializa atributos y valores
            for k, v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
            """El atributo created_at convierte el objeto a formato string
            a un objeto datetime la función strptime del modulos datetime
            analiza la cadena en created_at de acuerdo al formato dado
            """
            self.__dict__["created_at"] = datetime.strptime(
                self.__dict__["created_at"], "%Y-%m-%dT%H:%M:%S.%f")

            self.__dict__["updated_at"] = datetime.strptime(
                self.__dict__["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")

        else:
            self.id = str(uuid.uuid4())
            """Establece la fecha y hora de la creación al momento actual
            en formato ISO
            """
            self.created_at = datetime.now()
            """Establece la fecha y hora de actualización en formato ISO"""
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Devuelve una representacion en cadena del objeto
        incluyendo el nombre de la clase, el IDE y los atributos
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Actualiza la fecha y hora al momento actual en formato ISO"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Este metodo agrega el nombre de la clase al diccionario y devuelve
        todos los atributos en un diccionario
        Retorna la representacion de un diccionario de la instancia
        """
        data = dict(self.__dict__)
        data['created_at'] = self.__dict__['created_at'].isoformat()
        data['updated_at'] = self.__dict__['updated_at'].isoformat()
        data["__class__"] = self.__class__.__name__
        return data
