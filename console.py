#!/usr/bin/python3
"""Definimos una clase llamada HBNBCommand"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Clase que hereda HBNBCommand cmd.Cmd"""
    prompt = "(hbnb)"
    """prompt personalizado que muestra (hbnb)"""
    __classes = {
            "BaseModel"
    }

    def do_quit(self, arg):
        """Definimos un metodo do_quit y toma 2
        argumentos y salir del interprete de comandos
        """
        return True

    def do_EOE(self, arg):
        """
        Definimos un metodo do_EOE y toma 2 argumentos
        salimos con EOE (Ctrl-D)
        """
        print("")
        return True

    def emptylyne(self):
        """No hagas nada al recibir linea vacia"""
        pass

    def help_quit(self):
        """Salir del interpete de comandos"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Muestra la ayuda para el comando 'EOF'"""
        print("Salir del programa con EOF (Ctrl-D)")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
