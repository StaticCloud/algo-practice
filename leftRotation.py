def leftRotation(arr, positions):
    # assign the positions variable to a counter variable
    # move the first item in the array at the end of the array and reduce the counter
    # repeat until the counter has reached 0
    while positions > 0:
        first = arr[0]
        arr = arr[1:]
        arr.append(first)
        positions -= 1
        

    return arr

print(leftRotation([1, 2, 3], 2))