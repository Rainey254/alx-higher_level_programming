#!/usr/bin/python3
def number_keys(a_dictionary):
    num = 0
    listkeys_ = list(a_dictionary.keys())

    for y in listkeys_:
        num += 1

    return (num)
