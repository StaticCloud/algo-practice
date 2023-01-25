def validBrackets(str):
    stack = [];

    for i in str:
        if (i == '(') or (i == '[') or (i == '{'):
            stack.append(i)

        if (i == ')'):
            if (stack.pop() != '('):
                return False;

        if (i == ']'):
            if (stack.pop() != '['):
                return False;

        if (i == '}'):
            if (stack.pop() != '{'):
                return False;

    return True;


print(validBrackets("( [ ) ]"))