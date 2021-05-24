import os
import random
import time
from tkinter import *

from bin.Classess.Field import Field
from bin.Classess.Mine import Mine
from bin.Classess.Travel import Travel
from bin.Classess.Player import Player
import bin.Classess.Node as nd
import bin.Classess.Travel as tr
from resources.Globals import *

# WINDOW_X = 533 + 1200
# WINDOW_Y = 950
# FRAME_WIDTH = 533
# FRAME_HEIGHT = 533
#
# # Size of small image
# IMAGE_SIZE = 50
#
# AMOUNT_OF_MINES = 10
#
# DELAY_TIME = 0.5

# Creating objects
player = Player()
field = Field()
travel = Travel()

fringe = []
explored = []
action_list = []
images_coord = []


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
    global images_coord
    if bool:
        field.PuttingSmallImages()

        travel.points_coord.append(field.small_field_canvas.coords(field.canvas_small_images[0]))
        travel.points_coord.extend(field.mines_coord)

        for i in range(0, len(travel.points_coord)):
            travel.points_map[i + 1] = travel.points_coord[i]

        print(travel.points_map)


        for i in range(0, len(field.canvas_small_images)):
            images_coord.append(field.small_field_canvas.coords(field.canvas_small_images[i]))
        # print("Coords List: ", images_coord)

        nd.init_data(images_coord, field.cell_expense)

    # Drawing red/green rectangles
    for el in field.state_of_cell_array:
        if el[0] != 0:
            field.small_field_canvas.create_rectangle(el[0], el[1], el[0] + player.step - 2,
                                                      el[1] + player.step - 2, width=3, outline=el[2])

    DrawingLargeImage()


def DrawingLargeImage():
    large_img_name = field.large_image_array[player.current_array_y][player.current_array_x]

    field.PuttingLargeImage(large_img_name)


def NextDirection(action):
    # Define next direction
    current_direction = player.direction
    t = -1
    for i in range(4):
        if player.directions[i] == current_direction:
            t = i
            break

    # Write next direction to Player
    if action == "Right":
        player.direction = player.directions[(t + 1) % 4]
    elif action == "Left":
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


def Moving(action):
    # Moving
    if action == "Right":
        # player.MovingRight()
        field.Moving()
        Fill(False)
        next_direction = NextDirection(action)
        Arrow(next_direction)
    elif action == "Left":
        # player.MovingLeft()
        field.Moving()
        Fill(False)
        next_direction = NextDirection(action)
        Arrow(next_direction)
    elif action == "Up":
        player.Moving()
        field.Moving()
        Fill(False)
        MovingForward()
        Arrow(player.direction)


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
                if row == 10:
                    break

        column += 1
        if column == 10:
            column = 0
            row += 1
        if row == 10:
            break


def CellDesignation(array, color):
    for element in array:
        if element[0] == 0:
            element[0] = player.current_x
            element[1] = player.current_y
            element[2] = color
            break


def Action(action):
    if action in ["Right", "Left", "Up", "space"]:
        Moving(action)
    elif action in ["1", "2"]:
        if action == "1":
            CellDesignation(field.state_of_cell_array, "red")
        else:
            CellDesignation(field.state_of_cell_array, "green")


# Modified by Artem to search in the status area
def create_action_list(states, index):
    global fringe
    global action_list

    if index == 0:
        action_list.reverse()
        return True
    action_list.append(fringe[index].action)
    state_parent = [fringe[index].parent[0], fringe[index].parent[1]]
    create_action_list(states, states.index(state_parent))


