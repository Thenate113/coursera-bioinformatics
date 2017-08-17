#!usr/bin/python

# PatternToNumber(Pattern)
#     if Pattern contains no symbols
#         return 0
#     symbol ← LastSymbol(Pattern)
#     Prefix ← Prefix(Pattern)
#     return 4 · PatternToNumber(Prefix) + SymbolToNumber(symbol)
nuc_to_num = {'A':0, 'C':1, 'G':2, 'T':3}

def pattern_to_number(pattern):
    if len(pattern) <= 0:
        return 0
    return 4 * pattern_to_number(pattern[:-1]) + nuc_to_num[pattern[-1:]]

#print(pattern_to_number("GCCGCTATGCCGGTTCCG"))