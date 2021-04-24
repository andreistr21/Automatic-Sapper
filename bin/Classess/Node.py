class Node:
    def __init__(self):
        self.state = State()
        self.parent = None
        self.action = None


class State:
    def __init__(self):
        self.coord = []
        self.direction = ""
