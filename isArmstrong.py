def isArmstrong(num):
    length = len(str(num))
    sum = 0

    for integer in str(num):
        sum = sum + int(integer)**length

    return num == sum

print(isArmstrong(11))
print(isArmstrong(153))