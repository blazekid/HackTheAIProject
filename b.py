import pygame
import sys
import time
from random import choice, randrange
pygame.init()

class Question0:
    question = "Would you like to play a game for the next clue?"
    answer = ["yes", "no"]
    prompts = ["Let's start!!!", "You seriously think this will work?"]

class Question1:
    question = "Thirty white horses on a red hill: first they champ,\n then they stamp, then they stand still. What am I?"
    answer = ["tooth", "teeth"]
    prompts = ["Almost There", "Not that Far", "Try better"]

class Question2:
    question = "What's round, but not always around?\n "\
               "It's light sometimes; it's dark sometimes," \
               "\nEveryone wants to walk all over me.\nWhat am I?"
    answer = ["moon"]
    prompts = ["Almost There", "Not that Far", "Try better"]

class Question3:
    question = "Tear one off and scratch my head\n What once was red is black instead"
    answer = ["match"]
    prompts = ["Almost There", "Not that Far", "Try better"]

class Question4:
    question = "As I was going to St. Ives,\n I met a man with seven wives,\n Every wife had seven sacks,\n Every sack had seven cats,"\
                "Every cat has seven kits.\n Kits, cats, sacks, and wives,\n How many were going to St. Ives?"
    answer = ["one","1"]
    prompts = ["Almost There", "Not that Far", "Try better"]


class printclass:
    def __init__(self):
        self.width_printed_element = 0
        self.string_printed = ""
        self.printed = False
        pass

    def print2screen(self, text, x_offset, y_offset, inp_color='green'):
        # input_rect = pygame.Rect(0, (line - CURSOR) * 10, 1000, FONT_SIZE)
        self.render_obj = font.render(text, True, 'green', 'black')
        self.width_printed_element= self.render_obj.get_width()

        if self.string_printed !=text:
            self.printed = False
            self.string_printed = text
            mask_screen = pygame.Rect((x_offset,y_offset), (1000, FONT_SIZE))
            pygame.draw.rect(screen, 'black', mask_screen)
        if not self.printed:
            i = 0
            for alphabet in text:
                alphabet_render = font.render(alphabet, True, 'green', 'black')
                screen.blit(alphabet_render, (x_offset, y_offset))
                x_offset += alphabet_render.get_width()
                pygame.display.update()
                pygame.time.delay(100)
                self.printed = True
                i += 1
        else:
            screen.blit(self.render_obj, (x_offset, y_offset))
            pygame.display.update()

    def get_width(self):
        return self.width_printed_element

printx = printclass()


WIDTH, HEIGHT = 1080, 600
RES = (WIDTH, HEIGHT)
CURSOR = 0

FONT_SIZE = 15
alpha_value = randrange(30,40,5)

chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', "^", "&", "*", "(", ")", "|"]

font = pygame.font.Font("C:\\Users\\1000256474\\Desktop\\Quiz\\Hunt\\MSMINCHO.TTF", FONT_SIZE)
font_art = pygame.font.Font("C:\\Users\\1000256474\\Desktop\\Quiz\\Hunt\\MSMINCHO.TTF", 10)
font_1 = pygame.font.Font("C:\\Users\\1000256474\\Desktop\\Quiz\\Hunt\\MSMINCHO.TTF", FONT_SIZE - FONT_SIZE//6)
font_2 = pygame.font.Font("C:\\Users\\1000256474\\Desktop\\Quiz\\Hunt\\MSMINCHO.TTF", FONT_SIZE - FONT_SIZE//3)

green_chars = [font.render(char, True, (randrange(0,100), 255, randrange(0,100))) for char in chars]
green_chars_2 = [font_1.render(char, True, (40, randrange(100,175), 40)) for char in chars]
green_chars_3 = [font_2.render(char, True, (40, randrange(50,100), 40)) for char in chars]


screen = pygame.display.set_mode(RES)
display_surface = pygame.Surface(RES)
pygame.display.set_caption('Hack The AI')
display_surface.set_alpha(255)

clock = pygame.time.Clock()
input = ""

def matrix_animations():
    if last_point:
        return
    if display_surface.get_alpha() != alpha_value:
        display_surface.set_alpha(alpha_value)
    [symbol.draw() for symbol in symbols]
    [symbol.draw_2() for symbol in symbols_2]
    [symbol.draw_3() for symbol in symbols_3]
    pygame.time.delay(200)

def print_clue_and_exit():
    text_surface = font.render("Next Clue: Link!!!", True, 'green')
    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x + 1, input_rect.y + 1-CURSOR))
    text_surface = font.render("Press Enter To Exit!!!", True, 'green')
    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x + 2, input_rect.y + 1-CURSOR))

