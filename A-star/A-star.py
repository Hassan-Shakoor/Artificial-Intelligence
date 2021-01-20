from my_graph import Graph
from my_queue import PriorityQueue

def A_star_search(graph, start_node, goal_node):


    visited = []
    queue = PriorityQueue()
    queue.insert(start_node, 0,0)
    total_cost = 0
    func=0

    while not queue.is_empty():
        temp = []
        cost, node = queue.remove()

        if node not in visited:
            visited.append(node)

            if node[-1] == goal_node:
                break

            for i in graph.neighbours(node[-1]):
                if i not in visited:
                    heuristic=graph.get_h(i)
                    total_cost = cost + graph.get_cost(node[-1], i)

                    '''FUNC=TOTAL COST + HEURISTIC'''
                    func=total_cost+heuristic
                    
                    queue.insert(node + ',' + i, func,total_cost)
                    func=0

    print("Shortest Path:", node)
    print("Cost:", cost)


if __name__ == "__main__":

    # Defining Graph
    graph = Graph()

    # setting up nodes and neighbours
    graph.edges = {

        'S': set(['A', 'D']),

        'A': set(['S','B']),

        'B': set(['A', 'C', 'D','E']),

        'C': set(['B','G']),

        'D': set(['S', 'B', 'E']),

        'E': set(['D','B','G']),

        'G': set(['E','C'])

    }
    # setting up connection costs
    graph.weights = {

        'SA': 3, 'SD': 2,

        'AS': 3, 'AB': 5, 'BD': 1,

        'BE': 1, 'BC': 2, 'BA': 5,

        'CB': 2, 'CG': 4, 'DS': 2,

        'DB': 1, 'DE': 4, 'ED': 4, 'EG': 3,

        'EB': 1, 'GE': 3,'GC': 4

    }
    graph.heuristics={'S':7,'A':9,'B':4,'C':2,'D':5,'E':3,'G':0}

    A_star_search(graph, 'S', 'G')