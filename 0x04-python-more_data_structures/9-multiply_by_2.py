#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dir = a_dictionary.copy()
    listkeys_ = list(new_dir.keys())

    for g in listkeys_:
        new_dir[g] *= 2

    return (new_dir)
