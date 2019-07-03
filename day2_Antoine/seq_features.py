import bootcamp_utils

def numbers_negatives(seq):
    """Number of negative residues in a protein sequence"""
    seq = seq.upper()
    
    for am_ac in seq:
        if am_ac not in bootcamp_utils.aa:
            raise RuntimeError(f'{am_ac} is not a valid amino acid')
    
    return seq.count('D') + seq.count('E')