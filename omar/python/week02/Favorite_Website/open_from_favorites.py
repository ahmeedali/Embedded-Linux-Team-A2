#!/usr/bin/python3

import favwebs

def main():
    favwebs.show_favorites()
    website = favwebs.select_fav()
    favwebs.Firefox(website)

if __name__ == "__main__":
    main()