def MouseClickEvent(track):
    global fringe
    global explored
    global action_list

    print("The best individual is: {} {}".format(track[1], track[0]))
    for point in range(0, len(track[1]) + 1):
        start_position = field.small_field_canvas.coords(player.image_canvas_id)
        if point == len(track[1]):
            end_position = travel.points_map[1]
        else:
            end_position = travel.points_map[track[1][point]]

        node = nd.Node()
        if len(fringe) == 0:
            node.state.coord = start_position
            node.state.direction = "east"
        else:
            states = []
            for k in range(0, len(fringe)):
                new_state = fringe[k].state.coord
                states.append(new_state)
            start_node = fringe[-1]

            node.state.coord = start_node.state.coord
            node.state.direction = start_node.state.direction

        fringe.clear()
        explored.clear()
        action_list.clear()
        fringe = nd.graph_search_A(fringe, explored, node.state, end_position)
        # fringe = nd.graph_search(fringe, explored, node.state, end_position)

        states = []
        goal_all = []
        for i in range(0, len(fringe)):
            new_state = [fringe[i].state.coord, fringe[i].state.direction]
            states.append(new_state)
            if end_position[0] == fringe[i].state.coord[0] and end_position[1] == fringe[i].state.coord[1]:
                goal_all.append(fringe[i])

        elem_min = goal_all[0]
        for i in range(1, len(goal_all)):
            if elem_min.priority > goal_all[i].priority:
                elem_min = goal_all[i]
        index = fringe.index(elem_min)
        fringe = fringe[:index + 1]

        create_action_list(states, -1)

        # for i in range(0, len(fringe)):
        #     print('Node{} = State: {} {}, Parent: {} {} {}, Action: {}'.format(i + 1, fringe[i].state.coord, fringe[i].state.direction, fringe[i].parent[0], fringe[i].parent[1], fringe[i].parent[2], fringe[i].action))

        # print(action_list)

        # Start moving
        AutoMove()
        DrawFlag()

        time.sleep(SLEEP_AFTER_CHECK_MINE)


    # start_position = field.small_field_canvas.coords(player.image_canvas_id)
    # end_position = []
    #
    # # print("Pierwsza pozycja: {} {}".format(start_position[0], start_position[1]))
    #
    # for i in range(0, len(field.canvas_small_images)):
    #     img_coords = field.small_field_canvas.coords(field.canvas_small_images[i])
    #     if (img_coords[0] <= event.x and event.x <= img_coords[0] + IMAGE_SIZE) and (img_coords[1] <= event.y and event.y <= img_coords[1] + IMAGE_SIZE):
    #         end_position = img_coords
    #         print("Color cost: ", field.cell_expense[i])
    #
    # # if len(end_position) == 2:
    # #     print("Koncowa pozycja: {} {}".format(end_position[0], end_position[1]))
    #
    # node = nd.Node()
    # if len(fringe) == 0:
    #     node.state.coord = start_position
    #     node.state.direction = "east"
    # else:
    #     states = []
    #     for k in range(0, len(fringe)):
    #         new_state = fringe[k].state.coord
    #         states.append(new_state)
    #     start_node = fringe[-1]
    #
    #     node.state.coord = start_node.state.coord
    #     node.state.direction = start_node.state.direction
    #
    # fringe.clear()
    # explored.clear()
    # action_list.clear()
    # fringe = nd.graph_search_A(fringe, explored, node.state, end_position)
    # # fringe = nd.graph_search(fringe, explored, node.state, end_position)
    #
    # states = []
    # goal_all = []
    # for i in range(0, len(fringe)):
    #     new_state = [fringe[i].state.coord, fringe[i].state.direction]
    #     states.append(new_state)
    #     if end_position[0] == fringe[i].state.coord[0] and end_position[1] == fringe[i].state.coord[1]:
    #         goal_all.append(fringe[i])
    #
    # elem_min = goal_all[0]
    # for i in range(1, len(goal_all)):
    #     if elem_min.priority > goal_all[i].priority:
    #         elem_min = goal_all[i]
    # index = fringe.index(elem_min)
    # fringe = fringe[:index + 1]
    #
    # create_action_list(states, -1)
    #
    # # for i in range(0, len(fringe)):
    # #     print('Node{} = State: {} {}, Parent: {} {} {}, Action: {}'.format(i + 1, fringe[i].state.coord, fringe[i].state.direction, fringe[i].parent[0], fringe[i].parent[1], fringe[i].parent[2], fringe[i].action))
    #
    # print(action_list)
    #
    #
    #
    # # Start moving
    # AutoMove()


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
            if x == 0 and y == 0:
                continue
            else:
                mine = Mine(x, y)
                mines_array.append(mine)

                field.field_state_array[x][y] = True

                counter += 1


def MinesInArrays(mines_array, directory, imgs_array, bool_mines_coord):
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

    if bool_mines_coord:
        for i in range(len(mines_array)):
            field.mines_coord.append([mines_array[i].array_x, mines_array[i].array_y])


