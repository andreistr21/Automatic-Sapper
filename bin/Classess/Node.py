class Node:
    def __init__(self):
        self.state = State()
        self.parent = None
        self.action = ""


class State:
    def __init__(self):
        self.coord = []
        self.direction = ""


def successor(state):

    node_state_left = Node()
    node_state_right = Node()
    node_state_forward = Node()

    if state.direction == "east":

        node_state_left.state = State()
        node_state_left.state.coord = state.coord
        node_state_left.state.direction = "north"
        node_state_left.action = "Left"

        node_state_right.state = State()
        node_state_right.state.coord = state.coord
        node_state_right.state.direction = "south"
        node_state_right.action = "Right"

        if state.coord[0] + 53 < 533:
            node_state_forward.state = State()
            node_state_forward.state.coord = [state.coord[0] + 53, state.coord[1]]
            node_state_forward.state.direction = state.direction
            node_state_forward.action = "Up"

    elif state.direction == "west":

        node_state_left.state = State()
        node_state_left.state.coord = state.coord
        node_state_left.state.direction = "south"
        node_state_left.action = "Left"

        node_state_right.state = State()
        node_state_right.state.coord = state.coord
        node_state_right.state.direction = "north"
        node_state_right.action = "Right"

        if state.coord[0] > 3:
            node_state_forward.state = State()
            node_state_forward.state.coord = [state.coord[0] - 53, state.coord[1]]
            node_state_forward.state.direction = state.direction
            node_state_forward.action = "Up"

    elif state.direction == "north":

        node_state_left.state = State()
        node_state_left.state.coord = state.coord
        node_state_left.state.direction = "west"
        node_state_left.action = "Left"

        node_state_right.state = State()
        node_state_right.state.coord = state.coord
        node_state_right.state.direction = "east"
        node_state_right.action = "Right"

        if state.coord[1] > 3:
            node_state_forward.state = State()
            node_state_forward.state.coord = [state.coord[0], state.coord[1] - 53]
            node_state_forward.state.direction = state.direction
            node_state_forward.action = "Up"

    elif state.direction == "south":

        node_state_left.state = State()
        node_state_left.state.coord = state.coord
        node_state_left.state.direction = "east"
        node_state_left.action = "Left"

        node_state_right.state = State()
        node_state_right.state.coord = state.coord
        node_state_right.state.direction = "west"
        node_state_right.action = "Right"

        if state.coord[1] + 53 < 533:
            node_state_forward.state = State()
            node_state_forward.state.coord = [state.coord[0], state.coord[1] + 53]
            node_state_forward.state.direction = state.direction
            node_state_forward.action = "Up"

    if len(node_state_forward.state.coord) != 0:
        return [node_state_left, node_state_right, node_state_forward]
    else:
        return [node_state_left, node_state_right]


def graphsearch(fringe, explored, start_state, end_state_coord):

    node = Node()
    node.state = start_state
    node.parent = node.state
    #node.action = "Right"
    fringe.append(node)
    iter = 0

    bool = True
    while bool:
        if len(fringe) == 0:
            bool = False
            #return False

        elem = fringe[iter]

        if elem.state.coord == end_state_coord:
            bool = False
            return fringe

        explored.append(elem)

        another_states = successor(elem.state)
        for i in range(0, len(another_states)):
            n = len(fringe)
            for j in range(0, n):
                if another_states[i].state.coord[0] == fringe[j].state.coord[0] and another_states[i].state.coord[1] == fringe[j].state.coord[1]:
                    if another_states[i].state.direction == fringe[j].state.direction:
                        break
                    else:
                        # states = []
                        # for k in range(0, len(fringe)):
                        #     new_state = fringe[k].state
                        #     states.append(new_state)
                        # now_state = another_states[i].state
                        # if now_state in states:
                        #     break

                        states = []
                        for k in range(0, len(fringe)):
                            new_state = [fringe[k].state.coord, fringe[k].state.direction]
                            states.append(new_state)
                        now_state = [another_states[i].state.coord, another_states[i].state.direction]
                        if now_state in states:
                            break

                        # bool_break = False
                        # for k in range(0, n):
                        #     if another_states[i].state.coord[0] == fringe[k].state.coord[0] and another_states[i].state.coord[1] == fringe[k].state.coord[1]:
                        #         if another_states[i].state.direction == fringe[k].state.direction:
                        #             bool_break = True
                        # if bool_break:
                        #     break
                        another_states[i].parent = elem.state
                        fringe.append(another_states[i])
                else:
                    states = []
                    for k in range(0, len(fringe)):
                        new_state = [fringe[k].state.coord, fringe[k].state.direction]
                        states.append(new_state)
                    now_state = [another_states[i].state.coord, another_states[i].state.direction]
                    if now_state in states:
                        break
                    # if another_states[i] in fringe:
                    #     break
                    if another_states[i].state.direction == fringe[j].state.direction:
                        another_states[i].parent = elem.state
                        fringe.append(another_states[i])
        iter += 1
