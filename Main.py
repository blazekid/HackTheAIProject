import pygame
import sys
import time
import os
pygame.init()
from random import choice, randrange
import  random

import MatrixAnimations as MatrixAnimations
import Questions as Questions
matrix_animations = MatrixAnimations.MatrixAnimations()
question0 = Questions.QuestionPre()
question1 = Questions.Question1()
question2 = Questions.Question2()
question3 = Questions.Question3()
question4 = Questions.Question4()
question5 = Questions.Question5()
question6 = Questions.Question6()
question7 = Questions.Question7()  # Easter Egg 1
question8 = Questions.Question8()  # Easter Egg 2
commonprompts = Questions.CommonPrompts()

def main_funtion():
    pass

skip_typing = False

class printclass:
    def __init__(self):
        self.width_printed_element = 0
        self.y_coordinate = 0
        self.string_printed = ""
        self.printed = False

    def print2screen(self, text, x_offset, y_offset, inp_color='green'):
        lines = text.split("\n")
        self.render_obj = []
        for index in range(len(lines)):
            self.render_obj.append(font.render(lines[index], True, 'green', 'black'))

        if self.string_printed != text and not skip_typing:
            self.printed = False
            self.string_printed = text
            for index in range(len(lines)+5):
                mask_screen = pygame.Rect((x_offset,y_offset+index*FONT_SIZE), (1500, FONT_SIZE))
                pygame.draw.rect(screen, 'black', mask_screen)

        if not self.printed and not skip_typing:
            i = 0
            for index in range(len(lines)):
                x_offset = 0
                for alphabet in lines[index]:
                    alphabet_render = font.render(alphabet, True, 'green', 'black')
                    screen.blit(alphabet_render, (x_offset, y_offset+index*FONT_SIZE))
                    x_offset += alphabet_render.get_width()
                    pygame.display.update()
                    pygame.time.delay(5)
                    i += 1
            self.printed = True
        else:
            for index in range(len(self.render_obj)):
                screen.blit(self.render_obj[index], (x_offset, y_offset+index*FONT_SIZE))
                self.y_coordinate = y_offset+index*FONT_SIZE
        pygame.display.update()

    def get_y_coordinates(self):
        return self.y_coordinate

printx = printclass()

WIDTH, HEIGHT = 1080, 600
RES = (WIDTH, HEIGHT)
CURSOR = 0

FONT_SIZE = 15
alpha_value = randrange(30,40,5)


font = pygame.font.Font("C:\\Users\\1000256474\\Desktop\\Quiz\\HackTheAIProject\\MSMINCHO.TTF", FONT_SIZE)
font_art = pygame.font.Font("C:\\Users\\1000256474\\Desktop\\Quiz\\HackTheAIProject\\MSMINCHO.TTF", 10)
font_big = pygame.font.Font("C:\\Users\\1000256474\\Desktop\\Quiz\\HackTheAIProject\\MSMINCHO.TTF", 30)


screen = pygame.display.set_mode(RES)
display_surface = pygame.Surface(RES)
pygame.display.set_caption('Hack The AI')
display_surface.set_alpha(255)

clock = pygame.time.Clock()
input = ""
clue_printed = False

def print_clue_func():
    text_surface1 = font.render("Next clue can be found at: " + "C://HackTheAI//" + "clue.txt" , True, 'green')
    text_surface2 = font.render("Input OK to Continue playing for an Easter Egg", True, 'green')
    youtube_link = "https://www.youtube.com/watch?v=6Mawk3qenhI"
    if not os.path.exists('c:\\HackTheAI'):
        os.makedirs('c:\\HackTheAI')

    if clue_printed == False:
        fReport = open('c:\\HackTheAI\\' + 'clue.txt', 'w')
        fReport.write("Open the link for the clue : " + youtube_link)
        fReport.flush()
        fReport.close()
        update_clue_variable()
    # render at position stated in arguments
    screen.blit(text_surface1, (WIDTH/3, HEIGHT/2))
    screen.blit(text_surface2, (WIDTH /3, HEIGHT / 2 + FONT_SIZE))

def update_clue_variable():
    clue_printed = True

