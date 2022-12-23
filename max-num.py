def maxNum(arr):
    max = -9999999999999;

    for num in arr:
        if (num > max):
            max = num;

    return max;

print(maxNum([1,2,3,4,5,6,7,8,9,10]))