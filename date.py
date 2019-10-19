#!/usr/bin/env python3

# Created by DJ Watson
# Created on October 2019
# this program asks a grandmother if you can date her grandchild


def main():
    # input

    numinput = input("Enter age: ")
    # process and output

    try:
        intcheck = int(numinput)
        if intcheck >= 0:
            if (intcheck >= 25) & (intcheck <= 40):
                print("you can date my grandchild")
            else:
                print("you can't date my grandchild")
        else:
            print("invalid input")
    except ValueError:
        print("invalid input")


if __name__ == "__main__":
    main()