def user_input_box():
    y_coordinate = printx.get_y_coordinates()
    input_prefix = font.render("KatieWeirs@Desktop:~$ ", False, 'green', 'black')
    screen.blit(input_prefix, (0, y_coordinate + FONT_SIZE - CURSOR))

    x_coordinate = input_prefix.get_width()
    input_rect = pygame.Rect(x_coordinate, (y_coordinate+FONT_SIZE-CURSOR), 1000, FONT_SIZE)
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


ai_ascii_art = open("C:\\Users\\1000256474\\Desktop\\Quiz\\HackTheAIProject\\AI.txt", "r")
line_offset = []
id = 0
for line in ai_ascii_art:
    line_offset.append(line)
    id += 1
ai_ascii_art.seek(0)

run = True
user_text = ''
game_won = False
game_end = False  # TODO: make it false

last_point = False
time_start = 0
question = 0
received_enter = False
print_clue = False
give_easter_egg = False

waiting_for_only_enter = False
received_only_enter = False
wrong_answer_output_string = ""
write_answer_right_string = ""
hint_string = ""
katie_print_first_time = True
wrong_answers_list = []
hint_threshold = 5
wrong_answer = False

def get_question_object():
    if question == 1:
        return  question1
    elif question == 2:
        return  question2
    elif question == 3:
        return  question3
    elif question == 4:
        return  question4
    elif question == 5:
        return  question5
    elif question == 6:
        return  question6
    elif question == 7:
        return  question7
    elif question == 8:
        return  question8

katie_map = []
for index in range(len(line_offset)):
    x_offset = 0
    y_offset = index * 10
    for char_obj in line_offset[index]:
        render_char = font_art.render(char_obj, True, 'green', 'black')
        katie_map.append([render_char, (x_offset,y_offset)])
        x_offset += render_char.get_width()

random.shuffle(katie_map)

