def find_all_ORFs_both_strands(dna):

    return [ idna[idna.find("ATG"):threes] for idna in (dna, ''.join([('A','T','G','C')[ ('A','T','G','C').index(i)+ ( 1 if ('A','T','G','C').index(i)%2 == 0 else -1)] for i in dna[::-1]  ])) for j in range(3) for threes in range(j, len(idna)-1,3) if idna[threes:threes+3] in ("TAG","TAA","TGA") and len(idna[idna.find("ATG"):threes])%3 == 0 and len(idna[idna.find("ATG"):threes]) != 0]

print find_all_ORFs_both_strands("CTAATGCGAATGTAGCATCAAA")
