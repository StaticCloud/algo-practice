def isAnagram(strA, strB):
    # compare the length of the strings, if they're not the same return False
    # sort the strings using .sorted()
    # then compare if the two strings
    if len(strA) != len(strB):
        return False;

    sorted_A = sorted(strA);
    sorted_B = sorted(strB);

    return sorted_A == sorted_B;

print(isAnagram("listen", "silent"))