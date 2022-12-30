def isAnagram(strA, strB):
    # create one dictionary with unique keys
    # update respective values with number of times a letter appears
    # convert either dictionary to an array
    # iterate through it and use .get() to retrieve the respective letter's value from each dictionary
    # if it returns nothing, return false
    anagramDictA = {};
    anagramDictB = {};

    for letter in strA:
        if anagramDictA.get(letter) == None:
            anagramDictA[letter] = 1;
        else: 
            anagramDictA[letter] = anagramDictA[letter] + 1;

    for letter in strB:
        if anagramDictB.get(letter) == None:
            anagramDictB[letter] = 1;
        else: 
            anagramDictB[letter] = anagramDictB[letter] + 1;

    lettersA = list(anagramDictA.keys());
    lettersB = list(anagramDictB.keys());

    for letter in lettersA:
        if anagramDictA.get(letter) != anagramDictB.get(letter):
            return False;

    for letter in lettersB:
        if anagramDictA.get(letter) != anagramDictB.get(letter):
            return False;

    return True;
    

print(isAnagram("listen", "silent"))