def characterCount(str):
    characterDict = {};

    for letter in str:
        count = characterDict.get(letter)
        
        if count == None:
            characterDict[letter] = 1;
        else:
            characterDict[letter] += 1;

    return characterDict;

print(characterCount("hello world"))