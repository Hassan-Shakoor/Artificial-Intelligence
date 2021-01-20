import heapq
class PriorityQueue:
    def __init__(self):
        self.__queue = []
        self.__index = 0

    def insert(self, priority, item):
        heapq.heappush(self.__queue, (item, self.__index, priority))
        self.__index += 1

    def remove(self):

        temp = heapq.heappop(self.__queue)
        
        item = temp[0]
        cost = temp[-1]

        return cost, item

    def is_empty(self):

        return len(self.__queue) == 0
    def Print(self):

        print(self.__queue)


class Graph:
    def __init__(self):
        self.edges = {} # dictionary of edges NODE: NEIGHBOURS
        self.weights = {} # dictionary of NODES and their COSTS
        self.newlist=[]

    def neighbours(self, node):
        return self.edges[node]

    def get_cost(self, from_node, to_node):   
        return self.weights[(from_node + to_node)]


    def uniform_cost_search(self,graph, start, goal):
        visited = set()
        queue = PriorityQueue()
        queue.insert(0, start)
    
        while queue:
            cost, node = queue.remove()
            if node not in visited:
                visited.add(node)
    
                if node == goal:
                    final=[]
                    result=[]
                    minn=100000
                    temp=0
                    for x in self.newlist:
                        if node in x[2]:
                            if int(x[0]) < minn:
                                minn=x[0]
                                temp=x
                    temp=list(temp)
                    temp.pop(0)
                    temp.insert(0,start)
                    for i in temp:
                        if len(i)>1:
                            for x in i:
                                final.append(x)
                        else:
        
                            final.append(i)
                    for x in final:
                        if x not in result:
                            if x <= goal:
                                result.append(x)
                            
                    print("Cost: ",total_cost)
                    print("Shortest Path: ",sorted(result))
                    return
                neighb=graph.neighbours(node)
                for i in neighb:
                    if i not in visited:
                        total_cost = cost + graph.get_cost(node, i)
                        
                        
                        queue.insert(total_cost, i)
                self.newlist.append((total_cost,node,neighb))
if __name__ == "__main__":

    # Defining Graph
    graph = Graph()

    # setting up nodes and neighbours
    graph.edges = {
        'A': set(['B', 'D']),
        'B': set(['A','E','C']),
        'C': set(['B', 'E', 'G']),
        'D': set(['A','E','F']),
        'E': set(['B', 'C', 'D', 'G']),
        'F': set(['D','G']),
        'G': set(['F','E','C'])
    }

    # setting up connection costs
    graph.weights = {
        'AB': 5, 'AD': 3,
        'BA': 5, 'BE': 4, 'BC': 1,
        'CB': 1, 'CE': 6, 'CG': 8,
        'DA': 3, 'DE': 2, 'DF': 2,
        'EB': 4, 'EC': 6, 'ED': 2, 'EG': 4,
        'FD': 2, 'FG': 3,
        'GF': 3, 'GE': 4, 'GC': 8
    }

    graph.uniform_cost_search(graph, 'A', 'G') 
