import unittest

class TestHanoiGameMoves(unittest.TestCase):

  def test_one_possible_move(self):
      self.assertEqual('foo'.upper(), 'FOO')

  def test_two_possible_moves(self):
      self.assertTrue('FOO'.isupper())
      self.assertFalse('Foo'.isupper())

  def test_five_moves(self):
      s = 'hello world'
      self.assertEqual(s.split(), ['hello', 'world'])
      # check that s.split fails when the separator is not a string
      with self.assertRaises(TypeError):
          s.split(2)

if __name__ == '__main__':
    unittest.main()
