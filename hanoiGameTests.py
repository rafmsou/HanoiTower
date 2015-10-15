import unittest
from hanoiGame import HanoiGame
from tower import Tower

class TestHanoiGameMoves(unittest.TestCase):

  def test_action(self):
      hg = HanoiGame(None)
      hg.move()
      self.assertEqual(hg.left_tower.top(), 1)

if __name__ == '__main__':
    unittest.main()
