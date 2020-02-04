#!/usr/bin/python3
# gamelibraryproject.py
# KJ Klamer
# 1/27/2020
'''Runs prototype for the game library project'''
import pickle
from threading import Timer
import time
games = {}
games_library = open("game_lib.pickle","rb")
games = pickle.load(games_library)
games_library.close()

def add_edit_game():  
    
    def add():
        game_add = input("What is the Game You Would Like to Add? ")
        for key in games.keys():
            if game_add in games[key][1]:
                print("*** THAT GAME IS ALREADY IN THE LIBRARY ***\n")
            else:
                genre_add = input("   What is the game genre? ")
                title_add = input("   What is the game title? ")
                developer_add = input("   Who is the developer? ")
                publisher_add = input("   Who is the publisher? ")
                system_add = input("   What is the sytem? ")
                release_date_add = input("   When was it released? ")
                rating_add = input("   What is its rating? ")
                sing_multi_both_add = input("   Is it Singleplayer/Multiplayer or Both? ")
                price_add = input("   What is the price? ")
                beat_it_add = input("   Have you beat it before? ")
                purchase_date_add = input("   When was it purchased? ")
                notes_add = input("   Any notes for the game? ")
                games[game_add] = [genre_add, title_add, developer_add, publisher_add, system_add,
                                   release_date_add, rating_add, sing_multi_both_add, price_add, 
                                   beat_it_add, purchase_date_add, notes_add]    
                break
    def edit():
        game_edit = input("What is the Game You Would Like to Edit? ")
        for key in games.keys():
            if game_edit not in games[key][1]: 
                print("*** THAT GAME IS NOT IN THE LIBRARY ***\n") 
        
            else:
                genere_edit = input("   What is the game genre? ")
                title_edit = input("   What is the game title? ")
                developer_edit = input("   Who is the developer? ")
                publisher_edit = input("   Who is the publisher? ")
                system_edit = input("   What is the sytem? ")
                release_date_edit = input("   When was it released? ")
                rating_edit = input("   What is its rating? ")
                sing_multi_both_edit = input("   Is it Singleplayer/Multiplayer or Both? ")
                price_edit = input("   What is the price? ")
                beat_it_edit = input("   Have you beat it before? ")
                purchase_date_edit = input("   When was it purchased? ")
                notes_edit = input("   Any notes for the game? ")
                games[game_edit] = [genere_edit, title_edit, developer_edit, publisher_edit, system_edit,
                                    release_date_edit, rating_edit, sing_multi_both_edit, price_edit, beat_it_edit,
                                    purchase_date_edit, notes_edit]    
                    
                break                
    option = input(" Would you like to add/edit a game or quit to main menu? ")
    if option == "Add" or option == "add" or option == "a" or option == "A":
        add()
    elif option == "Edit" or option == "edit" or option == "e" or option == "E":
        edit()                                
    elif option == "Quit" or option == "quit" or option == "q" or option == "Q":
        print("...Returning to Menu...")
        return menu
def show_all_games():
    key_list = games.keys()    
    for key in key_list:
        print()
        print("Genre: ", games[key][0])
        print("Title: ", games[key][1])
        print("Developer: ", games[key][2])
        print("Publisher: ", games[key][3])
        print("System: ", games[key][4])
        print("Release Date: ", games[key][5])
        print("Rating: ", games[key][6])
        print("Single/Multi/Both: ", games[key][7])
        print("Price: ", games[key][8])
        print("Beat it: ", games[key][9])
        print("Purchase Date: ", games[key][10])
        print("Notes: ", games[key][11])
        print("----------------------")
   

