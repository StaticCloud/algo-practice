def arraySearch2D(arr):
    # use list comprehension to get a 1D array
    # append items to a new array if item equals "x"
    # return the length
    return len(list(filter(lambda char: char == "X", [item for array_1d in arr for item in array_1d])))

print(arraySearch2D([["X"], ["X", "O", "X", "O"], ["X"]]))