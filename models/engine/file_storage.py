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
        return FileStorage.__objects

    def new(self, obj):
        """Este metodo toma obj como argumento y construye __objects
        diccionario usando el nombre de la clase y el id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """El metodo save abre el archivo __file_path
        y json.dumps lo utiliza para escribir un diccionario a __objects
        en el archivo en formato json
        """
        with open(self.__file_path, "w", encoding="utf-8") as file:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            """
            k:Es la clave del elemento actual en FileStorage.__objects.
            v: valor del elemento actual en FileStorage.__objects.

            Para cada par clave-valor en FileStorage.__objects, se
            está creando un nuevo par clave-valor en la diccion (d)
            """
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """
        Deserialia el archivo json en __objects solo si el
        archivo __file_path existe
        """
        if path.exists(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
            obj_dict = json.load(file)
            obj_dict = {k: self.classes()[v["__class__"]](**v)
                        for k, v in obj_dict.items()}
            FileStorage.__objects = obj_dict
