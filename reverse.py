def reverse(string):
    # iterate through the string from the end of the string
    # append each item to a new string, which will be our reversed string
    strLen = len(string) - 1
    reversedStr = ""

    while strLen >= 0:
        reversedStr = reversedStr + string[strLen]
        strLen = strLen - 1;

    return reversedStr

print(reverse("just keep swimming"))