def DrawFlag():
    field.small_field_canvas.create_image(player.current_x, player.current_y, anchor=NW, image=field.flag_img)


# def IsItMine():
#     visited = 0     # 0 - not mine; 1 - on this mine for the first time; 2 - already been on this mine
#
#     # Checks if the player is on the mine
#     for i in field.mines_coord:
#         if i[0] == player.current_x and i[1] == player.current_y:
#             visited = 1
#             # Checks if the player has already been on this mine
#             for y in field.visited_mines:
#                 if y[0] == player.current_x and y[1] == player.current_y:
#                     visited = 2
#         if visited == 1:
#             DrawFlag()


def AutoMove():
    for action in action_list:
        # Program wait for better illustration
        time.sleep(DELAY_TIME)
        # Move once
        Action(action)
        # Check if player on mine and if yes, draw flag
        # IsItMine()
        # Update main window
        field.win.update()


# Draws rectangles that indicate type of cells
def DrawRectangle():
    x = 4
    y = 4

    color = None
    # Chose color for rectangle
    for i in range(len(field.cell_expense)):
        if field.cell_expense[i] == standard_cell_cost:
            color = "None"
        elif field.cell_expense[i] == sand_cell_cost:
            color = "yellow"
        elif field.cell_expense[i] == water_cell_cost:
            color = "dodger blue"
        elif field.cell_expense[i] == swamp_cell_cost:
            color = "green4"
        if color != "None":
            field.small_field_canvas.create_rectangle(x, y, x + IMAGE_SIZE + 2, y + IMAGE_SIZE + 2, width=2, outline=color)
        x += player.step
        if x + IMAGE_SIZE + 2 > field.width:
            x = 4
            y += player.step




def AddCostCellsToArray(amount, cost):
    counter = 0
    while counter < amount:
        r = random.randint(0, 99)
        if field.cell_expense[r] == 0:
            field.cell_expense[r] = cost
            counter += 1


def CostingOfCells():
    AddCostCellsToArray(amount_of_sand_cells, sand_cell_cost)
    AddCostCellsToArray(amount_of_water_cells, water_cell_cost)
    AddCostCellsToArray(amount_of_swamp_cells, swamp_cell_cost)
    AddCostCellsToArray(field.rows * field.columns - (amount_of_sand_cells + amount_of_water_cells + amount_of_swamp_cells), standard_cell_cost)

    # Draw rectangles
    DrawRectangle()


def click_button():
    btn.destroy()
    label = Label(field.win, text="Wait...\nAI conquers the world...", fg='black', font="20")
    label.place(x=50, y=570)
    field.win.update()
    track = tr.genetic_algorithm(travel.points_map)

    track[1].remove(1)
    label.config(text=track[1])
    field.win.update()
    MouseClickEvent(track)


def main():
    # Creating the main window of an application
    win_size = f'{WINDOW_X}x{WINDOW_Y}'
    field.win.title("Sapper")
    field.win.configure(bg='gray')
    field.win.geometry(win_size)
    print(f'Amount of mines: {AMOUNT_OF_MINES}')
    global btn
    btn = Button(field.win,
                 text="Search for mines",  # текст кнопки
                 background="#555",  # фоновый цвет кнопки
                 foreground="#ccc",  # цвет текста
                 padx="20",  # отступ от границ до содержимого по горизонтали
                 pady="8",  # отступ от границ до содержимого по вертикали
                 font="24",  # высота шрифта
                 command=click_button
                 )

    btn.place(x=50, y=570)

    # Create array with mines objects
    mines_array = []
    # Put mines on coordinates
    PutMines(mines_array)

    MinesInArrays(mines_array, "../../files/small_mines_images", field.small_image_array, True)
    MinesInArrays(mines_array, "../../files/large_mines_images", field.large_image_array, False)

    # Filling image arrays
    small_directory = "../../files/small_images"
    ImagesInArray(small_directory, field.small_image_array)
    large_directory = "../../files/large_images"
    ImagesInArray(large_directory, field.large_image_array)

    CostingOfCells()

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
    # field.win.bind("<Key>", Action)
    # field.small_field_canvas.bind("<Button-1>", MouseClickEvent)
    # Starting mainloop for window
    field.win.mainloop()


if __name__ == '__main__':
    main()
