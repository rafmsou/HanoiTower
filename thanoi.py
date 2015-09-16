from collections import deque
from tower import Tower

discs = range(1, 8)

left_tower = Tower('Torre Esquerda')
central_tower = Tower('Torre Central', sorted(discs, reverse=True))
right_tower = Tower('Torre Direita')

disc_1_mutex = True

class THanoi:
    def able_tower(self, d, tower):
        if len(tower) == 0:
            return True
        value = tower[len(tower) - 1]
        if d > value:
            return False
        return True

    def forward_move(self, d):
        if d in right_tower:
            self.best_move(d, left_tower, central_tower)
        elif d in central_tower:
            self.best_move(d, right_tower, left_tower)
        elif d in left_tower:
            self.best_move(d, right_tower, central_tower)

    def tower_complete(self, tower):
        num_elements = len(tower)
        if num_elements == 0:
            return False
        complete = (num_elements == (tower[0] - tower[num_elements - 1]) + 1)
        print 'Tower complete', complete
        return complete

    def complete_cycle(self):
           right_tower_complete = self.tower_complete(right_tower)
           left_tower_complete = self.tower_complete(left_tower)
           if(right_tower_complete and left_tower_complete):
               if(len(right_tower) == 1 and right_tower[0] == max(left_tower) + 1):
                   return True
               if(len(left_tower) == 1 and left_tower[0] == max(right_tower) + 1):
                   return True
           return False

    def tower_first_move(self, d):
        tower = self.get_tower(d)
        length = len(tower)
        if length % 2 == 0:
            return central_tower
        else:
            return self.get_opposite_tower(tower)

    def get_opposite_tower(self, tower):
        if tower.name == 'Torre Esquerda':
            return right_tower
        if tower.name == 'Torre Direita':
            return left_tower

    def best_move(self, d, tower_a, tower_b):
        if not self.able_tower(d, tower_a):
             self.move_disc(d, tower_b)
             return
        if not self.able_tower(d, tower_b):
             self.move_disc(d, tower_a)
             return

        disc_on_a = self.top(tower_a)
        disc_on_b = self.top(tower_b)

        parent_waiting = ((disc_on_a - 1) == d) or ((disc_on_b - 1) == d)

        if disc_on_b == 0 and not parent_waiting:
            self.move_disc(d, tower_b)
        elif disc_on_a == 0 and not parent_waiting:
            self.move_disc(d, tower_a)
        else:
            #two possible moves!
            if (disc_on_a - 1) == d:
                self.move_disc(d, tower_a)
            elif (disc_on_b - 1) == d:
                self.move_disc(d, tower_b)
            elif self.complete_cycle():
                tower = self.tower_first_move(d)
                self.move_disc(d, tower)
            else:
                self.complex_move(d, tower_a, tower_b)

    def complex_move(self, d, tower_a, tower_b):
        parent_disc_index = (d + 1)
        grandpa_disc_index = (d + 2)
        current_tower = self.get_tower(d)
        second_last_disc = current_tower[len(current_tower) - 2]
        if d == (second_last_disc - 1):
            if self.get_tower(grandpa_disc_index) == tower_a:
                self.move_disc(d, tower_b)
            else:
                self.move_disc(d, tower_a)

    def get_tower(self, d):
        if d in right_tower:
            return right_tower
        elif d in central_tower:
            return central_tower
        elif d in left_tower:
            return left_tower

    def top(self, tower):
        if len(tower) == 0:
            return 0
        value = tower[len(tower) - 1]
        return value

    def move_disc(self, d, tower):
        if d in left_tower:
            left_tower.pop()
        if d in central_tower:
            central_tower.pop()
        if d in right_tower:
            right_tower.pop()

        self.write_movement(d, tower)
        tower.append(d)

    def write_movement(self, d, tower):
        print d, '=>', tower

    def move(self):
        global disc_1_mutex
        if disc_1_mutex:
            self.forward_move(1)
            disc_1_mutex = False
        else:
            disc_on_left = self.top(left_tower)
            disc_on_center = self.top(central_tower)
            disc_on_right = self.top(right_tower)
            values = [v for v in [disc_on_left, disc_on_center, disc_on_right] if v != 1 and v > 0]
            minValue = min(values)
            self.forward_move(minValue)
            disc_1_mutex = True

th = THanoi()
th.move()
th.move()
th.move()
th.move()
th.move()
th.move()
th.move()
th.move()
th.move()
th.move()
th.move()
th.move()
th.move()
th.move()
th.move()
th.move()
th.move()
