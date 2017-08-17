#!usr/bin/python
import sys, Neighbors as nb

compliment = {'A':'T', 'T':'A',
              'G':'C', 'C':'G'}

def reverse_compliment(string):
    rev_com = []
    for char in string[::-1]:
        rev_com.append(compliment[char])

    return rev_com

nuc_to_num = {'A':0, 'C':1, 'G':2, 'T':3}

def pattern_to_number(pattern):
    if len(pattern) <= 0:
        return 0
    return 4 * pattern_to_number(pattern[:-1]) + nuc_to_num[pattern[-1:]]

num_to_nuc = {0:'A', 1:'C', 2:'G', 3:'T'}

def number_to_pattern(index, k):
    if k == 1:
        return num_to_nuc[index]
    prefix_index = int(index / 4)
    prefix_pattern = number_to_pattern(prefix_index, k - 1)
    return prefix_pattern + num_to_nuc[index % 4]


def compute_freq_with_mismatch(text, k, d):
    frequency_array = [0] * (pow(4,k))

    for i in range(0, len(text) - k + 1):
        pattern = text[i:i + k]
        rev_com = reverse_compliment(pattern)
        print(rev_com)
        neighborhood = nb.neighbors(pattern, d)
        for string in neighborhood:
            frequency_array[pattern_to_number(string)] += 1
        
        neighborhood = nb.neighbors(rev_com, d)
        for string in neighborhood:
            frequency_array[pattern_to_number(string)] += 1
    
    return frequency_array

def get_patterns(text, k, d):
    frequency_array = compute_freq_with_mismatch(text, k, d)
    val = max(frequency_array)
    patterns = []
    for i in range(0, len(frequency_array)):
        if val == frequency_array[i]:
            patterns.append(number_to_pattern(i, k))

    return patterns

input_file = open(sys.argv[1], "r")
pattern = input_file.readline().strip()
print(pattern)
k = int(input_file.read(1).strip())
print(k)
d = int(input_file.readline())
print(d)
output = get_patterns(pattern, k, d)
output_file = open("freq_with_mismatch_rev_comp.txt", "w")
print(*output)
output_file.write(' '.join(map(str, output)))
#print(*output)

