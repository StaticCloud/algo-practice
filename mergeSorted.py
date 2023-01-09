def mergeSort(arr1, arr2):
    # create unique index for both arrays
    # while index1 < arr1.length and index2 < arr2.length
        # is arr1[index1] > arr2[index2]
        # push arr2[index2] to the new array
        # otherwise push arr1[index1] to the new array
    sortedArr = []

    index1 = 0;
    index2 = 0;

    while (index1 < len(arr1) and index2 < len(arr2)):
        if (arr1[index1] < arr2[index2]):
            sortedArr.append(arr1[index1])
            index1 += 1;
        else:
            sortedArr.append(arr2[index2])
            index2 += 1;
    
    # the issue here is that the while loop exits if one index has exceeded the array 
    # so we need to accommodate for the remaining items in either array

    while (index1 < len(arr1)):
        sortedArr.append(arr1[index1])
        index1 += 1

    while (index2 < len(arr2)):
        sortedArr.append(arr2[index2])
        index2 += 1

    return sortedArr;

print(mergeSort([1,2,5,6],[3,4,7,8]))
# outputs [1, 2, 3, 4, 5, 6]