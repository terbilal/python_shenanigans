#!/usr/bin/env python3
# a bunch of random python exercises to reinforce learn ig (remember that this is a hobby u fucking digger)

def common_between_lists(list_one, list_two):
    """return a list of the common elemtns between two lists"""
    common_items = []
    # make first_list the longer one
    if len(list_one) > len(list_two):
        first_list, second_list = list_one[:], list_two[:]
    else:
        second_list, first_list = list_one[:], list_two[:]
    # use the fact the .remove method for lists removes only first instance of the item it finds UwU
    for item in first_list:
        if item in second_list:
            print(item)
            common_items.append(item)
            # remove the found instance in both copied lists
            first_list.remove(item)
            second_list.remove(item)
    return common_items

def reverse_string(string):
    char_list = [char for char in string]
    char_list.reverse()
    return "".join(char_list)
