class Graph:

    def __init__(self):

        self.edges = {} # dictionary of edges NODE: NEIGHBOURS

        self.weights = {} # dictionary of NODES and their COSTS



    def neighbours(self, node):

        return self.edges[node]



    def get_cost(self, from_node, to_node):
        

        return self.weights[(from_node + to_node)]
    def get_h(self,node):
        return self.heuristics.get(node)







if __name__ == "__main__":

    # testing out the graph class

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



    #print("Neighbours of Node A are:",graph.neighbours('S'))

    print("Cost going from A to D is:", graph.get_cost('S','G'))
