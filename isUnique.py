def isUnique(arr):
    numberCount = {}

    for number in arr:
        if numberCount.get(number) == None:
            numberCount[number] = 1;
        else:
            return False;

    return True;

print(isUnique([1,2,3,4,5,6,7]))