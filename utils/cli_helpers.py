import os
import sys
from simple_term_menu import TerminalMenu

def create_menu(options, title):
    menu = TerminalMenu(options, title=title)
    return menu.show()

def clear_terminal():
    if sys.platform.startswith("win"):
        os.system("cls")
    else:
        os.system("clear")