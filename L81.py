
def total_length(list):
    count = 0
    for x in list:
        count = count + len(x)
    print(count)

total_length(['Queen', 'rules'])
total_length([])
total_length(['balloons'])
total_length(["", '', "", ""])
