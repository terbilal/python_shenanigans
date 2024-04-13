#!/usr/bin/env python3
from time import sleep
from random import randint
# A file for some wheel re invention stuff just for practice : 
# Think before you code u fucking nigger : 
def is_list_sorted(i):
    l = i[:]
    # checking if a list of integers is sorted
    sorted_or_not = True
    # len minus one because we gonna compare index var to index+1 and len(l)+1 will produce IndexError
    for index in range(len(l)-1):
        if l[index] <= l[index+1]:
            continue
        else:
            sorted_or_not = False
            break
    return sorted_or_not

def sort_list(i):
    l = i[:]
    buffer = 0
    """reinventing the wheel"""
    while not is_list_sorted(l):
        # keep looping until list is sorted
        # same shit for length lol
        for index in range(len(l)-1):
            # flip if the order is out of order 
            if l[index] > l[index+1]:
                # use buffer to switch values
                buffer = l[index]
                l[index] = l[index+1]
                l[index+1] = buffer
    return l

def dramatic_sort_list(i):
    l = i[:]
    buffer = 0
    """reinventing the wheel"""
    while not is_list_sorted(l):
        # keep looping until list is sorted
        # same shit for length lol
        for index in range(len(l)-1):
            # flip if the order is out of order 
            if l[index] > l[index+1]:
                print(f"\r{l}")
                sleep(0.15)
                # use buffer to switch values
                buffer = l[index]
                l[index] = l[index+1]
                l[index+1] = buffer

while False:
    # randomize list everytime
    randomized_list = [randint(1, 100) for i in range(20)]
    print(randomized_list)
    dramatic_sort_list(randomized_list)

# comb sorting : 
def comb_sort(i):
    # cloning the list yada yada cuz janky and fuck you for thinking u could use lists normally as arguments :3
    l = i[:]
    list_length = len(l)
    iteration, gap = 1, 1
    # same idea as bubble sort : 
    while not is_list_sorted(l):
        # gap equals len of list divided by gap over and over till its 1 : 
        gap = round(list_length/(1.3 ** iteration))
        iteration += 1
        for index in range(list_length - gap):
            if l[index] > l[index+gap]:
                # switch if values are out of order
                buffer = l[index]
                l[index] = l[index+gap]
                l[index+gap] = buffer
    return l

def dramatic_comb_sort(i):
    # cloning the list yada yada cuz janky and fuck you for thinking u could use lists normally as arguments :3
    l = i[:]
    list_length = len(l)
    iteration, gap = 1, 1
    # same idea as bubble sort : 
    while not is_list_sorted(l):
        # gap equals len of list divided by gap over and over till its 1 : 
        gap = round(list_length/ (1.3 ** iteration))
        iteration += 1
        for index in range(list_length - gap):
            if l[index] > l[index+gap]:
                # dramatic part : 
                print(f"{l} {gap}")
                sleep(0.1)
                # switch if values are out of order
                buffer = l[index]
                l[index] = l[index+gap]
                l[index+gap] = buffer
    return l

while True:
    # randomize list everytime
    randomized_list = [randint(1, 100) for i in range(20)]
    print(randomized_list)
    dramatic_comb_sort(randomized_list)
