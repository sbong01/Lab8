def until_dot(s):
    index = 0
    while index < len(s) and s[index] != ".":
        index += 1
    print(s[:index])

until_dot("This is a sentence. This is another.")
until_dot("192.256.4")
until_dot("No dots here")
