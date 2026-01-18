import pygame

class Figure:

    def __init__(self, game):
        self.settings = game.settings
        self.v = self.settings.character_speed
        self.screen = game.screen
        self.image = pygame.image.load("images/figure.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen.get_rect().midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right:
            self.x += self.v
        if self.moving_left:
            self.x -= self.v
        if self.moving_down:
            self.y += self.v
        if self.moving_up:
            self.y -= self.v

        self.rect.x = self.x
        self.rect.y = self.y

    def blit(self):
        self.screen.blit(self.image, self.rect)
