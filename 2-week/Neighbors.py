#!usr/bin/python
import HammingDistance as hd

def neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return {'A', 'C', 'G', 'T'}
    neighborhood = set()
    
    suffix_neighbors = neighbors(pattern[1:], d)
    for text in suffix_neighbors:
        if hd.hamming_distance(pattern[1:], text) < d:
            neighborhood.add('A' + text)
            neighborhood.add('T' + text)
            neighborhood.add('C' + text)
            neighborhood.add('G' + text)
        else:
            neighborhood.add(pattern[0] + text)
    return neighborhood

#fi = open("neighbor_output.txt", "w")

neighborhood = neighbors("TGCAT", 2)
print("LOLOL")
print(len(neighborhood))
#fi.write('\n'.join(str(val) for val in neighborhood))