def fizzBuzz(arr):
    for num in arr:
        if (num % 15 == 0):
            print("Fizz Buzz")
        elif (num % 3 == 0):
            print("Fizz")
        elif (num % 5 == 0):
            print("Buzz")


fizzBuzz([1,2,3,4,5,6,7,8,9,10])