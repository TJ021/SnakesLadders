from salbnode import *
from salboard import *
from salbLLfunctions import *
import random
import unittest


class MyTestWhoWins(unittest.TestCase):

    # no snakes or ladders and both players move size are the same
    def test_whowins1(self):
        random_step = random.randint(1, 10000)
        random_board = random.randint(1, 10000)
        b = whowins(salb2salbLL(SALboard(random_board, {})), random_step,
                    random_step)
        self.assertEqual(b, 1, "if both players finish in the same amount of"
                               "moves then player 1 is the winner")

    # player2's move size is > player's move size and no snakes or ladders
    def test_whowins2(self):
        b = whowins(salb2salbLL(SALboard(100, {})), 1, 2)
        self.assertEqual(b, 2, "Both can finish and player2's moves should be"
                               "less")

    # player1's move size is > player2's move size and no snakes or ladders
    def test_whowins3(self):
        b = whowins(salb2salbLL(SALboard(100, {})), 2, 1)
        self.assertEqual(b, 1, "Both can finish and player1's moves should be"
                         "less")

    # if both players cant finish
    def test_whowins4(self):
        b = whowins(salb2salbLL(SALboard(100, {50: 20})), 1, 1)
        self.assertEqual(b, 2, "if both player's are in infinite loop then "
                               "player 2 is the winner")

    # if player 1 cant finish but player 2 can
    def test_whowins5(self):
        b = whowins(salb2salbLL(SALboard(10, {9: 6})), 1, 2)
        self.assertEqual(b, 2, "if player1 cant win then player2 is the winner")

    # if player 2 cant finish but player 1 can
    def test_whowins6(self):
        b = whowins(salb2salbLL(SALboard(10, {9: 6})), 2, 1)
        self.assertEqual(b, 1, "if player2 cant win then player1 is the winner")


if __name__ == '__main__':
    unittest.main()