def search_by_title():

    def genre():
        found_one = False
        genre = input("What is the genre? ")
        for key in games.keys():
            if genre == games[key][0]:
                found_one = True
                print()
                print("Genre: ", games[key][0])
                print("Title: ", games[key][1])
                print("Developer: ", games[key][2])
                print("Publisher: ", games[key][3])
                print("System: ", games[key][4])
                print("Release Date: ", games[key][5])
                print("Rating: ", games[key][6])
                print("Single/Multi/Both: ", games[key][7])
                print("Price: ", games[key][8])
                print("Beat it: ", games[key][9])
                print("Purchase Date: ", games[key][10])
                print("Notes: ", games[key][11])
                print("----------------------")
                
        if not found_one:
            print("*** NO MATCHES FOUND!***\n")

        
    def title():
        found_one = False
        genre = input("What is the title? ")
        for key in games.keys():
            if genre == games[key][1]:
                found_one = True
                print()
                print("Genre: ", games[key][0])
                print("Title: ", games[key][1])
                print("Developer: ", games[key][2])
                print("Publisher: ", games[key][3])
                print("System: ", games[key][4])
                print("Release Date: ", games[key][5])
                print("Rating: ", games[key][6])
                print("Single/Multi/Both: ", games[key][7])
                print("Price: ", games[key][8])
                print("Beat it: ", games[key][9])
                print("Purchase Date: ", games[key][10])
                print("Notes: ", games[key][11])
                print("----------------------")
    def developer():
        found_one = False
        genre = input("Who is the Developer? ")
        for key in games.keys():
            if genre == games[key][2]:
                found_one = True
                print()
                print("Genre: ", games[key][0])
                print("Title: ", games[key][1])
                print("Developer: ", games[key][2])
                print("Publisher: ", games[key][3])
                print("System: ", games[key][4])
                print("Release Date: ", games[key][5])
                print("Rating: ", games[key][6])
                print("Single/Multi/Both: ", games[key][7])
                print("Price: ", games[key][8])
                print("Beat it: ", games[key][9])
                print("Purchase Date: ", games[key][10])
                print("Notes: ", games[key][11])
                print("----------------------")
    def publisher():
        found_one = False
        genre = input("Who is the Publisher? ")
        for key in games.keys():
            if genre == games[key][3]:
                found_one = True
                print()
                print("Genre: ", games[key][0])
                print("Title: ", games[key][1])
                print("Developer: ", games[key][2])
                print("Publisher: ", games[key][3])
                print("System: ", games[key][4])
                print("Release Date: ", games[key][5])
                print("Rating: ", games[key][6])
                print("Single/Multi/Both: ", games[key][7])
                print("Price: ", games[key][8])
                print("Beat it: ", games[key][9])
                print("Purchase Date: ", games[key][10])
                print("Notes: ", games[key][11])
                print("----------------------")
    def system():
        found_one = False
        genre = input("What Type of System? ")
        for key in games.keys():
            if genre == games[key][4]:
                found_one = True
                print()
                print("Genre: ", games[key][0])
                print("Title: ", games[key][1])
                print("Developer: ", games[key][2])
                print("Publisher: ", games[key][3])
                print("System: ", games[key][4])
                print("Release Date: ", games[key][5])
                print("Rating: ", games[key][6])
                print("Single/Multi/Both: ", games[key][7])
                print("Price: ", games[key][8])
                print("Beat it: ", games[key][9])
                print("Purchase Date: ", games[key][10])
                print("Notes: ", games[key][11])
                print("----------------------")
    def release():
        found_one = False
        genre = input("When was it Released? ")
        for key in games.keys():
            if genre == games[key][5]:
                found_one = True
                print()
                print("Genre: ", games[key][0])
                print("Title: ", games[key][1])
                print("Developer: ", games[key][2])
                print("Publisher: ", games[key][3])
                print("System: ", games[key][4])
                print("Release Date: ", games[key][5])
                print("Rating: ", games[key][6])
                print("Single/Multi/Both: ", games[key][7])
                print("Price: ", games[key][8])
                print("Beat it: ", games[key][9])
                print("Purchase Date: ", games[key][10])
                print("Notes: ", games[key][11])
                print("----------------------")
    def rating():
        found_one = False
        genre = input("What is it's rating? ")
        for key in games.keys():
            if genre == games[key][6]:
                found_one = True
                print()
                print("Genre: ", games[key][0])
                print("Title: ", games[key][1])
                print("Developer: ", games[key][2])
                print("Publisher: ", games[key][3])
                print("System: ", games[key][4])
                print("Release Date: ", games[key][5])
                print("Rating: ", games[key][6])
                print("Single/Multi/Both: ", games[key][7])
                print("Price: ", games[key][8])
                print("Beat it: ", games[key][9])
                print("Purchase Date: ", games[key][10])
                print("Notes: ", games[key][11])
                print("----------------------")
    def sin_multi_both():
        found_one = False
        genre = input("Is it Singleplayer, Multiplayer, or Both ")
        for key in games.keys():
            if genre == games[key][7]:
                found_one = True
                print()
                print("Genre: ", games[key][0])
                print("Title: ", games[key][1])
                print("Developer: ", games[key][2])
                print("Publisher: ", games[key][3])
                print("System: ", games[key][4])
                print("Release Date: ", games[key][5])
                print("Rating: ", games[key][6])
                print("Single/Multi/Both: ", games[key][7])
                print("Price: ", games[key][8])
                print("Beat it: ", games[key][9])
                print("Purchase Date: ", games[key][10])
                print("Notes: ", games[key][11])
                print("----------------------")
    def beat_game():
        found_one = False
        genre = input("Have you beat the game? ")
        for key in games.keys():
            if genre == games[key][8]:
                found_one = True
                print()
                print("Genre: ", games[key][0])
                print("Title: ", games[key][1])
                print("Developer: ", games[key][2])
                print("Publisher: ", games[key][3])
                print("System: ", games[key][4])
                print("Release Date: ", games[key][5])
                print("Rating: ", games[key][6])
                print("Single/Multi/Both: ", games[key][7])
                print("Price: ", games[key][8])
                print("Beat it: ", games[key][9])
                print("Purchase Date: ", games[key][10])
                print("Notes: ", games[key][11])
                print("----------------------")
    def price():
        found_one = False
        genre = input("How Much Does it Cost? ")
        for key in games.keys():
            if genre == games[key][9]:
                found_one = True
                print()
                print("Genre: ", games[key][0])
                print("Title: ", games[key][1])
                print("Developer: ", games[key][2])
                print("Publisher: ", games[key][3])
                print("System: ", games[key][4])
                print("Release Date: ", games[key][5])
                print("Rating: ", games[key][6])
                print("Single/Multi/Both: ", games[key][7])
                print("Price: ", games[key][8])
                print("Beat it: ", games[key][9])
                print("Purchase Date: ", games[key][10])
                print("Notes: ", games[key][11])
                print("----------------------")
    def notes():
        found_one = False
        genre = input("Any notes on game? ")
        for key in games.keys():
            if genre == games[key][11]:
                found_one = True
                print()
                print("Genre: ", games[key][0])
                print("Title: ", games[key][1])
                print("Developer: ", games[key][2])
                print("Publisher: ", games[key][3])
                print("System: ", games[key][4])
                print("Release Date: ", games[key][5])
                print("Rating: ", games[key][6])
                print("Single/Multi/Both: ", games[key][7])
                print("Price: ", games[key][8])
                print("Beat it: ", games[key][9])
                print("Purchase Date: ", games[key][10])
                print("Notes: ", games[key][11])
                print("----------------------")
    def purchase_date():
        found_one = False
        genre = input("When was the Game Purchased? ")
        for key in games.keys():
            if genre == games[key][10]:
                found_one = True
                print()
                print("Genre: ", games[key][0])
                print("Title: ", games[key][1])
                print("Developer: ", games[key][2])
                print("Publisher: ", games[key][3])
                print("System: ", games[key][4])
                print("Release Date: ", games[key][5])
                print("Rating: ", games[key][6])
                print("Single/Multi/Both: ", games[key][7])
                print("Price: ", games[key][8])
                print("Beat it: ", games[key][9])
                print("Purchase Date: ", games[key][10])
                print("Notes: ", games[key][11])
                print("----------------------")       
        
    filter_options = True
    
    while filter_options:
        
        print("""
        What would you like to search by?
        ---------------------------------
    
                     OPTIONS
    
        1) genre
        2) Title
        3) Developer
        4) Publisher
        5) System
        6) Release Date
        7) Rating
        8) Singleplayer/Multiplayer/Both
        9) Beat the game
        10) Price
        11) Notes
        12) Purchase Date
    
        Q) Back to Main Menu
    
        """)
        
        option = input("What would you like to do? ")
        
        if option == "1":
            genre()
        elif option == "2":
            title()
        elif option == "3":
            developer()
        elif option == "4":
            publisher()
        elif option == "5":
            system()
        elif option == "6":
            release()
        elif option == "7":
            rating()
        elif option == "8":
            sin_multi_both
        elif option == "9":
            beat_game()
        elif option == "10":
            price() 
        elif option == "11":
            notes() 
        elif option == "12":
            purchase_date()        
        elif option == "Q" or option == "q":
            print("...Going Back...")
            return menu
        else:
            print("*** NOT A VALID CHOICE ***\n")       
