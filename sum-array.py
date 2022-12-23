def sumArray(arr):
    total = 0;

    for num in range(len(arr)):
        total = total + arr[num]

    return total;

print(sumArray([1,2,3,4,5]))