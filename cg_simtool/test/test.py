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





if __name__ == '__main__':
    unittest.main()