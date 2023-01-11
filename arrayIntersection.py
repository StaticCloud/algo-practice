def arrayIntersection(arr1, arr2):
    return list(set(arr1).intersection(set(arr2)))

print(arrayIntersection([1, 2, 3, 4], [3, 4, 5, 6]))