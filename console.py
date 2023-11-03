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

    def help_quit(self):
        """Muestra la ayuda para el comando 'quit'"""
        print("Salir del programa")

    def help_EOF(self):
        """Muestra la ayuda para el comando 'EOF'"""
        print("Salir del programa con EOF (Ctrl-D)")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
