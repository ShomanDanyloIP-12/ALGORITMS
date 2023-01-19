from time import time
from BFS import breadth_first_search
from RBFS import recursive_best_first_search
from puzzle import Puzzle


state=[[1, 3, 5,
        0, 4, 2,
        7, 8, 6],

       [5, 1, 3,
        4, 2, 6,
        0, 7, 8],

       [2, 3, 5,
        1, 8, 0,
        4, 7, 6],

       [1, 5, 2,
        7, 4, 8,
        0, 6, 3],

       [4, 1, 0,
        7, 6, 3,
        5, 2, 8],

       [0, 3, 6,
        1, 8, 5,
        4, 7, 2],

       [3, 5, 8,
        1, 6, 2,
        4, 0, 7],

       [1, 3, 8,
        6, 5, 0,
        4, 2, 7],

       [2, 0, 8,
        4, 1, 3,
        7, 6, 5],

       [6, 4, 2,
        7, 1, 8,
        0, 3, 5],

       [4, 1, 5,
        7, 8, 2,
        0, 6, 3],

       [3, 1, 6,
        2, 8, 0,
        4, 5, 7],

       [5, 2, 4,
        1, 0, 7,
        8, 6, 3],

       [1, 3, 8,
        5, 2, 0,
        4, 6, 7],

       [3, 5, 6,
        4, 0, 8,
        2, 1, 7],

       [4, 5, 2,
        3, 8, 1,
        0, 7, 6],

       [1, 8, 2,
        7, 0, 3,
        6, 4, 5],

       [7, 0, 3,
        2, 1, 8,
        6, 4, 5],

       [4, 2, 5,
        8, 7, 1,
        6, 0, 3],

       [1, 2, 3,
        4, 5, 6,
        7, 8, 0],
       ]

for i in range(0,20):
    try:
        Puzzle.num_of_instances=0
        Puzzle.instances_in_memory = 1
        t0=time()
        bfs=breadth_first_search(state[i])
        t1=time()-t0
        print('BFS:', bfs)
        print('states:',Puzzle.num_of_instances)
        print('states in memory:', Puzzle.instances_in_memory)
        print('time:',t1)
        print()
    except:
        print("Time is out")
        print('states:', Puzzle.num_of_instances)
        print('states in memory:', Puzzle.instances_in_memory)
        print('time:', t1)
        print()
    try:
        Puzzle.num_of_instances = 0
        Puzzle.instances_in_memory = 1
        t0 = time()
        RBFS = recursive_best_first_search(state[i])
        t1 = time() - t0
        print('RBFS:',RBFS)
        print('states:', Puzzle.num_of_instances)
        print('states in memory:', Puzzle.instances_in_memory)
        print('time:', t1)
        print()
    except:
        print("Time is out")
        print('states:', Puzzle.num_of_instances)
        print('states in memory:', Puzzle.instances_in_memory)
        print('time:', t1)
        print()

    print('------------------------------------------')