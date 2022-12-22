def countdown(num):
    numbers = [number for number in range(1, num + 1)]

    [print(number) for number in reversed(numbers)]

countdown(20)