def remove_game():
    removegame = input("What is the game you would like to delete? ")
    if removegame not in games:
        print("*** THAT GAME DOES NOT EXIST! ***\n")
    else:
        entry = games.pop(input)
        print(removegame, ":", entry[1]+", removed.")    
def save_data_base():
    save_data = input("Would you like to save, y/n? (hit enter to go back) ")
    if save_data == "y" or quit_question == "Y" or quit_question == "Yes" or quit_question == "yes": 
        print("...Saving...")
        print("")
        games = {}
        pickle_file = open("gamelib.pickle","wb")
        pickle.dump(games, pickle_file)
        pickle_file.close()
        
        pickle_file = open("gamelib.pickle","rb")
        games = pickle.load(pickle_file)        
        print("Done")
        return menu
    elif save_data == "n" or quit_question == "N" or quit_question == "No" or quit_question == "no":
        print("...Not Saved...")
        return menu
    else:
        print("...Going back to main menu...")
        return menu
def quit():
    quit_question = input("Would you like to save before quitting? (hit enter to go back) ")
    if quit_question == "y" or quit_question == "Y" or quit_question == "Yes" or quit_question == "yes": 
        print("...Saving...")
        print("")
        games = {}
        pickle_file = open("gamelib.pickle","wb")
        pickle.dump(games, pickle_file)
        pickle_file.close()
        
        pickle_file = open("gamelib.pickle","rb")
        games = pickle.load(pickle_file)        
        print("Done")
        exit()
    elif quit_question == "n" or quit_question == "N" or quit_question == "No" or quit_question == "no":
        print("...Ending Program...")
        exit()
    else:
        print("...Going back to main menu...")
        return menu
menu = True

while menu:
    print("""
    Welcome to the Game Library
    ---------------------------
    
            MAIN MENU
    
    1) Add/Edit a game
    2) Show All Games
    3) Search a Game by Filter
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
