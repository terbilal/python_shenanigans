#!/usr/bin/env python3
album_elements = ["artist name", "album name", "release year"]
def get_non_empty_input(prompt="Please input what you want to input : "):
    user_input = None
    while not user_input:
        user_input = input(prompt)
    return user_input

def get_album_dict(album_element_list=["album name"]):
    album = {}
    for album_element in album_element_list:
        album[album_element] = get_non_empty_input(f"please input the {album_element} : ")
    return album

albums = []
for i in range(3):
    albums.append(get_album_dict(album_elements))
print (albums)
