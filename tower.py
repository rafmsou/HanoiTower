from collections import deque

class Tower(deque):

    def __init__(self, name, discs = []):
        super(Tower, self).__init__(discs)
        self.name = name

    def __str__(self):
        return self.name
