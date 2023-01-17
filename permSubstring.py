def permSubstring(str, sub):
    for letter in sub:
        if letter not in str:
            return False
    
    return True

print(permSubstring("smapnuer", "super"))