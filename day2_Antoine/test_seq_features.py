import seq_features
import pytest

def test_number_negatives_single_aa():
    assert seq_features.numbers_negatives('E') == 1
    assert seq_features.numbers_negatives('D') == 1, 'failed with sequence "D"'

def test_number_negatives_empty():
    assert seq_features.numbers_negatives('') == 0
    
def test_number_negatives_lowercase():
    assert seq_features.numbers_negatives('acklwttae') == 1
    assert seq_features.numbers_negatives('ackleedalac') == 3
    
def test_number_negatives_uppercase():
    assert seq_features.numbers_negatives('ACKLWTTAE') == 1
    assert seq_features.numbers_negatives('DDDDEEEE') == 8
    
def test_number_negatives_invalid_aa():
    #context managment! pytest check the excinfo, check if there is runtime error
    with pytest.raises(RuntimeError) as excinfo:
        seq_features.numbers_negatives('ACKLZWTTAE')
    excinfo.match('Z is not a valid amino acid')
    #maintenant ce test ne passe plus, on va modifier la fonction
    