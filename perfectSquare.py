def isPerfectSquare(num):
    # iterate numbers from 1 to num
    # veritfy if a number to the power of 2 is equal to num
    # if so return true
    for number in range(num):
        if number**2 == num:
            return True

    return False

print(isPerfectSquare(36))