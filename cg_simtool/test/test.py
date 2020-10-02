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
        self.assertEqual(coordinates.shape[1], 3)

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

    def test_write_rigids(self):
        out = 'tmp'
        rigids = [
            [1,10],
            [400,600],
            [654, 768]
        ]
        tools_io.write_rigids(out, rigids)
        tmp = np.loadtxt(out, delimiter=':', dtype='int')
        self.assertEqual(len(tmp),len(rigids))
        self.assertIsInstance(tmp, np.ndarray)

        for id, rigid in enumerate(rigids):
            self.assertEqual(rigid[0], tmp[id][0])
            self.assertEqual(rigid[1], tmp[id][1])

        os.remove(out)
    def test_write_rigid_groups(self):
        out = 'tmp.txt'
        rigids_dict = {
            'CSD':[
                [1, 10],
                [20, 30]
            ],
            'CD': [
                [14, 15],
            ]
        }
        tools_io.write_rigid_groups(out, rigids_dict)
        tmp = open(out,'r')
        rigid_checked = {}
        for line in tmp.readlines():
            split = line.split()
            rigid_checked[split[1]] = []
            locations = [i for i in split[3:]]
            for loc in locations:
                loc_split = [int(i) for i in loc.split(':')]
                rigid_checked[split[1]].append(loc_split)
        self.assertEqual(rigid_checked, rigids_dict)
        self.assertIsNotNone(tmp)




        os.remove(out)

if __name__ == '__main__':
    unittest.main()