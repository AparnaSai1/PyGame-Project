# imports pygame module

import pygame

#defines constants used later

width = 810
height = 900
line_width = 15
win_line_width = 15
board_rows = 3
board_cols = 3
square_size = 100
red = (225,0,0)
line_color = (245,152,66)
BG_COLOR = (255,255,255)
size_of_box = 60
gray = (131,139,139)
black = (18,18,18)


#the method text_objects defines variables like fontsize, color that we will use in the main method later.
def text_objects(text, fontname, fontsize, color, xpos, ypos, screen):
    font = pygame.font.Font(fontname, fontsize)
    textSurface = font.render(text, True, color)
    textRect = textSurface.get_rect()
    textRect.center = (xpos, ypos)
    screen.blit(textSurface, textRect)


#creates Cell class
class Cell:

    # defines the positional arguments for def __init__
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

        self.selected = False

    # sets the value of the cell
    def set_cell_value(self, value):
        self.value = value

    # saves value when clicked on for when user hits enter button right after.
    def set_sketched_value(self, value):
        self.sketched_value = value

    # draws the outline around the cell when clicked on
    def draw(self):
        x = self.col * size_of_box
        y = self.row * size_of_box

        # the code below draws around the cell sides accordingly

        self.cell_boxes = pygame.Rect(x, y, size_of_box,size_of_box)
        if self.selected == True:
            pygame.draw.rect(self.screen, red, self.cell_boxes, width=line_width)
        else:
            pygame.draw.rect(self.screen, BG_COLOR, self.cell_boxes, width=line_width)
        if self.sketched_value > 0:
            text_objects(str(self.sketched_value), None, 20, gray, x + 12, y + 15, self.screen)
        elif self.value > 0:
            text_objects(str(self.value), None, 20, BG_COLOR, x + 50, y + 50, self.screen)


