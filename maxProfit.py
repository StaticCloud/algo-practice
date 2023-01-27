def maxProfit(arr):
    max = 0
    max_index = 0

    for i in range(0, len(arr)):
        if arr[i] > max:
            max = arr[i]
            max_index = i
    
    min = 9999999
    max_index = 0;

    for i in range(0, len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_index = i

    if min_index > max_index:
        return 0;

    return max - min;

print(maxProfit([1, 6, 7, 9]))
    
