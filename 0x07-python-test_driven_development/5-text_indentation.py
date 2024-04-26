#!/usr/bin/python3
"""Contains the function `text_intentation`"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:
    '.', '?' and ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        new_str = ""
        for i in text:
            if i == '.' or i == '?' or i == ':':
                new_str += i + "\n\n"
            else:
                new_str += i

    new_str = "\n".join(line.strip() for line in new_str.split("\n"))
    print(new_str, end="")
