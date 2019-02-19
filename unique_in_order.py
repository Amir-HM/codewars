def unique_in_order(x):
    new_list = []
    previous = None
    for item in x:
        if item != previous:
            new_list.append(item)
        previous = item
    print(new_list)

unique_in_order('AAAABBBCCDAABBB')
