def titleCase(str):
    # split the string up
    # iterate through it and capitalize each item
    # join the string again
    splitString = str.split(' ');

    capitalized = [word.capitalize() for word in splitString];

    return " ".join(capitalized)

print(titleCase("the quick brown fox jumped over the lazy dog"))