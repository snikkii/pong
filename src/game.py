import time
import pygame
import sys

class Game:
    def __init__(self, screen, screen_width, screen_height, ball_image, skateboard_image, skateboard_speed, ball_speed, left_wall, right_wall, background_image, clock):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.ball_image = ball_image
        self.skateboard_image = skateboard_image
        self.skateboard_speed = skateboard_speed
        self.ball_speed = ball_speed
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.background_image = background_image
        self.clock = clock

    def create_skateboard(self, skateboard_x, skateboard_y):
        skateboard_rectangle = self.skateboard_image.get_rect()
        skateboard_rectangle.x = skateboard_x
        skateboard_rectangle.y = skateboard_y
        return skateboard_rectangle

    def create_ball(self):
        return self.ball_image.get_rect()

    def play_with_keyboard(self, ball_rectangle, skateboard_rectangle, game_over_text, game_over_rectangle):
        run_game = True
        while run_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pressed = pygame.key.get_pressed()

            if ball_rectangle.bottom > skateboard_rectangle.y + 80:
                ball_rectangle.move(0, 0)
                self.screen.blit(self.background_image, (0, 0))
                self.screen.blit(self.ball_image, ball_rectangle)
                self.screen.blit(self.skateboard_image, skateboard_rectangle)
                self.screen.blit(game_over_text, game_over_rectangle)
                pygame.display.update()
                time.sleep(1.5)
                run_game = False
                pygame.display.update()
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                ball_rectangle = ball_rectangle.move(self.ball_speed)

                if ball_rectangle.left < 0 or ball_rectangle.right > self.screen_width:
                    self.ball_speed[0] = -self.ball_speed[0]
                if ball_rectangle.top < 0 or ball_rectangle.bottom > self.screen_width:
                    self.ball_speed[1] = -self.ball_speed[1]

                if ball_rectangle.colliderect(skateboard_rectangle):
                    self.ball_speed[1] = -self.ball_speed[1]

                if pressed[pygame.K_RIGHT] and not skateboard_rectangle.colliderect(self.right_wall):
                    skateboard_rectangle.x += self.skateboard_speed
                if pressed[pygame.K_LEFT] and not skateboard_rectangle.colliderect(self.left_wall):
                    skateboard_rectangle.x -= self.skateboard_speed



                self.screen.blit(self.background_image, (0, 0))
                self.screen.blit(self.ball_image, ball_rectangle)
                self.screen.blit(self.skateboard_image, skateboard_rectangle)
                pygame.display.update()
                self.clock.tick(70)

    def play_with_face(self):
        pass