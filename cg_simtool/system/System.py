from cg_simtool.tools import IO
from cg_simtool.tools import Checks
class System:

    def __init__(self):
        self.atoms = []
        self.n_atoms = 0
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
                if (len(self.coordinates)+len(self.mol_ids)+len(self.types_charges))/3 == len(self.coordinates):
                    self.n_atoms = len(self.coordinates)
                    self.atoms = [i for i in range(1, self.n_atoms + 1)]

        except TypeError:
            print("You should submit the files' paths as an array of strings")
            raise

    def check_rigids(self):
        types = self.types_charges[:,0]
        self.has_rigids = True if any(i >= 20 for i in types ) else False
        if (self.has_rigids):
            self.rigids = Checks.get_rigids(types)

    def save_rigids(self, out = 'rigids.dat'):


    def generate_bonds(self):
        bonds = []
        i = 1
        bond_id = 1
        while i < (self.n_atoms + 1):
            for rigid in self.rigids:
                if i == rigid[0]:
                    print('rigid at %s'%i)
                    start = i
                    end = rigid[1]
                    count = end - start
                    bonds.append('%s   1   %s   %s\n'%(i,end, end + 1))
                    i += count
                    break

            i += 1
            bond_id += 1

        self.bonds = bonds
