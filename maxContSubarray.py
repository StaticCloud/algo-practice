def maxSumArr(arr):
    allPos = True;

    if len(arr) == 2:
        return arr[0] + arr[1];
    
    for num in arr:
        if num < 0:
            allPos = False;
    
    if allPos == True:
        sum = 0;

        for num in arr:
            sum = sum + num;

        return sum;

    # set highest num and max sum to the first element
    highestNum = arr[0];
    maxSum = arr[0];

    for i in range(1, len(arr)):
        # is the sum of the current item and the highest sum greater than the current item?
        highestNum = max(arr[i], arr[i] + highestNum)
        # compare whatever highestSum returns and the current maxSum to determine the maximum continuous sum
        maxSum = max(maxSum, highestNum)

    return maxSum;

    

print(maxSumArr([-1, 2]))
print(maxSumArr([1, 2, 3, 4]))
print(maxSumArr([1, 2, -50, 4, 5]))
print(maxSumArr([-2,1,-3,4,-1,2,1,-5,4]))