#!/usr/bin/python

import sys

# PatternCount(Text, Pattern)
#     count = 0
#     for i = 0 to Text - Pattern
#         if Text(i, Pattern) = Pattern
#             count = count + 1
#     return count




def pattern_count(text, pattern):
    count = 0
    for i in range(0, len(text)-len(pattern) + 1):
        #print (text[i:len(pattern)+i])
        if text[i:len(pattern)+i] == pattern:
            count = count + 1
    return count


print (pattern_count("StrStr1", "St"))
#print pattern_count(str(sys.argv[1]), str(sys.argv[2]))
