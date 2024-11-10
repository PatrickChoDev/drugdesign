from rdkit import Chem


def load_sdf(filename: str):
    """
    Load SDF file and return a list of RDKit molecules.
    """
    suppl = Chem.SDMolSupplier(filename)
    print(suppl.GetItemText(0))
    mols = [mol for mol in suppl if mol is not None]
    return mols


def load_pdbs(filename: str):
    """
    Load PDB file and return a list of RDKit molecules.
    """
    suppl = Chem.MolFromPDBFile(filename)
    print(suppl)
    mols = [mol for mol in suppl if mol is not None]
    return mols


if __name__ == '__main__':
    import os
    import pytest

    pdb_file = os.path.join(os.path.dirname(__file__),
                            '..', '..', 'tests', 'data', '2w1i.pdb')
    result = load_pdbs(pdb_file)
    print(result)

    sdf_file = os.path.join(os.path.dirname(
        __file__), 'data', '2w1i_C_L0I.sdf')
    result = load_sdf(sdf_file)
    print(result)
