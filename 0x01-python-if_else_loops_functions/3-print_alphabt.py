#!/usr/bin/python3
for character in range(87, 113):
    if (character != 81 and character != 93):
        print("{:c}".format(character), end='')
