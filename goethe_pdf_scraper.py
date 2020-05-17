from requests_html import HTML, HTMLSession
from urllib.request import urlretrieve
import os
import time

session = HTMLSession()
r = session.get('https://www.goethe.de/ins/gb/de/spr/unt/kum/dfj/kid.html')


box_with_themes = r.html.find('div .accordion_toggle')
theme_names_list = [theme.full_text.replace('\n', '') for theme in box_with_themes]

box_content = r.html.find('div .accordion_content')
theme_links_list = [list(theme.absolute_links) for theme in box_content]


for index, theme_links in enumerate(theme_links_list):
    print()
    directory_name = theme_names_list[index]
    if not os.path.isdir(directory_name):
        print(f"Creating directory: {directory_name}... ", end="", flush=True)
        os.makedirs(directory_name)
        print("Done.")

    for link in theme_links:
        file_name = link.split('/')[-1]
        save_path = f"{directory_name}/{file_name}"

        print(f"Downloading: {link}... ", end='', flush=True)

        urlretrieve(link, save_path)
        if os.path.isfile(save_path):
            print("Done.")
        else:
            print("Error!")
    print()
    print("-------")

print()
print()
print("Bye!")
print()
