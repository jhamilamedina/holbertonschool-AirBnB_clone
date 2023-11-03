#!/usr/bin/python3
"""Definimos una clase llamada HBNBCommand"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Clase que hereda HBNBCommand cmd.Cmd"""
    prompt = "(hbnb)"
    """prompt personalizado que muestra (hbnb)"""

    def do_quit(self, arg):
        """Definimos un metodo do_quit y toma 2
        argumentos y salir del programa
        """
        return true

    def do_EOE(self, arg):
        """
        Definimos un metodo do_EOE y toma 2 argumentos
        salimos con EOE (Ctrl-D)
        """
        print()
        return true

    def emptylyne(self):
        """No hacer nada en esta linea vacia"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
