import pygame
from settings import Settings
from figure import Figure


class Game:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.resolution)
        self.__figure = Figure(self)
        self.__isRunning = False

    def start(self):
        self.__isRunning = True
        while self.__isRunning:
            self.check_events()
            self.__figure.update()
            self.update_screen()
        pygame.quit()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        # pygame.draw.circle(self.screen, self.settings.figure_color, (100, 100), 75)
        self.__figure.blit()
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__isRunning = False
            elif event.type == pygame.KEYDOWN:
                self.check_key_down_events(event)
            elif event.type == pygame.KEYUP:
                self.check_key_up_events(event)

    def check_key_down_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.__figure.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.__figure.moving_left = True
        elif event.key == pygame.K_UP:
            self.__figure.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.__figure.moving_down = True

    def check_key_up_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.__figure.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.__figure.moving_left = False
        elif event.key == pygame.K_UP:
            self.__figure.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.__figure.moving_down = False
