from doctest import master
from tkinter import *

# WINDOW_X = 533 + 1200
# WINDOW_Y = 950
# FRAME_WIDTH = 533
# FRAME_HEIGHT = 533
#
# # Size of small image
# IMAGE_SIZE = 50

from resources.Globals import *

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
        self.field_state_array = [[False for i in range(self.rows)] for j in range(self.columns)]
        self.small_image_array = [[0 for i in range(self.rows)] for j in range(self.columns)]
        self.large_image_array = [[0 for i in range(self.rows)] for j in range(self.columns)]
        self.cell_expense = [0 for i in range(self.rows * self.columns)]

        # Modified by Artem to search in the status area
        self.canvas_small_images = []
        self.rectangle = 0

        self.main_frame = Frame(master, width=FRAME_WIDTH, height=FRAME_HEIGHT, bd=0)
        self.main_frame.pack(anchor=NW)
        self.small_field_canvas = Canvas(self.main_frame, width=FRAME_WIDTH, height=FRAME_HEIGHT, highlightthickness=0,
                                         bg='black')

        self.small_field_canvas.pack()
        self.large_image_canvas = Canvas(self.win, width=WINDOW_X - 533 - 20, height=900, highlightthickness=0,
                                         bg='gray')
        self.large_image_canvas.place(x=FRAME_WIDTH + 5, y=3)

    # Clear Canvases
    def Moving(self):
        self.large_image_canvas.delete('all')

    def PuttingSmallImages(self):
        x = self.x_start
        y = self.y_start

        row = 0
        column = 0

        # Putting small images
        for i in range(self.columns):
            for j in range(self.rows):
                small_image_name = self.small_image_array[column][row]

                self.small_field_canvas.image = small_image_name
                self.canvas_small_images.append(
                    self.small_field_canvas.create_image(x, y, anchor=NW, image=small_image_name))
                # self.small_field_canvas.create_image(x, y, anchor=NW, image=small_image_name)

                x += self.image_size + self.x_start
                row += 1
            y += self.image_size + self.y_start
            x = self.x_start
            column += 1
            row = 0

    def PuttingLargeImage(self, large_img_name):
        self.large_image_canvas.image = large_img_name
        self.large_image_canvas.create_image(0, 0, anchor=NW, image=large_img_name)
