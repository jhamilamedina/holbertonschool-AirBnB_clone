#!/usr/bin/python3
"""Definimos una clase FileStorage"""

import json
from os import path
import datetime


class FileStorage:
    """Representacion de la clase FileStorage"""
    __file_path = "file.json"
    __objects = {}  # Suponiendo __objects es un atributo de la clase

    def all(self):
        """Este metodo all devuelve un diccionario a __objects
        cuando se llama a una instancia de la clase"""
        return self.__objects

    def new(self, obj):
        """Este metodo toma obj como argumento y construye __objects
        diccionario usando el nombre de la clase y el id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """El metodo save abre el archivo __file_path
        y json.dumps lo utiliza para escribir un diccionario a __objects
        en el archivo en formato json
        """
        data = {}

        odict = self.__objects
        data = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(data, file)

    def reload(self):
        """
        Deserialia el archivo json en __objects solo si el
        archivo __file_path existe
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

                for o in data.values():
                    from models.base_model import BaseModel
                    from models.user import User
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

    def attributes(self):
        """
        Devuelve los atributos válidos y sus tipos para el nombre de
        clase
        """
        attributes = {
            "BaseModel":
                {"id": str,
                    "created_at": datetime.datetime,
                    "updated_at": datetime.datetime},
            "User":
                {"email": str,
                    "password": str,
                    "first_name": str,
                    "last_name": str},
                }

        return attributes
