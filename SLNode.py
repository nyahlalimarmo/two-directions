class SLNode:

    def __init__(self, n = None):
        self._data = n
        self._next = None

    def __str__(self):
        return(str(self._data))

    def set_next(self, node_next):
        self._next = node_next

    def set_data(self, d):
        self._data = d

    def get_next(self):
        return self._next

    def get_data(self):
        return self._data