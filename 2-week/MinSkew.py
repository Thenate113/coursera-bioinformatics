#!usr/bin/python
import Skew

def min_skew(skew_array):
    min_val = min(skew_array)
    ret_array = []
    print(min_val)
    for i in range(0, len(skew_array)):
        if skew_array[i] == min_val:
            ret_array.append(i)

    return ret_array

fi = open("dataset_7_6.txt", "r")
skew_array = Skew.skew(fi.read().strip())
print(*min_skew(skew_array))