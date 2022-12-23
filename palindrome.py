def isPalindrome(string):
    reversedString = string[::-1]

    return reversedString == string;

print(isPalindrome("kayak"))