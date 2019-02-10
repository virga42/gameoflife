import unittest
from app import zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.lifeform1 = zoo.Lifeform("glider", "000010", 3)
        self.lifeform2 = zoo.Lifeform("exploder", "111010", 3)
        self.lifeform1a = zoo.Lifeform("glider", "111101", 3)
        self.lifeform3 = zoo.Lifeform("tenCellRow", "101010", 3)
        self.z1 = zoo.Zoo("test_single")
        self.z2 = zoo.Zoo("test_multiple")
        self.z3 = zoo.Zoo("test_duplicate")
        self.z4 = zoo.Zoo("test_remove")
        self.z5 = zoo.Zoo("test_get")
        self.z6 = zoo.Zoo("test_list")

    """ Testing creation of a zoo """
    def test_can_create_zoo(self):
        self.assertEqual(self.z1.name, "test_single")    

    """ Testing adding a lifeform to a zoo """
    def test_can_add_lifeform_to_empty_zoo(self):
        self.z1.add(self.lifeform1)
        self.assertEqual(self.z1.zoo, [self.lifeform1])

    """ Testing adding multiple lifeforms """
    def test_can_add_mutliple_lifeforms(self):
        self.z2.add(self.lifeform1)
        self.z2.add(self.lifeform2)
        self.assertIn(self.lifeform1, self.z2.zoo) 
        self.assertIn(self.lifeform2, self.z2.zoo)

    """ Testing adding a lifeform who's label already exists overwrites """
    def test_add_same_lifeform_does_not_duplicate(self):
        self.z3.add(self.lifeform1)
        self.z3.add(self.lifeform1a) # lifeform with same label but different data
        self.assertEqual(self.z3.zoo, [self.lifeform1a])

    """ Testing removing a lifeform """
    def test_removing_a_lifeform(self):
        self.z4.add(self.lifeform1)
        self.z4.add(self.lifeform2)
        self.z4.remove("glider")
        self.assertNotIn({"label": "glider", "cells": "000010", "width": 3}, self.z4.zoo)

    """ Testing getting a lifeform """
    def test_getting_a_lifeform(self):
        self.z5.add(self.lifeform1)
        self.z5.add(self.lifeform2)
        self.z5.add(self.lifeform3)
        self.assertEqual(self.z5.get("exploder"), {"label": "exploder", "cells": "111010", "width": 3})

    """ Testing getting a list of lifeforms in a zoo """
    def test_list_of_lifeforms_in_zoo(self):
        self.z6.add(self.lifeform1)
        self.z6.add(self.lifeform2)
        self.z6.add(self.lifeform3)
        self.assertEqual(self.z6.lst(), ["glider", "exploder", "tenCellRow"])
