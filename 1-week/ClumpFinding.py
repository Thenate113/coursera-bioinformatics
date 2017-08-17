#!usr/bin/python
import FrequencyArray, PatternToNumber, NumberToPattern
# BetterClumpFinding(Genome, k, t, L)
#     FrequentPatterns ← an empty set
#     for i ← 0 to 4k − 1
#         Clump(i) ← 0
#     Text ← Genome(0, L)
#     FrequencyArray ← ComputingFrequencies(Text, k)
#     for i ← 0 to 4k − 1
#         if FrequencyArray(i) ≥ t
#             Clump(i) ← 1
#     for i ← 1 to |Genome| − L
#         FirstPattern ← Genome(i − 1, k)
#         index ← PatternToNumber(FirstPattern)
#         FrequencyArray(index) ← FrequencyArray(index) − 1
#         LastPattern ← Genome(i + L − k, k)
#         index ← PatternToNumber(LastPattern)
#         FrequencyArray(index) ← FrequencyArray(index) + 1
#         if FrequencyArray(index) ≥ t
#             Clump(index) ← 1
#     for i ← 0 to 4k − 1
#         if Clump(i) = 1
#             Pattern ← NumberToPattern(i, k)
#             add Pattern to the set FrequentPatterns
#     return FrequentPatterns

def better_clump_finding(genome, k, l, t):
    frequent_patterns = []
    clump = [0] * pow(4, k)
    text = genome[0:l]
    frequency_array = FrequencyArray.computing_frequencies(text, k)
    for i in range(0, pow(4, k) - 1):
        if frequency_array[i] >= t:
            clump[i] = 1
    ga = 0
    for i in range(1, len(genome) - l + 1):
        first_pattern = genome[i: i + k]
        index = PatternToNumber.pattern_to_number(first_pattern)
        frequency_array[index] = frequency_array[index] - 1
        last_pattern = genome[i + l - k: i + l]
        index = PatternToNumber.pattern_to_number(last_pattern)
        frequency_array[index] = frequency_array[index] + 1
        if frequency_array[index] >= t:
            clump[index] = 1
    
    for i in range(0, pow(4, k) - 1):
        if clump[i] == 1:
            frequent_patterns.append(NumberToPattern.number_to_pattern(i, k))

    return frequent_patterns