def user_input_box():
    input_rect = pygame.Rect(printx.get_width()+5, (line-CURSOR)*10, 1000, FONT_SIZE)

    text_surface = font.render(user_text, True, 'green')
    rect = text_surface.get_rect()
    rect.topleft = (input_rect.x, input_rect.y)
    cursor = pygame.Rect(rect.topright, (5, rect.height))
    rect.size = text_surface.get_size()
    cursor.topleft = rect.topright
    if time.time() % 1 > 0.5:
        pygame.draw.rect(screen, 'green', cursor)

    # render at position stated in arguments
    screen.blit(text_surface, (input_rect.x, input_rect.y))

    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width() + 10)

class Symbol:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 40
        self.value = choice(green_chars)

    def draw(self):
        self.value = choice(green_chars)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1,10)
        screen.blit(self.value, (self.x, self.y))

    def draw_2(self):
        self.value_2 = choice(green_chars_2)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1,10)
        screen.blit(self.value_2, (self.x, self.y))

    def draw_3(self):
        self.value_3 = choice(green_chars_3)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1,10)
        screen.blit(self.value_3, (self.x, self.y))

symbols = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE)]
symbols_2 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE, WIDTH, FONT_SIZE*3)]
symbols_3 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE*2, WIDTH, FONT_SIZE*3)]

ai_ascii_art = open("C:\\Users\\1000256474\\Desktop\\Quiz\\Hunt\\AI.txt", "r")
line_offset = []
id = 0
for line in ai_ascii_art:
    line_offset.append(line)
    id += 1
ai_ascii_art.seek(0)

run = True
user_text = ''
game_won = False
last_point = False
time_start = 0
question = 0


# while loop for game heartbeat
while run:
    screen.blit(display_surface, (0, 0))
    display_surface.fill(pygame.Color('black'))
    if not game_won:
        # While loop to print the ascii art
        line = 0
        while True:
            x = line_offset[line]
            screen.blit(font_art.render(x, True, 'green', 'black'), (0, (line-CURSOR)*10))
            line += 1
            if line == len(line_offset):
                break

        if question == 0:
            solved = False
            q0 = Question0()
            printx.print2screen(q0.question, 0, (line - CURSOR) * 10, FONT_SIZE)
            user_input_box()
            if input in q0.answer:
                printx.print2screen("godd job guys!!!", 0, (line - CURSOR) * 10, FONT_SIZE)
                pygame.time.delay(200)
                question =1

        if question == 1:
            solved = False
            q1 = Question1()
            printx.print2screen(q1.question, 0, (line - CURSOR) * 10, FONT_SIZE)
            user_input_box()
            if input in q1.answer:
                printx.print2screen("godd job guys!!!", 0, (line - CURSOR) * 10, FONT_SIZE)
                pygame.time.delay(200)
                question = 2

        if question == 2:
            solved = False
            q2 = Question2()
            printx.print2screen(q2.question, 0, (line - CURSOR) * 10, FONT_SIZE)
            user_input_box()
            if input in q2.answer:
                printx.print2screen("godd job guys!!!", 0, (line - CURSOR) * 10, FONT_SIZE)
                question = 3

        if question == 3:
            solved = False
            q3 = Question3()
            printx.print2screen(q3.question, 0, (line - CURSOR) * 10, FONT_SIZE)
            user_input_box()
            if input in q3.answer:
                printx.print2screen("godd job guys!!!", 0, (line - CURSOR) * 10, FONT_SIZE)
                question = 4

        if question == 4:
            solved = False
            q4 = Question4()
            printx.print2screen(q4.question, 0, (line - CURSOR) * 10, FONT_SIZE)
            user_input_box()
            if input in q4.answer:
                printx.print2screen("godd job guys!!!", 0, (line - CURSOR) * 10, FONT_SIZE)
                game_won = True
                time_start = time.time()

    if game_won:
        matrix_animations()
        current_time = time.time()
        if current_time-time_start > 30:
            last_point = True
            print_clue_and_exit()

    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.update()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pass

        if event.type == pygame.KEYDOWN:

            # Check for backspace
            if event.key == pygame.K_BACKSPACE:

                # get text input from 0 to -1 i.e. end.
                if len(user_text) > 0:
                    user_text = user_text[:-1]

            elif event.key == pygame.K_RETURN:
                input = user_text
                if user_text == "hello":
                    game_won = True
                    time_start = time.time()
                user_text = ""
                CURSOR += 1

            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode



