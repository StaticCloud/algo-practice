def camelCase(str):
    # split the string between spaces
    # set the first character to lower case
    # iterate through the rest of the strings and set them to uppercase
    splitString = str.split(' ');

    splitString[0] = splitString[0].lower();

    for index in range(1, len(splitString)):
        splitString[index] = splitString[index].capitalize();

    return ''.join(splitString);

print(camelCase("this is the end"))