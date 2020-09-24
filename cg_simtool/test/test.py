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
        self.assertIsInstance(mol_ids, np.ndarray)
        self.assertEqual(mol_ids.dtype, int)





if __name__ == '__main__':
    unittest.main()