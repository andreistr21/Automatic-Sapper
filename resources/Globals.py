import random

FRAME_WIDTH = 555
FRAME_HEIGHT = 555

WINDOW_X = FRAME_WIDTH + 1200
WINDOW_Y = 950

# Size of small image
IMAGE_SIZE = 50

MIN_AMOUNT_OF_MINES = 6
MAX_AMOUNT_OF_MINES = 11
AMOUNT_OF_MINES = random.randint(MIN_AMOUNT_OF_MINES, MAX_AMOUNT_OF_MINES)

DELAY_TIME = 0.2
SLEEP_AFTER_CHECK_MINE = 2

STEP = IMAGE_SIZE + 5

standard_cell_cost = 10

amount_of_sand_cells = 10
sand_cell_cost = 20

amount_of_water_cells = 10
water_cell_cost = 40

amount_of_swamp_cells = 10
swamp_cell_cost = 80

x_start = 5
y_start = 5

NUMBER_OF_INDIVIDUALS_FOR_DUEL = 4
NUMBER_OF_POINTS_PERMUTATION = 10
PERCENT_OF_MUTATION = 0.01
PERCENT_OF_OUTGOING_INDIVIDUALS = 0.03


label_text = ""
