def linearSearch(arr, target):
    
    for index in range(len(arr)):
        if arr[index] == target:
            return index;
    
    return -1;

print(linearSearch([1,2,3,4,5,6,7], 3))