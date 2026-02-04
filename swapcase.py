def swap_case(s):
    c = []
    for char in s:
        if char.isupper():
            c.append(char.lower())
        elif char.islower():
            c.append(char.upper())
        else:
            c.append(char)
    final = ''.join(c)
    return final

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)