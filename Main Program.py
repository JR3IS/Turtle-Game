import turtle
import random
import time
import Menu as menu
import Test_Copy as game



def start():
    print("Start Game")
    menu.menu_window.clear()
    game.start_game()

def show_controls():
    print("Controls")

def show_high_score():
    print("High Score")

def quit_game():
    print("Quit Game")

# Added close_menu function to button_functions
button_functions = [start, show_controls, show_high_score, quit_game]

menu.create_menu(button_functions)
turtle.done()
