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
    comp = { 'A':'T', 'T':'A', 'G':'C', 'C':'G' }
    ORFs = []
    for idna in ( dna, ''.join([comp[i] for i in dna[::-1]])):
        for j in range(3):
            for threes in range(j,len(idna)-1,3):
                if idna[threes:threes+3] in ("TAG","TAA","TGA"):
                    for k in range(j,threes,3):
                        if idna[k:k+3] == "ATG":
                            ORFs.append(idna[k:threes])
                            break
    return ORFs

print find_all_ORFs_both_strands_full("CTAATGCGAATGTAGCATCAAACTAATGCGAATGTAGCATCAAACTAATGCGAATGTAGCATCAAA")

