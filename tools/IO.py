import numpy as np

def read_coordinates(paths):
    coords = np.ndarray(shape=(0,3), dtype='float')
    for path in paths:
        try:
            curr_coords  = np.loadtxt(path , dtype='float')
            coords.concat(curr_coords)
        except FileNotFoundError:
            print('File %s was not found'%path)
            raise
    return coords

def read_molecules_ids(paths):
    shift = 0
    ids = []
    for path in paths:
        try:
            curr_ids = np.loadtxt(path, dtype='int')
            tmp = [i+shift for i in curr_ids]
            shift += len(set(curr_ids))
            ids.concat(tmp)
        except FileNotFoundError:
            print('File %s was not found'%path)
            raise

def read_types_charges(paths):
    tnc  = []
    for path in paths:
        tnc.concat(np.loadtxt(path,dtype='int'))