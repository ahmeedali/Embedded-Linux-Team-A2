#! /usr/bin/python3

import webbrowser

LIST_OF_SITES = [
"https://www.youtube.com",
"https://www.linkedin.com",
"https://www.github.com",
"https://www.stackoverflow.com",
"https://www.udemy.com",
]

def firefox(site):
    webbrowser.open("https://www."+site+".com")

