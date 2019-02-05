import unittest
from app import zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.lifeform1 = {"name": "glider", "cells": "000010", "width": 3}
        self.lifeform2 = {"name": "exploder", "cells": "111010", "width": 3}
        self.lifeform1a = {"name": "glider", "cells": "111101", "width": 3}
        self.z1 = zoo.Zoo("test_single")
        self.z2 = zoo.Zoo("test_multiple")
        self.z3 = zoo.Zoo("test_duplicate")

    """ Testing creation of a zoo """
    def test_can_create_zoo(self):
        self.assertEqual(self.z1.name, "test_single")    

    """ Testing adding a lifeform to a zoo """
    def test_can_add_lifeform_to_empty_zoo(self):
        self.z1.add(self.lifeform1)
        self.assertEqual(self.z1.zoo, [{"name": "glider", "cells": "000010", "width": 3}])

    """ Testing adding multiple lifeforms """
    def test_can_add_mutliple_lifeforms(self):
        self.z2.add(self.lifeform1)
        self.z2.add(self.lifeform2)
        self.assertIn({"name": "exploder", "cells": "111010", "width": 3}, self.z2.zoo) 
        self.assertIn({"name": "glider", "cells": "000010", "width": 3}, self.z2.zoo)

    """ Testing adding a lifeform who's name already exists overwrites """
    def test_add_same_lifeform_does_not_duplicate(self):
        self.z3.add(self.lifeform1)
        self.z3.add(self.lifeform1a) # lifeform with same name but different data
        self.assertEqual(self.z3.zoo, [{"name": "glider", "cells": "111101", "width": 3}])

    """ Testing removing a lifeform