#!usr/bin/python
import sys, HammingDistance as hd

def approx_pattern_matching(pattern, text, d):
    matches = []
    for i in range(0, len(text) - len(pattern) + 1):
        substr = text[i:i + len(pattern)]
        if hd.hamming_distance(pattern, substr) <= d:
            matches.append(i)
    return matches

input_file = open(sys.argv[1], "r")
pattern = input_file.readline().strip()
text = input_file.readline().strip()
d = int(input_file.readline())
output = approx_pattern_matching(pattern, text, d)
output_file = open("approx_patt_match_output.txt", "w")
output_file.write(' '.join(str(val) for val in output))
print(*output)
