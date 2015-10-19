from collections import deque
from tower import Tower, TowerPosition
from hanoiGameGui import HanoiGameGui

class HanoiGame(HanoiGameGui):

    def __init__(self, canvas):
        super(HanoiGame, self).__init__(canvas)
        discs = range(1, 8)
        self.left_tower = Tower('Torre Esquerda', TowerPosition.Left)
        self.central_tower = Tower('Torre Central', TowerPosition.Center, sorted(discs, reverse=True))
        self.right_tower = Tower('Torre Direita', TowerPosition.Right)
        self.disc_1_mutex = True

    def move(self):
        if self.disc_1_mutex:
            self.forward_move(1)
            self.disc_1_mutex = False
        else:
            disc_on_left = self.left_tower.top()
            disc_on_center = self.central_tower.top()
            disc_on_right = self.right_tower.top()
            values = [v for v in [disc_on_left, disc_on_center, disc_on_right] if v != 1 and v > 0]
            minValue = min(values)
            self.forward_move(minValue)
            self.disc_1_mutex = True

    def able_tower(self, d, tower):
        if len(tower) == 0:
            return True
        value = tower[len(tower) - 1]
        if d > value:
            return False
        return True

    def forward_move(self, d):
        if d in self.right_tower:
            self.next_move(d, self.left_tower, self.central_tower)
        elif d in self.central_tower:
            self.next_move(d, self.right_tower, self.left_tower)
        elif d in self.left_tower:
            self.next_move(d, self.right_tower, self.central_tower)

    def next_move(self, d, tower_a, tower_b):
        #first movement
        if len(tower_a) == 0 and len(tower_b) == 0:
            self.move_disc(d, tower_b)
            return

        #if any tower is unable to receive the disk, it goes the other way
        if not self.able_tower(d, tower_a):
             self.move_disc(d, tower_b)
             return
        if not self.able_tower(d, tower_b):
             self.move_disc(d, tower_a)
             return

        disc_on_a = tower_a.top()
        disc_on_b = tower_b.top()

        if (disc_on_a - 1) == d:
            self.move_disc(d, tower_a)
        elif (disc_on_b - 1) == d:
            self.move_disc(d, tower_b)
        elif d == 1:
            tower = self.disc1_new_tower(tower_a, tower_b)
            print('disc1 new tower', tower)
            self.move_disc(d, tower)

    def disc1_new_tower(self, tower_a, tower_b):

        print('inside disc1_new_tower >>>')
        current_tree = []
        disc1_current_tower = self.get_tower(1)

        i = len(disc1_current_tower) - 1
        current_tree.append(disc1_current_tower[i])

        while disc1_current_tower[i - 1] - disc1_current_tower[i] == 1:
            i-=1
            current_tree.append(disc1_current_tower[i])

        print('current tree', current_tree)

        max_current_tree = max(current_tree)
        print('max current tree', max_current_tree)

        len_current_tree = len(current_tree)
        print('len current tree', len_current_tree)

        len_is_odd = len_current_tree % 2 != 0
        print ('len is odd', len_is_odd)

        building_tower = self.get_tower(max_current_tree + 1)
        if len_is_odd:
            if building_tower == tower_a:
                return tower_a
            return tower_b
        else:
            if building_tower == tower_a:
                return tower_b
            return tower_a

    def get_tower(self, d):
        if d in self.right_tower:
            return self.right_tower
        elif d in self.central_tower:
            return self.central_tower
        elif d in self.left_tower:
            return self.left_tower

    def move_disc(self, d, tower):
        if d in self.left_tower:
            self.left_tower.pop()
        if d in self.central_tower:
            self.central_tower.pop()
        if d in self.right_tower:
            self.right_tower.pop()

        #self.write_movement(d, tower)
        super(HanoiGame, self).moveDiscToTower(d, tower)
        tower.append(d)

    def write_movement(self, d, tower):
        print(d, '=>', tower)

    def animate(self):
        super(HanoiGame, self).animateFromQueue()
