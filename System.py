class System:

    def __init__(self):
        self.atoms = []
        self.charges = []
        self.coordinates = []

    def init_system(self, n_atoms = 0, mol_id_paths, types_paths, coordinates_paths):
        try:
            if len(mol_id_paths) != len(types_paths) or len(mol_id_paths)!= len(coordinates_paths) or len(coordinates_paths) != len(types_paths):
                raise IndexError("Must have the exact number of files for all parameters")
        except TypeError:
            print("You should submit the files' paths as an array of strings")
            raise