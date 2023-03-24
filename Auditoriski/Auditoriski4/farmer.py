from searching_framework.utils import Problem
from searching_framework.informed_search import greedy_best_first_graph_search, best_first_graph_search, \
    recursive_best_first_search, astar_search

def valid(state):
    farmer, volk, jare, zelka = state
    if volk == jare and farmer != volk:
        return False
    if jare == zelka and farmer != jare:
        return False
    return True

class Farmer(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = {}

        farmer, volk, jare, zelka = state

        # Farmerot se prenesuva samiot sebesi
        farmer_new = 'e' if farmer == 'w' else 'w'
        state_new = farmer_new, volk, jare, zelka
        if valid(state_new):
            successors['Farmer nosi farmer'] = state_new

        #Farmerot go prenesuva volkot
        if farmer == volk:
            volk_new = 'e' if farmer == 'w' else 'w'
            state_new = farmer_new, volk_new, jare, zelka
            if valid(state_new):
                successors['Farmer nosi volk'] = state_new

        # Farmerot go prenesuva jarete
        if farmer == jare:
            jare_new = 'e' if farmer == 'w' else 'w'
            state_new = farmer_new, volk, jare_new, zelka
            if valid(state_new):
                successors['Farmer nosi jare'] = state_new

        # Farmerot ja prenesuva zelkata
        if farmer == zelka:
            zelka_new = 'e' if farmer == 'w' else 'w'
            state_new = farmer_new, volk, jare, zelka_new
            if valid(state_new):
                successors['Farmer nosi zelka'] = state_new

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def h(self, node):
        state = node.state
        goal = self.goal
        counter = 0
        for x, y in zip(state, goal):
            if x != y:
                counter += 1
        return counter


if __name__ == "__main__":
    initial_state = ('e', 'e', 'e', 'e')
    goal_state = ('w', 'w', 'w', 'w')

    farmer = Farmer(initial_state, goal_state)

    answer = astar_search(farmer)

    print(answer.solution())
