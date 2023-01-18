def reverseInPlace(arr):
    counter = len(arr) - 1

    while counter > 0:
        first = arr[0]
        arr = arr[1:]
        arr.append(first)
        counter -= 1;

    return arr

print(reverseInPlace([2, 4, 6, 8]))