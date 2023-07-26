def no_c(my_string):
    string2 = (my_string.translate({ord(i): None for i in 'cC'}))
    return string2
