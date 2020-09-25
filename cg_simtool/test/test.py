#!/bin/env python
import unittest
import os

from cg_simtool.tools import tools_io, tools_checks
import numpy as np
class IOTest(unittest.TestCase):
    def test_read_coordinates(self):
        paths = ['test/mock_data/coordinates1.txt', 'test/mock_data/coordinates2.txt']
        coordinates = tools_io.read_coordinates(paths)
        self.assertIsInstance(coordinates, np.ndarray)
        self.assertEquals(coordinates.shape[1], 3)

    def test_read_molecules_ids(self):
        paths = ['test/mock_data/mol1.txt', 'test/mock_data/mol2.txt']
        mol_ids = tools_io.read_molecules_ids(paths)
        self.assertIsNotNone(mol_ids)
        self.assertIsInstance(mol_ids, np.ndarray)
        self.assertEqual(mol_ids.dtype, int)
        self.assertEqual(len(mol_ids), 21)

    def test_read_type_charges(self):
        paths = ['test/mock_data/tnc1.txt', 'test/mock_data/tnc2.txt']
        types, charges = tools_io.read_types_charges(paths)
        self.assertIsNotNone(types)
        self.assertIsInstance(types, np.ndarray)
        self.assertEqual(types.dtype, int)
        self.assertEqual(len(types), 50)
        self.assertIsNotNone(charges)
        self.assertIsInstance(charges, np.ndarray)
        self.assertEqual(charges.dtype, float)
        self.assertEqual(len(charges), 50)
        self.assertEqual(len(charges), len(types))


if __name__ == '__main__':
    unittest.main()