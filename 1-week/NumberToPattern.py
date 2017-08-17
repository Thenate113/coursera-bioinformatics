#!usr/bin/python

num_to_nuc = {0:'A', 1:'C', 2:'G', 3:'T'}

def number_to_pattern(index, k):
    if k == 1:
        return num_to_nuc[index]
    prefix_index = int(index / 4)
    prefix_pattern = number_to_pattern(prefix_index, k -1)
    return prefix_pattern + num_to_nuc[index % 4]

#print(number_to_pattern(7591, 10))