def filter_list(l):
    new_l = []
    # check each element of the list and if not string
    # append to a new list
    for i in l:
        if type(i) != str:
            new_l.append(i)
    return new_l


print(filter_list([1,32,4,'g','mjau']))