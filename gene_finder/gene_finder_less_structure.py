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
def Pull_that_shit_out( dna ):
    dna_split = []
    for i in (" TAG ", " TAA "," TGA "):
        if len(dna.split(i)) > 1:
            dna_split = (dna.split(i))
    working = []
    for i in xrange(len(dna_f1_splits)):
        print "Code needed"
        if dna_f1_splits[i][0]+dna_f1_splits[i][1]+dna_f1_splits[i][2] == "ATG":
            working.append(dna_f1_splits[i])

    return working


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
    rdna = dna[::-1]
    print rdna

    tmp = ''

    for i in rdna:
        tmp = tmp+compl[i]

    rdna = tmp
    print rdna

    dna_f1 = ''.join([ dna[i] + dna[i+1] + dna[i+2] + ' ' for i in xrange(0, len(dna)-2,3) ]) 
    dna_f2 = ''.join([ dna[i] + dna[i+1] + dna[i+2] + ' ' for i in xrange(1, len(dna)-2, 3) ])
    dna_f3 = ''.join([ dna[i] + dna[i+1] + dna[i+2] + ' ' for i in xrange(2, len(dna)-2, 3) ])

    print dna_f1
    dna_f1_splits = []
    dna_f2_splits = []
    dna_f3_splits = []
    for i in (" TAG ", " TAA "," TGA "):
        if len(dna_f1.split(i)) > 1:
            dna_f1_splits = (dna_f1.split(i))
    for i in (" TAG ", " TAA "," TGA "):
        if len(dna_f2.split(i)) > 1:
            dna_f2_splits.append(dna_f2.split(i))
    for i in (" TAG ", " TAA "," TGA "):
        if len(dna_f3.split(i)) > 1:
            dna_f3_splits.append(dna_f3.split(i))

    print "Splits"
    print dna_f1_splits
    working = []
    for i in xrange(len(dna_f1_splits)):
        print "Code needed"
        if dna_f1_splits[i][0]+dna_f1_splits[i][1]+dna_f1_splits[i][2] == "ATG":
            working.append(dna_f1_splits[i])

    print
    print "WORKING STUFF"
    print working
    print

    print dna_f2_splits
    print dna_f3_splits
    print

    print dna_f1
    print dna_f2
    print dna_f3

find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")



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
