import pygame

class SettingsText:
    def __init__(self, color, screen_width, screen_height, screen, text, font):
        self.color = color
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = screen
        self.text = text
        self.font = font

    def draw(self, screen):
        text = self.font.render(self.text, 1, (0, 0, 0))
        text_rectangle = text.get_rect()
        text_rectangle.center = (self.screen_width // 2, self.screen_height)
        pygame.draw.rect(screen, self.color, text_rectangle, 0, 5)
        pygame.draw.rect(screen, (0, 0, 0), text_rectangle, 2, 5)
        self.screen.blit(text, text_rectangle)