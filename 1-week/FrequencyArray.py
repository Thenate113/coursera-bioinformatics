#!usr/bin/python
#   ComputingFrequencies(Text, k)
#         for i ← 0 to 4k − 1
#             FrequencyArray(i) ← 0
#         for i ← 0 to |Text| − k
#             Pattern ← Text(i, k)
#             j ← PatternToNumber(Pattern)
#             FrequencyArray(j) ← FrequencyArray(j) + 1
#         return FrequencyArray

nuc_to_num = {'A':0, 'C':1, 'G':2, 'T':3}

def pattern_to_number(text):
    length = len(text)
    total = 0
    for i in range(1, length + 1):
        total = total + nuc_to_num[text[i-1]] * pow(4, (length - i))
    return total

def computing_frequencies(text, k):
    frequency_array = [0] * (pow(4,k))
    for i in range(len(text) - k + 1):
        #print(text[i:i + k] + str(pattern_to_number(text[i:i + k])))
        frequency_array[pattern_to_number(text[i:i + k])] += 1

    return frequency_array

fi = open("freq_array_output.txt", "w")
fi.write(' '.join(map(str, computing_frequencies("GATTCAGCCGCCTCAACGTCGCACCCGTGCATTTAATGTTAGGCTCGGGGAAACTGACCTTCAAGCTACCGTTTGCGCCACTTCAACCTCAAGAAACCAGAATCGTAGTCGGCTGTGTGTGAGGATCACAAGGGACCAATACTTACGGCCCATTGGCAGGCGGCCCCTACGATCGACCACCCGTATTAGGTAATGTGAAGTTGGTTGAGCAGCCCGCGCTTTATACACAGTGCAAAAGCTCCACGCCATTCTCTGAAGGCCGTCCCCTACGACTCGAAAAGAACAGGAATCTTCCCCCTCCGATGAGTGAGGTGAGGGACTTTCAGTCAATGAGCTATTCATAAGAGGCCGCGCCTTTTGGGCCTGCGTGGACGAAGGATGTTTCTCTCAGTACCCCGACATTATTATTAGATATTCCTTCGCAATTGCGAGCGGAACACGCATTACGAGCTAAGACTGAGTATGGAATTTTGAAGCAAGCATCGGGGTTAGCAGACGCTCGGGCATTGTCGGGCAAAAGGGCATTGGTTCCCAGTCCAATGGCCGTTCGCGAACGCTTGACCACGCAATGGGTTTTTTCAGGTCCCGAGTCTTCCTCTCGACCCGTGTTCGCCGGACTCGATGCCTTAGTATTGAACTCCCTGCCCAGAGACGTCGAGCTCAATTGCACCTCATCAATCAGGGAGCTAATGATCA", 
6)) ))
