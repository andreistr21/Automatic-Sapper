from doctest import master
from tkinter import *

from PIL import Image, ImageTk

WINDOW_X = 1100
WINDOW_Y = 540
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
        self.arrayPosition = [[0] * field.cows] * field.cows

    def Moving(self, event):
        # Moving
        if event.keysym == "Right":
            if self.current_x + self.step < FRAME_WIDTH:
                self.current_x += self.step
                canvas.delete('all')
                field.Fill()
                self.Rectangle()
        elif event.keysym == "Left":
            if self.current_x - self.step >= self.x_start:
                self.current_x -= self.step
                canvas.delete('all')
                field.Fill()
                self.Rectangle()
        elif event.keysym == "Up":
            if self.current_y - self.step >= self.y_start:
                self.current_y -= self.step
                canvas.delete('all')
                field.Fill()
                self.Rectangle()
        elif event.keysym == "Down":
            if self.current_y + self.step < FRAME_HEIGHT:
                self.current_y += self.step
                canvas.delete('all')
                field.Fill()
                self.Rectangle()

    # Drawing rectangle
    def Rectangle(self):
        canvas.create_rectangle(self.current_x, self.current_y, self.current_x + self.step - 2,
                                self.current_y + self.step - 2, width=3, outline='red')


class Field(object):
    def __init__(self):
        self.width = 533
        self.height = 533
        self.image_size = 50
        self.rows = 10
        self.cows = 10
        self.x_start = 3
        self.y_start = 3

    # Putting images
    def Fill(self):
        x = self.x_start
        y = self.y_start
        for i in range(self.cows):
            for j in range(self.rows):
                canvas.create_image(x, y, anchor=NW, image=img)
                x += self.image_size + self.x_start
            y += self.image_size + self.y_start
            x = self.x_start


def main():
    # Creating the main window of an application
    window_size = f'{WINDOW_X}x{WINDOW_Y}'
    global window
    window = Tk()
    window.title("Sapper")
    window.geometry(window_size)

    # Creating the frame
    frame = Frame(master, width=FRAME_WIDTH, height=FRAME_HEIGHT, bd=1)
    frame.pack(anchor=NW)

    # Creating the canvas
    global canvas
    canvas = Canvas(frame, width=FRAME_WIDTH, height=FRAME_HEIGHT, bg='white')
    canvas.pack()

    # Loading image
    global img
    img = PhotoImage(file="../files/imgs/image.png")

    # Creating objects
    global player
    global field
    field = Field()
    player = Player()

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
