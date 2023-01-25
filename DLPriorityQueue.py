import DLNode

class PriorityQueue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def size(self):
        return self.length

    def is_empty(self):
        return self.length == 0

    def first(self):
        if self.is_empty():
            return None
        else:
            return self.front.get_data()

    def enqueue(self, item):
        node = DLNode.DLNode(item)
        if self.is_empty():
            self.front = node
            self.rear = node
        elif node.get_data() < self.front.get_data():
            current = self.front
            self.front.set_prev(node)
            self.front = node
            node.set_next(current)
        else:
            if node.get_data() < self.front.get_data():
                current = self.front
                self.front.set_prev(node)
                self.front = node
                node.set_next(current)
            elif node.get_data() == self.front.get_data():
                current = self.front
                current.set_next(node)
                current.set_prev(current)
                self.front.set_prev(None)
            else:
                current = self.front
                #while current.get_next() != None and current.get_next().get_data() < node.get_data():
                    #current = current.get_next
                #if current.get_next() != None:
                while current != None and node.get_data() > current.get_data():
                    current = current.get_next()
                if node.get_data() < current.get_data() and node.get_data() >= current.get_data():
                    node.get_next().set_prev(node)
                    current.set_next(node)
                    node.set_prev(current)
        
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            front_data = self.front.get_data()
            self.front = self.front.get_next()
            #set new front
            self.front.set_prev(None)
            self.length -= 1
            if self.is_empty():
                self.front = None
                front_data = None
        return front_data

    def __str__(self):
        s = ""
        start = self.front
        while start != None:
            s += str(start) + "\n"
            start = start.get_next()
        return s
