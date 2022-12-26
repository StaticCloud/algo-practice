def factorial(num):
    total = 1;
    for i in range(1, num):
        total = total * i;

    return total;

print(factorial(10))