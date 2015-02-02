# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids_less_structure import aa, codons
import random
from random import shuffle
from load import load_seq

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###
def splicer( dna ):
    dna_split_test = [dna.split(i) for i in (" TAG ", " TAA "," TGA ") if len(dna.split(i)) > 1]
    if len(dna_split_test) > 0: dna_split = dna_split_test[0]
    else: return []
    for i in xrange(len(dna_split)):
        loc = dna_split[i].find("ATG")
        if loc == -1: continue
        else: dna_split[i] = dna_split[i][loc:]

    return [ dna_split[i][dna_split[i].find("ATG"):] for i in range(len(dna_split)) if dna_split[i].find("ATG") > -1 and ''.join([dna_split[i][j] for j in range(3)]) == "ATG"]

def find_all_ORFs_both_strands_old(dna):
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
    orf = []
    for idna in (dna, rdna):
        for j in xrange(3):
            dna_f = ''.join([ idna[i] + idna[i+1] + idna[i+2] + ' ' for i in xrange(j, len(dna)-2,3)])
            out = splicer(dna_f)
            
            for i in xrange(len(out)):
                orf.append(out[i].replace(' ',''))
    return orf

#print find_all_ORFs_both_strands("CTAATGCGAATGTAGCATCAAACTAATGCGAATGTAGCATCAAA")

def find_all_ORFs_both_strands(dna):
    # Setting up the end array
    ORFs = []

    # Sets idna as both dna and the reverse compliment of dna, then iterates through both
    for idna in ( dna, ''.join([b[b.index(i)+(1 if b.index(i)%2==0 else -1)]for i in dna[::-1]for b in [['A','T','G','C']]])):

        # Sets j to allow for out of phase checks of triplet codons
        for j in range(3):

            # Starter is where to start checking for the start codon
            starter = j

            # Sets up the triplets starting at phase shift by j
            for threes in range(j,len(idna)-1,3):

                # Checks to see if triplet is stop codon
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

    # ...
    return ORFs


### END OF WEEK ONE ###



def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    # TODO: implement this
    return max(find_all_ORFs_both_strands(dna),key=len)
    
#print longest_ORF("CTAATGCGAATGTAGCATCAAACTAATGCGAATGTAGCATCAAACTAATGCGAATGTAGCATCAAA")


def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this
    print [ longest_ORF(dna) for i in range(num_trials) if shuffle(dna)]
    print len( max ( [ longest_ORF(dna) for i in range(num_trials) if shuffle(dna)]   ), key =len)
    
    #print ''.join( random.shuffle( list(dna) ) )

print longest_ORF_noncoding("CTAATGCGAATGTAGCATCAAACTAATGCGAATGTAGCATCAAACTAATGCGAATGTAGCATCAAA",2)

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
