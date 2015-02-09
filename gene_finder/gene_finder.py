# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids_less_structure import aa, codons
import random
from random import shuffle
from load import load_seq, load_salmonella_genome

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###

def find_all_ORFs_both_strands(dna):
    '''
    Finds all ORFs in a strand in both direction and in each frame. It does require both a start codon and an end codon
    >>> find_all_ORFs_both_strands("CTAATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    >>> find_all_ORFs_both_strands("CTAATGCGAATGTAGCATCAAAATGCGAATGTAGCATCAAATAG")
    ['ATGCGAATG', 'ATGCGAATG', 'ATGCTACATTCGCAT']
    '''
    # Setting up the end array
    ORFs = []

    # Sets idna as both dna and the reverse compliment of dna, then iterates through both
    for idna in ( dna, ''.join([b[b.index(i)+(1 if b.index(i)%2==0 else -1)]for i in dna[::-1]for b in [['A','T','G','C']]])):
        for j in range(3):
            starter = j
            # Sets up the triplets starting at phase shift by j
            for threes in range(j,len(idna)-1,3):
                if idna[threes:threes+3] in ("TAG","TAA","TGA"):
                    # Looks back to check for start codon, beginning at the starter
                    for k in range(starter,threes,3):

                        # Finds the triplet that codes for the start codon
                        if idna[k:k+3] == "ATG":

                            # Sets the starter to the end of the stop codon
                            starter = threes

                            # Append this ORF to the output array
                            ORFs.append(idna[k:threes])

                            # Get out of this loop and go back to finding end codons
                            break
    return ORFs


### END OF WEEK ONE ###


def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("CTAATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    return max(find_all_ORFs_both_strands(dna),key=len)


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF
    >>> longest_ORF_noncoding( "CTAATGCGAATGTAGCATCAAA", 1500 )
    18

    This test confirms that trying this numerous amount of times recieves the same value.
    """
    longest = []
    shuffled = []

    for i in range(num_trials):
        # Not a very pretty way of shuffling DNA
        shuffled = [i for i in dna]
        shuffle(shuffled)
        dna = ''.join([i for i in shuffled])

        # If it finds the longest it will return
        try:
            longest.append(longest_ORF(dna))
        except: continue

    return len(max(longest,key = len))
    

def coding_strand_to_AA_clean(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function

    does not check for start and stop codons (it assumes that the input
    DNA sequence represents an protein coding region).
    
    dna: a DNA sequence represented as a string
    returns: a string containing the sequence of amino acids encoded by the
             the input DNA fragment

    >>> coding_strand_to_AA_clean("ATGCGA")
    'MR'
    >>> coding_strand_to_AA_clean("ATGCCCGCTTT")
    'MPA'
    """
    returned = []
    # sets i to be codons
    for i in range(0,len(dna),3):

        # sweep through all codons in list
        for j in range(len(codons)):
    
            # see if dna is in codons set
            if dna[i:i+3] in codons[j]:
        
                # append the AA to which dna codon matches
                returned.append(aa[j])

    return ''.join([i for i in returned])
    

def coding_strand_to_AA(dna):
    '''
    This converts DNA to AA. In one line.
    >>> coding_strand_to_AA("ATGCGA")
    'MR'
    >>> coding_strand_to_AA("ATGCCCGCTTT")
    'MPA'

    '''
    # Sets i to weep dna, j to sweep codons and sees where it sees where i:i+3 is in Codons
    # and returns the AA sequence for that codon.

    return ''.join([ aa[j] for i in range(0,len(dna),3) for j in range(len(codons)) if dna[i:i+3] in codons[j]])


def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    # Finds the ORF length for threshold
    ORF_length = longest_ORF_noncoding( dna ,threshold)

    # End ORFs
    Real_ORFs = []

    # Finds all the ORFs and sets i to them
    for i in find_all_ORFs_both_strands(dna):
        if len(i) > ORF_length:
             Real_ORFs.append(coding_strand_to_AA(i))

    return len(Real_ORFs),Real_ORFs


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print gene_finder( load_seq("./data/X73525.fa"), 1500)
