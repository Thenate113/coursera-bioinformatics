#!usr/bin/python

def hamming_distance(str1, str2):
    diff = 0
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            diff += 1

    return diff

print(hamming_distance(
    "CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA",
    "CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG"
))
#print(hamming_distance("CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG", "ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"))
#fi = open("dataset_9_3.txt", "r")

#print(hamming_distance(fi.readline(), fi.readline()))