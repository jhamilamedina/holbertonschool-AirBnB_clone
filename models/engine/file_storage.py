#!/usr/bin/python3
"""Definimos una clase FileStorage"""

import json
from os import path
import datetime


class FileStorage:
    def __init__(self):
        """Representacion de la clase FileStorage"""
        self.__file_path = "file.json"
        self.__objects = {}  # Suponiendo __objects es un atributo de la clase

    def all(self):
        """Este metodo all devuelve un diccionario a __objects
        cuando se llama a una instancia de la clase"""
        return self.__objects

    def new(self, obj):
        """Este metodo toma obj como argumento y construye __objects
        diccionario usando el nombre de la clase y el id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """El metodo save abre el archivo __file_path
        y json.dumps lo utiliza para escribir un diccionario a __objects
        en el archivo en formato json
        """
        data = {}
        for k, obj in self.__objects.items():
            data[k] = obj.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            """
            k:Es la clave del elemento actual en FileStorage.__objects.
            v: valor del elemento actual en FileStorage.__objects.
            Para cada par clave-valor en FileStorage.__objects, se
            está creando un nuevo par clave-valor en la diccion (d)
            """
            json.dump(data, file)

    def reload(self):
        """
        Deserialia el archivo json en __objects solo si el
        archivo __file_path existe
        """
        if not path.exists(self.__file_path):
            return
        with open(self.__file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
