from collections import deque
class Tower(deque):

    def __init__(self, name, index, discs = []):
        super(Tower, self).__init__(discs)
        self.name = name
        self.index = index

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def top(self):
        if len(self) == 0:
            return 0
        value = self[len(self) - 1]
        return value

from enum import Enum
class TowerPosition(Enum):
    Left = 0
    Center = 1
    Right = 2
