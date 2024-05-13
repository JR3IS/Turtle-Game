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
pygame.mixer.music.load(r"Sounds\bg_music.wav")
pygame.mixer.music.set_volume(0.5) # Adjust Volume
# Play background music in a loop (-1 means loop indefinitely)
pygame.mixer.music.play(-1)
# Load sound effects
click_sound = pygame.mixer.Sound("Sounds\click.wav")
open_page_sound = pygame.mixer.Sound("Sounds\open_page.ogg")
open_page_sound.set_volume(0.5) # Adjust Volume
start_game = pygame.mixer.Sound("Sounds\start_game.ogg")
quit_game_sound = pygame.mixer.Sound("Sounds\quit_game.ogg")

# Menu Button Functions
def start():
    print("Start Game")
    start_game.play()
    menu.menu_window.clear()
    game.start_game(exit_to_menu)

def show_controls():
    print("Controls")
    open_page_sound.play()
    menu.menu_window.clear()
    ctrl.display_controls(exit_to_menu)

def show_leaderboard():
    print("Leaderboard")
    open_page_sound.play()
    menu.menu_window.clear()
    lb.display_leaderboard(exit_to_menu)

def quit_game():
    print("Quit Game")
    quit_game_sound.play()
    pygame.time.wait(550) # Creates a small delay so the sound can be heard
    sys.exit()

# Callback Exit to Menu Function    
def exit_to_menu():
    print("Exit to Menu")
    click_sound.play()
    menu.create_menu(button_functions)

# Added close_menu function to button_functions
button_functions = [start, show_controls, show_leaderboard, quit_game]

menu.create_menu(button_functions)
turtle.done()
