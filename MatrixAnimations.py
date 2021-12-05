import pygame
import sys
import time
from random import choice, randrange

WIDTH, HEIGHT = 1080, 600
RES = (WIDTH, HEIGHT)
alpha_value = randrange(30, 40, 5)
FONT_SIZE = 15

class MatrixAnimations:
    def __init__(self):
        font = pygame.font.Font("C:\\Users\\1000256474\\Desktop\\Quiz\\HackTheAIProject\\MSMINCHO.TTF", FONT_SIZE)
        font_art = pygame.font.Font("C:\\Users\\1000256474\\Desktop\\Quiz\\HackTheAIProject\\MSMINCHO.TTF", 10)
        font_1 = pygame.font.Font("C:\\Users\\1000256474\\Desktop\\Quiz\\HackTheAIProject\\MSMINCHO.TTF",
                                  FONT_SIZE - FONT_SIZE // 6)
        font_2 = pygame.font.Font("C:\\Users\\1000256474\\Desktop\\Quiz\\HackTheAIProject\\MSMINCHO.TTF",
                                  FONT_SIZE - FONT_SIZE // 3)

        chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', "^", "&", "*", "(", ")", "|"]
        self.green_chars = [font.render(char, True, (randrange(0, 100), 255, randrange(0, 100))) for char in chars]
        self.green_chars_2 = [font_1.render(char, True, (40, randrange(100, 175), 40)) for char in chars]
        self.green_chars_3 = [font_2.render(char, True, (40, randrange(50, 100), 40)) for char in chars]

        self.symbols = [Symbol(x, randrange(-HEIGHT, 0), self.green_chars) for x in range(0, WIDTH, FONT_SIZE)]
        self.symbols_2 = [Symbol(x, randrange(-HEIGHT, 0), self.green_chars_2) for x in range(FONT_SIZE, WIDTH, FONT_SIZE * 3)]
        self.symbols_3 = [Symbol(x, randrange(-HEIGHT, 0), self.green_chars_3) for x in range(FONT_SIZE * 2, WIDTH, FONT_SIZE * 3)]

    def start_animations(self, display_surface, screen):
        if display_surface.get_alpha() != alpha_value:
            display_surface.set_alpha(alpha_value)
        [symbol.draw(screen, self.green_chars) for symbol in self.symbols]
        [symbol.draw(screen, self.green_chars_2) for symbol in self.symbols_2]
        [symbol.draw(screen, self.green_chars_3) for symbol in self.symbols_3]
        pygame.time.delay(150)

class Symbol:
    def __init__(self, x, y, green_chars):
        self.x = x
        self.y = y
        self.speed = 40

    def draw(self, screen, green_chars):
        self.value = choice(green_chars)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1, 10)
        screen.blit(self.value, (self.x, self.y))










