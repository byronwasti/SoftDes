def find_all_ORFs_both_strands(dna):
    comp = { 'A':'T', 'T':'A', 'G':'C', 'C':'G' }
    for idna in ( dna, ''.join([comp[i] for i in dna[::-1]])):  
        print
        print "IDNA"
        print idna
        print
        for j in range(3):
            print "Iterate"
            for threes in range(j,len(idna)-1,3):
                #print "Threes"
                #print idna[threes:threes+3],
                if idna[threes:threes+3] == "ATG":
                    print
                    print "Equal to ATG start"
                    #print idna[threes:threes+3]
                    for k in range(threes,len(idna),3):
                        print idna[k:k+3]
                        if idna[k:k+3] in ("TAG","TAA","TGA"):
                            print "FINAL:"+ idna[threes:k]
                            break
                    #print idna[threes:threes+3]
                
                
    

print find_all_ORFs_both_strands("CTAATGCGAATGTAGCATCAAA")
