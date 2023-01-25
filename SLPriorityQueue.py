import SLNode

class PriorityQueue:

    def __init__(self):
        self.front = None
        self.length = 0

    def enqueue(self, item):
        node = SLNode.SLNode(item)
        if self.is_empty():
            self.front = node
            #self.front.get_next = node
        else:
            #check if node is less than item at front or equal to front
            if node.get_data() < self.front.get_data():
                node.set_next(self.front)
                #previous front is set as next
                self.front = node
                #change node to become front
            elif node.get_data() == self.front.get_data():
                #if equal value, first value entered should be first returned
                self.front.set_next(node)
            else:
            #if node is greater than front, run through whole thing and find spot for it in queue
                current = self.front
                #next = self.front.get_next()
                #nonetype because there is no next data yet
                while current != None and node.get_data() > current.get_data():
                    next = current.get_next()
                    if node.get_data() < next.get_data() and node.get_data() >= current.get_data():
                        current.set_next(node)

        self.length += 1

    def first(self):
        if self.length == 0:
            return None
        else:
            return self.front.get_data()

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            front_data = self.front.get_data()
            self.front = self.front.get_next()
            #set new front
            self.length -= 1
            if self.is_empty():
                self.front = None
                front_data = None
        return front_data

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

    def __str__(self):
        s = ""
        start = self.front
        while start != None:
            s += str(start) + "\n"
            start = start.get_next()
        return s
