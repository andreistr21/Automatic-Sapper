import random

FRAME_WIDTH = 555
FRAME_HEIGHT = 555

WINDOW_X = FRAME_WIDTH + 1200
WINDOW_Y = 950

# Size of small image
IMAGE_SIZE = 50

MIN_AMOUNT_OF_MINES = 0
MAX_AMOUNT_OF_MINES = 11
AMOUNT_OF_MINES = random.randint(MIN_AMOUNT_OF_MINES, MAX_AMOUNT_OF_MINES)

DELAY_TIME = 0.5

STEP = IMAGE_SIZE + 5

standard_cell_cost = 10

amount_of_sand_cells = 10
sand_cell_cost = 20

amount_of_water_cells = 10
water_cell_cost = 40

amount_of_swamp_cells = 10
swamp_cell_cost = 5

x_start = 5
y_start = 5
