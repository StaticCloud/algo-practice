def productOfLargestTwo(arr):
    # have a largest number two really small numbers
    # compare an item in the array against the first item in the largest number array
    # if it's smaller than the first item, compare it against the second item
    # replace both numbers if they're respectively smaller than the items in the array
    largestTwo = [-9999999, -9999999];

    for num in arr:
        if (num > largestTwo[0]):
            largestTwo[0] = num;
        elif (num > largestTwo[1]):
            largestTwo[1] = num;

    print(largestTwo)
    return largestTwo[0] * largestTwo[1];

print(productOfLargestTwo([12,13,5,6,89,9]))