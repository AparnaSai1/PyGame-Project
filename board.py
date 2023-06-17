# imports necessary modules and classes.
import sys
from board import Board
from cell import *
import pygame

#initalizes pygame
pygame.init()
#creates another page, this solves an error we were having with overlaying pages
pygame.display.set_caption("Home Page")
#defines screen and color variables.
screen = pygame.display.set_mode((width, height))
black = (18, 18, 18)
white = (255,255,255)
#screen.blit is not done because we dont want home page to print here but just create another page to shift to.

# global difficulty
difficulty = [0]
var = [0]

#the method draw_game_start creates the Sudoku home screen that includes the difficulty level buttons.
def draw_game_start(screen, board):
    # uses pygame function to upload an image as the home screen background instead of a color
    sudokuimage = pygame.image.load("sudokuimage.jpg")
    # uses pygame function to rescale image to fit home screen dimensions.
    sudokuimage = pygame.transform.scale(sudokuimage, (3000, 3000))
    screen.blit(sudokuimage, (0, 0))
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)
    # Prints Sudoku Title & Game Mode
    title_surface = start_title_font.render("Welcome to Sudoku",0,black)
    title_rectangle = title_surface.get_rect(center = (width//2,height//2-250))
    middle_surface = start_title_font.render("Select Game Mode:",0,black)
    middle_rectangle = middle_surface.get_rect(center=(width//2,height//2-50))
    screen.blit(middle_surface,middle_rectangle)
    screen.blit(title_surface,title_rectangle)

    # EASY, MEDIUM, & HARD BUTTON

    # text
    easy_text = button_font.render("Easy",0,(255,255,255))
    medium_text = button_font.render("Medium",0,(255,255,255))
    hard_text = button_font.render("Hard",0,(255,255,255))

    # surface
    easy_surface = pygame.Surface((easy_text.get_size()[0]+20,easy_text.get_size()[1]+20))
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20, medium_text.get_size()[1] + 20))
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20, hard_text.get_size()[1] + 20))

    # surface.fill
    easy_surface.fill(line_color)
    medium_surface.fill(line_color)
    hard_surface.fill(line_color)

    # surface.blit
    easy_surface.blit(easy_text, (10, 10))
    medium_surface.blit(medium_text, (10, 10))
    hard_surface.blit(hard_text, (10, 10))

    # prints a combination of the text and rectangle to create buttons.
    easy_rectangle = easy_surface.get_rect(bottomright=(width//3,height//2+100))
    medium_rectangle = medium_surface.get_rect(midbottom=(width // 2, height // 2 + 100))
    hard_rectangle = hard_surface.get_rect(bottomleft=(600, height // 2 + 100))
    screen.blit(easy_surface,easy_rectangle)
    screen.blit(medium_surface, medium_rectangle)
    screen.blit(hard_surface, hard_rectangle)

    # while loop using pygame mousebuttondown method which gives buttons functionality.

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rectangle.collidepoint(event.pos):
                    difficulty[0] = 30
                    screen.fill(black)
                    board.draw()
                    return
                if medium_rectangle.collidepoint(event.pos):
                    difficulty[0] = 40
                    screen.fill(black)
                    board.draw()
                    return
                elif hard_rectangle.collidepoint(event.pos):
                    difficulty[0] = 50
                    screen.fill(black)
                    board.draw()
                    return
        pygame.display.update()



# the method draw_win_screen prints a screen with win message along with
# a functional exit button after user meets sudoku game requirements.
def draw_win_screen(screen):
    winner = True
    game_over_font = pygame.font.Font(None, 40)
    sudokuimage = pygame.image.load("sudokuimage.jpg")
    sudokuimage = pygame.transform.scale(sudokuimage, (3000, 3000))
    screen.blit(sudokuimage, (0, 0))

    # prints Game Won text

    if winner == True:
        text = 'Game Won!'
    game_over_surf = game_over_font.render(text, 0, black)
    game_over_rect = game_over_surf.get_rect(
        center=(width // 2, height // 2 - 100))
    screen.blit(game_over_surf, game_over_rect)

    # EXIT BUTTON
    exit_text = button_font.render("Exit", 0, (255, 255, 255))
    exit_surface = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
    exit_surface.fill(line_color)
    exit_surface.blit(exit_text, (10, 10))
    exit_rectangle = exit_surface.get_rect(center=(width // 2, height // 2 + 100))
    screen.blit(exit_surface, exit_rectangle)

    # adds functionality to exit button

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_rectangle.collidepoint(event.pos):
                    exit()
        pygame.display.update()


# the draw_gameover_screen method prints the screen the user sees when they did not meet winning requirements.
def draw_gameover_screen(screen):
    winner = True
    game_over_font = pygame.font.Font(None, 40)
    sudokuimage = pygame.image.load("sudokuimage.jpg")
    sudokuimage = pygame.transform.scale(sudokuimage, (2200, 2200))
    screen.blit(sudokuimage, (0, 0))

    # prints Game Over text

    if winner == True:
        text = 'Game Over :('
    game_over_surf = game_over_font.render(text, 0, black)
    game_over_rect = game_over_surf.get_rect(
        center=(width // 2, height // 2 - 100))
    screen.blit(game_over_surf, game_over_rect)

    # RESTART BUTTON

    button_font = pygame.font.Font(None, 70)
    restart_text = button_font.render("Restart", 0, (255, 255, 255))
    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
    restart_surface.fill(line_color)
    restart_surface.blit(restart_text, (10, 10))
    restart_rectangle = restart_surface.get_rect(center=(width // 2, height // 2 + 100))
    screen.blit(restart_surface, restart_rectangle)

    #adds functionality to restart button.

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_rectangle.collidepoint(event.pos):
                    return
        pygame.display.update()

#the method the_big_one() prints the three buttons under the board while playing
# and takes care of clicking functionality.

def the_big_one():
     while True:

        #EXIT BUTTON

        button_font = pygame.font.Font(None, 70)
        exit_button_text = button_font.render("Exit", 0, (255, 255, 255))
        exit_surface = pygame.Surface((exit_button_text.get_size()[0] + 20, exit_button_text.get_size()[1] + 20))
        exit_surface.fill((18, 18, 18))
        exit_surface.blit(exit_button_text, (10, 10))
        exit_rectangle = exit_surface.get_rect(bottomleft=(0, 900))
        screen.blit(exit_surface, exit_rectangle)

        # RESTART BUTTON

        restart_button_text = button_font.render("Restart", 0, (255, 255, 255))
        restart_surface = pygame.Surface(
            (restart_button_text.get_size()[0] + 20, restart_button_text.get_size()[1] + 20))
        restart_surface.fill((18, 18, 18))
        restart_surface.blit(restart_button_text, (10, 10))
        restart_rectangle = restart_surface.get_rect(bottomright=(810, 900))
        screen.blit(restart_surface, restart_rectangle)

        # RESET BUTTON

        reset_button_text = button_font.render("Reset", 0, (255, 255, 255))
        reset_surface = pygame.Surface((reset_button_text.get_size()[0] + 20, reset_button_text.get_size()[1] + 20))
        reset_surface.fill((18, 18, 18))
        reset_surface.blit(reset_button_text, (10, 10))
        reset_rectangle = reset_surface.get_rect(midbottom=(405, 900))
        screen.blit(reset_surface, reset_rectangle)

        # the method after_input used to call functions after every user input.
        def after_input():
            board.place_number(value)
            board.update_board()
            if board.is_full() == True:
                if board.check_board() == True:
                    # prints winner screen
                    draw_win_screen(screen)
                else:
                    # prints game over screen if user lost
                    winner = True
                    game_over_font = pygame.font.Font(None, 40)
                    sudokuimage = pygame.image.load("sudokuimage.jpg")
                    sudokuimage = pygame.transform.scale(sudokuimage, (2200, 2200))
                    screen.blit(sudokuimage, (0, 0))
                    if winner == True:
                        text = 'Game Over :('
                    game_over_surf = game_over_font.render(text, 0, black)
                    game_over_rect = game_over_surf.get_rect(
                        center=(width // 2, height // 2 - 100))
                    screen.blit(game_over_surf, game_over_rect)
                    button_font = pygame.font.Font(None, 70)
                    restart_text = button_font.render("Restart", 0, (255, 255, 255))
                    restart_surface = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
                    restart_surface.fill(line_color)
                    restart_surface.blit(restart_text, (10, 10))
                    restart_rectangle = restart_surface.get_rect(center=(width // 2, height // 2 + 100))
                    screen.blit(restart_surface, restart_rectangle)
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if restart_rectangle.collidepoint(event.pos):
                                    var[0] = 1
                                    return
                        pygame.display.update()

        # event handler
        # everything below takes care of clicking and entering numbers.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if var[0] == 1:
                    var[0] = 0
                    return
                x, y = event.pos
                if y <= 810:
                    col = y // 90
                row = x // 90
                # initializes row and column indexes clicked for use in functions
                board.click(x, y)
                board.select(row, col)
                init_clicked_row = int(event.pos[1] / 90)
                init_clicked_col = int(event.pos[0] / 90)
                pygame.draw.rect(screen, (255, 255, 255),
                                 pygame.Rect(init_clicked_col * 90, init_clicked_row * 90, 90, 90), 2)
                if var[0] == 0:
                    # buttons on bottom of game screen
                    if reset_rectangle.collidepoint(event.pos):
                        board.reset_to_original()
                        board.draw()
                        continue
                    elif restart_rectangle.collidepoint(event.pos):
                        return
                    elif exit_rectangle.collidepoint(event.pos):
                        exit()
            if event.type == pygame.KEYDOWN:
                # actions after user inputs each number from 1-9
                if event.key == pygame.K_1:
                    value = 1
                    board.sketch(value)
                # actions if user deletes input
                if event.key == pygame.K_BACKSPACE:
                    board.clear()
                    board.draw()
                # actions if user presses enter
                if event.key == pygame.K_RETURN:
                    board.draw()
                    after_input()
            if event.type == pygame.KEYDOWN:
                # actions after user inputs each number from 1-9
                if event.key == pygame.K_2:
                    value = 2
                    board.sketch(value)
                    # actions if user deletes input
                    if event.key == pygame.K_BACKSPACE:
                        board.clear()
                        board.draw()
                        # actions if user presses enter
                    if event.key == pygame.K_RETURN:
                        board.draw()
                        after_input()
            if event.type == pygame.KEYDOWN:
                # actions after user inputs each number from 1-9
                if event.key == pygame.K_3:
                    value = 3
                    board.sketch(value)
                    # actions if user deletes input
                    if event.key == pygame.K_BACKSPACE:
                        board.clear()
                        board.draw()
                        # actions if user presses enter
                    if event.key == pygame.K_RETURN:
                        board.draw()
                        after_input()
            if event.type == pygame.KEYDOWN:
                # actions after user inputs each number from 1-9
                if event.key == pygame.K_4:
                    value = 4
                    board.sketch(value)
                    # actions if user deletes input
                    if event.key == pygame.K_BACKSPACE:
                        board.clear()
                        board.draw()
                        # actions if user presses enter
                    if event.key == pygame.K_RETURN:
                        board.draw()
                        after_input()
            if event.type == pygame.KEYDOWN:
                # actions after user inputs each number from 1-9
                if event.key == pygame.K_5:
                    value = 5
                    board.sketch(value)
                    # actions if user deletes input
                    if event.key == pygame.K_BACKSPACE:
                        board.clear()
                        board.draw()
                        # actions if user presses enter
                    if event.key == pygame.K_RETURN:
                        board.draw()
                        after_input()
            if event.type == pygame.KEYDOWN:
                # actions after user inputs each number from 1-9
                if event.key == pygame.K_6:
                    value = 6
                    board.sketch(value)
                    # actions if user deletes input
                    if event.key == pygame.K_BACKSPACE:
                        board.clear()
                        board.draw()
                        # actions if user presses enter
                    if event.key == pygame.K_RETURN:
                        board.draw()
                        after_input()
            if event.type == pygame.KEYDOWN:
                # actions after user inputs each number from 1-9
                if event.key == pygame.K_7:
                    value = 7
                    board.sketch(value)
                    # actions if user deletes input
                    if event.key == pygame.K_BACKSPACE:
                        board.clear()
                        board.draw()
                        # actions if user presses enter
                    if event.key == pygame.K_RETURN:
                        board.draw()
                        after_input()
            if event.type == pygame.KEYDOWN:
                # actions after user inputs each number from 1-9
                if event.key == pygame.K_8:
                    value = 8
                    board.sketch(value)
                    # actions if user deletes input
                    if event.key == pygame.K_BACKSPACE:
                        board.clear()
                        board.draw()
                        # actions if user presses enter
                    if event.key == pygame.K_RETURN:
                        board.draw()
                        after_input()
            if event.type == pygame.KEYDOWN:
                # actions after user inputs each number from 1-9
                if event.key == pygame.K_9:
                    value = 9
                    board.sketch(value)
                    # actions if user deletes input
                    if event.key == pygame.K_BACKSPACE:
                        board.clear()
                        board.draw()
                        # actions if user presses enter
                    if event.key == pygame.K_RETURN:
                        board.draw()
                        after_input()

        pygame.display.update()

# the main method initalizes pygame, the board function, sets variables, and calls methods in the necessary order

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((width,height))
    board = Board(810, 900, screen, 30)
    draw_game_start(screen, board)
    dif = difficulty[0]
    board = Board(810, 900, screen, dif)
    board.draw()
    button_font = pygame.font.Font(None, 70)
    the_big_one()
    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((width, height))
    board = Board(810, 900, screen, 30)
    draw_game_start(screen, board)
    dif = difficulty[0]
    board = Board(810, 900, screen, dif)
    board.draw()
    button_font = pygame.font.Font(None, 70)
    the_big_one()
    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((width, height))
    board = Board(810, 900, screen, 30)
    draw_game_start(screen, board)
    dif = difficulty[0]
    board = Board(810, 900, screen, dif)
    board.draw()
    button_font = pygame.font.Font(None, 70)
    the_big_one()
    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((width, height))
    board = Board(810, 900, screen, 30)
    draw_game_start(screen, board)
    dif = difficulty[0]
    board = Board(810, 900, screen, dif)
    board.draw()
    button_font = pygame.font.Font(None, 70)
    the_big_one()
    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((width, height))
    board = Board(810, 900, screen, 30)
    draw_game_start(screen, board)
    dif = difficulty[0]
    board = Board(810, 900, screen, dif)
    board.draw()
    button_font = pygame.font.Font(None, 70)
    the_big_one()
    pygame.init()
    pygame.display.set_caption("Sudoku")
    screen = pygame.display.set_mode((width, height))
    board = Board(810, 900, screen, 30)
    draw_game_start(screen, board)
    dif = difficulty[0]
    board = Board(810, 900, screen, dif)
    board.draw()
    button_font = pygame.font.Font(None, 70)
    the_big_one()
