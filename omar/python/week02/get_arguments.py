#!/usr/bin/python3
import sys

def main():
    # Script name/path
    print("The name/path of the script:", sys.argv[0])

    # Arguments passed count
    n = len(sys.argv)
    print("\nNumber of arguments passed:", n)

    # Arguments list
    print("\nArguments list:", end = " ")
    # argsList = list(sys.argv[1:n])
    argsList = sys.argv[1:n]
    print(argsList)

if __name__ == '__main__':
    main()