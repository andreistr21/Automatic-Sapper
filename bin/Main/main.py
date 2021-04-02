from tkinter import *
import os

from bin.Classess.Player import Player
from bin.Classess.Field import Field

WINDOW_X = 533 + 1200
WINDOW_Y = 950
FRAME_WIDTH = 533
FRAME_HEIGHT = 533

# Size of small image
IMAGE_SIZE = 50

# Creating objects
player = Player()
field = Field()


# Putting images
def Fill():
    x = field.x_start
    y = field.y_start

    row = 0
    column = 0

    # Drawing small images
    for i in range(field.columns):
        for j in range(field.rows):
            small_image_name = field.small_image_array[column][row]

            field.small_field_canvas.image = small_image_name
            field.small_field_canvas.create_image(x, y, anchor=NW, image=small_image_name)

            x += field.image_size + field.x_start
            row += 1
        y += field.image_size + field.y_start
        x = field.x_start
        column += 1
        row = 0

    # Drawing red/green rectangles
    for el in field.state_of_cell_array:
        if el[0] != 0:
            field.small_field_canvas.create_rectangle(el[0], el[1], el[0] + player.step - 2,
                                                     el[1] + player.step - 2, width=3, outline=el[2])

    DrawingLargeImage()


def DrawingLargeImage():
    large_img_name = field.large_image_array[player.current_array_y][player.current_array_x]

    field.large_image_canvas.image = large_img_name
    field.large_image_canvas.create_image(0, 0, anchor=NW, image=large_img_name)


# Drawing rectangle
def Rectangle():
    field.small_field_canvas.create_rectangle(player.current_x, player.current_y, player.current_x + player.step - 2,
                                              player.current_y + player.step - 2, width=3, outline='blue2')


def Moving(event):
    # Moving
    if event.keysym == "Right":
        if player.current_x + player.step < FRAME_WIDTH:
            player.current_x += player.step
            field.small_field_canvas.delete('all')
            field.large_image_canvas.delete('all')
            player.current_array_x += 1
            Fill()
            Rectangle()
        elif player.current_y + player.step < FRAME_HEIGHT:
            player.current_x = player.x_start
            field.small_field_canvas.delete('all')
            field.large_image_canvas.delete('all')
            player.current_array_x = 0
            player.current_array_y += 1
            player.current_y += player.step
            Fill()
            Rectangle()
    elif event.keysym == "Left":
        if player.current_x - player.step >= player.x_start:
            player.current_x -= player.step
            field.small_field_canvas.delete('all')
            field.large_image_canvas.delete('all')
            player.current_array_x -= 1
            Fill()
            Rectangle()
        elif player.current_y - player.step >= player.y_start:
            player.current_x = FRAME_WIDTH - player.step
            field.small_field_canvas.delete('all')
            field.large_image_canvas.delete('all')
            player.current_array_x = 9
            player.current_array_y -= 1
            player.current_y -= player.step
            Fill()
            Rectangle()
    elif event.keysym == "Up":
        if player.current_y - player.step >= player.y_start:
            player.current_y -= player.step
            field.small_field_canvas.delete('all')
            field.large_image_canvas.delete('all')
            player.current_array_y -= 1
            Fill()
            Rectangle()
    elif event.keysym == "Down":
        if player.current_y + player.step < FRAME_HEIGHT:
            player.current_y += player.step
            field.small_field_canvas.delete('all')
            field.large_image_canvas.delete('all')
            player.current_array_y += 1
            Fill()
            Rectangle()


def ImagesInArray(directory, array):
    # Filling array from directory
    row = column = 0
    for file in os.listdir(directory):
        image_name = file
        image_path = f"{directory}/{image_name}"
        if directory == "../files/large_images":
            image = PhotoImage(master=field.large_image_canvas, file=image_path)
        else:
            image = PhotoImage(master=field.small_field_canvas, file=image_path)

        array[row][column] = image
        column += 1
        if column == 10:
            column = 0
            row += 1


def CellDesignation(array, color):
    for element in array:
        if element[0] == 0:
            element[0] = player.current_x
            element[1] = player.current_y
            element[2] = color
            break


def Action(event):
    if event.keysym in ["Right", "Left", "Up", "Down"]:
        Moving(event)
    elif event.keysym in ["1", "2"]:
        if event.keysym == "1":
            CellDesignation(field.state_of_cell_array, "red")
        else:
            CellDesignation(field.state_of_cell_array, "green")


def main():
    # Creating the main window of an application
    win_size = f'{WINDOW_X}x{WINDOW_Y}'
    # global win
    # win = Tk()
    field.win.title("Sapper")
    field.win.configure(bg='gray')
    field.win.geometry(win_size)

    # Filling image arrays
    large_directory = "../../files/large_images"
    ImagesInArray(large_directory, field.large_image_array)
    small_directory = "../../files/small_images"
    ImagesInArray(small_directory, field.small_image_array)

    # Filling window with images
    Fill()
    # Drawing rectangle (player)
    Rectangle()
    # Binding keyboard press to function
    field.win.bind("<Key>", Action)
    # Starting mainloop for window
    field.win.mainloop()


if __name__ == '__main__':
    main()
