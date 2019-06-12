#define the function to be tested
def get_full_name(first, last, middle = ""):
    if middle:
        full_name = "{0},{1},{2}".format(first,middle,last)
    else:
        full_name = "{0},{1}".format(first,last)
    return full_name.title()
