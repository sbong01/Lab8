def count_character(name, letter):
    index = 0
    count = 0
    while index < len(name):
        if name[index:index + len(letter)] == letter:
            count += 1
            index += len(letter)
        else:
            index += 1
    return count


print(count_character("bonobos", "o"))



# ##for
# def count2(string, target):
#     count=0
#     for ch in string:
#         if ch == target:
#             count= count +1
#     return count
#
# print(count2("bonobos", "o"))
