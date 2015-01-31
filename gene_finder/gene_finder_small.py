'''
This code is actually somewhat readable
'''
def find_all_ORFs_both_strands(dna):
    return [ idna[idna.find("ATG"):threes] for idna in (dna, ''.join([('A','T','G','C')[ ('A','T','G','C').index(i)+ ( 1 if ('A','T','G','C').index(i)%2 == 0 else -1)] for i in dna[::-1]  ])) for j in range(3) for threes in range(j, len(idna)-1,3) if idna[threes:threes+3] in ("TAG","TAA","TGA") and len(idna[idna.find("ATG"):threes])%3 == 0 and len(idna[idna.find("ATG"):threes]) != 0]



'''
This code uses the fewest number of characters for this
particular algorithm
'''

def A(d):return[c[c.find("ATG"):t]for c in (d,''.join([b[b.index(i)+(1 if b.index(i)%2==0 else -1)]for i in d[::-1]for b in [['A','T','G','C']]]))for j in range(3)for t in range(j,len(c)-1,3)if c[t:t+3]in ("TAG","TAA","TGA")and len(c[c.find("ATG"):t])%3==0 and len(c[c.find("ATG"):t])!=0]


#This is the testing of the functions
#print find_all_ORFs_both_strands("CTAATGCGAATGTAGCATCAAA")
#print A("CTAATGCGAATGTAGCATCAAACTAATGCGAATGTAGCATCAAA")

def find_all_ORFs_both_strands_full(dna):
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


def find_all_ORFs_both_strands_list(dna):
    ORFs = []
    for idna in ( dna, ''.join([b[b.index(i)+(1 if b.index(i)%2==0 else -1)]for i in dna[::-1]for b in [['A','T','G','C']]])):
        for j in range(3):
            starter = j
            for threes in range(j,len(idna)-1,3):
                #if idna[threes:threes+3] in ("TAG","TAA","TGA"):
                if idna[threes:threes+3] in ("ATG"):
                    
                    #for k in range(starter,threes,3):
                        if idna[k:k+3] == "ATG":
                            starter = threes
                            ORFs.append(idna[k:threes])
                            break
    return ORFs


print find_all_ORFs_both_strands_full("CTAATGCGAATGTAGCATCAAACTAATGCGAATGTAGCATCAAACTAATGCGAATGTAGCATCAAA")