# while loop for game heartbeat
while run:
    screen.blit(display_surface, (0, 0))
    display_surface.fill(pygame.Color('black'))
    if not game_won and not game_end and not print_clue:
        # While loop to print the ascii art
        if katie_print_first_time:
            for i in range(len(katie_map)):
                screen.blit(katie_map[i][0], katie_map[i][1])
                pygame.time.delay(0) # TODO: Update to 2
                pygame.display.update()
            line = len(line_offset)+1
            katie_print_first_time = False
        else:
            line = 0
            while True:
                x = line_offset[line]
                screen.blit(font_art.render(x, True, 'green', 'black'), (0, (line-CURSOR)*10))
                line += 1
                if line == len(line_offset):
                    break
            line += 1

        if question == 0:
            if not waiting_for_only_enter:
                printx.print2screen(question0.question, 0, (line - CURSOR) * 10, FONT_SIZE)
            user_input_box()
            if input == question0.answer[0]:
                printx.print2screen(question0.prompts[0] + commonprompts.cont_text[0], 0, (line - CURSOR) * 10, FONT_SIZE)
                waiting_for_only_enter = True
                pygame.time.delay(200)
            elif input == question0.answer[1]:
                printx.print2screen(question0.prompts[1] + commonprompts.cont_text[0], 0, (line - CURSOR) * 10, FONT_SIZE)
                waiting_for_only_enter = True
                pygame.time.delay(200)

            if waiting_for_only_enter and received_only_enter:
                question = 1
                input = ""
                received_only_enter = False
                waiting_for_only_enter = False

        if question != 0:
            question_obj = get_question_object()
            if not waiting_for_only_enter:
                printx.print2screen(question_obj.question, 0, (line - CURSOR) * 10, FONT_SIZE)
                user_input_box()

            if question == 5:
                inputs = input.split(" ")
                if len(inputs) == 2:
                    if inputs[0] in question_obj.answer and inputs[1] in question_obj.answer:
                        wrong_answer = False
                    else:
                        wrong_answer = True
                else:
                    wrong_answer = True
            else:
                if input != "" and input in question_obj.answer:
                    wrong_answer = False
                else:
                    wrong_answer = True

            if not wrong_answer and received_enter:
                if not write_answer_right_string:
                    write_answer_right_string = random.choice(commonprompts.right_answer) + commonprompts.cont_text[1]
                    if question == 7:
                        write_answer_right_string = "Here is your egg, Easter Elephant" + commonprompts.cont_text[1]
                for index in range(10):
                    mask_screen = pygame.Rect((0, (line + index) * FONT_SIZE), (1500, FONT_SIZE))
                    pygame.draw.rect(screen, 'black', mask_screen)
                printx.print2screen(write_answer_right_string, 0, (line - CURSOR) * 10, FONT_SIZE)
                waiting_for_only_enter = True
                pygame.time.delay(200)
            elif input != "" and received_enter:
                if not wrong_answer_output_string:
                    skip_typing = False
                    if len(wrong_answers_list) == hint_threshold:
                        wrong_answer_output_string = random.choice(commonprompts.hint_precursor) + random.choice(question_obj.hint) + \
                                                commonprompts.cont_text[1]
                        wrong_answers_list = []
                    elif (len(wrong_answers_list)+1) % 3 == 0:
                        wrong_answer_output_string = random.choice(commonprompts.wrong_answer) + random.choice(question_obj.prompts) + \
                                                commonprompts.cont_text[2]
                        wrong_answers_list.append(input)
                    else:
                        wrong_answer_output_string = random.choice(commonprompts.wrong_answer) + random.choice(commonprompts.basic_prompts) + commonprompts.cont_text[1]
                        wrong_answers_list.append(input)
                printx.print2screen(wrong_answer_output_string, 0, printx.get_y_coordinates() + FONT_SIZE, FONT_SIZE)
                pygame.time.delay(200)
                skip_typing = True

            if waiting_for_only_enter and received_only_enter:
                question += 1
                wrong_answers_list = []
                received_only_enter = False
                waiting_for_only_enter = False
                input = ""
                skip_typing = False
                if question == 7:
                    game_won = True
                    time_start = time.time()
                if question == 8:
                    game_end = True

    if game_won:
        matrix_animations.start_animations(display_surface, screen)
        current_time = time.time()
        if current_time-time_start > 10:
            last_point = True
            game_won = False
            display_surface.fill(pygame.Color('green'))
            katie_print_first_time = True
            pygame.time.delay(200)
            display_surface.set_alpha(255)
            print_clue = True

    if print_clue:
        print_clue_func()
        user_input_box()
        if input == "ok":
            print_clue = False
            input = ""
            give_easter_egg = True
            for index in range(10):
                y_offset = printx.get_y_coordinates()
                mask_screen = pygame.Rect((0, y_offset+index*FONT_SIZE), (1500, FONT_SIZE))
                pygame.draw.rect(screen, 'black', mask_screen)

    if game_end:
        lines = question8.question.split('\n')
        text_surface1 = font.render(lines[0], True, 'green')
        text_surface2 = font.render(lines[1], True, 'green')
        text_surface3 = font.render(lines[2], True, 'green')
        text_surface4 = font.render(lines[3], True, 'green')
        text_surface5 = font_big.render(lines[4], True, 'green')

        # render at position stated in arguments
        screen.blit(text_surface1, (WIDTH / 5, HEIGHT / 2.5))
        screen.blit(text_surface2, (WIDTH / 5, HEIGHT / 2.5 + FONT_SIZE))
        screen.blit(text_surface3, (WIDTH / 5, HEIGHT / 2.5 + FONT_SIZE*2))
        screen.blit(text_surface4, (WIDTH / 5, HEIGHT / 2.5 + FONT_SIZE*3))
        screen.blit(text_surface5, (-44, HEIGHT / 2.5 + FONT_SIZE * 4))

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
            received_enter = False
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:

                # get text input from 0 to -1 i.e. end.
                if len(user_text) > 0:
                    user_text = user_text[:-1]

            elif event.key == pygame.K_RETURN:
                received_enter = True
                input = str(user_text.lower())
                wrong_answer_output_string = ""
                write_answer_right_string = ""
                hint_string = ""
                if user_text == "hello":
                    game_won = True
                    time_start = time.time()

                if user_text == "":
                    received_only_enter = True

                user_text = ""
                CURSOR += 0# Change to one to create next line effect

            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode

if __name__ == "__main__":
    main_function()
