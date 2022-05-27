import time
import pygame
import sys
import os
from settings_text import SettingsText
from game import Game

pygame.init()
pygame.font.init()

screen_height = 595
screen_width = 1200


screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()
background_picture = pygame.image.load("./resource/backgroundPic.png")
ball_picture = pygame.image.load("./resource/ball.png")
skateboard_picture = pygame.image.load("./resource/skateboard.png")
pygame.display.set_caption("pong game")

# fonts
heading_font = pygame.font.SysFont("monospace", 30)
text_font =  pygame.font.SysFont("monospace", 20)
game_over_font = pygame.font.SysFont("monospace", 50)

# menu
start_text = heading_font.render("How do you want to control the skateboard?", 1, (0, 0, 0))
start_text_rectangle = start_text.get_rect()
start_text_rectangle.center = (screen_width // 2, 150)
play_with_keys = SettingsText((000, 255, 127), screen_width, 200, screen, " Press \'k\' for keyboard ", text_font)
play_with_face = SettingsText((000, 255, 127), screen_width, 250, screen, " Press \'f\' for face ", text_font)
exit_game = SettingsText((255, 246, 143), screen_width, 350, screen, " Press \'e\' for exit ", text_font)

# game over
game_over_text = game_over_font.render("game over", 1, (0, 0, 0))
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (screen_width // 2, screen_height // 2)

# game
game = Game(screen, screen_width, screen_height, ball_picture, skateboard_picture, 7, [6, 6], pygame.Rect(-2, 0, 2, 600), pygame.Rect(1200, 0, 2, 600), background_picture, pygame.time.Clock())
skateboard_x = 100
skateboard_y = 490
skateboard_rectangle = game.create_skateboard(skateboard_x, skateboard_y)
ball_rectangle = game.create_ball()

settings = True

def show_menu():
    screen.blit(background_picture, (0, 0))
    screen.blit(start_text, start_text_rectangle)
    play_with_keys.draw(screen)
    play_with_face.draw(screen)
    exit_game.draw(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_k]:
            game.play_with_keyboard(ball_rectangle, skateboard_rectangle, game_over_text, game_over_rectangle)

        if pressed[pygame.K_f]:
            print("with face")
        if pressed[pygame.K_e]:
            time.sleep(0.5)
            sys.exit()
        if settings:
            show_menu()

        pygame.display.update()
        clock.tick(60)
