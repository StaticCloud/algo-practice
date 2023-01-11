def doubleTripleMap(arr):

    def isEven(num):
        return num * 2 if num % 2 == 0 else num * 3

    return [isEven(num) for num in arr]

print(doubleTripleMap([1,2,3,4,5,6]))