#! /usr/bin/python3

import firelink

print(*firelink.LIST_OF_SITES, sep='\n')
site = input("Please Enter the Site you want to visit between those previous sites: ")

for x in firelink.LIST_OF_SITES:
    if ("https://www."+site.lower()+".com") == x:
        firelink.firefox(site)