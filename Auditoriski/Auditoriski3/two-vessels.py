from searching_framework.utils import Problem
from searching_framework.uninformed_search import *


class Container(Problem):
    def __init__(self, capacities, initial, goal=None):
        super().__init__(initial, goal)
        self.capacities = capacities

    def successor(self, state):
        # state = (j0, j1)
        successors = dict()  # dict e mapa od java

        j0, j1 = state
        c0, c1 = self.capacities

        # akcii za praznenje na sadovite bidejkji vo tekstot na zadacata
        # pisuva deka moze da se ispraznat sadovite pa mora da se definiraat akciite
        if j0 > 0:
            successors['Isprazni go sadot J0'] = (0, j1)  # key / value

        if j1 > 0:
            successors['Isprazni go sadot J1'] = (j0, 0)  # key / value

        # akcii za preturanje na tecnost od eden vo drug sad
        if j0 > 0 and j1 < c1:  # ako ima tecnost vo j0 i j1 ne e skroz napolnet
            delta = min(c1 - j1, j0)  # se pretura cela tecnost od j0 ili se pretura uste kolku so ima mesto vo j1,
            # se zema pomaloto
            successors['Preturi od J0 vo J1'] = (j0 - delta, j1 + delta)  # key / value

        if j1 > 0 and j0 < c0:
            delta = min(c0 - j0, j1)
            successors['Preturi od J1 vo J0'] = (j0 + delta, j1 - delta)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal


if __name__ == "__main__":
    container = Container([15, 5], (5, 5), (10, 0))  # capacities, initial, goal

    result = depth_first_tree_search(container)
    print(result.solution())  # ja pecati nizata od akcii so se pominuvaat
    print(result.solve())  # ja pecati listata na sostojbi
