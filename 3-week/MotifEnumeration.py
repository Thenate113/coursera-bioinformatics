#!usr/bin/python
import sys
import Neighbors as nb
import HammingDistance as hd

def motif_enumeration(dna, k, d):
    patterns = {}
    kmers = []
    k_str = dna[0]
    for i in range(0, len(k_str) - k + 1):
        kmers.append(k_str[i:i + k])
    print(kmers)
    return
    for pattern in neighbors:
        for i in range(1, len(dna)):
            right_neighbors = nb.neighbors(dna[i])
            

input_file = open(sys.argv[1], "r")

k = int(input_file.read(2).strip())
d = int(input_file.read(2).strip())

with input_file as f:
    dna = f.read().splitlines()

motif_enumeration(dna, k, d)
# text = input_file.readline().strip()
# d = int(input_file.readline())
