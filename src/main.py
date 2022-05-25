import time
import pygame
import sys

# TODO face recognition
# TODO communication with publisher
# TODO let ball bounce more random
# import zmq
#
# ctx = zmq.Context()
#
# #  Socket to talk to server
# print("Connecting to server…")
# sub = ctx.socket(zmq.SUB)
# sub.connect("tcp://127.0.0.1:5555")
# sub.setsockopt(zmq.CONFLATE, True)
# sub.setsockopt(zmq.SUBSCRIBE, b'')

#  Do 10 requests, waiting each time for a response
# for _ in range(10):
#     print("hi")
#     message: dict = sub.recv_json()
#     print(message)
# sub.close()


def ball_animation(rect):
    if rect.left < 0 or rect.right > screen_width:
        ball_speed[0] = -ball_speed[0]

    if rect.top < 0 or rect.bottom > screen_height:
        ball_speed[1] = -ball_speed[1]

    if rect.colliderect(skateboard_rectangle):
        ball_speed[1] = -ball_speed[1]


def draw_game():
    screen.blit(background_picture, (0, 0))
    screen.blit(ball_picture, ball_rectangle)
    screen.blit(skateboard_picture, skateboard_rectangle)
    pygame.display.update()


pygame.init()
pygame.font.init()

screen_height = 595
screen_width = 1200

screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()
background_picture = pygame.image.load("resource/backgroundPic.png")
ball_picture = pygame.image.load("resource/ball.png")
skateboard_picture = pygame.image.load("resource/skateboard.png")
pygame.display.set_caption("Face Recognition Demo Game")

# figure
skateboard_x = 100
skateboard_y = 490
skateboard_speed = 7

# skateboard
skateboard_rectangle = skateboard_picture.get_rect()
print(skateboard_rectangle)
skateboard_rectangle.x = skateboard_x
skateboard_rectangle.y = skateboard_y

# ball
ball_speed = [5, 5]
ball_rectangle = ball_picture.get_rect()

# left and right wall
left_wall = pygame.Rect(-2, 0, 2, 600)
right_wall = pygame.Rect(1200, 0, 2, 600)

# game over
game_over_font = pygame.font.SysFont("monospace", 50)
game_over_text = game_over_font.render("game over", 1, (0, 0, 0))
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (screen_width // 2, screen_height // 2)

go = True

while go:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    ball_rectangle = ball_rectangle.move(ball_speed)

    pressed = pygame.key.get_pressed()  # remove with data from face recognition

    if ball_rectangle.bottom > skateboard_y + 80:
        ball_rectangle.move(0, 0)
        screen.blit(background_picture, (0, 0))
        screen.blit(ball_picture, ball_rectangle)
        screen.blit(skateboard_picture, skateboard_rectangle)
        screen.blit(game_over_text, game_over_rectangle)
        pygame.display.update()
        time.sleep(1.5)
        sys.exit()
    else:
        ball_animation(ball_rectangle)

    if pressed[pygame.K_RIGHT] and not skateboard_rectangle.colliderect(right_wall):
        skateboard_rectangle.x += skateboard_speed
    if pressed[pygame.K_LEFT] and not skateboard_rectangle.colliderect(left_wall):
        skateboard_rectangle.x -= skateboard_speed

    draw_game()

    clock.tick(60)
