import sys

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

    def MovingRight(self):
        if self.current_x + self.step < FRAME_WIDTH:
            self.current_x += self.step
            self.current_array_x += 1
        elif self.current_y + self.step < FRAME_HEIGHT:
            self.current_x = self.x_start
            self.current_array_x = 0
            self.current_array_y += 1
            self.current_y += self.step

    def MovingLeft(self):
        if self.current_x - self.step >= self.x_start:
            self.current_x -= self.step
            self.current_array_x -= 1
        elif self.current_y - self.step >= self.y_start:
            self.current_x = FRAME_WIDTH - self.step
            self.current_array_x = 9
            self.current_array_y -= 1
            self.current_y -= self.step

    def MovingUp(self):
        if self.current_y - self.step >= self.y_start:
            self.current_y -= self.step
            self.current_array_y -= 1

    def MovingDown(self):
        if self.current_y + self.step < FRAME_HEIGHT:
            self.current_y += self.step
            self.current_array_y += 1
