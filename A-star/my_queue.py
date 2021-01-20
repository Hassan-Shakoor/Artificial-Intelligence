import heapq
class PriorityQueue:
    def __init__(self):

        self.__queue = []

        self.__index = 0



    def insert(self, item, priority,cost):

        heapq.heappush(self.__queue, (priority, self.__index, item,cost))

        self.__index += 1



    def remove(self):

        temp = heapq.heappop(self.__queue)

        

        heuristic_cost = temp[0]
        cost=temp[-1]

        item = temp[-2]



        return cost, item



    def is_empty(self):


        return len(self.__queue) == 0

    

    

if __name__ == "__main__":

    

    # testing priority queue

    queue = PriorityQueue()

    queue.insert('e', 9)

    queue.insert('a', 2)

    queue.insert('h', 13)

    queue.insert('c', 11)

    print(queue.remove())

    print(queue.remove())

    print(queue.remove())
