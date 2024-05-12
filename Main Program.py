import turtle
import Menu as menu
import Game as game
import Leaderboard as lb
import Controls as ctrl
import sys

def start():
    print("Start Game")
    menu.menu_window.clear()
    game.start_game(exit_to_menu)

def show_controls():
    print("Controls")
    menu.menu_window.clear()
    ctrl.display_controls(exit_to_menu)

def show_leaderboard():
    print("Leaderboard")
    menu.menu_window.clear()
    lb.display_leaderboard(exit_to_menu)

def quit_game():
    print("Quit Game")
    sys.exit()
    
def exit_to_menu():
    print("Exit to Menu")
    menu.create_menu(button_functions)

# Added close_menu function to button_functions
button_functions = [start, show_controls, show_leaderboard, quit_game]

menu.create_menu(button_functions)
turtle.done()
