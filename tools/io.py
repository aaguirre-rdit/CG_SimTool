import numpy as np

def read_coordinates(paths):
    coords = np.ndarray(shape=(,3), dtype='float')
    for path in paths:
        try:
            curr_coords  = np.loadtxt(path , dtype='float')
            coords.concat(curr_coords)
        except FileNotFoundError:
            print('File %s was not found'%path)
            raise
    return coords
