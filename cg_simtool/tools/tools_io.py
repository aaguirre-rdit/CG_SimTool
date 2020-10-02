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
            curr_ids = np.loadtxt(path, dtype=int)
            tmp = [int(i+shift) for i in curr_ids]
            shift += len(set(curr_ids))
            ids = np.concatenate((ids, tmp)).astype('int')
        except FileNotFoundError:
            print('File %s was not found'%path)
            raise
    return ids

def read_types_charges(paths):
    types = []
    charges = []
    for path in paths:
        data = np.loadtxt(path, dtype='float')
        curr_types = np.array([int(i[0]) for i in data])
        curr_charges = np.array([float(i[1]) for i in data])
        types = np.concatenate((types, curr_types)).astype('int')
        charges = np.concatenate((charges, curr_charges)).astype('float')

    return types, charges

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

def write_rigid_groups(out = 'rigid_groups.txt', rigids_dict = {}):
    file = open(out, 'w')
    for key in rigids_dict.keys():
        groups = rigids_dict[key]
        strfied = ''
        for group in groups:
            strfied = strfied + ' %s:%s'%(group[0], group[1])
        file.write('group %s id %s\n' % (key, strfied))
    file.close()

