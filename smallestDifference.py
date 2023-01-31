def smallestDifference(arr1, arr2):
    # set the min difference to the largest integer
    minDiff = float('inf');
    # initialize absolute value
    absolute = 0;
    # set pairs to an empty array
    pairs = [];
    # iterate through both arrays
    i = 0;
    j = 0;

    while (i < len(arr1) and j < len(arr2)):
        absolute = abs(arr1[i] - arr2[j]);

        if (absolute < minDiff):
            minDiff = absolute;
            pairs = [arr1[i], arr2[j]]

            # this edge case is important because the following if statements wont occur if BOTH items in each array are equal
            if (minDiff == 0):
                return pairs

        if (arr1[i] < arr2[j]):
            i = i + 1;
        elif (arr1[i] > arr2[j]):
            j = j + 1;

    return pairs

print(smallestDifference([2, 4, 6, 8, 15, 20], [17, 25, 30, 47]))
print(smallestDifference([1, 6, 7, 9], [8, 9, 10, 11, 12, 13]))