import os
import pytest
from drugdesign.data.preprocessor import load_pdbs, load_sdf


def test_load_pdb():
    pdb_file = os.path.join(os.path.dirname(__file__), 'data', '2w1i.pdb')
    result = load_pdbs(pdb_file)
    print(result)
    assert result is not None
    # Add more assertions based on the expected structure of the result


def test_load_sdf():
    sdf_file = os.path.join(os.path.dirname(
        __file__), 'data', '2w1i_C_L0I.sdf')
    result = load_sdf(sdf_file)
    print(result)
    assert result is not None
    # Add more assertions based on the expected structure of the result


if __name__ == "__main__":
    pytest.main()
