#!/usr/bin/env python3
numbers = [number for number in range(1,101)]
ordinal_numbers = []

for number in numbers:
    # if the number has 1 in the right most digit add 'st' to it and append to ordianl numbers list, and so on and so forth with other digits
    if (number % 10) == 1:
        ordinal_numbers.append(f"{str(number)}st")
    elif (number % 10) == 2:
        ordinal_numbers.append(f"{str(number)}nd")
    elif (number % 10) == 3:
        ordinal_numbers.append(f"{str(number)}rd")
    else:
        ordinal_numbers.append(f"{str(number)}th")

for n in ordinal_numbers:
    print(n)
