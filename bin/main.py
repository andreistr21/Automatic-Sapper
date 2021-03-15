from doctest import master
from tkinter import *

from PIL import Image, ImageTk

WINDOW_X = 1100
WINDOW_Y = 540
FRAME_WIDTH = 533
FRAME_HEIGHT = 533
IMAGE_SIZE = 50
X_START = Y_START = 3
STEP = IMAGE_SIZE + X_START

current_x = 3
current_y = 3


def Rectangle():
    global current_x
    global current_y
    canvas.create_rectangle(current_x, current_y, current_x + STEP - 2, current_y + STEP - 2, width=3, outline='red')

    # t_x = current_x - STEP
    # t_y = current_y - STEP
    # canvas.create_rectangle(t_x, t_y, STEP, STEP, width=3, outline='white')

    window.bind("<Key>", Moving)


def Field():
    x = X_START
    y = Y_START
    for i in range(10):
        for j in range(10):
            canvas.create_image(x, y, anchor=NW, image=img)
            x += IMAGE_SIZE + X_START
        y += IMAGE_SIZE + Y_START
        x = X_START


def Moving(event):
    global current_x
    global current_y
    if event.keysym == "Right":
        if current_x + STEP < FRAME_WIDTH:
            current_x += STEP
            canvas.delete('all')
            Field()
            Rectangle()
    elif event.keysym == "Left":
        if current_x - STEP >= X_START:
            current_x -= STEP
            canvas.delete('all')
            Field()
            Rectangle()
    elif event.keysym == "Up":
        if current_y - STEP >= Y_START:
            current_y -= STEP
            canvas.delete('all')
            Field()
            Rectangle()
    elif event.keysym == "Down":
        if current_y + STEP < FRAME_HEIGHT:
            current_y += STEP
            canvas.delete('all')
            Field()
            Rectangle()


def main():
    # This creates the main window of an application
    window_size = f'{WINDOW_X}x{WINDOW_Y}'
    global window
    window = Tk()
    window.title("Sapper")
    window.geometry(window_size)

    frame = Frame(master, width=FRAME_WIDTH, height=FRAME_HEIGHT, bd=1)
    frame.pack(anchor=NW)

    global canvas
    canvas = Canvas(frame, width=FRAME_WIDTH, height=FRAME_HEIGHT, bg='white')
    canvas.pack()

    global img
    img = PhotoImage(file="../files/imgs/image.png")

    # x = X_START
    # y = Y_START
    # for i in range(10):
    #     for j in range(10):
    #         canvas.create_image(x, y, anchor=NW, image=img)
    #         x += IMAGE_SIZE + X_START
    #     y += IMAGE_SIZE + Y_START
    #     x = X_START

    # canvas.create_rectangle(X_START, Y_START, X_START + IMAGE_SIZE, Y_START + IMAGE_SIZE, width=3, outline='red')

    # app = Sapper.

    # global current_x
    # global current_y
    # current_x = 3
    # current_y = 3

    Field()
    Rectangle()
    window.bind("<Key>", Moving)
    window.mainloop()

    # moving(window)
    # window.mainloop()


if __name__ == '__main__':
    main()
