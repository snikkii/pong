import random
import threading
import time
import pygame
import sys
import zmq
import cv2


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
        ball_rectangle = self.ball_image.get_rect()
        ball_rectangle.x = random.randint(0, 1000)
        return ball_rectangle

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

    def play_with_face(self, ball_rectangle, skateboard_rectangle, game_over_text, game_over_rectangle):
        video_capture = cv2.VideoCapture(0)
        width = video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)
        face_locations = []
        process_this_frame = True
        run_game = True
        while run_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    video_capture.release()
                    cv2.destroyAllWindows()
                    sys.exit()

            ret, frame = video_capture.read()
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            if process_this_frame:
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            i = 0
            for (top, right, bottom, left) in face_locations:
                i += 1
                if i == 1:
                    right *= 4
                    left *= 4
                relPosX = (right + left) * 0.5 / width

            if ball_rectangle.bottom > skateboard_rectangle.y + 80:
                ball_rectangle.move(0, 0)
                self.screen.blit(self.background_image, (0, 0))
                self.screen.blit(self.ball_image, ball_rectangle)
                self.screen.blit(self.skateboard_image, skateboard_rectangle)
                self.screen.blit(game_over_text, game_over_rectangle)
                pygame.display.update()
                time.sleep(1.5)
                video_capture.release()
                cv2.destroyAllWindows()
                run_game = False
                pygame.display.update()
            else:
                ball_rectangle = ball_rectangle.move(self.ball_speed)

                if ball_rectangle.left < 0 or ball_rectangle.right > self.screen_width:
                    self.ball_speed[0] = -self.ball_speed[0]
                if ball_rectangle.top < 0 or ball_rectangle.bottom > self.screen_width:
                    self.ball_speed[1] = -self.ball_speed[1]

                if ball_rectangle.colliderect(skateboard_rectangle):
                    self.ball_speed[1] = -self.ball_speed[1]

                if relPosX < 0.5 and not skateboard_rectangle.colliderect(self.right_wall):
                    skateboard_rectangle.x += self.skateboard_speed
                if relPosX > 0.5 and not skateboard_rectangle.colliderect(self.left_wall):
                    skateboard_rectangle.x -= self.skateboard_speed

                self.screen.blit(self.background_image, (0, 0))
                self.screen.blit(self.ball_image, ball_rectangle)
                self.screen.blit(self.skateboard_image, skateboard_rectangle)
                pygame.display.update()
                self.clock.tick(60)

