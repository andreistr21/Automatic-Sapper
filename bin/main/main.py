import os
import random
from tkinter import *

from bin.classess.Field import Field
from bin.classess.Mine import Mine
from bin.classess.Player import Player
from bin.classess.Node import Node

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


def Arrow(direction):
    image = ""
    if direction == "north":
        image = player.arrow_north_image
    elif direction == "south":
        image = player.arrow_south_image
    elif direction == "west":
        image = player.arrow_west_image
    elif direction == "east":
        image = player.arrow_east_image

    field.small_field_canvas.itemconfig(player.image_canvas_id, image=image)


# Putting images
def Fill(bool):
    if bool:
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
# def Rectangle(bool, direction):
#     if bool:
#         field.rectangle = field.small_field_canvas.create_rectangle(player.current_x, player.current_y, player.current_x + player.step - 2,
#                                                   player.current_y + player.step - 2, width=3, outline='blue2')
#     else:
#         if direction == "East" and field.small_field_canvas.coords(field.rectangle)[0] + player.step < FRAME_WIDTH:
#             field.small_field_canvas.move(field.rectangle, player.step, 0)
#         elif direction == "West" and field.small_field_canvas.coords(field.rectangle)[0] > player.x_start:
#             field.small_field_canvas.move(field.rectangle, -player.step, 0)
#         elif direction == "North" and field.small_field_canvas.coords(field.rectangle)[1] > player.y_start:
#             field.small_field_canvas.move(field.rectangle, 0, -player.step)
#         elif direction == "South" and field.small_field_canvas.coords(field.rectangle)[1] + player.step < FRAME_HEIGHT:
#             field.small_field_canvas.move(field.rectangle, 0, player.step)


def Next_direction(side):
    # Define next direction
    current_direction = player.direction
    t = -1
    for i in range(4):
        if player.directions[i] == current_direction:
            t = i
            break

    # Write next direction to Player
    if side == "Right":
        player.direction = player.directions[(t + 1) % 4]
    elif side == "Left":
        player.direction = player.directions[(t - 1) % 4]

    return player.direction


def MovingForward():
    if player.direction == "east" and field.small_field_canvas.coords(player.image_canvas_id)[0] + player.step < FRAME_WIDTH:
        field.small_field_canvas.move(player.image_canvas_id, player.step, 0)
    elif player.direction == "west" and field.small_field_canvas.coords(player.image_canvas_id)[0] > player.x_start:
        field.small_field_canvas.move(player.image_canvas_id, -player.step, 0)
    elif player.direction == "north" and field.small_field_canvas.coords(player.image_canvas_id)[1] > player.y_start:
        field.small_field_canvas.move(player.image_canvas_id, 0, -player.step)
    elif player.direction == "south" and field.small_field_canvas.coords(player.image_canvas_id)[1] + player.step < FRAME_HEIGHT:
        field.small_field_canvas.move(player.image_canvas_id, 0, player.step)


def Moving(event):
    # Moving
    if event.keysym == "Right":
        # player.MovingRight()
        field.Moving()
        Fill(False)
        next_direction = Next_direction(event.keysym)
        Arrow(next_direction)
    elif event.keysym == "Left":
        # player.MovingLeft()
        field.Moving()
        Fill(False)
        next_direction = Next_direction(event.keysym)
        Arrow(next_direction)
    elif event.keysym == "Up":
        player.Moving()
        field.Moving()
        Fill(False)
        MovingForward()
        Arrow(player.direction)
    # elif event.keysym == "space":
    #     player.MovingDown()
    #     field.Moving()
    #     Fill()
    #     Arrow(player.arrow_south_image)


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
    if event.keysym in ["Right", "Left", "Up", "space"]:
        Moving(event)
    elif event.keysym in ["1", "2"]:
        if event.keysym == "1":
            CellDesignation(field.state_of_cell_array, "red")
        else:
            CellDesignation(field.state_of_cell_array, "green")


# Modified by Artem to search in the status area
def MouseClickEvent(event):
    print(len(field.canvas_small_images), field.canvas_small_images)
    for i in range(0, len(field.canvas_small_images)):
        print(field.small_field_canvas.coords(field.canvas_small_images[i]))
    print("Lewy przycisk myszy zostal nacisniety!")
    node = Node()
    print(node.state.coord, node.state.direction, node.action, node.parent)
    node.state.coord = field.small_field_canvas.coords(field.canvas_small_images[5])
    node.state.direction = "N"
    node.action = "l"
    node.parent = 1
    print(node.state.coord, node.state.direction, node.parent, node.action)
    print("Pozycje myszy: {} {}".format(event.x, event.y))


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

    # Add arrow image to Player class
    images = []
    for file in os.listdir("../../files/arrow"):
        path = f"../../files/arrow/{file}"
        img = PhotoImage(master=field.small_field_canvas, file=path)
        images.append(img)

    player.arrow_east_image = images[0]
    player.arrow_north_image = images[1]
    player.arrow_south_image = images[2]
    player.arrow_west_image = images[3]

    # Filling window with images
    Fill(True)
    # Drawing arrow (player)
    image = player.arrow_east_image
    player.image_canvas_id = field.small_field_canvas.create_image(player.current_x, player.current_y, anchor=NW,
                                                                   image=image)
    # Arrow(player.direction)
    # Rectangle(True, "None")
    # Rectangle()
    # Binding keyboard press to function
    field.win.bind("<Key>", Action)
    field.small_field_canvas.bind("<Button-1>", MouseClickEvent)
    # Starting mainloop for window
    field.win.mainloop()


if __name__ == '__main__':
    main()