# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids_less_structure import aa, codons
import random
from load import load_seq

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###
def splicer( dna ):

    dna_split_test = [dna.split(i) for i in (" TAG ", " TAA "," TGA ") if len(dna.split(i)) > 1]
    if len(dna_split_test) > 0: dna_split = dna_split_test[0]
    else: return

    for i in xrange(len(dna_split)):
        loc = dna_split[i].find("ATG")
        if loc == -1: continue
        else: dna_split[i] = dna_split[i][loc:]

    return [ dna_split[i][dna_split[i].find("ATG"):] for i in range(len(dna_split)) if dna_split[i].find("ATG") > -1 and ''.join([dna_split[i][j] for j in range(3)]) == "ATG"]

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    # TODO: implement this
    
    compl = { 'A':'T', 'T':'A', 'G':'C', 'C':'G' }
    rdna = ''.join([ compl[i] for i in dna[::-1] ])

    working = []

    for idna in (dna, rdna):
        for j in xrange(3):
            dna_f = ''.join([ idna[i] + idna[i+1] + idna[i+2] + ' ' for i in xrange(j, len(dna)-2,3)])
            out = splicer(dna_f)
            
            if  out != None:
                for i in xrange(len(out)):
                    working.append(out[i])

    return working

print find_all_ORFs_both_strands("CTAATGCGAATGTAGCATCAAA")



### END OF WEEK ONE ###



def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this
    pass


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this
    pass

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    # TODO: implement this
    pass

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    # TODO: implement this
    pass

'''
if __name__ == "__main__":
    import doctest
    doctest.testmod()
'''
