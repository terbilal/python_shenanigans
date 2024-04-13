#!/usr/bin/env python
# list of people i would invite rn to dinner
persons = ["will wood", "suckerpinch", "inA", "yoko", "hasan"]
for person in persons:
    print (f"{person.title()}, I invite you to dinner :3")

# people who cant make it :
print()
unpersons = ["will wood", "yoko", "hasan"]
for unperson in unpersons:
    # remove unperson from invited and print them out
    if unperson in persons:
        print (f"{unperson.title()} sadly can't attend the dinner")
        persons.remove(unperson)

# replace the uninvted persons with more persons
new_invites = ["charlie", "ange", "wube software director"]
for new_invite in new_invites:
    persons.append(new_invite)

# reprint the persons
print()
for person in persons:
    print (f"{person.title()}, I invite you to dinner :3")

# bigger table found :
print("We found a bigger table so we will invite more people")
persons.insert(0, "ambiguos guest 1")
persons.insert(int(len(persons)/2), "ambiguos guest 2")
persons.append("finaly ambiguos guest")

# reprint the persons
print()
for person in persons:
    print (f"{person.title()}, I invite you to dinner :3")

# table wont arrive :(
print("Only left place is for two people, because big table won't arrive which is D:")
while len(persons) > 2:
    print (f"Sorry {persons.pop().title()} Dont have space for you on the tiny table D:")

# print left invited persons
print()
for person in persons:
    print (f"{person.title()}, You're still invited")

# empty the list and print it :
del persons[0]
del persons[0]
print(persons)
