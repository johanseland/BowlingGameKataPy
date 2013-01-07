import unittest

class BowlingGame():
    def roll(self, pins):
        None
    def score(self):
        return 0


class BowlingGameTest(unittest.TestCase):
    def test_GutterGame(self):
        game = BowlingGame()
        for i in range(20):
            game.roll( 0 )
        self.assertEqual( 0, game.score() )



            
