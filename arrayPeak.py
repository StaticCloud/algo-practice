def peakArray(arr):
    largest = -99999

    for num in arr:
        if num > largest:
            largest = num
    
    return largest

print(peakArray([2, 4, 6, 8, 10]))