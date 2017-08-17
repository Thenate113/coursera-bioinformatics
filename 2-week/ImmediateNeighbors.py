#!usr/bin/python

def immediate_neighbors(pattern):
    neighborhood = set()
    neighborhood.add(pattern)
    for i in range(0, len(pattern)):
        symbol = pattern[i]        
        neighborhood.add(pattern[:i] + 'A' + pattern[i+1:])
        neighborhood.add(pattern[:i] + 'C' + pattern[i+1:])
        neighborhood.add(pattern[:i] + 'T' + pattern[i+1:])
        neighborhood.add(pattern[:i] + 'G' + pattern[i+1:])
    return neighborhood

print(immediate_neighbors("ACT"))