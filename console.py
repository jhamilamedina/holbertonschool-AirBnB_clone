#!/usr/bin/python3
"""Definimos una clase llamada HBNBCommand"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return ret1
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return ret1


class HBNBCommand(cmd.Cmd):
    """Clase que hereda HBNBCommand cmd.Cmd"""
    prompt = "(hbnb)"
    """prompt personalizado que muestra (hbnb)"""
    __classes = {
            "BaseModel"
    }

    def emptyline(self):
        """No haga nada al recibir una linea vacia"""
        pass

    def do_quit(self, arg):
        """Definimos un metodo do_quit y toma 2
        argumentos y salir del interprete de comandos
        """
        return True

    def do_EOF(self, arg):
        """
        Definimos un metodo do_EOE y toma 2 argumentos
        señal EOF para salir del programa
        """
        print("")
        return True

    def help_quit(self):
        """Salir del interpete de comandos"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Muestra la ayuda para el comando EOF"""
        print("Salir del programa con EOF")

    def do_create(self, arg):
        """Crea una nueva instancia de clase e imprime
        el id
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
