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

    # def Moving(self, event):
    #     # Moving
    #     if event.keysym == "Right":
    #         if self.current_x + self.step < FRAME_WIDTH:
    #             self.current_x += self.step
    #             field.small_field_canvas.delete('all')
    #             field.large_image_canvas.delete('all')
    #             self.current_array_x += 1
    #             field.Fill()
    #             self.Rectangle()
    #         elif self.current_y + self.step < FRAME_HEIGHT:
    #             self.current_x = self.x_start
    #             field.small_field_canvas.delete('all')
    #             field.large_image_canvas.delete('all')
    #             self.current_array_x = 0
    #             self.current_array_y += 1
    #             self.current_y += self.step
    #             field.Fill()
    #             self.Rectangle()
    #     elif event.keysym == "Left":
    #         if self.current_x - self.step >= self.x_start:
    #             self.current_x -= self.step
    #             field.small_field_canvas.delete('all')
    #             field.large_image_canvas.delete('all')
    #             self.current_array_x -= 1
    #             field.Fill()
    #             self.Rectangle()
    #         elif self.current_y - self.step >= self.y_start:
    #             self.current_x = FRAME_WIDTH - self.step
    #             field.small_field_canvas.delete('all')
    #             field.large_image_canvas.delete('all')
    #             self.current_array_x = 9
    #             self.current_array_y -= 1
    #             self.current_y -= self.step
    #             field.Fill()
    #             self.Rectangle()
    #     elif event.keysym == "Up":
    #         if self.current_y - self.step >= self.y_start:
    #             self.current_y -= self.step
    #             field.small_field_canvas.delete('all')
    #             field.large_image_canvas.delete('all')
    #             self.current_array_y -= 1
    #             field.Fill()
    #             self.Rectangle()
    #     elif event.keysym == "Down":
    #         if self.current_y + self.step < FRAME_HEIGHT:
    #             self.current_y += self.step
    #             field.small_field_canvas.delete('all')
    #             field.large_image_canvas.delete('all')
    #             self.current_array_y += 1
    #             field.Fill()
    #             self.Rectangle()

    # # Drawing rectangle
    # def Rectangle(self):
    #     field.small_field_canvas.create_rectangle(self.current_x, self.current_y, self.current_x + self.step - 2,
    #                                               self.current_y + self.step - 2, width=3, outline='blue2')
