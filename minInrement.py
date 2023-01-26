def minIncrement(arr):
    # create an object for the unique numbers
    # append each number to the object
    # if the number already exists in the object, keep incrementing it until it's no longer a unique number
    # append 1 to increment
    # return incremented
    unique = {};
    increments = 0;

    for num in arr:
        if (unique.get(num) != None):
            while (unique.get(num) == True):
                num = num + 1;
                increments = increments + 1

        unique[num] = True;

    return increments;

print(minIncrement([3, 2, 1, 2, 1, 7]))