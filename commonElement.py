def commonElement(arr1, arr2):
    elementDict = {}

    for element in arr1:
        if elementDict.get(element) == None:
            elementDict[element] = True

    for element in arr2:
        if elementDict.get(element) == True:
            return element;

print(commonElement([1, 9, 8, 7],[10, 12, 1, 6, 5]))