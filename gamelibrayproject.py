#!/usr/bin/python3
# gamelibraryproject.py
# KJ Klamer
# 1/27/2020
'''Runs prototype for the game library project'''
def add_edit_game():
    print("running.add_edit_game()")
def show_all_games():
    print("running.print_all_games()")
def search_by_title():
    print("running add_new()")
def remove_game():
    print("running.remove_game()")
def save_data_base():
    print("running.savedatabase()")
def quit():
    print("running quit()")
    exit()
menu = True

while menu:
    print("""
    Welcome to Big Brother Inc.
    ---------------------------
    
    MAIN MENU
    1) Add/Edit a game
    2) Show All Games
    3) Search By Game Title
    4) Remove Saved Game
    5) Quick Save Game
    
    Q) Quit
    
    """)
    
    choice = input("What would you like to do? ")
    if choice == "1":
        add_edit_game()
    elif choice == "2":
        show_all_games()
    elif choice == "3":
        search_by_title()
    elif choice == "4":
        remove_game()
    elif choice == "5":
        save_data_base()
    elif choice == "Q" or choice == "q":
        quit()
    else:
        print("*** NOT A VALID CHOICE ***\n")
        
print("Goodbye.")