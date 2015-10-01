from collections import deque

class Tower(deque):

    def __init__(self, name, index, discs = []):
        super(Tower, self).__init__(discs)
        self.name = name
        self.index = index

    def __str__(self):
        return self.name
