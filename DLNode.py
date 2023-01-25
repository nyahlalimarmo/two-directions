class DLNode:

    def __init__(self, n = None):
        self.data = n
        self.next = None
        self.prev = None

    def __str__(self):
        return(str(self.data))

    def get_data(self):
        return self.data
    def get_next(self):
        return self.next
    def get_prev(self):
        return self.prev

    def set_data(self, d):
        self.data = d
    def set_next(self, n):
        self.next = n
    def set_prev(self, p):
        self.prev = p