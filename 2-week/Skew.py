#!usr/bin/python

def skew(genome):
    nuc_to_skew = {
        "A":0,
        "T":0,
        "C":-1,
        "G":1
    }
    skew_array = [0] * (len(genome) + 1)
    for i in range(1, len(skew_array)):
        skew_array[i] = skew_array[i - 1] + nuc_to_skew[genome[i - 1]]
    
    return skew_array

print(max(skew("GCATACACTTCCCAGTAGGTACTG")))
#print(*skew("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"))

#print(' '.join(map(str, skew("CATGGGCATCGGCCATACGCC"), " " )))