print (' '.join(map(str, better_clump_finding("CTGTGACGCGGCTAGCCCGAGATACTAATGTACCGGCCCCGGCCTTCCGTCCGCAAACAACACATCGAGACGTGGAAAACAAGCGCTGGCTTGACATGTGGACCTGGTTTTCGGGAATGAGCAGGATGCCTGGATGGCGTACAGCGTAGGTATTTAACAGTGGCGTTCGATGAATAATAGAAGACACGGGAAACGCACATAAATGAGAATAAGTGCGGATGTAAGAATAAATGCTTCCTCGAAGTGGCTAGCGTGTATAAGCGTGTAAGACGACTATTCCGTACGACCTATCTAATTACGGCTGATATCCTTGTCTGCATCGACTGATGAGTCCCCCCCGGGTTTCTCAGCGGTGCGATTACGTCGTAAAGACGTTCAACAAAATGGGTGTTCGCGATGTAGGGGACGCGTGGACGAAGAGCCCGCCAAGAGCCCGCCGGCCTACATGTCTCGGAAGAGCCCGCGCAAGAGCCCGAGAAATGTAAAGAGCCCGGGCATCAGCCACGAAGAGCCCGAAGAGCCCGTCACTCGAGCATAAGAGCCCGGGAGGCTTTAAAGAGCCCGTTTCACCAATTGACGCTAAAGCGAAGAGCCCGACCAAGAGCCCGTAAGAAGAGCCCGGTTGTCCCACCCAATTGACTTAAAAAGTAATTGACTTGGACACCAAAGAGATGTCTCAAATTGACTTAAGAGCCAATTGACTTATAAAATTGACTTTCATTGGTCAATTGACTTCAATTGACTTTTGCCCGCCCTGCATACGTCCCGCTCCAATTGAATTGAATTGACTTAAATTGACTTAATTGACTTGATGGTCGTTAGCCTGCCACCTCCTTGACAAAAAATTGACTTTGACTTTTGACTTCCCGAGCCCGAGCCCGGAAATTGAGACTACAGTTTCAAGAGCCCGAATTGACTTCCCGTTAAGAGCCCGTAAAGAATTGACTTCTAGTGGGGAATTGACTTCGTACGGATATTCTACAGTAGTAGGGCAGCTTAATTGACTTTTGGGAATTATTGCGAGTTATCCCATGTTCTGTGGTAAGCCGTTATTGAGCCCAATCGCGGCTGAGGAGGCCTAGGGAAAATTGACTTACTTAAGTGAGGGCTACGACGCTACCTCGAGAATTGACTTGGACATGAATTGACTTCTTGGGCTGAGAAATTGACTTTCTCCAATTGACAATTGACTTTTCCCACGGTTATGAACAGTGAACAGGGGTGCACCGGTTTGAAGCTGCGTATCAGCTTATGAACAGTTATGAACAGACATATGAACAGGCATATATATAGGTCCGCAATATGAACAGAACAGGAATCCGCAGTATGAACAGAACTATGAACAGATTCGATTATCTATGAACAGATCCCAACTATGAACAGGCCACCAAAGCAAGCGCTATGAACAGTAGCCTGGATCTATAGTTGCCACGGAGCACACAGTGATAGGCCGTATGAACAGCGACATTTATGAACAGACAGTGAGCTAAATATGAACAGCGTCGTGCATTTGGAAGAAACGGTAGCCACGATCCATCTCGAGGATATGAACAGACGTATGAACTATGAACAGTCTGCACTCAAGCGACCACTTATGAACAGACTATGAACAGAACAGATATGAACAGGGAAGTGTATCGCAACCATATGACAGGGAGTGCCCCGTATGAACAGGTCCCTATTATGAACAGCAGAATGTTGTATACGAAGGCGTACAGCAATATGAACAGGCGCTCTTTATGAACAGGAGTATAGACACGTTACCCTGTTCTGCTCTTCGTGGGGAAGAACGTGGTGAGTGAGGTGATAGTGCCGTCAACATACCGAAAAGGTAGTGCGCGCTAGCAAGAGCCTCCCCGCCTAGGAGGGTCTGAGCTTCCACTACTTGTAATGCTAAGACACTTACCCAAGTGGCAGCGAGCGAACAGGAATAATTTTGAATAACAGTGATTGGGGCGCTATGGTTCTCTGGTTAAGAACAGACCACCAAGTTCCTCCGTTTCCCCTCTACTGCTCAAGACCCTGTAACCCCATTGTGTCAGCTCGAGTCCGCTATAGGGAGCGAAAGTTCATAGAGCAGTGTCTATCAGCTTGCTATAGGAGAATGATAAATCATCTAAGTCTACGGAAAGAACATCCGTTTACCTTGAACTTGCATTAGATGGGCCACCTAGTATGGGCGTTATGTGATTTCTTTTACGACCAGGGCGCAGGGACGTCATATCTTTTTTAATTTACGGCTTGCTGTGTTACTGTCTCGGTACAGGCCTCCTACACTCTCACCCGATCGAAATTGCCTTAAAGAGTCAACCACCAACTGGGGCCGCCCTGTGGCGCTATCAGGCGTCAGCTCAGCTGATACACTAAGTACTCGGATCTGCTCGACACGCGATTGCTTCATCAGCCATTTGTAACGCGAGACTCGGCAGTGCCTAGGTCAGACGCTGCGCGGGCCATACACCGAACGTAGCGGGCCATATAGTGGCGGGCCATGCGGGCCATCTATTGCGGGCCATGAGCGGGCGCGGGCCATTCGTCACGTTTGGCGGGCCATCAGTAAGTCCAAAATAACGACGCGCCGGCTATACCTCTGGCGGGCCATGCCATGGGTTTAAGAGAATGCACCTTAGAAATATGCGGGACAATCAGTCGACGTCACGTGCTGTTGAGAATCAGCTCAGGCGGGCCATATGCCATCGGGCTAAGCGGCCTTCTCAAAGCGGGCCATGGCCATTGCGCACAGTTTCTCGCGGGCCATGAGTGGATTACTCTTAGCGGGCCATTATCATCCTATCCAAACATGGTGCGGGCGCGGGCCATCGCGGGCCATCGGGCGGGCCATCTTGTCGCATTATGTATACGGCCTACGGGCCTCCCCGTTGAGGGCTCGCAAGCGAGCGGGCCATAGTGCGGGTGTTCCGTGTTCGTGTTCCGTTGTTCCGTGCATCGTGTTCCGTTTGTTCCGTGTGTTCCGTAACAATGTGTTCCGTCCGTGGATATAGATGTATGTGAAACAAAATGCATGCGTGTTCCGTCGTACAGGCGATGGTGTTCCGTAATAGGTAGACTTGATTTCTGGGCCTCGACATGTAGCCCGATCAAGGCGTAACAGGCGTAAGCGATTACTGTCGAAGTGTTCCGTGTGTCGGGAACCGCGGTGACAACAGGCAGGTTCTCAGAATTGTGTTCCGTAAGCAGGAGTTTGGGTCCAGCTGGTGCTGTGTTCCGTGTGTTCCGTACGGGCTTTACAGGGGCTGCCCCGTTGTGGACGCACATGTTAGTGAGGCGTGTGTTCCGTAATAGTGTTCCGTTCATCGAGGGCCTTGCCGTGTTCCGTCAGAAATATAGTGTGTTCCGTGTGACGGAGCAAGGAAGTGTTCCGTCATCTAGTGTTCCGTGATCTTGTGTTCCGTCGCACCCTGTGTGTTCCGTTCTAGCTTAACAGTGTTCCGTTGCACGTAGGTAAAGACCGCTTGTCGCAAGTTAGCGACAGTCTTGGTACGTCAAGGCTAGTAGGTCCAGTAGTGTGGAATTCGAAGATGACACCCGATGTACAACGGCAAGAAGGGGAACTGGCGTCCAGGTGGCGGGTAGAGCCGACCGTTGGGGTGGGTTAGTCTAACCCTTAAACTTTCCAGGCAGTGCTTTGAGCTAAGGCATCCTAAGACACAGGGAGCGCAGAGGCGCGTGTAGCGGTATATACGCGAACTCACAATATAATGGACGGGGGCAACTCGTTATCCTTGTTTGCGAATTCTAAGACGTGCGAACTTACAGGGATCACTATTCTATTGAAGAGACCCGCGAGCTACTAGTAACGCAAGTAAATAGTTTAACTAGGGATCTGCTGATGCACCGTTCGTAATAACTTTGAACGCCTTAGTCAGCAATTAACCGCTGATCATGCGGTGCGGGGAATACACGCAAAGTTCTGGTCGTGAGCTATTGAGGTGCACGTATTGATTTAAGCCGAGAATCTCCCCACCCGCGACAAGCATAAGAAGGTACAAGCATAATAACAAGCATATACGTTGCTGCGCTCAACAGTAAATAGACAAGCATAAGTTCATATTGACAAGCATAGCAGAACTAATCGTCCGATACAAGCATATAACAAGCATATACCATCACAAGCATAGCATACTTGACAAGCATATCGCCCTGCAATTAGGTACAAGCATAACTTAATTTGGCACAAGCATGCTCCCAATACACATTCCTCGGATTAATGATGCTCCCAAATGCTCCCAATGCTCCCATCCCAAATATGTCCTGGACCCCTAGACAAGCACAATGCTCCCACTCGCCAGCCGATGCTCCATGATGCTCCCAGGGGTAGGCAACGTTTCATGCTCCCAACAAGCATATAGTTCCCCTAGCTACAAGCAATGCTCCCACGGTAGGGGCTAATGCTCCCAATAGACCACGCTTACGTGGGTCATGCTCCCATACCATCACAAGCATATTGATGATGCTCCCATACAGGATGCTCCCATGCTCCCAAGCAATGCTCCCAATAGGATAAATGCTCCCAATACAAGCATAGAATCCCCTAGGATAACTAACCTACAAGCATAACCCCATGCTCCCATGCTCCCACCCCTAGCTTAATGGGTCCCCTAGCTGGCTCCCCCCCCCTAGCTTTGCCCCTAGTATGCTCCCACATAACACGCCAGAGGGATGCTCCCAGAATGCTCCCACGAAATGCTCCCATAGCTTCTTAACGCGATCCATAGGTATGCTCCCACTATATGCTCCCAAAAATTCGTTATGCTCCCAACATTTAGGATAACGATAACCGAGAGAAAGAAAAAAAAAAATAGGATAATAGGATAACTAGGATAACCAGCACGATAGGATAACAACACCGTGATAGGATAACTAGGATAACAGGATAACACCGAGAAAAAAAACAGAAAAAAAGTTAAGAGTAGGATAACAAAAGGAAGTTATCACGGGCGTTATAGGATAACGATGAGCTAGGATTAGGATAACAGGATAACAGATAGGATAACAAAAAACATATACTGGCCAGTAGGATAACAGAGTCGTGTCTAACCAGAGAAAAAAAGAAATAGGATAACTAGAAAAAAAGAATAGGATAACCTCGACCCCCAAGAAAAAAACTTATGTAGGCTTTATAACTAGACGGTCCATGAGAGAAAAAAACCCGAATTTTAAGAAAAAAAGATTACTAAGAAAAAAAAAACGATTGGCTGCCTGACAACACCGACGAGAAAAAAAAAAAAACAGGAGAAAAAAACTGGAGAAAAAAAATTCTCGGTGACACATGACCAGAAAAAAATCAGTGGGCGCGAGCAGCTTCTCTGCCTCTCCTGCCCCTATACAAGTTGGAGTAACCGATAAAGTTGGAGAGAGTTAACAAGTTGGAGGTGATCAACACAATGTGCACAAGTTGGAGGGAGGCCCCTCCAAGTTGGAGCCATCAATAGGAGTCATGAAAGTTGGAGGTCATTCGACTCTAGTGAAAAGTTGGAGGTGTGGGACTTAGTTGCAAAGTTGGAGAGGACTTAGTTCCTTGGCAAAAGTTGGAGTTAGTCTCGGTATAAAAGTTGGAGGGCGCTTTGCATTGCAGCACTGCCTAAGGACTTGGACTTAGTGGACAAGTTGGAGGTAGCTGGACTTAGTTTAGTAGATGCGAGTTCGTCCGCCGAAAAAGTTGGAGGTTTGTCAAGTTGGAGGGAGGGGGAGGACTTAGTGAAGAAGTTGGAAGTTGGAGGGAGGGTGTGATTGTCGGACTTAGAAGTTGGAGACCGGGACTTAGTGGACTTAGTTCCGGCTGGACTTAAGTTGGAGGTGCTAATTCGGAAGTTGGAGAAGTTGGAGTTGCCGGACTTAGTCTGGGAAGTTGGAGGTCCGGACTTAGTATCGGACTGAAGTTGGAGAAGTTGGAGCTTAGTCAGCAAAGTTGGAGTTCTCCGCAGATTAGATAGGACTTAGTTACCGGTTTAGGACTTAGTTTACCATTTGGACTTAGTGGGTCAAGTGGTTCCTGTTTTATTACGAACTAAGCTGGCGGTACAAAGGGACTTAGTTAGTCATAAACCTATGAAACCATGGTCATGGTCTTAGGTGACCGTAAATGGGCCGCGTCTCCGCAGTCACCTCCTCCCATAACCCGGAATGTCAGTACATGCAAGTCTCTGTACTTTTTGTGTTCAAGAATCTATGGGCCCTAGGCCTTGACTTAGCCCGATGGTATTATTACTCTTTGCCTCAGACGACCAGCTTCTCGTTAAACAAGTAGCAGCACAAGCGTAATGAAATATCTTCACGAAGTTCTAGGAGTCGCGCTTATGGTATGGGCGCTTGCACAGGCACCGCGTGCTGGGCCCTTATTCCTTGTGAAGCCGGGGGCAGTCTCACAATTCCTATGATGAAACCTCTCTGATGATCCTACATTCTGGGAGTCATTTTACTACTCTGGGCCTGGTAGCAAGCTTTACAGGGAAGAAGGGGAAGCTGTTAGCGACAGGGAAGCTGTCGCGGAACAGGGAAGTTACAGGGAAGTATGGTGCACCACTATCAAATGTCCATACCTGCTTTCTAACGGCCTACCGCATTAAACACAGTCCGCCCGACGACACAGGGAAGCTATCAGATCCGTGGCGTGCCACAGGGAAGCATCCTTCTTCCTGCACACGGAACTATTAGGTGGTCTGCCCATAAAAGATCCGGACAGGGAAGGGCAACAGGGAAGGGTCCCGCCTTATGTACAGGGAAGAGGACCTGTACAGGGAAGGCCGGTTCGCTGACAGGGAAGAGGGGTTAGGTGCCACATCGTATCACTCACAGGGAAGCAGGGAAGCAGGGAAGGGTGCAAGACAGGGAAGAAGGTGATCGCCACAGGGAAGCAACAGGGAAGGGACAGGGAAGACCGCTGCTGACCTACAGGGAAGACCAAGAGAGAGACGCACAGGGAACAACAGGGAAGCGAACTCCAAAGCATACACCAAGTACAGGGAAGACAGGGAAGGGGAAGAACAGGGAAGTATCGTAAACTCCGGTCAACTCGCAAATAATAAGCCGTAGGGATACTCCCGTATAATATGTGGGTATAAGTCAACTCTCTGATACCCCGAAGTACCATTCCGGAAGAAGAGCGTTCTTAATGTTTTGTATAGCGTTTGACATTGTAGATGCTACATTTGCTCGACCCCAAGTCGCGTCGTGTTTTATTGTAAATCGAAACGCTAGTCATGCTTCAGTAATGCCCGCTCTTGTTCCTCGCTTGCACAAGCTTACTTTAACCCGGCCGCTGTAGACCTATATGGCGCGCCCACCGCAAGAATACGCATTCGCAACAAAGAGAAATCCACTAACACAATGCTGCTGTTTTGGCGGCGTTTCAAACCCACCAGATTTTCCGCACACATTTTTGCTCACCTCGGAGTTGATGTTCGTAGCTGATGTAATTACCAAATATTGGCAAGCGACGTACACAATGTGTCTACTTTTCGGGGTCTTTACGTGTAAACCTAATCTTGGGCAGGAAGCTTTCATACGTCTTTACCACAGGCCGCGGTCCGGAATATCCCGCTCTCCGAAGAGTAAATCAGGTGGTCGCGGTTAGTAGGCGTAAGCATGACAGAGGAAGTCAGGCCACCCTGCTAGGCCAAATGGGGCTCATGCGCGTTCCCAATCCCATATATCATGGAAATTATTATCTCCTACCGGCGCCAATGACGAATGTCAAATCTCGAGCGTCCTCGAATTCTGACCTCCGTAAAGCCGTCGTCAAGTCATAGGGGAGGGCGAAGAAGGACTAAACGATCGATGACAACCCTCTGACGTGGGGCCTTGCTCTGATTATATAATGAACCTTCTGACAGCCCTCGGTCACAATACCACTGCTGTAGGATTGTGTCAATACGAACTTGCTAAAGTTTACCGAAAAGATCGCACGAAAACGGCTGTGTTAGTGGCTACGAGTTATAACCGGCTATTCGCGCGGGGGGCAGCAAGCCACACTGAACCGGATGTGATGCGCTCAAGGCACCCAATCGGCGGCACCCAAACTGGGCACCCAATGGTGGAGGCACCCAATCTTGGCTGGGCACCCAAACCAAGGCACCCAATGGCGTATCACTCTTGGCACCCAAACCCAACCCAAAGGCACCCAAAAGGCACCCAACTCGCCATCCACAGGGCACCCAACGGTTACCTACCGTACGGCACCCAAGGGCTGATGGGCGGTTACATAATGAGACTAGTTCTACTTCGCGAGGGTCGCAGGCTGCACTTCGGCACCCAAATTCATCATAATTAGGATTCGGCACCCAAGGCACCCAATTAAACCCCCGCCATTCGAAGGTGGATCTTATAGGCACCGGCACCCAACCTGTCGCCTTAGGCACCCAACTGGACCATGAAATGGAGTCCTTGGGCACCCAATGGAAGAAGTCTCGTCAAGATGGTCACACGTTGGGTCGGCACGGCGGCACCCAAACGCAAAGGACCTTAGCACGGGCAGGCACCCAAGCACCCAAGTCTCTAACCTTCCAGACGGCAGACTAGGCACCCAAACCCAAGGCGATATTGGCACCCAAGTCATGGCACCCAATTGTTCCAATTGCATTTCAGGCGAGCGCTACACTAGAACGTAATTACTACTGGTTATTTTAGGCGTCGTCTCTCGTCGTGCGGCTCGTATCTTGTTTTTACCCTTCTTGTTTTATAGGGTCAGATCAAGGATCTTGTTTTTTGACTTATAGGGTCACTAATAGTGTTAGTCAGTCTCGTGTTAGTCAGGGTCAGTGTTAGTCGTGTTAGTCCTCCCGTTGTGTTAGTCGTGTTAGTGTGTTAGTCTTCCCTCTCCAGTGTTAGGTGTGTGTTAGTCAATAGGGTCATTGTCTTGTTTTTTTTTCTTGTTTTTCTTGTTTTTATAGGGTCACTTGTTTTTATAGGGAGTGTTAGTCTAGGTGTTAGTCTTGTATAGGGTGTTAGTCTTGTTTTTCTTGTGTTAGGTGTTAGTCGTCTTCTTGTTTTATAGGGTGTGTTAGTCTTTATAGGGTCAAATAGGGTCATAGGGGTGTTAGTCGTTAGTCGGTCAAGTGTTAGTCAGTCGTCAATAGGGTCAATAGGGTCAATAGGGTCAATATGTGTTAGTCTAGGGTCATAGGGTCAATAGGGTCAGTGTTAGTCGTGTGTTAGTCGTTAGTCGTGTTAGTCGTGTTAGTCGTGTTAGTC",
9, 573, 16))))