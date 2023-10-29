#!/usr/bin/python3
""" de engine importamos el archivo file_storage de
la clase FileStorage"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
