#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.
Unittest classes:
        TestFileStorage_instantiation
        TestFileStorage_methods
"""

import unittest
import json
import os
from time import sleep
import models
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from os import path

class TestFileStorage_instantiation(unittest.TestCase):
    """Define una clase llamada TestStorage que hereda de unittest.
    TestCase y representa un conjunto de prueas unitarias relaconadas
    """
    def test_file_path1(self):
        self.assertTrue(path.exists(FileStorage._FileStorage__file_path))


    def test_FileStorage_instantiation_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    """Pruebas unitarias para probar metodos de la
    clase FileStorage
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        bm = BaseModel()
        models.storage.new(bm)
        self.assertIn("BaseModel." + bm.id, models.storage.all().keys())
        self.assertIn(bm, models.storage.all().values())

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_update_now(self):
        bm = BaseModel()
        original_updated_at = bm.updated_at
        original_created_at = bm.created_at
        sleep(1)
        bm.save()
        self.assertNotEqual(original_updated_at, bm.updated_at)
        self.assertTrue(original_created_at, bm.created_at)
        self.assertNotEqual(bm.updated_at, bm.created_at)

    def test_save(self):
        bm = BaseModel()
        self.assertIsNone(bm.save())

    def test_update_type(self):
        bm = BaseModel()
        self.assertTrue(type(bm.updated_at) == datetime)

    def test_save_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        bm = BaseModel()
        models.storage.new(bm)
        models.storage.save()
        models.storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + bm.id, obj)

    def test_reload_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
