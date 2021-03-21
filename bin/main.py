from doctest import master
from tkinter import *

import os

from PIL import Image, ImageTk

WINDOW_X = 533 + 1200
WINDOW_Y = 950
FRAME_WIDTH = 533
FRAME_HEIGHT = 533

# Size of small image
IMAGE_SIZE = 50


class Player(object):
    def __init__(self):
        self.x_start = 3
        self.y_start = 3
        self.current_x = self.x_start
        self.current_y = self.y_start
        self.step = IMAGE_SIZE + self.x_start
        self.current_array_x = 0
        self.current_array_y = 0

    def Moving(self, event):
        # Moving
        if event.keysym == "Right":
            if self.current_x + self.step < FRAME_WIDTH:
                self.current_x += self.step
                field_canvas.delete('all')
                large_image_canvas.delete('all')
                self.current_array_x += 1
                field.Fill()
                self.Rectangle()
            elif self.current_y + self.step < FRAME_HEIGHT:
                self.current_x = self.x_start
                field_canvas.delete('all')
                large_image_canvas.delete('all')
                self.current_array_x = 0
                self.current_array_y += 1
                self.current_y += self.step
                field.Fill()
                self.Rectangle()
        elif event.keysym == "Left":
            if self.current_x - self.step >= self.x_start:
                self.current_x -= self.step
                field_canvas.delete('all')
                large_image_canvas.delete('all')
                self.current_array_x -= 1
                field.Fill()
                self.Rectangle()
            elif self.current_y - self.step >= self.y_start:
                self.current_x = FRAME_WIDTH - self.step
                field_canvas.delete('all')
                large_image_canvas.delete('all')
                self.current_array_x = 9
                self.current_array_y -= 1
                self.current_y -= self.step
                field.Fill()
                self.Rectangle()
        elif event.keysym == "Up":
            if self.current_y - self.step >= self.y_start:
                self.current_y -= self.step
                field_canvas.delete('all')
                large_image_canvas.delete('all')
                self.current_array_y -= 1
                field.Fill()
                self.Rectangle()
        elif event.keysym == "Down":
            if self.current_y + self.step < FRAME_HEIGHT:
                self.current_y += self.step
                field_canvas.delete('all')
                large_image_canvas.delete('all')
                self.current_array_y += 1
                field.Fill()
                self.Rectangle()

    # Drawing rectangle
    def Rectangle(self):
        field_canvas.create_rectangle(self.current_x, self.current_y, self.current_x + self.step - 2,
                                      self.current_y + self.step - 2, width=3, outline='red')


def DrawingLargeImage():
    large_img_name = large_image_array[player.current_array_y][player.current_array_x]
    # large_img_path = f"{large_directory}/{large_img_name}"
    # large_img = PhotoImage(file=large_img_path)

    large_image_canvas.image = large_img_name
    large_image_canvas.create_image(0, 0, anchor=NW, image=large_img_name)


class Field(object):
    def __init__(self):
        self.width = 533
        self.height = 533
        self.image_size = 50
        self.rows = 10
        self.columns = 10
        self.x_start = 3
        self.y_start = 3

    # Putting images
    def Fill(self):
        x = self.x_start
        y = self.y_start
        row = 0
        column = 0
        for i in range(self.columns):
            for j in range(self.rows):
                small_image_name = small_image_array[column][row]
                # small_image_path = f"{small_directory}/{small_image_name}"
                # small_img = PhotoImage(file=small_image_path)

                field_canvas.image = small_image_name
                field_canvas.create_image(x, y, anchor=NW, image=small_image_name)
                x += self.image_size + self.x_start
                row += 1
            y += self.image_size + self.y_start
            x = self.x_start
            column += 1
            row = 0
        DrawingLargeImage()


def ImagesInArray(directory, array):
    # Filling array from directory
    row = column = 0
    for file in os.listdir(directory):
        image_name = file
        image_path = f"{directory}/{image_name}"
        image = PhotoImage(file=image_path)

        array[row][column] = image
        column += 1
        if column == 10:
            column = 0
            row += 1


def main():
    # Creating the main window of an application
    window_size = f'{WINDOW_X}x{WINDOW_Y}'
    global window
    window = Tk()
    window.title("Sapper")
    window.geometry(window_size)

    # Creating objects
    global player
    global field
    field = Field()
    player = Player()

    # Creating arrays with names of images
    global large_image_array
    global small_image_array
    small_image_array = [[0 for i in range(field.rows)] for j in range(field.columns)]
    large_image_array = [[0 for i in range(field.rows)] for j in range(field.columns)]

    # Filling image arrays
    global large_directory
    global small_directory
    large_directory = "../files/large_images"
    ImagesInArray(large_directory, large_image_array)
    small_directory = "../files/small_images"
    ImagesInArray(small_directory, small_image_array)

    # Creating the frames
    main_frame = Frame(master, width=FRAME_WIDTH, height=FRAME_HEIGHT, bd=1)
    main_frame.pack(anchor=NW)

    # Creating the canvas
    global field_canvas
    field_canvas = Canvas(main_frame, width=FRAME_WIDTH, height=FRAME_HEIGHT, bg='white')
    field_canvas.pack()

    # Creating the canvas for large image
    global large_image_canvas
    large_image_canvas = Canvas(window, width=WINDOW_X - 533 - 20, height=900, bg='white')
    large_image_canvas.place(x=FRAME_WIDTH + 5, y=player.y_start)

    # Loading image
    global img
    img = PhotoImage(file="../files/small_images/image.png")

    # Filling window with images
    Field.Fill(field)
    # Drawing rectangle (player)
    Player.Rectangle(player)
    # Binding keyboard press to function
    window.bind("<Key>", player.Moving)
    # Starting mainloop for window
    window.mainloop()


if __name__ == '__main__':
    main()
