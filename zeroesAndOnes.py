def zeroesAndOnes(str):
    zeroes = 0;
    ones = 0;

    for char in str:
        if char == "0":
            zeroes += 1;
        if char == "1":
            ones += 1;

    return zeroes == ones;

print(zeroesAndOnes("0001111"))