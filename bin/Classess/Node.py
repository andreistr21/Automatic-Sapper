#from bin.Main.main import player


class Node:
    def __init__(self):
        self.state = State()
        self.parent = None
        self.action = None


class State:
    def __init__(self):
        self.coord = []
        self.direction = ""


def successor(state):

    if state.direction == "east":
        node_state_left = Node()
        node_state_right = Node()
        node_state_forward = Node()

        #state_left = state.coord
        node_state_left.state = State()
        node_state_left.state.coord = state.coord
        node_state_left.state.direction = "north"
        node_state_left.parent = state
        node_state_left.action = "Left"

        #state_right = state.coord
        node_state_right.state = State()
        node_state_right.state.coord = state.coord
        node_state_right.state.direction = "south"
        node_state_right.parent = state
        node_state_right.action = "Right"

        #state_forward = state.coord
        #state_forward[0] = 53
        node_state_forward.state = State()
        node_state_forward.state.coord = [state.coord[0] + 53, state.coord[1]]
        node_state_forward.state.direction = state.direction
        node_state_forward.parent = state
        node_state_forward.action = "Up"

        return [node_state_left, node_state_right, node_state_forward]

    #elif state.direction == "west":

    #elif state.direction == "north":

    #elif state.direction == "south":


def hello():
    print("Hello Node!")
