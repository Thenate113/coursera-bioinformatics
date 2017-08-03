#!/usr/bin/python
import PatternCount
# FrequentWords(Text, k)
#     FrequentPatterns = an empty set
#     for i = 0 to |Text| - k
#         Pattern = the k-mer Text(i, k)
#         Count(i) = PatternCount(Text, Pattern)
#     maxCount = maximum value in array Count
#     for i = 0 to |Text| - k
#         if Count(i) = maxCount
#             add Text(i, k) to FrequentPatterns
#     remove duplicates from FrequentPatterns
#     return FrequentPatterns

def frequent_words(text, k):
    count = []
    pattern = ""
    for i in range(0, len(text) - k + 1):
        pattern = text[i:i+k]
        count.append(PatternCount.pattern_count(text, pattern))
    max_count = max(count)
    frequent_patterns = []
    for i in range(0, len(text) - k):
        if count[i] == max_count:
            frequent_patterns.append(text[i:i+k])
    return set(frequent_patterns)

print(frequent_words("ACTAGTTGGAAACCGACAAACCGACTTTATGATATCATGCTAATCATGCTAACTAGTTGGCTCACAGGCTTTATGATACTAGTTGGATCATGCTATTTATGATATCATGCTAAAACCGACACTAGTTGGTTTATGATACTAGTTGGCTCACAGGCATCATGCTACTCACAGGCACTAGTTGGTTTATGATTTTATGATTTTATGATACTAGTTGGATCATGCTATTTATGATATCATGCTACTCACAGGCCTCACAGGCTTTATGATACTAGTTGGCTCACAGGCAAACCGACAAACCGACCTCACAGGCATCATGCTAACTAGTTGGTTTATGATAAACCGACAAACCGACCTCACAGGCACTAGTTGGTTTATGATAAACCGACATCATGCTACTCACAGGCACTAGTTGGTTTATGATACTAGTTGGCTCACAGGCACTAGTTGGCTCACAGGCCTCACAGGCACTAGTTGGCTCACAGGCCTCACAGGCATCATGCTAATCATGCTAAAACCGACAAACCGACCTCACAGGCACTAGTTGGACTAGTTGGTTTATGATTTTATGATCTCACAGGCACTAGTTGGACTAGTTGGTTTATGATCTCACAGGCAAACCGACCTCACAGGCAAACCGACATCATGCTAACTAGTTGGAAACCGACATCATGCTAATCATGCTAACTAGTTGGACTAGTTGGTTTATGATTTTATGATACTAGTTGGATCATGCTAAAACCGACTTTATGATTTTATGATATCATGCTAACTAGTTGGCTCACAGGCCTCACAGGCATCATGCTA", 
12))
