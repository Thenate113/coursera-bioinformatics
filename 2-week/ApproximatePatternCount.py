#!usr/bin/python
import sys, HammingDistance as hd

def approximate_pattern_count(pattern, text, d):
    count = 0
    for i in range(0, len(text) - len(pattern) + 1):
        string = text[i:i + len(pattern)]
        if hd.hamming_distance(pattern, string) <= d:
            count+= 1
    
    return count

# input_file = open(sys.argv[1], "r")
# pattern = input_file.readline().strip()
# text = input_file.readline().strip()
# d = int(input_file.readline())

#print(approximate_pattern_count(pattern, text, d))
print("OMGLL")
print(approximate_pattern_count("TGT", "CGTGACAGTGTATGGGCATCTTT", 1))
