from cg_simtool.tools import IO


class System:

    def __init__(self):
        self.atoms = []
        self.types_charges = []
        self.coordinates = []
        self.contains_rigids = False

    def init_system(self, n_atoms = 0, mol_id_paths, tnc_paths, coordinates_paths):
        try:
            if len(mol_id_paths) != len(types_paths) or len(mol_id_paths)!= len(coordinates_paths) or len(coordinates_paths) != len(types_paths):
                raise IndexError("Must have the exact number of files for all parameters")
            else:
                self.coordinates = IO.read_coordinates(coordinates_paths)
                self.mol_ids = IO.read_molecules_ids(mol_id_paths)
                self.types_charges = IO.read_types_charges(tnc_paths)

        except TypeError:
            print("You should submit the files' paths as an array of strings")
            raise