def vowelCount(string):
    count = 0;
    vowels = ["a","e","i","o","u"];

    for letter in string:
        if letter in vowels:
            count = count + 1;

    return count;

print(vowelCount("the quick brown fox jumped over the lazy dog"))