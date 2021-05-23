import queue
from itertools import permutations, islice, combinations


class Travel:
    def __init__(self):
        self.points_coord = []
        self.points_map = {}


def genetic_algorithm(travel_map):
    population = queue.PriorityQueue()
    road_map = list(travel_map.keys())
    points_permutation = list(map(list, islice(permutations(road_map), 10)))
    # for i in range(0, len(points_permutation)):
    #     distance =
    #     subject = Track()
    # print(points_permutation)
    # print(len(points_permutation))

