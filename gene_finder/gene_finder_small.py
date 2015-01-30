def find_all_ORFs_both_strands(dna):
    comp = { 'A':'T', 'T':'A', 'G':'C', 'C':'G' }
    return [ idna[idna.find("ATG"):threes] for idna in (dna, ''.join([comp[i] for i in dna[::-1]])) for j in range(3) for threes in range(j, len(idna)-1,3) if idna[threes:threes+3] in ("TAG","TAA","TGA") and len(idna[idna.find("ATG"):threes])%3 == 0 and len(idna[idna.find("ATG"):threes]) != 0]


print find_all_ORFs_both_strands("CTAATGCGAATGTAGCATCAAA")
