import numpy as np

def read_coordinates(paths):
    coords = np.ndarray(shape=(0,3), dtype='float')
    for path in paths:
        try:
            curr_coords  = np.loadtxt(path , dtype='float')
            coords = np.concatenate((coords, curr_coords))
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
            ids = np.concatenate((ids, tmp))
        except FileNotFoundError:
            print('File %s was not found'%path)
            raise

def read_types_charges(paths):
    tnc  = []
    for path in paths:
        tnc = np.concatenate((tnc,np.loadtxt(path,dtype='int')))


def write_rigids(out, rigids):
    file = open(out,'w')
    if rigids is None:
        raise TypeError('rigids not provided')

    try:
        for rigid in rigids:
            file.write('%s:%s\n'%(rigid[0],rigid[1]))
        file.close()
    except TypeError:
        exit()

def write_rigid_groups(out = 'rigid_groups.txt',rigids_dict = {}):
    file = open(out, 'w')
    for key in rigids_dict.keys():
        groups = rigids_dict[key]
        strfied = ' '.join(groups)
        file.write('group %s id %s\n' % (key, strfied))
    file.close()

