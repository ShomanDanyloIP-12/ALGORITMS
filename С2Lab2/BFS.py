from queue import Queue
from puzzle import Puzzle
from func_timeout import func_timeout

def rbfs(initial_state):
    return func_timeout(1800, breadth_first_search, args=[initial_state])

def breadth_first_search(initial_state):
    start_node = Puzzle(initial_state, None, None, 0)
    if start_node.goal_test():
        return start_node.find_solution()
    q = Queue()
    q.put(start_node)
    explored=[]
    while not(q.empty()):
        node=q.get()
        explored.append(node.state)
        children=node.generate_child()
        Puzzle.instances_in_memory = len(explored)
        for child in children:
            if child.state not in explored:
                if child.goal_test():
                    return child.find_solution()
                q.put(child)
    return