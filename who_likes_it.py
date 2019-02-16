def likes(array):
    arr_len = len(array)
    if arr_len == 0:
        return("no one likes this")
    elif arr_len == 1:
        return("{0} likes this".format(array[0]))
    elif arr_len == 2:
        return("{0} and {1} like this".format(array[0], array[1]))
    elif arr_len == 3: 
        return("{0}, {1} and {2} like this".format(array[0],array[1],array[2]))
    else:
        return("{0}, {1} and {2} others like this".format(array[0], array[1], arr_len-2))
