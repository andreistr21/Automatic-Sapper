import random
from tkinter import *
import os

from bin.classess.Player import Player
from bin.classess.Field import Field
from bin.classess.Mine import Mine

WINDOW_X = 533 + 1200
WINDOW_Y = 950
FRAME_WIDTH = 533
FRAME_HEIGHT = 533

# Size of small image
IMAGE_SIZE = 50

AMOUNT_OF_MINES = 10

# Creating objects
player = Player()
field = Field()


# Putting images
def Fill():
    field.PuttingSmallImages()

    # Drawing red/green rectangles
    for el in field.state_of_cell_array:
        if el[0] != 0:
            field.small_field_canvas.create_rectangle(el[0], el[1], el[0] + player.step - 2,
                                                      el[1] + player.step - 2, width=3, outline=el[2])

    DrawingLargeImage()


def DrawingLargeImage():
    large_img_name = field.large_image_array[player.current_array_y][player.current_array_x]

    field.PuttingLargeImage(large_img_name)


# Drawing rectangle
def Rectangle():
    field.small_field_canvas.create_rectangle(player.current_x, player.current_y, player.current_x + player.step - 2,
                                              player.current_y + player.step - 2, width=3, outline='blue2')


def Moving(event):
    # Moving
    if event.keysym == "Right":
        player.MovingRight()
        field.Moving()
        Fill()
        Rectangle()
    elif event.keysym == "Left":
        player.MovingLeft()
        field.Moving()
        Fill()
        Rectangle()
    elif event.keysym == "Up":
        player.MovingUp()
        field.Moving()
        Fill()
        Rectangle()
    elif event.keysym == "Down":
        player.MovingDown()
        field.Moving()
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

        is_done = False
        while not is_done:
            if array[row][column] == 0:
                array[row][column] = image
                is_done = True
            else:
                column += 1
                if column == 10:
                    column = 0
                    row += 1

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


def PutMines(mines_array):
    counter = 0

    while counter < AMOUNT_OF_MINES:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

        is_equal = False

        for mine in mines_array:
            if mine.array_x == x and mine.array_y == y:
                is_equal = True
        if not is_equal:
            mine = Mine(x, y)
            mines_array.append(mine)

            field.field_state_array[x][y] = True

            counter += 1


def MinesInArrays(mines_array, directory, imgs_array):
    counter = 0

    temp_array = []

    if directory == "../../files/small_mines_images":
        for file in os.listdir(directory):
            if counter < AMOUNT_OF_MINES:
                image_name = file
                image_path = f"{directory}/{image_name}"
                image = PhotoImage(master=field.small_field_canvas, file=image_path)

                temp_array.append(image)

                counter += 1

        for i in range(AMOUNT_OF_MINES):
            mines_array[i].small_img = temp_array[i]

            # Add images in image array
            imgs_array[mines_array[i].array_x][mines_array[i].array_y] = temp_array[i]

    elif directory == "../../files/large_mines_images":
        for file in os.listdir(directory):
            if counter < AMOUNT_OF_MINES:
                image_name = file
                image_path = f"{directory}/{image_name}"
                image = PhotoImage(master=field.large_image_canvas, file=image_path)

                temp_array.append(image)

                counter += 1

        for i in range(AMOUNT_OF_MINES):
            mines_array[i].large_img = temp_array[i]

            # Add images in image array
            imgs_array[mines_array[i].array_x][mines_array[i].array_y] = temp_array[i]


def main():
    # Creating the main window of an application
    win_size = f'{WINDOW_X}x{WINDOW_Y}'
    field.win.title("Sapper")
    field.win.configure(bg='gray')
    field.win.geometry(win_size)

    # Create array with mines objects
    mines_array = []
    # Put mines on coordinates
    PutMines(mines_array)

    MinesInArrays(mines_array, "../../files/small_mines_images", field.small_image_array)
    MinesInArrays(mines_array, "../../files/large_mines_images", field.large_image_array)

    # Filling image arrays
    small_directory = "../../files/small_images"
    ImagesInArray(small_directory, field.small_image_array)
    large_directory = "../../files/large_images"
    ImagesInArray(large_directory, field.large_image_array)

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
