import turtle
import Menu as menu
import Game as game
import Leaderboard as lb
import Controls as ctrl
import sys
import pygame

# Initialize pygame mixer
pygame.mixer.init()
# Load BG music
pygame.mixer.music.load(r"Sounds\bg_music.mp3")
# Load sound effects
click_sound = pygame.mixer.Sound("Sounds\click.wav")
# Play background music in a loop (-1 means loop indefinitely)
pygame.mixer.music.play(-1)

def start():
    print("Start Game")
    click_sound.play()
    menu.menu_window.clear()
    game.start_game(exit_to_menu)

def show_controls():
    print("Controls")
    click_sound.play()
    menu.menu_window.clear()
    ctrl.display_controls(exit_to_menu)

def show_leaderboard():
    print("Leaderboard")
    click_sound.play()
    menu.menu_window.clear()
    lb.display_leaderboard(exit_to_menu)

def quit_game():
    print("Quit Game")
    click_sound.play()
    sys.exit()
    
def exit_to_menu():
    print("Exit to Menu")
    click_sound.play()
    menu.create_menu(button_functions)

# Added close_menu function to button_functions
button_functions = [start, show_controls, show_leaderboard, quit_game]

menu.create_menu(button_functions)
turtle.done()
