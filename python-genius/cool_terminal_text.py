#!/usr/bin/python3
import os
from pyfiglet import Figlet

def print_cool(text):
    cool_text = Figlet(font="slant")

    os.system("clear")

    return str(cool_text.renderText(text))

if __name__ == "__main__":
    print(print_cool("happy new year"))
