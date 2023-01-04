def multiplyInto20(arr):
    # compare the first item in the array to every item
    # then pop it and compare everything with the new first item
    # if there are two numbers in the array that multiply into 20, return true
    # otherwise return false
    while len(arr):
        firstItem = arr[0]

        for num in range(1, len(arr)):
            if firstItem * arr[num] == 20:
                return True;
        
        arr.pop(0)
    
    return False;

print(multiplyInto20([20, -20, 18, 2, 3, 4]))