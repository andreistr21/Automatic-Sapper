from doctest import master
from tkinter import *

# from bin.main import PlayerReturn as player
# from bin.main import DrawingLargeImage

WINDOW_X = 533 + 1200
WINDOW_Y = 950
FRAME_WIDTH = 533
FRAME_HEIGHT = 533

# Size of small image
IMAGE_SIZE = 50

step = IMAGE_SIZE + 3


class Field(object):
    def __init__(self):
        self.win = Tk()
        self.width = 533
        self.height = 533
        self.image_size = 50
        self.rows = 10
        self.columns = 10
        self.x_start = 3
        self.y_start = 3
        self.state_of_cell_array = [[0 for i in range(3)] for j in range(200)]
        self.small_image_array = [[0 for i in range(self.rows)] for j in range(self.columns)]
        self.large_image_array = [[0 for i in range(self.rows)] for j in range(self.columns)]

        self.main_frame = Frame(master, width=FRAME_WIDTH, height=FRAME_HEIGHT, bd=0)
        self.main_frame.pack(anchor=NW)
        self.small_field_canvas = Canvas(self.main_frame, width=FRAME_WIDTH, height=FRAME_HEIGHT, highlightthickness=0,
                                         bg='light gray')
        self.small_field_canvas.pack()
        self.large_image_canvas = Canvas(self.win, width=WINDOW_X - 533 - 20, height=900, highlightthickness=0,
                                         bg='gray')
        self.large_image_canvas.place(x=FRAME_WIDTH + 5, y=3)

    # # Putting images
    # def Fill(self):
    #     x = self.x_start
    #     y = self.y_start
    #
    #     row = 0
    #     column = 0
    #
    #     # Drawing small images
    #     for i in range(self.columns):
    #         for j in range(self.rows):
    #             small_image_name = self.small_image_array[column][row]
    #
    #             self.small_field_canvas.image = small_image_name
    #             self.small_field_canvas.create_image(x, y, anchor=NW, image=small_image_name)
    #
    #             x += self.image_size + self.x_start
    #             row += 1
    #         y += self.image_size + self.y_start
    #         x = self.x_start
    #         column += 1
    #         row = 0
    #
    #     # Drawing red/green rectangles
    #     for el in self.state_of_cell_array:
    #         if el[0] != 0:
    #             self.small_field_canvas.create_rectangle(el[0], el[1], el[0] + step - 2,
    #                                                      el[1] + step - 2, width=3, outline=el[2])
    #
    #     DrawingLargeImage()
        # self.DrawingLargeImage()

    # def DrawingLargeImage(self):
    #     large_img_name = self.large_image_array[player.current_array_y][player.current_array_x]
    #
    #     self.large_image_canvas.image = large_img_name
    #     self.large_image_canvas.create_image(0, 0, anchor=NW, image=large_img_name)