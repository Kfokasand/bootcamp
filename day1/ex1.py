def complement_base(base):
    """Returns the Watson-Crick complement of a base."""
    if base in 'Aa':
        return 'T'
    elif base in 'Tt':
        return 'A'
    elif base in 'Gg':
        return 'C'
    else:
        return 'G'


def reverse_complement(seq):
    """Compute reverse complement of a sequence."""
    # Initialize reverse complement
    rev_seq = ''
    
    # Loop through and populate list with reverse complement
    for base in reversed(seq):
        rev_seq += complement_base(base)
        
    return rev_seq

def reverse_complementa(seq):
    """Compute reverse complement of a sequence."""
     # Initialize reverse complement
    rev_seq = ''
    
    # Loop through and populate list with reverse complement
    for base in seq[::-1]:
        rev_seq += complement_base(base)
        
    return rev_seq